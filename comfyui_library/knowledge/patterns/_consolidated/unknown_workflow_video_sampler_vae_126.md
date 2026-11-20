---
name: unknown_workflow_video_sampler_vae_126
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7132
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan VACE视频编辑参考深度出视频-KJ版_1908545903828082690.json, 视频生成/图生视频/Wan VACE视频编辑根据遮罩编辑视频-KJ版_1908558258645118978.json, 视频生成/图生视频/Wan+VACE视频编辑工作流（5合一完整版）_1922686919644430338.json, 视频生成/图生视频/控制人物动作、跳舞视频、wan2.1 vace_1926291391310184449.json, 视频生成/图生视频/龙明VACE视频编辑工作流（5合一完整版）_1928687484622815233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_126

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan VACE视频编辑参考深度出视频-KJ版_1908545903828082690.json、视频生成/图生视频/Wan VACE视频编辑根据遮罩编辑视频-KJ版_1908558258645118978.json、视频生成/图生视频/Wan+VACE视频编辑工作流（5合一完整版）_1922686919644430338.json、视频生成/图生视频/控制人物动作、跳舞视频、wan2.1 vace_1926291391310184449.json、视频生成/图生视频/龙明VACE视频编辑工作流（5合一完整版）_1928687484622815233.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
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
- `DepthAnything_V2` —— 4/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 4/5 个有
- `easy imageSize` —— 4/5 个有
- `GrowMaskWithBlur` —— 3/5 个有
- `InvertMask` —— 3/5 个有
- `LayerUtility: ColorPicker` —— 3/5 个有
- `MaskPreview+` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `WanVideoVACEModelSelect` —— 3/5 个有
- `DownloadAndLoadSAM2Model` —— 2/5 个有
- `GetImageRangeFromBatch` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `ImagePadKJ` —— 2/5 个有
- `InspyrenetRembg` —— 2/5 个有
- `Pick From Batch (mtb)` —— 2/5 个有
- `PointsEditor` —— 2/5 个有
- `Sam2Segmentation` —— 2/5 个有
- `WanVideoVACEStartToEndFrame` —— 2/5 个有
- `easy imageScaleDownToSize` —— 2/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/5 个有
- `Note _O` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
