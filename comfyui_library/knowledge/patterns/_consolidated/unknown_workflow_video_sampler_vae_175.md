---
name: unknown_workflow_video_sampler_vae_175
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.704
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LayerUtility: ImageRemoveAlpha, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/FusionX-VACE视频编辑_1934231438495801345.json, 视频生成/图生视频/FusionX-VACE深度_姿势二选一视频转绘_1934166540621107202.json, 视频生成/图生视频/VACE14B视频手工遮罩局部视频编辑_1922883836873510914.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_175

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/FusionX-VACE视频编辑_1934231438495801345.json、视频生成/图生视频/FusionX-VACE深度_姿势二选一视频转绘_1934166540621107202.json、视频生成/图生视频/VACE14B视频手工遮罩局部视频编辑_1922883836873510914.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `DownloadAndLoadSAM2Model` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `InvertMask` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `LayerMask: BiRefNetUltraV2` —— 2/3 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PointsEditor` —— 2/3 个有
- `Sam2Segmentation` —— 2/3 个有
- `WanVideoApplyNAG` —— 2/3 个有
- `WanVideoTeaCache` —— 2/3 个有
- `WanVideoTextEncodeSingle` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `DepthAnything_V2` —— 1/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `LayerUtility: ColorPicker` —— 1/3 个有
- `Pick From Batch (mtb)` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `WanVideoTextEncode` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
