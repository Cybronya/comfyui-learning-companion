---
name: unknown_workflow_video_lora_sampler_698
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7415
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSizeAndCount, GetNode, ImpactFloat, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, MemoryCleaner, PrimitiveFloat, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, SetNode, StringFunction|pysssss, VAEDecodeTiled, VHS_VideoCombine, easy anythingIndexSwitch, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [平台全量/视频-视频外扩-LTX2.3_2043961459784290305.json, 视频生成/图生视频/视频-图生视频扩写-LTX2.0_2009176912333119490.json, 视频生成/图生视频/视频-图生视频扩写-LTX2.3_2037088437668421634.json, 视频生成/图生视频/视频-首尾帧视频扩写-LTX2.3_2037097528180609026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_698

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/视频-视频外扩-LTX2.3_2043961459784290305.json、视频生成/图生视频/视频-图生视频扩写-LTX2.0_2009176912333119490.json、视频生成/图生视频/视频-图生视频扩写-LTX2.3_2037088437668421634.json、视频生成/图生视频/视频-首尾帧视频扩写-LTX2.3_2037097528180609026.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `GetNode`
- `ImpactFloat`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MemoryCleaner`
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
- `CM_FloatToInt` —— 3/4 个有
- `ImageScaleBy` —— 3/4 个有
- `JWFloatToString` —— 3/4 个有
- `LTXVAudioVAEDecode` —— 3/4 个有
- `LTXVCropGuides` —— 3/4 个有
- `LTXVLatentUpsampler` —— 3/4 个有
- `LatentUpscaleModelLoader` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `easy saveText` —— 3/4 个有
- `EmptyImage` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `ImageFromBatch` —— 2/4 个有
- `ImageFromBatch+` —— 2/4 个有
- `LTXVChunkFeedForward` —— 2/4 个有
- `LTXVImgToVideoConditionOnly` —— 2/4 个有
- `LTXVImgToVideoInplace` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `ModelPatchTorchSettings` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `Qwen3_VQA` —— 2/4 个有
- `ResizeImagesByLongerEdge` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy imageSize` —— 2/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `FloatConstant` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageLoader` —— 1/4 个有
- `ImagePadKJ` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `LTX2SamplingPreviewOverride` —— 1/4 个有
- `LTXAddVideoICLoRAGuide` —— 1/4 个有
- `LTXICLoRALoaderModelOnly` —— 1/4 个有
- `LTXVImgToVideoInplaceKJ` —— 1/4 个有
- `LTXVScheduler` —— 1/4 个有
- `VAEDecode` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `VHS_VideoInfoLoaded` —— 1/4 个有
- `VRAMReserver` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
