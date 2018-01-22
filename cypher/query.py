from typing import Iterable, Tuple, Type, Union

from .comparisons import Comparison
from .models import Edge, Model, Node


ModelInstance = Union[
    Model,
    Tuple[Model, str],
]
ModelUnit = Union[
    Model,
    Type[Model],
    Tuple[Model, str],
    Tuple[Type[Model], str],
]
EdgeUnit = Union[
    Edge,
    Type[Edge],
    Tuple[Edge, str],
    Tuple[Type[Edge], str],
]
NodeUnit = Union[
    Node,
    Type[Node],
    Tuple[Node, str],
    Tuple[Type[Node], str],
]


class Query:
    """
    Cypher query builder.
    """
    def create(self, *models: ModelInstance) -> 'Query':
        """
        Schedule models for creation.

        :param models: models to create
        :return: self
        """
        raise NotImplementedError

    def update(self, *models: ModelInstance) -> 'Query':
        """
        Schedule models for update.

        :param models: models to update
        :return: self
        """
        raise NotImplementedError

    def match(self, node: NodeUnit, *where: Comparison) -> 'Query':
        """
        Set the starting node to the cypher `MATCH` query.

        :param node: node to match
        :param where: conditions for the `node` to match
        :return: self
        """
        raise NotImplementedError

    def match_or_create(self, node: NodeUnit, *where: Comparison) -> 'Query':
        """
        Set the starting node to the cypher `MERGE` query.

        :param node: node to match
        :param where: conditions for the `node` to match
        :return: self
        """
        raise NotImplementedError

    def connected_through(self, edge: EdgeUnit, *where: Comparison) -> 'Query':
        """
        Add an edge to the cypher query.

        :param edge: edge to match
        :param where: conditions for the `edge` to match
        :return: self
        """
        raise NotImplementedError

    def to(self, node: NodeUnit, *where: Comparison) -> 'Query':
        """
        Add the right node to the `-[]->` connection in the cypher query.

        :param node: node to match
        :param where: conditions for the `node` to match
        :return: self
        """
        raise NotImplementedError

    def by(self, node: NodeUnit, *where: Comparison) -> 'Query':
        """
        Add the right node to the `<-[]-` connection in the cypher query.

        :param node: node to match
        :param where: conditions for the `node` to match
        :return: self
        """
        raise NotImplementedError

    def where(self, *conditions: Comparison) -> 'Query':
        """
        Add arbitrary conditions.

        :param conditions: conditions to meet
        :return: self
        """
        raise NotImplementedError

    def delete(self, *variables: str) -> 'Query':
        """
        Schedule the models represented by the listed variables for deletion.

        :param variables: models to delete
        :return: self
        """
        raise NotImplementedError

    def result(
        self,
        *variables: str,
        distinct: bool=False,
        limit: int=None,
        skip: int=None,
        order_by: str=None,
    ) -> Iterable:
        """
        Execute the query and map the results.
        
        :param variables: data to return
        :param distinct: add `DISTINCT` to the query
        :param limit: limit the number of results
        :param skip: skip a number of results
        :param order_by: add ordering
        :return: result of the query mapped by appropriate types.
        """
        raise NotImplementedError
