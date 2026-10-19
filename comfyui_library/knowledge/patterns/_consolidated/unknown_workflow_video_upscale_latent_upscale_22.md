---
name: unknown_workflow_video_upscale_latent_upscale_22
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.595143
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, GuHaiAutoImageSplit, ImageFromBatch+, ImageResizeKJv2, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PreviewImage, PrimitiveFloat, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SetNode, TTResolutionSelector, Text, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2043896162343718913.json, 视频生成/图生视频/2052031676158627841.json, 视频生成/图生视频/2052075045547192321.json, 视频生成/图生视频/2042239582070116353.json, 视频生成/图生视频/2042767802834100226.json, 视频生成/图生视频/2042852519000416258.json, 视频生成/图生视频/2053503554211594241.json, 视频生成/图生视频/2037164842150268930.json, 视频生成/图生视频/2052391533508345857.json, 视频生成/图生视频/2052341833979703297.json, 视频生成/图生视频/2050965347808882690.json, 视频生成/图生视频/2050947229229301761.json, 视频生成/图生视频/2051990736962367489.json, 视频生成/文生视频/LTX2.3-四宫格剧情生成-音画同步-图生视频_2050173609158684674.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_22

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2043896162343718913.json、视频生成/图生视频/2052031676158627841.json、视频生成/图生视频/2052075045547192321.json、视频生成/图生视频/2042239582070116353.json、视频生成/图生视频/2042767802834100226.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveFloat`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `TTResolutionSelector`
- `Text`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 13/14 个有
- `ComfyMathExpression` —— 13/14 个有
- `FloatConstant` —— 13/14 个有
- `ImageScaleBy` —— 13/14 个有
- `Int` —— 13/14 个有
- `SimpleMath+` —— 13/14 个有
- `MultiTextConcatenate` —— 11/14 个有
- `RH_Utils` —— 11/14 个有
- `CR Text` —— 4/14 个有
- `CustomAddLabel` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 2/14 个有
- `Label (rgthree)` —— 2/14 个有
- `RH_Nano_Banana2_Image2Image` —— 2/14 个有
- `SaveImage` —— 2/14 个有
- `ShowText|pysssss` —— 2/14 个有
- `easy convertAnything` —— 2/14 个有
- `Audio Duration (mtb)` —— 1/14 个有
- `LTX2_NAG` —— 1/14 个有
- `LoadAudio` —— 1/14 个有
- `PrimitiveInt` —— 1/14 个有
- `PurgeVRAM_UTK` —— 1/14 个有
- `SaveAudio` —— 1/14 个有
- `SetReserveVRAM` —— 1/14 个有
- `ShowAnything|Mie` —— 1/14 个有
- `SimpleCalculatorKJ` —— 1/14 个有
- `easy mathInt` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
