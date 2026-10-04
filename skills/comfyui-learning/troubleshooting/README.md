# Troubleshooting Skill


## Purpose


让 Agent 理解 ComfyUI 错误。


---


## Input


- Error Log
- Workflow
- Node Database
- Model Database



---


## Output


Error Analysis Report


---


## Example


用户：


CUDA out of memory



Agent:


原因：

当前 Workflow 使用的视频模型较大。

相关因素：

- 模型大小
- 视频长度
- 分辨率

排查：

```
1. 降低 frames
2. 检查 dtype
3. 检查 offload
```
