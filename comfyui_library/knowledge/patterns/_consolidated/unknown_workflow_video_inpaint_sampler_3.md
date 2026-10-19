---
name: unknown_workflow_video_inpaint_sampler_3
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.865667
common_nodes: [GrowMaskWithBlur, ImageResizeKJ, InpaintPreprocessor, JjkText, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1927919884900909058.json, 视频生成/图生视频/1927712380627599361.json, 视频生成/图生视频/1943604409752580098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1927919884900909058.json、视频生成/图生视频/1927712380627599361.json、视频生成/图生视频/1943604409752580098.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `GrowMaskWithBlur`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `DownloadAndLoadSAM2Model` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `PointsEditor` —— 1/3 个有
- `PreviewAnimation` —— 1/3 个有
- `Sam2Segmentation` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
