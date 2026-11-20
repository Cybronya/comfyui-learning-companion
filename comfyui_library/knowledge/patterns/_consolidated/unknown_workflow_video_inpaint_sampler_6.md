---
name: unknown_workflow_video_inpaint_sampler_6
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6194
common_nodes: [BlockifyMask, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetImageSizeAndCount, GetNode, GrowMask, INPAINT_MaskedFill, LoadWanVideoT5TextEncoder, PointsEditor, PreviewImage, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.1视频局部重绘-物品迁移_1980574528835338242.json, 平台全量/Wan视频局部重绘工作流 可更换指定产品_1978007177644441601.json, 平台全量/Wan视频局部重绘工作流 文生视频局部重绘_1978122628647018498.json, 数字人/数字人/VACE局部替换视频替换人物服装赞助商LOGO修复_2067260822749007874.json, 数字人/数字人/视频局部重绘 参考重绘Wan2.1_2056966345102807041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/Wan2.1视频局部重绘-物品迁移_1980574528835338242.json、平台全量/Wan视频局部重绘工作流 可更换指定产品_1978007177644441601.json、平台全量/Wan视频局部重绘工作流 文生视频局部重绘_1978122628647018498.json、数字人/数字人/VACE局部替换视频替换人物服装赞助商LOGO修复_2067260822749007874.json、数字人/数字人/视频局部重绘 参考重绘Wan2.1_2056966345102807041.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INPAINT_MaskedFill`
- `LoadWanVideoT5TextEncoder`
- `PointsEditor`
- `PreviewImage`
- `Sam2Segmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 4/5 个有
- `InvertMask` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `WanVideoLoraSelectMulti` —— 4/5 个有
- `AddLabel` —— 3/5 个有
- `EmptyImage` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `ImageResizeKJ` —— 3/5 个有
- `LayerMask: BiRefNetUltra` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `VHS_VideoInfo` —— 2/5 个有
- `BiRefNetRMBG` —— 1/5 个有
- `Float` —— 1/5 个有
- `ImageCropByMask` —— 1/5 个有
- `Int` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `SeCModelLoader` —— 1/5 个有
- `SeCVideoSegmentation` —— 1/5 个有
- `Text` —— 1/5 个有
- `WanVideoLoraSelect` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
