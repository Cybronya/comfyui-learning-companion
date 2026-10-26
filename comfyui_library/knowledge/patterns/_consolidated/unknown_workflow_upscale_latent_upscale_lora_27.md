---
name: unknown_workflow_upscale_latent_upscale_lora_27
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.827455
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602.json, 图片生成/文生图/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850.json, 数字人/数字人/LTX2.3数字人25秒长视频工作流 V2.3_2034646872190623745.json, 数字人/数字人/LTX2.3数字人说话唱歌 精准对口型_2059893900621475841.json, 数字人/数字人/最新LTX2.3首尾帧视频工作流 V3.0_2034864223569842177.json, 视频生成/图生视频/ALTX2.3- 小寻唱歌·AI 对口型唱歌 MV 生成器_2089802778116972546.json, 视频生成/图生视频/KK图生视频工作流_2079742870340325377.json, 视频生成/图生视频/LTX 2.3 多人数字人--音频驱动图片生视频_2030885319217782785.json, 视频生成/图生视频/LTX 2.3 多人数字人--音频驱动图片生视频_2031213206097633281.json, 视频生成/图生视频/LTX2.3图生视频说话唱歌_骆驼版本_2037907809546805250.json, 视频生成/图生视频/万象AI真人短剧专用图生视频工作流（LTX2.3自动提示词优化版自动横屏竖屏自动时长）_2040620367496089602.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_27

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602.json、图片生成/文生图/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850.json、数字人/数字人/LTX2.3数字人25秒长视频工作流 V2.3_2034646872190623745.json、数字人/数字人/LTX2.3数字人说话唱歌 精准对口型_2059893900621475841.json、数字人/数字人/最新LTX2.3首尾帧视频工作流 V3.0_2034864223569842177.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVEmptyLatentAudio` —— 10/11 个有
- `PrimitiveBoolean` —— 10/11 个有
- `PrimitiveInt` —— 10/11 个有
- `PrimitiveStringMultiline` —— 10/11 个有
- `ResizeImagesByLongerEdge` —— 10/11 个有
- `LoadAudio` —— 9/11 个有
- `ResizeImageMaskNode` —— 9/11 个有
- `SaveVideo` —— 8/11 个有
- `Int` —— 7/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/11 个有
- `RH_LLMAPI_Pro_Node` —— 7/11 个有
- `easy showAnything` —— 7/11 个有
- `LTXVAudioVAEEncode` —— 6/11 个有
- `SetLatentNoiseMask` —— 6/11 个有
- `SimpleMath+` —— 6/11 个有
- `SolidMask` —— 6/11 个有
- `TrimAudioDuration` —— 6/11 个有
- `CR Text` —— 4/11 个有
- `Any Switch (rgthree)` —— 3/11 个有
- `CM_IntToFloat` —— 3/11 个有
- `CR Integer To String` —— 3/11 个有
- `GetAudioDurationFromAudio` —— 3/11 个有
- `MathExpression|pysssss` —— 3/11 个有
- `RHHiddenNodes` —— 3/11 个有
- `RH_LLMAPI_NODE` —— 3/11 个有
- `VHS_VideoCombine` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `easy promptReplace` —— 3/11 个有
- `CM_FloatToInt` —— 2/11 个有
- `LayerUtility: PurgeVRAM V2` —— 2/11 个有
- `MelBandRoFormerModelLoader` —— 2/11 个有
- `MelBandRoFormerSampler` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `SoundFlow_GetLength` —— 2/11 个有
- `AudioInfo` —— 1/11 个有
- `ConditioningConcat` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LTXVImgToVideoInplaceKJ` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `TT_img_enc_v2` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
