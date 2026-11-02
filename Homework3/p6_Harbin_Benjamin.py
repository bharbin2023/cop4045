from __future__ import annotations


class Entry:
	def __init__(self, name: str, parent: Entry | None) -> None:
		self.name = name
		self._parent = parent

	def parent(self) -> Entry | None:
		return self._parent

	def absolute_path(self) -> tuple[Entry, ...]:
		if self._parent is None:
			return (self,)
		return (self,) + self._parent.absolute_path()

	def size(self) -> int:
		raise NotImplementedError


class File(Entry):
	def __init__(self, name: str, parent: Entry | None, bytes: int) -> None:
		if bytes < 0:
			raise ValueError("bytes must be nonnegative")
		super().__init__(name, parent)
		self.bytes = bytes

	def size(self) -> int:
		return self.bytes


class Folder(Entry):
	def __init__(self, name: str, parent: Entry | None, children: list[Entry] | None = None) -> None:
		super().__init__(name, parent)
		self._children = children if children is not None else []

	def children(self) -> tuple[Entry, ...]:
		return tuple(self._children)

	def size(self) -> int:
		return sum(child.size() for child in self._children)


def find_large_files(entry: Entry, minimum_size: int) -> list[Entry]:
	results = [entry] if entry.size() >= minimum_size else []
	if isinstance(entry, Folder):
		for child in entry.children():
			results.extend(find_large_files(child, minimum_size))
	return results
