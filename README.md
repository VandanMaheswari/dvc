```mkdir dv```

```cd dvc```

```code .```

```conda create -p venv python=3.8 -y```

```source activate ./venv```

```git init```

```touch .gitignore```

```touch README.md```

```pip install -r requirements.txt```

```dvc init```

```dvc repro``` reproducing command to run the stages inside dvc.yaml

```dvc dag``` (directed acyclic graph) to get the graphical represtation of the stage connectivity

```dvc add <file name>```

```git add <file_names> && git commit -m "file added successfully```

```dvc remote add myremote <any_remote_location>```

```dvc push```

```https://dvc.org/doc```