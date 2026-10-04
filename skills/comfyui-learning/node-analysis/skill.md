# Node Analysis Skill


## Skill Purpose


Node Analysis Skill 用于让 AI Agent 理解 ComfyUI 节点生态。


负责：

- 扫描 ComfyUI 节点
- 分析节点定义
- 建立节点数据库
- 提供节点搜索能力


---


# Core Ability


Agent 可以回答：


用户：

> KSampler 是什么？


Agent：

读取 node_database:

```
Node:
KSampler

Category:
sampling

Purpose:
扩散采样核心节点

Input:
model
positive
negative
latent

Output:
latent
```



---


# Input Source


主要扫描：


## ComfyUI 原生节点



ComfyUI/nodes.py



## Custom Nodes



ComfyUI/custom_nodes/



---


# Analysis Flow

```
ComfyUI

    |

    v

Node Scanner

    |

    v

Node Metadata

    |

    v

Node Database

    |

    v

Agent Search
```



---


# Design Principle


自动扫描负责：

- 节点发现
- 参数读取
- 结构分析


人工确认负责：

- 节点用途描述
- 使用建议
- 最佳实践


因为节点功能需要上下文理解。
