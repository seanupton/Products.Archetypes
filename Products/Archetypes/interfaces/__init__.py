"""
This file is here to make the module importable.
"""
import Products.Five
from Products.Archetypes import utils
from _annotations import IATAnnotatable, IATAnnotations
from _base import IBaseObject, IBaseContent, IBaseFolder, IBaseUnit
from _field import IField, IObjectField, IImageField, IFileField
from _layer import ILayer, ILayerContainer, ILayerRuntime
from locking import IEditBeginsEvent
from locking import ITTWLockable
from locking import ILock
from locking import IEditEndsEvent
from _marshall import IMarshall
from _orderedfolder import IOrderedFolder, IOrderedContainer
from _referenceable import IReferenceable
from _referenceengine import IReference, IContentReference, IReferenceCatalog, IUIDCatalog
from _schema import ISchema, ISchemata, ICompositeSchema, IBindableSchema, IManagedSchema 
from _storage import IStorage, ISQLStorage
from _templatemixin import ITemplateMixin
from _vocabulary import IVocabulary
from _athistoryaware import IATHistoryAware
from _archetypetool import IArchetypeTool

# BBB
from Interface.bridge import createZope3Bridge

# metadata will follow style of other interfaces come CMF 1.6
from metadata import IExtensibleMetadata
from Products.Five.bridge import fromZ2Interface
IExtensibleMetadata=fromZ2Interface(IExtensibleMetadata)

import annotations
import base
import field
import layer
import marshall
import metadata
import orderedfolder
import referenceable
import referenceengine
import schema
import storage
import vocabulary
import templatemixin
import athistoryaware

# generate zope2 interfaces
_m=utils.makeZ3Bridges
_m(annotations, IATAnnotatable, IATAnnotations)
_m(base, IBaseObject, IBaseContent, IBaseFolder, IBaseUnit)
_m(field, IField, IObjectField, IImageField, IFileField)
_m(layer, ILayer, ILayerContainer, ILayerRuntime)
_m(marshall, IMarshall)
_m(referenceable, IReferenceable)
_m(referenceengine, IReference, IContentReference, IReferenceCatalog, IUIDCatalog)
_m(schema, ISchema, ISchemata, ICompositeSchema, IBindableSchema, IManagedSchema )
_m(storage, IStorage, ISQLStorage)
_m(vocabulary, IVocabulary)
_m(orderedfolder, IOrderedFolder, IOrderedContainer)
_m(templatemixin, ITemplateMixin)
_m(athistoryaware, IATHistoryAware)


