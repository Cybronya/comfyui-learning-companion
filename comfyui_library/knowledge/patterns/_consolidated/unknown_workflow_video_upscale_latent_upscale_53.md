---
name: unknown_workflow_video_upscale_latent_upscale_53
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.561286
common_nodes: [BasicScheduler, BlockifyMask, CFGGuider, CLIPTextEncode, EmptyImage, GetImageSize, GetImageSize+, GrowMaskWithBlur, ImageCompositeFromMaskBatch+, ImageConcanate, ImageScaleBy, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SimpleCalculatorKJ, SolidMask, VAEDecode, VAEDecodeTiled, VAEEncode, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/LTX2.3 编辑视频 R2V｜（可选）+参考图（指定替换对象）_2046580568468492290.json, 平台全量/LTX2.3局部重绘工作流_2036070204169527297.json, 平台全量/LTX2.3视频局部重绘_2036259073968054274.json, 平台全量/LTX2.3视频局部重绘_2042131429320040450.json, 视频生成/图生视频/LTX2.3 局部修改｜去字幕、去水印 (稳定版) 自动抠图_2045082277629136897.json, 视频生成/文生视频/LTX 2.3 参考引导局部重绘工作流_2041676758285553666.json, 视频生成/文生视频/ltx23_inpaint_masked_Reference2Video 视频编辑工作流_2042807285466009602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_53

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/LTX2.3 编辑视频 R2V｜（可选）+参考图（指定替换对象）_2046580568468492290.json、平台全量/LTX2.3局部重绘工作流_2036070204169527297.json、平台全量/LTX2.3视频局部重绘_2036259073968054274.json、平台全量/LTX2.3视频局部重绘_2042131429320040450.json、视频生成/图生视频/LTX2.3 局部修改｜去字幕、去水印 (稳定版) 自动抠图_2045082277629136897.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `BlockifyMask`
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyImage`
- `GetImageSize`
- `GetImageSize+`
- `GrowMaskWithBlur`
- `ImageCompositeFromMaskBatch+`
- `ImageConcanate`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
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
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SimpleCalculatorKJ`
- `SolidMask`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 6/7 个有
- `INTConstant` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `MaskToImage` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `TrimAudioDuration` —— 6/7 个有
- `DualCLIPLoader` —— 5/7 个有
- `EmptyAudio` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `LTXVAudioVAELoader` —— 5/7 个有
- `CreateVideo` —— 4/7 个有
- `DownloadAndLoadSAM2Model` —— 4/7 个有
- `GetImageRangeFromBatch` —— 4/7 个有
- `ImageInvert` —— 4/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `LTX2SamplingPreviewOverride` —— 4/7 个有
- `PointsEditor` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `Sam2Segmentation` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `RecordAudio` —— 3/7 个有
- `ReservedRegionFrameComposer` —— 3/7 个有
- `ResizeImageMaskNode` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `LTXAVTextEncoderLoader` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `PrimitiveString` —— 2/7 个有
- `RMBG` —— 2/7 个有
- `SAM3Segment` —— 2/7 个有
- `UNETLoader` —— 2/7 个有
- `VAELoaderKJ` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `BiRefNetRMBG` —— 1/7 个有
- `DF_Get_image_size` —— 1/7 个有
- `Image Blank` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `JWImageResizeByLongerSide` —— 1/7 个有
- `JWStringConcat` —— 1/7 个有
- `SeCModelLoader_Ultra-Fast` —— 1/7 个有
- `SeCVideoSegmentation_Ultra-Fast` —— 1/7 个有
- `SeedGenerator` —— 1/7 个有
- `String Literal` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `VRAMReserver` —— 1/7 个有
- `easy mathInt` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `ttN seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 24 | 24 - 24 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，7 个样本，取值集中（一致性 100%）
