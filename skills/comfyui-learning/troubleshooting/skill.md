# Troubleshooting Skill


## Skill Purpose


Troubleshooting Skill 用于帮助 AI Agent 分析 ComfyUI 运行错误。


目标：

不是自动修复。

而是：

- 理解错误
- 定位原因
- 解释影响
- 提供排查方向


---


# Core Ability


Agent 可以分析：


用户:

> ComfyUI 报这个错误是什么意思？


输入：

```
error log
+ workflow
+ node database
+ model database
```


输出：

```
错误类型
可能原因
影响节点
排查步骤
学习解释
```



---


# Supported Problems


## Model Loading Error


例如：


- Cannot load model
- Missing file
- Wrong format



---


## Node Error


例如：


- Node not found
- Missing custom node
- Invalid input



---


## CUDA Error


例如：


- CUDA out of memory
- CUDA error
- Device mismatch



---


## Workflow Error


例如：


- Invalid workflow
- Missing connection
- Wrong parameter



---


# Analysis Pipeline

```
Error Log

    ↓

Error Classification

    ↓

Related Node Search

    ↓

Related Model Search

    ↓

Explanation
```



---


# Design Principle


Agent 不直接修改用户环境。


负责：

- 解释
- 分析
- 指导排查
