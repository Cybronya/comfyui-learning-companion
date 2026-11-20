---
name: unknown_workflow_video_upscale_latent_upscale_24
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.586667
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, FloatConstant, GetNode, ImageResizeKJv2, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, TTResolutionSelector, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/LTX-2.3 自动四宫格播客一致性工作流 V2.3_2038470088306728961.json, 视频生成/图生视频/5月5图生视频_2051078081040920578.json, 视频生成/图生视频/AI代码侠土豆-LTX-2.3 图生视频（四宫格剧情版）_2034097997692280833.json, 视频生成/图生视频/LTX-2.3 四宫格图生视频（剧情版）_2040707568892387330.json, 视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2038254658686296066.json, 视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2038259870465531906.json, 视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2041784308112822274.json, 视频生成/图生视频/LTX-2.3 图生视频（四宫格）_2054370983934480386.json, 视频生成/图生视频/LTX2.3 四宫格慢剧短片特效+自动提示词_2050099809972965377.json, 视频生成/图生视频/LTX2.3-四宫格剧情生成-音画同步-图生视频_2039166886298001410.json, 视频生成/图生视频/LTX2.3-四宫格图生视频_2052930530554990593.json, 视频生成/图生视频/LTX2.3-数字人唱歌-四宫格分镜-MV视频制作_2054902081458319361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_24

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/LTX-2.3 自动四宫格播客一致性工作流 V2.3_2038470088306728961.json、视频生成/图生视频/5月5图生视频_2051078081040920578.json、视频生成/图生视频/AI代码侠土豆-LTX-2.3 图生视频（四宫格剧情版）_2034097997692280833.json、视频生成/图生视频/LTX-2.3 四宫格图生视频（剧情版）_2040707568892387330.json、视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2038254658686296066.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `FloatConstant`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleBy`
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
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `TTResolutionSelector`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 11/12 个有
- `GuHaiAutoImageSplit` —— 11/12 个有
- `ImageFromBatch+` —— 11/12 个有
- `Int` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `RH_LLMAPI_Pro_Node` —— 11/12 个有
- `Text` —— 11/12 个有
- `CR Text Replace` —— 5/12 个有
- `MultiTextConcatenate` —— 4/12 个有
- `RH_Utils` —— 4/12 个有
- `CustomAddLabel` —— 3/12 个有
- `CR Text` —— 2/12 个有
- `INTConstant` —— 2/12 个有
- `SaveImage` —— 2/12 个有
- `CM_IntToFloat` —— 1/12 个有
- `CR Float To Integer` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `JoinStrings` —— 1/12 个有
- `LTXVAudioVAEEncode` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `PreviewAudio` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `Qwen3_VQA` —— 1/12 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/12 个有
- `RH_Nano_Banana2_Image2Image` —— 1/12 个有
- `SetLatentNoiseMask` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有
- `SolidMask` —— 1/12 个有
- `Text Multiline` —— 1/12 个有
- `VHS_LoadAudioUpload` —— 1/12 个有
- `easy convertAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
