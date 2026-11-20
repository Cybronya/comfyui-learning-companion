---
name: unknown_workflow_video_sampler_unet_78
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8915
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, Display Any (rgthree), EasyCache, Fast Groups Bypasser (rgthree), ImageResizeKJv2, ImageScaleToMaxDimension, KSamplerSelect, Label (rgthree), LoadImage, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadAudioUpload, VHS_LoadVideo, VHS_VideoCombine, easy seed]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 Turbo加速优化-文生视频_九宫格_四视图生视频_视频全能编辑_2086440255061839873.json, 视频生成/文生视频/MiniMax H3全功能-文生视频_九宫格_四视图生视频_视频全能编辑_2084907936194842625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_78

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Turbo加速优化-文生视频_九宫格_四视图生视频_视频全能编辑_2086440255061839873.json、视频生成/文生视频/MiniMax H3全功能-文生视频_九宫格_四视图生视频_视频全能编辑_2084907936194842625.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `Display Any (rgthree)`
- `EasyCache`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `ImageScaleToMaxDimension`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `ModelPreviewOverrideKJ` —— 1/2 个有
- `VRAM_Debug` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
