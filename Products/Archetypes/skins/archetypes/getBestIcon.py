## Script (Python) "getBestIcon"
##title=Find most specific icon for an (sub)object
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
from Products.CMFCore.utils import getToolByName
mtr = getToolByName(context, 'mimetypes_registry', None)
if mtr is None:
    return context.getIcon()
lookup = mtr.lookup(context.getContentType())
if not lookup:
    return context.getIcon()

mti = lookup[0]
return mti.icon_path
