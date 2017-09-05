import {GraphQLSchema} from 'graphql/type/schema';
import {FragmentDefinitionNode} from 'graphql/language/ast';
import {Model, CodegenDocument} from '../models/interfaces';
import pascalCase = require('pascal-case');
import {typeFromAST} from 'graphql/utilities/typeFromAST';
import {print} from 'graphql/language/printer';
import {buildInnerModelsArray} from './inner-models-builer';

export const handleFragment = (schema: GraphQLSchema, fragmentNode: FragmentDefinitionNode, primitivesMap: any, flattenInnerTypes: boolean): CodegenDocument => {
  const rawName = fragmentNode.name.value;
  const fragmentName = pascalCase(rawName);
  const root = typeFromAST(schema, fragmentNode.typeCondition);

  let result: CodegenDocument = {
    name: fragmentName,
    rawName: rawName,
    isQuery: false,
    isSubscription: false,
    isMutation: false,
    isFragment: true,
    innerTypes: [],
    hasInnerTypes: false,
    variables: [],
    hasVariables: false,
    document: print(fragmentNode),
    rootType: []
  };

  let appendTo: Model = {
    name: 'Fragment',
    schemaTypeName: rawName,
    fields: [],
    isObject: true,
    isFragment: true,
    fragmentsUsed: [],
    inlineFragments: []
  };

  result.rootType = [appendTo];
  result.innerTypes = [appendTo, ...buildInnerModelsArray(schema, root, flattenInnerTypes, fragmentNode.selectionSet, primitivesMap, appendTo)];
  result.hasInnerTypes = result.innerTypes.length > 0;

  return result;
};
