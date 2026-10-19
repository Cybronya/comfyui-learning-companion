---
name: unknown_workflow_video_upscale_latent_upscale_80
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7374
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSizeAndCount, GetNode, ImageScaleBy, ImpactFloat, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PrimitiveFloat, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, SetNode, StringFunction|pysssss, VAEDecodeTiled, VHS_VideoCombine, easy anythingIndexSwitch, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2009176912333119490.json, 视频生成/图生视频/2037088437668421634.json, 视频生成/图生视频/2037097528180609026.json, 视频生成/文生视频/视频-文生视频扩写-LTX2.0_2009188273779904513.json, 视频生成/文生视频/视频-文生视频扩写-LTX2.3_2037067149814013954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_80

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2009176912333119490.json、视频生成/图生视频/2037088437668421634.json、视频生成/图生视频/2037097528180609026.json、视频生成/文生视频/视频-文生视频扩写-LTX2.0_2009188273779904513.json、视频生成/文生视频/视频-文生视频扩写-LTX2.3_2037067149814013954.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageScaleBy`
- `ImpactFloat`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `StringFunction|pysssss`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 4/5 个有
- `JWFloatToString` —— 4/5 个有
- `LTXVPreprocess` —— 4/5 个有
- `MemoryCleaner` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `easy saveText` —— 4/5 个有
- `EmptyImage` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `LTXVChunkFeedForward` —— 3/5 个有
- `LTXVCropGuides` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `ModelPatchTorchSettings` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `GetImageSize` —— 2/5 个有
- `LTXVImgToVideoConditionOnly` —— 2/5 个有
- `LTXVImgToVideoInplace` —— 2/5 个有
- `LTXVScheduler` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `PrimitiveBoolean` —— 2/5 个有
- `ResizeImagesByLongerEdge` —— 2/5 个有
- `VAEDecode` —— 2/5 个有
- `ComfyMathExpression` —— 1/5 个有
- `FloatConstant` —— 1/5 个有
- `ImageFromBatch` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `ImageLoader` —— 1/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `LTXVImgToVideoInplaceKJ` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `VRAMReserver` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
