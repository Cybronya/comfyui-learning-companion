---
name: unknown_workflow_video_upscale_latent_upscale_117
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.852333
common_nodes: [AudioConcat, CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, DF_Integer, DisTorchPurgeVRAMV2, EmptyLTXVLatentVideo, GetImageSize+, ImageResizeKJv2, ImageSizeInfo, JWImageSequenceExtractFromBatch, JWInteger, JWStringGetLine, JjkConcat, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RH_LLMAPI_Pro_Node, RandomNoise, ResizeLongestToNode, SamplerCustomAdvanced, ShowText, TextBoxMira, VAEDecodeTiled, VHS_MergeImages, VHS_VideoCombine, easy mathInt, easy saveText, easy showAnything, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/图生视频/三分镜叙事长视频 Gemini优化+LTX 2.3+VBVR 六阶段采样_2039591147898675202.json, 视频生成/图生视频/高动态九分镜视频QWEN3VL+LTX 2_3+VBVR 六阶段采样_2049764225769283585.json, 视频生成/文生视频/SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_117

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/三分镜叙事长视频 Gemini优化+LTX 2.3+VBVR 六阶段采样_2039591147898675202.json、视频生成/图生视频/高动态九分镜视频QWEN3VL+LTX 2_3+VBVR 六阶段采样_2049764225769283585.json、视频生成/文生视频/SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
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
- `1hew_ImageGridSplit` —— 2/3 个有
- `If ANY execute A else B` —— 2/3 个有
- `JWStringSplit` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/3 个有
- `string_util_StrFind` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
