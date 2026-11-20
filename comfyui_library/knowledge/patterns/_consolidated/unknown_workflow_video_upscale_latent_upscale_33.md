---
name: unknown_workflow_video_upscale_latent_upscale_33
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.5939
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, GetImageRangeFromBatch, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/ltx2高清upscale放大模型视频二次高清数字人视频高清（48gb）_2011501078994493441.json, 平台全量/video_ltx2_3_i2v_edit_anything_2032847435281731585.json, 平台全量/video_ltx2_3_inpaint_2053050258128687106.json, 平台全量/video_ltx2_i2v_HD_upscale_basic_2010357744250920961.json, 平台全量/video_ltx2_i2v_upscale_advanced_2010380854765297665.json, 平台全量/视频-主体参考替换-ltx2_3_ref_inpaint_2054752219555221505.json, 平台全量/视频-主体替换-ltx2_3_inpaint_2054752189607890945.json, 视频生成/图生视频/ltx2.3文生视频+局部重绘（根据人物参考图）_2053822010148564993.json, 视频生成/图生视频/video_ltx2_3_ref_inpaint_2053155104752193538.json, 视频生成/文生视频/ltx2.3文生视频+局部重绘_2053834955712671746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_33

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/ltx2高清upscale放大模型视频二次高清数字人视频高清（48gb）_2011501078994493441.json、平台全量/video_ltx2_3_i2v_edit_anything_2032847435281731585.json、平台全量/video_ltx2_3_inpaint_2053050258128687106.json、平台全量/video_ltx2_i2v_HD_upscale_basic_2010357744250920961.json、平台全量/video_ltx2_i2v_upscale_advanced_2010380854765297665.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `GetImageRangeFromBatch`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 9/10 个有
- `ImageResizeKJv2` —— 8/10 个有
- `ComfyMathExpression` —— 7/10 个有
- `EmptyLTXVLatentVideo` —— 7/10 个有
- `LTXVAddGuideMulti` —— 7/10 个有
- `PrimitiveInt` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `VAEDecodeTiled` —— 7/10 个有
- `BasicScheduler` —— 6/10 个有
- `BlockifyMask` —— 6/10 个有
- `CheckpointLoaderSimple` —— 6/10 个有
- `DrawMaskOnImage` —— 6/10 个有
- `GrowMaskWithBlur` —— 6/10 个有
- `MaskToImage` —— 6/10 个有
- `PreviewImage` —— 6/10 个有
- `SAM3_Detect` —— 6/10 个有
- `SAM3_TrackPreview` —— 6/10 个有
- `SAM3_TrackToMask` —— 6/10 个有
- `SAM3_VideoTrack` —— 6/10 个有
- `VHS_VideoInfo` —— 6/10 个有
- `LTXVImgToVideoInplace` —— 4/10 个有
- `LoadImage` —— 4/10 个有
- `VAEDecode` —— 4/10 个有
- `VAEEncode` —— 4/10 个有
- `GetImageSize` —— 3/10 个有
- `ImageScaleBy` —— 3/10 个有
- `ResizeImagesByLongerEdge` —— 3/10 个有
- `VAELoader` —— 3/10 个有
- `GetImageSizeAndCount` —— 2/10 个有
- `ImageConcanate` —— 2/10 个有
- `ImageFromBatch` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `easy seed` —— 2/10 个有
- `GetLatentSizeAndCount` —— 1/10 个有
- `LTXVAudioVAEDecode` —— 1/10 个有

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
