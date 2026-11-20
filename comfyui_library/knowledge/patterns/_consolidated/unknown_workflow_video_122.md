---
name: unknown_workflow_video_122
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.848667
common_nodes: [BBoxesToSAM2, DownloadAndLoadQwenModel, DownloadAndLoadSAM2Model, DrawMaskOnImage, ETN_ApplyMaskToImage, Fast Groups Bypasser (rgthree), GrowMask, ImageConcanate, ImageFromBatch, LayerMask: LoadFlorence2Model, LayerMask: LoadSAM2Model, LayerMask: MaskPreview, LayerMask: ObjectDetectorFL2, LayerMask: SAM2UltraV2, LayerMask: SegmentAnythingUltra V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadImage, MaskPreview+, PreviewImage, QwenVLDetection, Sa2VANodeTpl, Sam2Segmentation, SaveImage, SeCModelLoader_Ultra-Fast, SeCVideoSegmentation_Ultra-Fast, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/Sa2VA最新图像遮罩提取技术_1988894641175007234.json, 平台全量/Sa2VA最新图像遮罩提取技术_1988485945743859714.json, 平台全量/Sa2VA最新图像遮罩提取技术_1989910670126796801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_122

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Sa2VA最新图像遮罩提取技术_1988894641175007234.json、平台全量/Sa2VA最新图像遮罩提取技术_1988485945743859714.json、平台全量/Sa2VA最新图像遮罩提取技术_1989910670126796801.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BBoxesToSAM2`
- `DownloadAndLoadQwenModel`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `ETN_ApplyMaskToImage`
- `Fast Groups Bypasser (rgthree)`
- `GrowMask`
- `ImageConcanate`
- `ImageFromBatch`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: LoadSAM2Model`
- `LayerMask: MaskPreview`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2UltraV2`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `QwenVLDetection`
- `Sa2VANodeTpl`
- `Sam2Segmentation`
- `SaveImage`
- `SeCModelLoader_Ultra-Fast`
- `SeCVideoSegmentation_Ultra-Fast`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerMask: MaskGrow` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
