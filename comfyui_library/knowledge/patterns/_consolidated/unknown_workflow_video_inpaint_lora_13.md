---
name: unknown_workflow_video_inpaint_lora_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.588
common_nodes: [BlockifyMask, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetImageSizeAndCount, GetNode, GrowMask, INPAINT_MaskedFill, InvertMask, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, PointsEditor, PreviewAny, PreviewImage, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/VACE局部替换视频替换人物服装赞助商LOGO修复_2067260822749007874.json, 数字人/数字人/视频局部重绘 参考重绘Wan2.1_2056966345102807041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/VACE局部替换视频替换人物服装赞助商LOGO修复_2067260822749007874.json、数字人/数字人/视频局部重绘 参考重绘Wan2.1_2056966345102807041.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INPAINT_MaskedFill`
- `InvertMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PointsEditor`
- `PreviewAny`
- `PreviewImage`
- `Sam2Segmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Float` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageCropByMask` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerMask: BiRefNetUltra` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `Text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
