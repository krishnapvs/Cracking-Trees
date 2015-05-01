class BST(object):
	def __init__(self):
		self.root=None
		self.size=0

	def length(self):
		return self.size

	def __len__(self):
		return self.length

	def __iter__(self):
		return self.root.__iter__()

	def put(self,key,value):
		if self.root:
			self.put_(key,value,self.root)
		else:
			self.root=TreeNode(key,value)
		self.size=self.size+1

	def put_(self,key,value,node):
		if key < node.key:
			if node.hasLeftChild():
				self.put_(key,value,node.left)
			else:
				node.left=TreeNode(key,value, parent=node)
		else:
			if node.hasRightChild():
				self.put_(key,value,node.right)
			else:
				node.right=TreeNode(key,value, parent=node)

	def __setitem__(self,key,value):
		self.put(key,value)

	def get(self,key):
		if self.root:
			res=self.get_(key,self.root)
			if res:
				return res.payload
			else:
				return None
		else:
			return None

	def get_(self,key,node):
		if not node:
			return None
		elif node.key==key:
			return node
		elif key < node.key:
			return self.get_(key,node.left)
		else:
			return self.get_(key,node_right)

	def __getitem__(self,key):
		return self.get(key)

	def __contains__(self,key):
		if self._get(key):
			return True
		else:
			return False

	def delete(self,key):
		if self.size>1:
			node=self.get_(key,self.root)
			if node:
				self.remove(node)
				self.size=self.size-1
		if self.size==1 and self.root.key == key:
			self.root=None
			self.size=0
		else:
			raise KeyError('Error, key not in tree')

	def remove(self,node):
		if node.isLeaf():
			if node.parent.left==node:
				node.parent.left=None
				#del(node)
			else:
				node.parent.right=None
				#del(node)
		if not hasBothChildren:
			if node.hasLeftChild:
				node.left.parent=node.parent
				if node.parent.left==node:
					node.parent.left=node.left
				else:
					node.parent.right=node.left
			else:
				node.right.parent=node.right
				if node.parent.left==node:
					node.parent.left=node.right
				else:
					node.parent.right=node.right

	def __delitem__(self,key):
		self.delete(key)

class TreeNode(object):
	def __init__(self,key,value,left=None,right=None,parent=None):
		self.key=key
		self.left=left
		self.right=right
		self.parent=parent
		self.payload=value

	def hasLeftChild(self):
		if self.left:
			return True
		else:
			return False

	def hasRightChild(self):
		if self.right:
			return True
		else:
			return False

	def isLeftChild(self):
		return self.parent and (self.parent.left==self)

	def isRightChild(self):
		return self.parent and (self.parent.right==self)

	def isRoot(self):
		return not(self.parent)

	def isLeaf(self):
		return not(self.left or self.right)

	def hasAnyChildren(self):
		return self.left or self.right

	def hasBothChildren(self):
		return self.left and self.right

	def replaceNodeData(self,key,value,lc,rc):
		self.key=key
		self.left=lc
		self.right=rc
		self.payload=value
		if self.left:
			self.left.parent=self
		if self.right:
			self.right.parent=self


b=BST()
for i in range(10,0,-1):
	b.put(i,i+1)

print b.root
print b
