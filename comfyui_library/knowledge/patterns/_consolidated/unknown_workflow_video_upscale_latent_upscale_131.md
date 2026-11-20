---
name: unknown_workflow_video_upscale_latent_upscale_131
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9295
common_nodes: [BasicGuider, BasicScheduler, BatchImagesNode, CLIPLoader, CR String To Number, ComfyMathExpression, GuHaiAutoImageSplit, ImageBatchMulti, ImageFromBatch+, ImageResizeKJv2, Int, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ExtendCanvasV2, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3ImageToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, SplitSigmas, StringConcatenate, StringSubstring, Text Load Line From File, Text Multiline, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy mathInt, easy showAnything, easy sleep]
problems: []
missing: []
members: [图片生成/图生图/comfyui 工作流_2109468418498981890.json, 视频生成/图生视频/comfyui 工作流_2114318472292429826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_131

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/comfyui 工作流_2109468418498981890.json、视频生成/图生视频/comfyui 工作流_2114318472292429826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CR String To Number`
- `ComfyMathExpression`
- `GuHaiAutoImageSplit`
- `ImageBatchMulti`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ExtendCanvasV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `SplitSigmas`
- `StringConcatenate`
- `StringSubstring`
- `Text Load Line From File`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy mathInt`
- `easy showAnything`
- `easy sleep`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
