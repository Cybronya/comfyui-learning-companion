---
name: unknown_workflow_video_lora_unet_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CLIPLoader, LoraLoaderModelOnly, ModelAttentionBackend, ModelPreviewOverrideKJ, SaveVideo, UNETLoader, VAELoader, easy modelLoaderPack, easy multiTrackEditor, easy multitrackProject, easy multitrackProjectVideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/H3长视频自动化项目流，上下文_分镜自由配置_2095729705352777729.json, 视频生成/文生视频/MiniMaxH3-极简导演台_2095698242704076801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_unet_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/H3长视频自动化项目流，上下文_分镜自由配置_2095729705352777729.json、视频生成/文生视频/MiniMaxH3-极简导演台_2095698242704076801.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`
- `easy modelLoaderPack`
- `easy multiTrackEditor`
- `easy multitrackProject`
- `easy multitrackProjectVideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
