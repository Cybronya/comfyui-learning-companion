---
name: unknown_workflow_video_upscale_latent_upscale_45
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.490333
common_nodes: [Anything Everywhere, CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2_NAG, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2042618627672772609.json, 视频生成/图生视频/2035556711162978305.json, 视频生成/图生视频/2043718764537057282.json, 视频生成/图生视频/2060612930189746177.json, 视频生成/图生视频/2073725528359661570.json, 视频生成/图生视频/2078784827976937473.json, 视频生成/图生视频/2060324398200090625.json, 视频生成/图生视频/2075890796582236161.json, 视频生成/文生视频/LTX2.3-生长视频版-27秒6分钟生成-数字人说话&唱歌-加强版_2036248412106002433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_45

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2042618627672772609.json、视频生成/图生视频/2035556711162978305.json、视频生成/图生视频/2043718764537057282.json、视频生成/图生视频/2060612930189746177.json、视频生成/图生视频/2073725528359661570.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 9 个 workflow 都包含：
- `Anything Everywhere`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 8/9 个有
- `CR Float To Integer` —— 7/9 个有
- `LTXVAudioVAEEncode` —— 7/9 个有
- `SetLatentNoiseMask` —— 7/9 个有
- `SolidMask` —— 7/9 个有
- `VHS_LoadAudioUpload` —— 7/9 个有
- `easy showAnything` —— 7/9 个有
- `WujiCleaner` —— 6/9 个有
- `AudioCrop` —— 2/9 个有
- `LTXVAudioVAEDecode` —— 2/9 个有
- `LTXVEmptyLatentAudio` —— 2/9 个有
- `LTXVReferenceAudio` —— 2/9 个有
- `LoadAudio` —— 2/9 个有
- `LoraLoaderModelOnly` —— 2/9 个有
- `AudioConcat` —— 1/9 个有
- `ImageAddMulti` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `LTXAddVideoICLoRAGuideAdvanced` —— 1/9 个有
- `LTXICLoRALoaderModelOnly` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `TrimVideoLatent` —— 1/9 个有
- `easy imageRemBg` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
