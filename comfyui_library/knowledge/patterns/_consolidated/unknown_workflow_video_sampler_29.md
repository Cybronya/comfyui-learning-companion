---
name: unknown_workflow_video_sampler_29
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7445
common_nodes: [ImageResizeKJv2, LoadImage, RunningHub VideoAsPrompt Loader, RunningHub VideoAsPrompt Sampler(CogVideoX), VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Video-As-Prompt视频特效迁移大模型_1986433188270665729.json, 视频生成/图生视频/Video-As-Prompt，视频lora终结者？？？_1978743309952765954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_29

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Video-As-Prompt视频特效迁移大模型_1986433188270665729.json、视频生成/图生视频/Video-As-Prompt，视频lora终结者？？？_1978743309952765954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `RunningHub VideoAsPrompt Loader`
- `RunningHub VideoAsPrompt Sampler(CogVideoX)`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
