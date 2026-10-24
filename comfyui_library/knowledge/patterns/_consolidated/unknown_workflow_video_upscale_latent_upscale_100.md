---
name: unknown_workflow_video_upscale_latent_upscale_100
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.466
common_nodes: [BasicScheduler, BlockifyMask, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyImage, Fast Groups Bypasser (rgthree), GetImageSize, GetImageSize+, GetNode, GrowMaskWithBlur, INTConstant, ImageCompositeFromMaskBatch+, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PreviewImage, PrimitiveFloat, PrimitiveInt, RandomNoise, ReservedRegionFrameComposer, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAEEncode, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 参考引导局部重绘工作流_2041676758285553666.json, 视频生成/文生视频/ltx23_inpaint_masked_Reference2Video 视频编辑工作流_2042807285466009602.json, 视频生成/文生视频/视频去字幕（参考）-0.5版本 循环_2048762397640364034.json, 视频生成/文生视频/视频去字幕（参考）-0.5版本_2048741719289630722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_100

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 参考引导局部重绘工作流_2041676758285553666.json、视频生成/文生视频/ltx23_inpaint_masked_Reference2Video 视频编辑工作流_2042807285466009602.json、视频生成/文生视频/视频去字幕（参考）-0.5版本 循环_2048762397640364034.json、视频生成/文生视频/视频去字幕（参考）-0.5版本_2048741719289630722.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `BlockifyMask`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetImageSize+`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageCompositeFromMaskBatch+`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ReservedRegionFrameComposer`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `EmptyAudio` —— 3/4 个有
- `ImageFromBatch+` —— 3/4 个有
- `JWImageResizeByLongerSide` —— 3/4 个有
- `RecordAudio` —— 3/4 个有
- `SeCModelLoader_Ultra-Fast` —— 3/4 个有
- `SeCVideoSegmentation_Ultra-Fast` —— 3/4 个有
- `VRAMReserver` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageCropV2` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `LTXVAudioVAEDecode` —— 2/4 个有
- `LTXVLatentUpsampler` —— 2/4 个有
- `MaskRepeatBatch` —— 2/4 个有
- `PrimitiveBoundingBox` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `easy imageSize` —— 2/4 个有
- `BiRefNetRMBG` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `DF_Get_image_size` —— 1/4 个有
- `EmptyLTXVLatentVideo` —— 1/4 个有
- `Image Blank` —— 1/4 个有
- `Int` —— 1/4 个有
- `JWStringConcat` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `RMBG` —— 1/4 个有
- `SAM3Segment` —— 1/4 个有
- `String Literal` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `VHS_BatchManager` —— 1/4 个有
- `easy batchAnything` —— 1/4 个有
- `easy forLoopEnd` —— 1/4 个有
- `easy forLoopStart` —— 1/4 个有
- `easy mathInt` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 24 | 24 - 24 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，4 个样本，取值集中（一致性 100%）
