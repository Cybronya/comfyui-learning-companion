---
name: unknown_workflow_video_upscale_latent_upscale_156
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6015
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, ImageResizeKJv2, KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderModelOnly, MMH3LatentUpscaleWithModelParams, MMH3SpatialSplitParams, MMH3TemporalSplitParams, MMH3UltimateUpscale, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SeedNode, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/图生视频/（新）MinimaxH3_R2V-2Stage-VEDA 加速 视频生成工作流_2109325714523774977.json, 视频生成/视频生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_156

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/（新）MinimaxH3_R2V-2Stage-VEDA 加速 视频生成工作流_2109325714523774977.json、视频生成/视频生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MMH3LatentUpscaleWithModelParams`
- `MMH3SpatialSplitParams`
- `MMH3TemporalSplitParams`
- `MMH3UltimateUpscale`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SeedNode`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `Textbox` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VedaSparseAttention` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
