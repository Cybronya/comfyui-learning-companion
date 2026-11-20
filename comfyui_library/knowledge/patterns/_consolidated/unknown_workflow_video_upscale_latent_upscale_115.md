---
name: unknown_workflow_video_upscale_latent_upscale_115
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.517667
common_nodes: [BasicScheduler, BlockifyMask, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, DrawMaskOnImage, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageRangeFromBatch, GetNode, GrowMaskWithBlur, ImageResizeKJv2, KSamplerSelect, LTXVAddGuideMulti, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, MaskToImage, PreviewImage, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SAM3_Detect, SAM3_TrackPreview, SAM3_TrackToMask, SAM3_VideoTrack, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/ltx2.3文生视频+局部重绘（根据人物参考图）_2053822010148564993.json, 视频生成/图生视频/video_ltx2_3_ref_inpaint_2053155104752193538.json, 视频生成/文生视频/ltx2.3文生视频+局部重绘_2053834955712671746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_115

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/ltx2.3文生视频+局部重绘（根据人物参考图）_2053822010148564993.json、视频生成/图生视频/video_ltx2_3_ref_inpaint_2053155104752193538.json、视频生成/文生视频/ltx2.3文生视频+局部重绘_2053834955712671746.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `BlockifyMask`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DrawMaskOnImage`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MaskToImage`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SAM3_Detect`
- `SAM3_TrackPreview`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有

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
