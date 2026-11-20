---
name: unknown_workflow_video_upscale_latent_upscale_119
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.481
common_nodes: [Anything Everywhere, CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ManualSigmas, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetNode, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 双人角色+音色参考生视频_2042618627672772609.json, 视频生成/图生视频/LTX2.3 音色参考（ID-lora）生视频_2043718764537057282.json, 视频生成/图生视频/LTX2.3+首尾帧gguf_2037924833685671937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_119

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 双人角色+音色参考生视频_2042618627672772609.json、视频生成/图生视频/LTX2.3 音色参考（ID-lora）生视频_2043718764537057282.json、视频生成/图生视频/LTX2.3+首尾帧gguf_2037924833685671937.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ManualSigmas`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 2/3 个有
- `LTXVReferenceAudio` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MelBandRoFormerModelLoader` —— 2/3 个有
- `MelBandRoFormerSampler` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `AudioConcat` —— 1/3 个有
- `ImageAddMulti` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LTXAddVideoICLoRAGuideAdvanced` —— 1/3 个有
- `LTXICLoRALoaderModelOnly` —— 1/3 个有
- `LTXVImgToVideoInplaceKJ` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `TrimVideoLatent` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `VRAMReserver` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
