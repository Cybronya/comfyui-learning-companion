---
name: unknown_workflow_lora_sampler_clip_11
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.872688
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/LTX-2.3_ICLoRA_Motion_Track运动控制_2073317347884093441.json, 图片生成/文生图/LTX2.3提示词自动优化流_2073313535265951745.json, 图片生成/文生图/LTX2.3提示词自动优化流_2073314279406792706.json, 图片生成/文生图/LTX2.3自动首中尾帧流_2073320995959689218.json, 视频生成/图生视频/2052231209417232385.json, 视频生成/图生视频/2044864850374955009.json, 视频生成/图生视频/2073317124101201921.json, 视频生成/图生视频/2035325472770367490.json, 视频生成/图生视频/2057749829224329218.json, 视频生成/图生视频/2033038199701905410.json, 视频生成/图生视频/2035325465820405761.json, 视频生成/图生视频/2051490555791720450.json, 视频生成/图生视频/2051660543777361922.json, 视频生成/图生视频/2051217425542201345.json, 视频生成/图生视频/2051911216334942209.json, 视频生成/图生视频/2051654152509501441.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/LTX-2.3_ICLoRA_Motion_Track运动控制_2073317347884093441.json、图片生成/文生图/LTX2.3提示词自动优化流_2073313535265951745.json、图片生成/文生图/LTX2.3提示词自动优化流_2073314279406792706.json、图片生成/文生图/LTX2.3自动首中尾帧流_2073320995959689218.json、视频生成/图生视频/2052231209417232385.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
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
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleModelLoader` —— 15/16 个有
- `LoadImage` —— 15/16 个有
- `RH_LLMAPI_Pro_Node` —— 15/16 个有
- `LTXVImgToVideoInplace` —— 14/16 个有
- `LTXVLatentUpsampler` —— 14/16 个有
- `LTXVPreprocess` —— 13/16 个有
- `ResizeImagesByLongerEdge` —— 13/16 个有
- `FloatConstant` —— 12/16 个有
- `LTXVImgToVideoInplaceKJ` —— 12/16 个有
- `LTXVChunkFeedForward` —— 11/16 个有
- `ModelPatchTorchSettings` —— 11/16 个有
- `PathchSageAttentionKJ` —— 11/16 个有
- `SimpleMath+` —— 11/16 个有
- `CR Prompt Text` —— 8/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/16 个有
- `PrimitiveStringMultiline` —— 8/16 个有
- `DualCLIPLoader` —— 7/16 个有
- `PreviewAny` —— 7/16 个有
- `TextGenerateLTX2Prompt` —— 7/16 个有
- `ResizeImageMaskNode` —— 6/16 个有
- `easy int` —— 5/16 个有
- `PrimitiveBoolean` —— 3/16 个有
- `GetImageSize` —— 2/16 个有
- `ImageResizeKJv2` —— 2/16 个有
- `LTXAddVideoICLoRAGuide` —— 2/16 个有
- `LTXICLoRALoaderModelOnly` —— 2/16 个有
- `LTXVImgToVideoConditionOnly` —— 2/16 个有
- `AIO_Preprocessor` —— 1/16 个有
- `CR String To Combo` —— 1/16 个有
- `CR Text Concatenate` —— 1/16 个有
- `Image Resize` —— 1/16 个有
- `ImpactStringSelector` —— 1/16 个有
- `LTX2_NAG` —— 1/16 个有
- `LTXVDrawTracks` —— 1/16 个有
- `LTXVScheduler` —— 1/16 个有
- `LTXVSparseTrackEditor` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `RHHiddenNodes` —— 1/16 个有
- `RH_RhartImageG2TextToImage` —— 1/16 个有
- `Resize` —— 1/16 个有
- `VHS_LoadVideo` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 16 | 100% |
| 高度 | 25 | 25 - 25 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，16 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，16 个样本，取值集中（一致性 100%）
