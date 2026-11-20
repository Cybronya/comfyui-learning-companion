---
key: 平台全量/SeedVR2.5高清放大与批量拆图工作流 V2.0_2039320315628625921.json
name: SeedVR2.5高清放大与批量拆图工作流 V2.0_2039320315628625921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5高清放大与批量拆图工作流 V2.0_2039320315628625921.json
hash: 3cd586596234d097
coverage: 0.901961
learned_at: 2026-11-14 00:59:40
nodes: [SeedVR2LoadVAEModel, Image Comparer (rgthree), SaveImage, easy clearCacheAll, easy cleanGpuUsed, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, MarkdownNote, MarkdownNote, PreviewImage, ImageScaleToTotalPixels, easy int, easy int, JoinImageWithAlpha, SeedVR2LoadVAEModel, easy mathInt, easy clearCacheAll, easy cleanGpuUsed, SeedVR2VideoUpscaler, Int, RHUploadZip_V2, SeedVR2LoadDiTModel, MarkdownNote, ImageFromBatch+, ImageFromBatch+, LoadImage, JoinImageWithAlpha, JoinImageWithAlpha, JoinImageWithAlpha, JoinImageWithAlpha, JoinImageWithAlpha, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, MarkdownNote, MarkdownNote, PreviewImage, PreviewBridge, PreviewBridge, PreviewBridge, PreviewBridge, PreviewBridge, PreviewBridge, PreviewBridge, PreviewBridge, JoinImageWithAlpha, JoinImageWithAlpha, JoinImageWithAlpha, JoinImageWithAlpha, JoinImageWithAlpha, JoinImageWithAlpha, JoinImageWithAlpha, SaveImage, JoinImageWithAlpha, JoinImageWithAlpha, PreviewBridge, easy imageInsetCrop, PreviewBridge, PreviewBridge, ImageFromBatch+, INTConstant, JoinImageWithAlpha, JoinImageWithAlpha, easy int, GroupSwitcher, SaveImage, HAIGC_SaveImagesToZip, PreviewBridge, PreviewBridge, ImageFromBatch+, easy imageInsetCrop, INTConstant, MarkdownNote, LoadImage, LoadImage, GroupSwitcher, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy cleanGpuUsed, easy clearCacheAll, easy cleanGpuUsed, easy clearCacheAll, ImageTile+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageTile+, SaveImage, ImageBatchMulti, ImageBatchMulti, PreviewImage, easy int, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SeedVR2LoadDiTModel, TextBox]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5高清放大与批量拆图工作流 V2.0_2039320315628625921.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5高清放大与批量拆图工作流 V2.0_2039320315628625921.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（102 个）：
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `SaveImage`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `MarkdownNote`
- `MarkdownNote`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `easy int`
- `easy int`
- `JoinImageWithAlpha`
- `SeedVR2LoadVAEModel`
- `easy mathInt`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `Int`
- `RHUploadZip_V2`
- `SeedVR2LoadDiTModel`
- `MarkdownNote`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `LoadImage`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `MarkdownNote`
- `MarkdownNote`
- `PreviewImage`
- `PreviewBridge`
- `PreviewBridge`
- `PreviewBridge`
- `PreviewBridge`
- `PreviewBridge`
- `PreviewBridge`
- `PreviewBridge`
- `PreviewBridge`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `SaveImage`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `PreviewBridge`
- `easy imageInsetCrop`
- `PreviewBridge`
- `PreviewBridge`
- `ImageFromBatch+`
- `INTConstant`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `easy int`
- `GroupSwitcher`
- `SaveImage`
- `HAIGC_SaveImagesToZip`
- `PreviewBridge`
- `PreviewBridge`
- `ImageFromBatch+`
- `easy imageInsetCrop`
- `INTConstant`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `GroupSwitcher`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `ImageTile+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageTile+`
- `SaveImage`
- `ImageBatchMulti`
- `ImageBatchMulti`
- `PreviewImage`
- `easy int`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadDiTModel`
- `TextBox`

## 知识

覆盖率 **90%**（92/102）

**有卡**：`SeedVR2LoadVAEModel`、`SaveImage`、`easy clearCacheAll`、`easy cleanGpuUsed`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`easy int`、`JoinImageWithAlpha`、`easy mathInt`、`Int`、`RHUploadZip_V2`、`ImageFromBatch+`、`LoadImage`、`PreviewBridge`、`easy imageInsetCrop`、`INTConstant`、`GroupSwitcher`、`HAIGC_SaveImagesToZip`、`ImageTile+`、`ImageBatchMulti`、`TextBox`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、HAIGC_SaveImagesToZip、PreviewBridge、SaveImage、easy cleanGpuUsed
