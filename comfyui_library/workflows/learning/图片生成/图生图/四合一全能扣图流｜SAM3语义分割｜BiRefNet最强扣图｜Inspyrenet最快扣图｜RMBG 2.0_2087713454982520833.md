---
key: 图片生成/图生图/四合一全能扣图流｜SAM3语义分割｜BiRefNet最强扣图｜Inspyrenet最快扣图｜RMBG 2.0_2087713454982520833.json
name: 四合一全能扣图流｜SAM3语义分割｜BiRefNet最强扣图｜Inspyrenet最快扣图｜RMBG 2.0_2087713454982520833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/四合一全能扣图流｜SAM3语义分割｜BiRefNet最强扣图｜Inspyrenet最快扣图｜RMBG 2.0_2087713454982520833.json
hash: bf0af49866d0b293
coverage: 0.823529
learned_at: 2026-10-23 12:37:19
nodes: [ImpactInt, RH_Translator, ThresholdMask, LoadRembgByBiRefNetModel, easy sam3ImageSegmentation, RembgByBiRefNet, InspyrenetRembg, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, Any Switch (rgthree), LayerMask: LoadBiRefNetModelV2, easy sam3ModelLoader, RMBG, LayerMask: BiRefNetUltraV2, 孤海注释, Fast Groups Muter (rgthree), LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/四合一全能扣图流｜SAM3语义分割｜BiRefNet最强扣图｜Inspyrenet最快扣图｜RMBG 2.0_2087713454982520833.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/四合一全能扣图流｜SAM3语义分割｜BiRefNet最强扣图｜Inspyrenet最快扣图｜RMBG 2.0_2087713454982520833.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（17 个）：
- `ImpactInt`
- `RH_Translator`
- `ThresholdMask`
- `LoadRembgByBiRefNetModel`
- `easy sam3ImageSegmentation`
- `RembgByBiRefNet`
- `InspyrenetRembg`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `Any Switch (rgthree)`
- `LayerMask: LoadBiRefNetModelV2`
- `easy sam3ModelLoader`
- `RMBG`
- `LayerMask: BiRefNetUltraV2`
- `孤海注释`
- `Fast Groups Muter (rgthree)`
- `LoadImage`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`ImpactInt`、`RH_Translator`、`ThresholdMask`、`LoadRembgByBiRefNetModel`、`easy sam3ImageSegmentation`、`RembgByBiRefNet`、`InspyrenetRembg`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`LayerMask: LoadBiRefNetModelV2`、`easy sam3ModelLoader`、`RMBG`、`LayerMask: BiRefNetUltraV2`、`LoadImage`

**用到的条目**：LoadImage、SaveImage、ImpactInt、RH_Translator、RMBG、InspyrenetRembg、LoadRembgByBiRefNetModel、RembgByBiRefNet
