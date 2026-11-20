---
name: unknown_workflow_video_inpaint_sampler
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82775
common_nodes: [GrowMaskWithBlur, ImageConcatMulti, ImageResizeKJ, InpaintPreprocessor, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, PDIMAGE_LongerSize, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX视频换脸双倍加速V1.0_1933564125639266306.json, 视频生成/图生视频/VACE 14B SAM2稳定分割主体参考替换（非强控）V1_1924715150803128321.json, 视频生成/图生视频/VACE 14B注意力蒙版视频生视频V2_1922710502047367170.json, 视频生成/图生视频/【视频换脸】FusionX 图生视频一键换脸_1933854710413578242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/FusionX视频换脸双倍加速V1.0_1933564125639266306.json、视频生成/图生视频/VACE 14B SAM2稳定分割主体参考替换（非强控）V1_1924715150803128321.json、视频生成/图生视频/VACE 14B注意力蒙版视频生视频V2_1922710502047367170.json、视频生成/图生视频/【视频换脸】FusionX 图生视频一键换脸_1933854710413578242.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `GrowMaskWithBlur`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PDIMAGE_LongerSize`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch+` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 3/4 个有
- `Note Plus (mtb)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ACE_ImageFaceCrop` —— 2/4 个有
- `APersonMaskGenerator` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有
- `WanVideoEnhanceAVideo` —— 2/4 个有
- `WanVideoExperimentalArgs` —— 2/4 个有
- `WanVideoSLG` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `WanVideoVACEModelSelect` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `LayerMask: LoadFlorence2Model` —— 1/4 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/4 个有
- `LayerMask: ObjectDetectorFL2` —— 1/4 个有
- `LayerMask: SAM2VideoUltra` —— 1/4 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/4 个有
- `MaskPreview` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
