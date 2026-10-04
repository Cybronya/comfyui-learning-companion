# Workflow Scanner Tools

## Purpose

这一组工具用于执行 ComfyUI Workflow 自动扫描任务。

功能：

- 扫描 Workflow 文件
- 解析 ComfyUI JSON
- 提取节点信息
- 提取模型信息
- 生成 Workflow Metadata
- 构建 Workflow Manifest


---

# Workflow Scanner Pipeline

```
Workflow Folder

    |

    v

scan_workflows.py

    |

    v

workflow_files.json

    |

    v

extract_nodes.py

    |

    v

extract_workflow_metadata.py

    |

    v

build_manifest.py

    |

    v

workflow_manifest.json
```


---

# Usage


## Scan workflows

```bash
python scan_workflows.py \
    --input ../../../../workflows \
    --output workflow_files.json
```


## Extract Metadata

```bash
python extract_nodes.py \
    --workflow workflow.json

python extract_workflow_metadata.py \
    --workflow workflow.json
```


## Build Database

```bash
python build_manifest.py \
    --input metadata/ \
    --output workflow_manifest.json
```


---

# Design Principle

Scanner 负责：

- 自动发现
- 自动解析
- 自动结构化

不负责：

- 审美评价
- 效果判断
- 创意推荐

这些属于：

workflow-analysis Skill
