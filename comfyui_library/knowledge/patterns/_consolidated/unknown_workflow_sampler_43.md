---
name: unknown_workflow_sampler_43
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [LoadAudio, LoadImage, RunningHub DreamID-Omni Loader, RunningHub DreamID-Omni Sampler, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/2033998163958304770.json, 视频生成/文生视频/Dreamid-Omni 音画同步 ComfyUI 工作流_2035627766984478722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_43

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2033998163958304770.json、视频生成/文生视频/Dreamid-Omni 音画同步 ComfyUI 工作流_2035627766984478722.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `LoadImage`
- `RunningHub DreamID-Omni Loader`
- `RunningHub DreamID-Omni Sampler`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
