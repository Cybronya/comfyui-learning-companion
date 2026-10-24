---
name: unknown_workflow_video_upscale_latent_upscale_14
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.594118
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, TTResolutionSelector, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/5月5图生视频_2051078081040920578.json, 视频生成/图生视频/AI代码侠土豆-LTX-2.3 图生视频（四宫格剧情版）_2034097997692280833.json, 视频生成/图生视频/LTX-2.3 四宫格图生视频（剧情版）_2040707568892387330.json, 视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2038254658686296066.json, 视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2038259870465531906.json, 视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2041784308112822274.json, 视频生成/图生视频/LTX-2.3 图生视频（四宫格）_2054370983934480386.json, 视频生成/图生视频/LTX-2.3 文&图生视频（双采高动态版）_2042065827050033153.json, 视频生成/图生视频/LTX-2.3首尾帧_2031962115128430594.json, 视频生成/图生视频/LTX-2.3首尾帧（双采高动态版）_2042066721300815873.json, 视频生成/图生视频/LTX2.3 四宫格慢剧短片特效+自动提示词_2050099809972965377.json, 视频生成/图生视频/LTX2.3-四宫格剧情生成-音画同步-图生视频_2039166886298001410.json, 视频生成/图生视频/LTX2.3-四宫格图生视频_2052930530554990593.json, 视频生成/图生视频/LTX2.3-数字人唱歌-四宫格分镜-MV视频制作_2054902081458319361.json, 视频生成/图生视频/LTX2.3四宫格图生视频_2050412323076091906.json, 视频生成/图生视频/opsv-LTX2.3-4帧合一剧情_2050847417603502081.json, 视频生成/图生视频/opsv-LTX2.3-4帧合一剧情_2054591035602423809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_14

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/5月5图生视频_2051078081040920578.json、视频生成/图生视频/AI代码侠土豆-LTX-2.3 图生视频（四宫格剧情版）_2034097997692280833.json、视频生成/图生视频/LTX-2.3 四宫格图生视频（剧情版）_2040707568892387330.json、视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2038254658686296066.json、视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2038259870465531906.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `TTResolutionSelector`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 16/17 个有
- `Int` —— 16/17 个有
- `LTXVImgToVideoInplaceKJ` —— 16/17 个有
- `RH_LLMAPI_Pro_Node` —— 16/17 个有
- `Text` —— 16/17 个有
- `ImageScaleBy` —— 15/17 个有
- `LTXVImgToVideoConditionOnly` —— 15/17 个有
- `ComfyMathExpression` —— 14/17 个有
- `FloatConstant` —— 14/17 个有
- `GuHaiAutoImageSplit` —— 13/17 个有
- `ImageFromBatch+` —— 13/17 个有
- `PreviewImage` —— 13/17 个有
- `CR Text Replace` —— 8/17 个有
- `MultiTextConcatenate` —— 7/17 个有
- `RH_Utils` —— 7/17 个有
- `CustomAddLabel` —— 5/17 个有
- `CR Text` —— 4/17 个有
- `Fast Groups Bypasser (rgthree)` —— 3/17 个有
- `LTXVPreprocess` —— 3/17 个有
- `Label (rgthree)` —— 3/17 个有
- `RH_Nano_Banana2_Image2Image` —— 3/17 个有
- `SaveImage` —— 3/17 个有
- `INTConstant` —— 2/17 个有
- `ImageConcatMulti` —— 2/17 个有
- `ImageStitch` —— 2/17 个有
- `CM_IntToFloat` —— 1/17 个有
- `CR Float To Integer` —— 1/17 个有
- `DualCLIPLoader` —— 1/17 个有
- `JoinStrings` —— 1/17 个有
- `LTXVAudioVAEEncode` —— 1/17 个有
- `PreviewAny` —— 1/17 个有
- `PreviewAudio` —— 1/17 个有
- `PrimitiveBoolean` —— 1/17 个有
- `Qwen3_VQA` —— 1/17 个有
- `SetLatentNoiseMask` —— 1/17 个有
- `ShowText|pysssss` —— 1/17 个有
- `SolidMask` —— 1/17 个有
- `Text Multiline` —— 1/17 个有
- `TextGenerateLTX2Prompt` —— 1/17 个有
- `VHS_LoadAudioUpload` —— 1/17 个有
- `easy cleanGpuUsed` —— 1/17 个有
- `easy convertAnything` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 17 | 100% |
| 高度 | 25 | 25 - 25 | 17 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，17 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，17 个样本，取值集中（一致性 100%）
