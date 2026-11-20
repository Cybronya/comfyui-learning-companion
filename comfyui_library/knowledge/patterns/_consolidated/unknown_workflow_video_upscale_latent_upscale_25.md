---
name: unknown_workflow_video_upscale_latent_upscale_25
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.486333
common_nodes: [Anything Everywhere, CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2_NAG, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ManualSigmas, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/「Supermate」LTX2.3-数字人说话&唱歌-加强版_2042665378840584193.json, 视频生成/图生视频/LTX2.3 三图首中尾帧参考_2035556614480076801.json, 视频生成/图生视频/LTX2.3 双人角色+音色参考生视频_2042618627672772609.json, 视频生成/图生视频/LTX2.3 双图首尾帧参考_2035556594234167298.json, 视频生成/图生视频/LTX2.3 数字人说话&唱歌_2035556711162978305.json, 视频生成/图生视频/LTX2.3 音色参考（ID-lora）生视频_2043718764537057282.json, 视频生成/图生视频/LTX2.3-数字人说话唱歌长视频版 图生视频加强版_2060612930189746177.json, 视频生成/图生视频/LTX2.3-数字人说话唱歌长视频版 图生视频加强版_2073725528359661570.json, 视频生成/图生视频/LTX2.3-数字人说话唱歌长视频版 图生视频加强版_2078784827976937473.json, 视频生成/图生视频/LTX2.3-生长视频版数字人说话唱歌图生视频加强版_2060324398200090625.json, 视频生成/图生视频/LTX2.3-生长视频版数字人说话唱歌图生视频加强版_2075890796582236161.json, 视频生成/文生视频/LTX2.3-生长视频版-27秒6分钟生成-数字人说话&唱歌-加强版_2036248412106002433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_25

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/「Supermate」LTX2.3-数字人说话&唱歌-加强版_2042665378840584193.json、视频生成/图生视频/LTX2.3 三图首中尾帧参考_2035556614480076801.json、视频生成/图生视频/LTX2.3 双人角色+音色参考生视频_2042618627672772609.json、视频生成/图生视频/LTX2.3 双图首尾帧参考_2035556594234167298.json、视频生成/图生视频/LTX2.3 数字人说话&唱歌_2035556711162978305.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 11/12 个有
- `MelBandRoFormerModelLoader` —— 10/12 个有
- `MelBandRoFormerSampler` —— 10/12 个有
- `PrimitiveStringMultiline` —— 10/12 个有
- `CR Float To Integer` —— 8/12 个有
- `LTXVAudioVAEEncode` —— 8/12 个有
- `SetLatentNoiseMask` —— 8/12 个有
- `SolidMask` —— 8/12 个有
- `VHS_LoadAudioUpload` —— 8/12 个有
- `easy showAnything` —— 8/12 个有
- `WujiCleaner` —— 7/12 个有
- `LTXVAudioVAEDecode` —— 4/12 个有
- `LTXVEmptyLatentAudio` —— 4/12 个有
- `AudioCrop` —— 2/12 个有
- `CR Text` —— 2/12 个有
- `LTXVImgToVideoInplaceKJ` —— 2/12 个有
- `LTXVReferenceAudio` —— 2/12 个有
- `LoadAudio` —— 2/12 个有
- `LoraLoaderModelOnly` —— 2/12 个有
- `RH_LLMAPI_Pro_Node` —— 2/12 个有
- `ShowText|pysssss` —— 2/12 个有
- `AudioConcat` —— 1/12 个有
- `ImageAddMulti` —— 1/12 个有
- `ImageResizeKJv2` —— 1/12 个有
- `LTXAddVideoICLoRAGuideAdvanced` —— 1/12 个有
- `LTXICLoRALoaderModelOnly` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `TrimVideoLatent` —— 1/12 个有
- `easy imageRemBg` —— 1/12 个有

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
