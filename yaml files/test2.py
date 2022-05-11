from structurediff import DataComparison, DataFile
import structurediff

comparison = DataComparison(DataFile('example.yaml'), DataFile('example2.yaml'), VERBOSITY)
print(comparison)