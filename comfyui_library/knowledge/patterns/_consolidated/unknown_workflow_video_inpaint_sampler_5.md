---
name: unknown_workflow_video_inpaint_sampler_5
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.822833
common_nodes: [GrowMaskWithBlur, ImageConcatMulti, ImageFromBatch+, ImageResizeKJ, InpaintPreprocessor, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PDIMAGE_LongerSize, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/VACE 14B 视频转绘ACC加速换脸V1.0_1927585502306656257.json, 平台全量/【视频换脸】wan2.1+FusionX 图生视频一键换脸_1954131114262720514.json, 平台全量/视频换脸_1959895321860059137.json, 视频生成/图生视频/FusionX视频换脸双倍加速V1.0_1933564125639266306.json, 视频生成/图生视频/VACE 14B SAM2稳定分割主体参考替换（非强控）V1_1924715150803128321.json, 视频生成/图生视频/【视频换脸】FusionX 图生视频一键换脸_1933854710413578242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_5

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/VACE 14B 视频转绘ACC加速换脸V1.0_1927585502306656257.json、平台全量/【视频换脸】wan2.1+FusionX 图生视频一键换脸_1954131114262720514.json、平台全量/视频换脸_1959895321860059137.json、视频生成/图生视频/FusionX视频换脸双倍加速V1.0_1933564125639266306.json、视频生成/图生视频/VACE 14B SAM2稳定分割主体参考替换（非强控）V1_1924715150803128321.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `GrowMaskWithBlur`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PDIMAGE_LongerSize`
- `PreviewImage`
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
- `ACE_ImageFaceCrop` —— 5/6 个有
- `APersonMaskGenerator` —— 5/6 个有
- `RH_Captioner` —— 5/6 个有
- `Text Concatenate` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `Note Plus (mtb)` —— 4/6 个有
- `WanVideoEnhanceAVideo` —— 2/6 个有
- `WanVideoExperimentalArgs` —— 2/6 个有
- `WanVideoSLG` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `WanVideoVACEModelSelect` —— 2/6 个有
- `Crop Face` —— 1/6 个有
- `LayerMask: LoadFlorence2Model` —— 1/6 个有
- `LayerMask: ObjectDetectorFL2` —— 1/6 个有
- `LayerMask: SAM2VideoUltra` —— 1/6 个有
- `MaskPreview` —— 1/6 个有
- `WanVideoLoraSelect` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
