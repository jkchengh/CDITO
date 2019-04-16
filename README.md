# CDITO

This is a code repository of Conflict-directed Incremental Total Ordering
This repository is associated with the paper [_Efficiently Exploring Ordering Problems through Conflict-directed Search_](http://mers-papers.csail.mit.edu/Conference/2019/ICAPS19_Chen_CDITO/chen2019cdito.pdf). If you have any question, please email me at jkchen 'at' csail.mit.edu, or create an issue [here](https://github.com/jkchengh/CDITO/issues).

## Citation
Please cite our work if you would like to use the code.
```
@inproceedings{chen2019cdito,
  author    = {Jingkai Chen and Cheng Fang and David Wang and Andrew Wang and Brian Williams},
  title     = {Efficiently Exploring Ordering Problems through Conflict-directed Search},
  booktitle = {Proceedings of the Twenty-Ninth International Conference on Automated Planning and Scheduling (ICAPS 2019)},
  year      = {2019},
  file      = {:Conference/2019/ICAPS19_Chen_CDITO/chen2019cdito.pdf:PDF},
  keywords  = {ordering, search, conflict, hybrid planning},
  abstract  = {In planning and scheduling, solving problems with both state and temporal constraints is hard since these constraints may be highly coupled. Judicious orderings of events enable solvers to efficiently make decisions over sequences of actions to satisfy complex hybrid specifications. The ordering problem is thus fundamental to planning. Promising recent works have explored the ordering problem as search, incorporating a special tree structure for efficiency. However, such approaches only reason over partial order specifications. Having observed that an ordering is inconsistent with respect to underlying constraints, prior works do not exploit the tree structure to efficiently generate orderings that resolve the inconsistency. In this paper, we present Conflict-directed Incremental Total Ordering (CDITO), a conflict-directed search method to incrementally and systematically generate event total orders given ordering relations and conflicts returned by sub-solvers. Due to its ability to reason over conflicts, CDITO is much more efficient than Incremental Total Ordering. We demonstrate this by benchmarking on temporal network configuration problems that involve routing network flows and allocating bandwidth resources over time.}
}
```
