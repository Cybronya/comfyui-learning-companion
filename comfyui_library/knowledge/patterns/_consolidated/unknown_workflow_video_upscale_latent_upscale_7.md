---
name: unknown_workflow_video_upscale_latent_upscale_7
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.595409
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, Int, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, TTResolutionSelector, Text, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3 文&图生视频（双采高动态版）_2042065827050033153.json, 视频生成/图生视频/LTX-2.3首尾帧_2031962115128430594.json, 视频生成/图生视频/LTX-2.3首尾帧（双采高动态版）_2042066721300815873.json, 视频生成/图生视频/LTX2.3四宫格图生视频_2050412323076091906.json, 视频生成/图生视频/opsv-LTX2.3-4帧合一剧情_2050847417603502081.json, 视频生成/图生视频/opsv-LTX2.3-4帧合一剧情_2054591035602423809.json, 视频生成/图生视频/testCl图生视频_2052031676158627841.json, 视频生成/图生视频/testD_2052075045547192321.json, 视频生成/图生视频/【优化版】LTX-2.3首尾帧_2032479656754028546.json, 视频生成/图生视频/万象AI+RH-LTX2.3-四宫格剧情生成-音画同步-图生视频_2042239582070116353.json, 视频生成/图生视频/万象AI+RH-LTX2.3-四宫格剧情生成-音画同步-图生视频_2042767802834100226.json, 视频生成/图生视频/万象AI+RH-LTX2.3-四宫格剧情生成-音画同步-图生视频_2042852519000416258.json, 视频生成/图生视频/万象AI+RH-LTX2.3-四宫格剧情生成-音画同步-图生视频_2053503554211594241.json, 视频生成/图生视频/四宫格剧情视频生成画音同步-LTX-2.3 图生视频_2037164842150268930.json, 视频生成/图生视频/图生视频5号_2052391533508345857.json, 视频生成/图生视频/图生视频三号_2052341833979703297.json, 视频生成/图生视频/小兔图生视频_2050965347808882690.json, 视频生成/图生视频/新新新四宫格图生视频_2050947229229301761.json, 视频生成/图生视频/测试A_断开LLM正面词_2051990736962367489.json, 视频生成/图生视频/测试B_删MultiText_2051999667881295873.json, 视频生成/图生视频/测试版1_随风1秒_2051983699100614658.json, 视频生成/文生视频/LTX2.3-四宫格剧情生成-音画同步-图生视频_2050173609158684674.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_7

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3 文&图生视频（双采高动态版）_2042065827050033153.json、视频生成/图生视频/LTX-2.3首尾帧_2031962115128430594.json、视频生成/图生视频/LTX-2.3首尾帧（双采高动态版）_2042066721300815873.json、视频生成/图生视频/LTX2.3四宫格图生视频_2050412323076091906.json、视频生成/图生视频/opsv-LTX2.3-4帧合一剧情_2050847417603502081.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 22 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `TTResolutionSelector`
- `Text`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplaceKJ` —— 21/22 个有
- `ImageScaleBy` —— 19/22 个有
- `LTXVImgToVideoConditionOnly` —— 19/22 个有
- `CR Text Replace` —— 18/22 个有
- `ComfyMathExpression` —— 18/22 个有
- `FloatConstant` —— 18/22 个有
- `GuHaiAutoImageSplit` —— 18/22 个有
- `ImageFromBatch+` —— 18/22 个有
- `PreviewImage` —— 18/22 个有
- `RH_Utils` —— 16/22 个有
- `MultiTextConcatenate` —— 15/22 个有
- `CR Text` —— 6/22 个有
- `CustomAddLabel` —— 4/22 个有
- `Fast Groups Bypasser (rgthree)` —— 4/22 个有
- `LTXVPreprocess` —— 4/22 个有
- `Label (rgthree)` —— 4/22 个有
- `RH_Nano_Banana2_Image2Image` —— 4/22 个有
- `SaveImage` —— 4/22 个有
- `ImageConcatMulti` —— 3/22 个有
- `DualCLIPLoader` —— 2/22 个有
- `ImageStitch` —— 2/22 个有
- `PreviewAny` —— 2/22 个有
- `ShowText|pysssss` —— 2/22 个有
- `TextGenerateLTX2Prompt` —— 2/22 个有
- `easy convertAnything` —— 2/22 个有
- `PrimitiveBoolean` —— 1/22 个有
- `easy cleanGpuUsed` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 22 | 100% |
| 高度 | 25 | 25 - 25 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，22 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，22 个样本，取值集中（一致性 100%）
