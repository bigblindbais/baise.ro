id: iden
group: MLR
title: Identification of Unmodeled Objects via Relational Descriptions
pubkeys: 2017_baisero_identification

Successful human-robot interaction requires advanced communication
algorithms which are able to parse instances of human language and associate
the symbolic components with perceptual representations of the environment.
The identification problem is one instance where this is required, and is
defined as the problem of correctly identifying an object out of many given
a relational description.

The description problem is alike to a standard classification
problem&mdash;each object representing a separate class&mdash;with the key
difference that the number of classes and their associated semantics are not
predefined, but rather differ in problem instance.  As a further consequence,
the output classes also have features associated with them, e.g.  a mug which
could be the object of identification could have measurable features relative
to its color, shape, or position.

<div class="thumbnail">
  <img src="{{ url_for('static', filename='img/iden.png') }}"
    alt="tabletop identification scenario with multiple blocks and the respective identification probabilities"
    />
  <div class="caption">
    Full pipeline composed of perception, segmentation, identification and
    grasp of unmodeled objects.
  </div>
</div>

To address the description problem, we propose a logistic-regression-like
stochastic model which outputs a likelihood over all objects.  The model
exploits contextual information by weighing the significance of each
description predicate by how much other objects in the scenario exhibit that
same property, which in turn allows the given descriptions to be flexibly given
as long as they focus in one way or another on combinations of properties which
make the referent object distinguishible from the rest of the environment.
