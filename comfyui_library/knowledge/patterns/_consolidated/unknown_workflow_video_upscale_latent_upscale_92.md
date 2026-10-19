---
name: unknown_workflow_video_upscale_latent_upscale_92
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8495
common_nodes: [AudioConcat, CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, DF_Integer, DisTorchPurgeVRAMV2, EmptyLTXVLatentVideo, GetImageSize+, ImageResizeKJv2, ImageSizeInfo, JWImageSequenceExtractFromBatch, JWInteger, JWStringGetLine, JjkConcat, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RH_LLMAPI_Pro_Node, RandomNoise, ResizeLongestToNode, SamplerCustomAdvanced, ShowText, TextBoxMira, VAEDecodeTiled, VHS_MergeImages, VHS_VideoCombine, easy mathInt, easy saveText, easy showAnything, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/图生视频/SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497.json, 视频生成/图生视频/2039591147898675202.json, 视频生成/图生视频/2049764225769283585.json, 视频生成/文生视频/SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_92

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497.json、视频生成/图生视频/2039591147898675202.json、视频生成/图生视频/2049764225769283585.json、视频生成/文生视频/SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioConcat`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `DF_Integer`
- `DisTorchPurgeVRAMV2`
- `EmptyLTXVLatentVideo`
- `GetImageSize+`
- `ImageResizeKJv2`
- `ImageSizeInfo`
- `JWImageSequenceExtractFromBatch`
- `JWInteger`
- `JWStringGetLine`
- `JjkConcat`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `ResizeLongestToNode`
- `SamplerCustomAdvanced`
- `ShowText`
- `TextBoxMira`
- `VAEDecodeTiled`
- `VHS_MergeImages`
- `VHS_VideoCombine`
- `easy mathInt`
- `easy saveText`
- `easy showAnything`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `1hew_ImageGridSplit` —— 3/4 个有
- `If ANY execute A else B` —— 3/4 个有
- `JWStringSplit` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 3/4 个有
- `string_util_StrFind` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有

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
