import unittest

from p6_Harbin_Benjamin import Entry, File, Folder, find_large_files


class AbsolutePathTests(unittest.TestCase):
	def test_root_path_contains_only_root(self) -> None:
		root = Folder("root", None)

		self.assertEqual(root.absolute_path(), (root,))

	def test_path_runs_from_entry_to_root(self) -> None:
		root = Folder("root", None)
		folder = Folder("folder", root)
		file_entry = File("file.txt", folder, 4)

		self.assertEqual(file_entry.absolute_path(), (file_entry, folder, root))


class FindLargeFilesTests(unittest.TestCase):
	def test_finds_large_entries_recursively_including_folders(self) -> None:
		root_children: list[Entry] = []
		root = Folder("root", None, root_children)
		folder_children: list[Entry] = []
		folder = Folder("folder", root, folder_children)
		nested_children: list[Entry] = []
		nested = Folder("nested", folder, nested_children)
		large_file = File("large.bin", folder, 10)
		small_file = File("small.bin", folder, 3)
		nested_file = File("nested.bin", nested, 7)
		root_children.append(folder)
		folder_children.extend((large_file, small_file, nested))
		nested_children.append(nested_file)

		self.assertEqual(
			find_large_files(root, 10),
			[root, folder, large_file],
		)

	def test_threshold_is_inclusive_for_nested_files(self) -> None:
		root = Folder("root", None)
		nested_children: list[Entry] = []
		nested = Folder("nested", root, nested_children)
		exact_file = File("exact.bin", nested, 5)
		nested_children.append(exact_file)

		self.assertEqual(find_large_files(nested, 5), [nested, exact_file])


if __name__ == "__main__":
	unittest.main()