---
key: 平台全量/抠图工作流大合集（BiRefNet，Ben2，Inspyrenet，SAM3）_2024674321590919170.json
name: 抠图工作流大合集（BiRefNet，Ben2，Inspyrenet，SAM3）_2024674321590919170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/抠图工作流大合集（BiRefNet，Ben2，Inspyrenet，SAM3）_2024674321590919170.json
hash: 971acfe550aefb5a
coverage: 0.72093
learned_at: 2026-11-14 02:06:53
nodes: [MaskPreview, SaveImage, SaveImage, MaskPreview, MaskPreview+, easy sam3ModelLoader, SaveImage, easy sam3ModelLoader, SaveImage, easy showAnything, PreviewImage, easy sam3Visualization, MaskPreview+, PreviewImage, LoadImage, MaskPreview, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SaveImage, LayerMask: BenUltra, InspyrenetRembg, SaveImage, RembgByBiRefNet, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LayerMask: LoadBenModel, LoadRembgByBiRefNetModel, MaskPreview, SaveImage, Reroute, LoadRembgByBiRefNetModel, ImageConcatMulti, LoadImage, RembgByBiRefNet, easy sam3Visualization, SAM3PointCollector, easy sam3ImageSegmentation, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), easy sam3ImageSegmentation]
patterns: []
missing: []
---

# 平台全量/抠图工作流大合集（BiRefNet，Ben2，Inspyrenet，SAM3）_2024674321590919170.json

> 来源文件 `comfyui_library/workflows/平台全量/抠图工作流大合集（BiRefNet，Ben2，Inspyrenet，SAM3）_2024674321590919170.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（43 个）：
- `MaskPreview`
- `SaveImage`
- `SaveImage`
- `MaskPreview`
- `MaskPreview+`
- `easy sam3ModelLoader`
- `SaveImage`
- `easy sam3ModelLoader`
- `SaveImage`
- `easy showAnything`
- `PreviewImage`
- `easy sam3Visualization`
- `MaskPreview+`
- `PreviewImage`
- `LoadImage`
- `MaskPreview`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `LayerMask: BenUltra`
- `InspyrenetRembg`
- `SaveImage`
- `RembgByBiRefNet`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LayerMask: LoadBenModel`
- `LoadRembgByBiRefNetModel`
- `MaskPreview`
- `SaveImage`
- `Reroute`
- `LoadRembgByBiRefNetModel`
- `ImageConcatMulti`
- `LoadImage`
- `RembgByBiRefNet`
- `easy sam3Visualization`
- `SAM3PointCollector`
- `easy sam3ImageSegmentation`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `easy sam3ImageSegmentation`

## 知识

覆盖率 **72%**（31/43）

**有卡**：`MaskPreview`、`SaveImage`、`MaskPreview+`、`easy sam3ModelLoader`、`easy sam3Visualization`、`LoadImage`、`LayerMask: BenUltra`、`InspyrenetRembg`、`RembgByBiRefNet`、`LayerMask: LoadBenModel`、`LoadRembgByBiRefNetModel`、`ImageConcatMulti`、`SAM3PointCollector`、`easy sam3ImageSegmentation`

**用到的条目**：LoadImage、MaskPreview、MaskPreview+、SaveImage、easy sam3ImageSegmentation、easy sam3ModelLoader、easy sam3Visualization、ImageConcatMulti
