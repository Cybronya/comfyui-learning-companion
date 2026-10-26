---
name: unknown_workflow_lora_sampler_clip_161
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.83575
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, GetImageSize, ImageResizeKJv2, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAddGuideMulti, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, VAEDecodeTiled, VHS_LoadVideo]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3 Edit anything 添加_替换_消除_风格转绘_2073320203206873090.json, 图片生成/文生图/LTX2.3局部重绘_2073316928126545922.json, 视频生成/图生视频/LTX2.3-视频局部重绘_2036802494948450306.json, 视频生成/图生视频/添加_替换_消除_风格转绘_2060274127046533121.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_161

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/LTX2.3 Edit anything 添加_替换_消除_风格转绘_2073320203206873090.json、图片生成/文生图/LTX2.3局部重绘_2073316928126545922.json、视频生成/图生视频/LTX2.3-视频局部重绘_2036802494948450306.json、视频生成/图生视频/添加_替换_消除_风格转绘_2060274127046533121.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `ToggleAnyNode` —— 3/4 个有
- `BlockifyMask` —— 2/4 个有
- `CLIPLoader` —— 2/4 个有
- `EmptyImage` —— 2/4 个有
- `EmptyLTXVLatentVideo` —— 2/4 个有
- `GetImageRangeFromBatch` —— 2/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `ImageCompositeFromMaskBatch+` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `LTXVLatentUpsampler` —— 2/4 个有
- `LatentUpscaleModelLoader` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `ResizeImagesByLongerEdge` —— 2/4 个有
- `SAM3Segment` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `TextGenerate` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `MaskToImage` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
