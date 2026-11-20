---
name: unknown_workflow_video_sampler_unet_75
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.725
common_nodes: [CLIPLoader, ComfyMathExpression, Label (rgthree), LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine, workflow>运行采样]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3无限视频生成_2096054807244136449.json, 视频生成/文生视频/MiniMax-H3无限视频生成_2096045789138219009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_75

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3无限视频生成_2096054807244136449.json、视频生成/文生视频/MiniMax-H3无限视频生成_2096045789138219009.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `Label (rgthree)`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `workflow>运行采样`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `ReservedVRAMSetter` —— 1/2 个有
- `VRAM_Debug` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
