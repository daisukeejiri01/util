# PythonからRスクリプトを呼び出す
import subprocess

# Rスクリプトのパス
path = "" # path to your R script

# PythonからRスクリプトを呼び出す
subprocess.run(["Rscript", path ])