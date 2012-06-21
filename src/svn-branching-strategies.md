Title: SVN branching strategies
Date: 2011-08-27

The linked SO question mentioned two branching strategies commonly used in parallel developments.

    * Trunk as stable point and development of new features in separate branch.
    * Trunk as development mainline with every releases tagged or branched in a
      separate branch.

Currently we're using more of the former approach where development mostly done in trunk and when we're releasing new features, we tagged it and push it to live. For new features that would take time or quite experimental, we create a new branch and once it ready, merge back to trunk. This would keep trunk stable most of the time and allow us to do any quick bug fixes in the trunk as it arise. With svn ability to remember merge (1.5 above), the work flow is quite straightforward.

I would start with creating new branch for the new feature to work on. While working on the branch, I would merge latest changes to the trunk into my current branch. Once it ready, merging it back to trunk would be accomplish by `svn merge --reintegrate` in the trunk. One limitation of `--reintegrate` switch is it make the branch unusable anymore. You simply would delete the branch.

Now there's certain situation that I need to create 2 separate branch for different set of new features. For example I need to work on a set of features in branch A and for another set of features I prefer to work in new branch B. This is because feature in branch B maybe would not finish or ready in time with branch A. But still, I need to base branch B with branch A because it contain some related changes. And of course while developing in branch B, I want to merge changes in branch A to make sure I have all the latest changes to the code base.

With modern DVCS such as git or mercurial the workflow is feasible because they can intelligently merge all the changes between the various branch but svn is not that smart.  While I can merge changes in branch A to branch B, the problem arise when try merge B back into trunk while A also has been merged into trunk prior to that (because branch A was released first). SVN would see a conflict since some changes in B already being merged when we merge A back into trunk.

This is the very reason why I want to look into alternative way of structuring our development process. We definitely won't move to dvcs such as git or mercurial. But it look like making trunk as development mainline would be more problematic as mentioned in the SO's answer. It also doesn't seem to solve the problem that we have.
