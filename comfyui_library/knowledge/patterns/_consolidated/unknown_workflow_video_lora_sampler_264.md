---
name: unknown_workflow_video_lora_sampler_264
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.942875
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, CheckpointLoaderSimple, DualCLIPLoader, EmptyLTXVLatentVideo, JWInteger, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PreviewAny, PrimitiveInt, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy convertAnything]
problems: []
missing: []
members: [视频生成/图生视频/2039199521229512706.json, 视频生成/图生视频/2076654345638207490.json, 视频生成/图生视频/2038220174460981249.json, 视频生成/图生视频/LTX2.3-图生视频-没字幕版工作流_2038226644200067073.json, 视频生成/图生视频/2030107128194666498.json, 视频生成/图生视频/2031574051621183490.json, 视频生成/图生视频/2031643477628428290.json, 视频生成/图生视频/2050884030723305474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_264

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2039199521229512706.json、视频生成/图生视频/2076654345638207490.json、视频生成/图生视频/2038220174460981249.json、视频生成/图生视频/LTX2.3-图生视频-没字幕版工作流_2038226644200067073.json、视频生成/图生视频/2030107128194666498.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `JWInteger`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy convertAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 7/8 个有
- `LTXVImgToVideoInplace` —— 7/8 个有
- `LTXVPreprocess` —— 7/8 个有
- `RH_LLMAPI_Pro_Node` —— 7/8 个有
- `LTXVScheduler` —— 6/8 个有
- `SetLatentNoiseMask` —— 6/8 个有
- `SolidMask` —— 6/8 个有
- `LTXVLatentUpsampler` —— 5/8 个有
- `LatentUpscaleModelLoader` —— 5/8 个有
- `ImageSharpen` —— 4/8 个有
- `LTX2SamplingPreviewOverride` —— 4/8 个有
- `LTXVChunkFeedForward` —— 4/8 个有
- `LayerFilter: GaussianBlur` —— 4/8 个有
- `ModelPatchTorchSettings` —— 4/8 个有
- `RTXVideoSuperResolution` —— 4/8 个有
- `VAELoader` —— 3/8 个有
- `ImageFromBatch+` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `LazySwitch1way` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `DuckHideNode` —— 1/8 个有
- `GetImageRangeFromBatch` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `LTXVAddGuideMulti` —— 1/8 个有
- `RH_RhartTextG3ProPreviewImageToText` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `ttN concat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 93 | 93 - 93 | 8 | 100% |
| 高度 | 20 | 20 - 20 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 93，观测区间 93 - 93，8 个样本，取值集中（一致性 100%）
- 高度 中位数 20，观测区间 20 - 20，8 个样本，取值集中（一致性 100%）
