---
name: unknown_workflow_upscale_latent_upscale_lora_53
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9002
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, Seed Everywhere, Text, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2055146860268015617.json, 视频生成/图生视频/2055152472892690433.json, 视频生成/图生视频/2054821497482555394.json, 视频生成/文生视频/LTX 2.3 图片+音频数字人 2.0｜Dev-Dare 音画驱动增强版_2051714450033524738.json, 视频生成/文生视频/视频-文生视频扩写-LTX2.3-VBVR_2054821471918272513.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_53

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2055146860268015617.json、视频生成/图生视频/2055152472892690433.json、视频生成/图生视频/2054821497482555394.json、视频生成/文生视频/LTX 2.3 图片+音频数字人 2.0｜Dev-Dare 音画驱动增强版_2051714450033524738.json、视频生成/文生视频/视频-文生视频扩写-LTX2.3-VBVR_2054821471918272513.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `Seed Everywhere`
- `Text`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `ImageScaleBy` —— 4/5 个有
- `Int` —— 4/5 个有
- `JWFloatToString` —— 4/5 个有
- `MemoryCleaner` —— 4/5 个有
- `PromptRelaySmartEncode` —— 4/5 个有
- `RH_LLMAPI_NODE` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `StringFunction|pysssss` —— 4/5 个有
- `VRAMReserver` —— 4/5 个有
- `easy anythingIndexSwitch` —— 4/5 个有
- `easy int` —— 4/5 个有
- `easy positive` —— 4/5 个有
- `easy seed` —— 4/5 个有
- `Audio Duration (mtb)` —— 3/5 个有
- `Float` —— 3/5 个有
- `GetLatentSizeAndCount` —— 3/5 个有
- `JWImageResizeByLongerSide` —— 3/5 个有
- `LTXVAudioVAEEncode` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `MelBandRoFormerModelLoader` —— 3/5 个有
- `MelBandRoFormerSampler` —— 3/5 个有
- `Qwen3_VQA_Plus` —— 3/5 个有
- `SetLatentNoiseMask` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `SolidMask` —— 3/5 个有
- `TrimAudioDuration` —— 3/5 个有
- `easy saveText` —— 3/5 个有
- `DisTorchPurgeVRAMV2` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `Image_Resize_longsize` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `Qwen3ASRLoader_DFT` —— 2/5 个有
- `Qwen3ASRTranscribe_DFT` —— 2/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `PromptRelayEncode` —— 1/5 个有
- `image_scale_pixel_v2` —— 1/5 个有

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
