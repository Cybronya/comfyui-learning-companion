---
key: 图片生成/图生图/Nunchaku版本InsertAnything_1921815681019363330.json
name: Nunchaku版本InsertAnything_1921815681019363330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku版本InsertAnything_1921815681019363330.json
hash: 8ff46e14d13e4f8a
coverage: 0.933333
learned_at: 2026-10-23 11:10:06
nodes: [InsertAnythingInferencer, CR Prompt Text, LayerMask: SegmentAnythingUltra V3, LayerMask: SegmentAnythingUltra V3, CR Prompt Text, LayerMask: LoadSegmentAnythingModels, PreviewImage, InsertAnythingImageProcessor, MaskOption, LoadImage, LoadImage, SaveImage, MaskOption, InsertAnythingLoader, LayerMask: LoadSegmentAnythingModels]
patterns: []
missing: []
---

# 图片生成/图生图/Nunchaku版本InsertAnything_1921815681019363330.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku版本InsertAnything_1921815681019363330.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（15 个）：
- `InsertAnythingInferencer`
- `CR Prompt Text`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerMask: SegmentAnythingUltra V3`
- `CR Prompt Text`
- `LayerMask: LoadSegmentAnythingModels`
- `PreviewImage`
- `InsertAnythingImageProcessor`
- `MaskOption`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `MaskOption`
- `InsertAnythingLoader`
- `LayerMask: LoadSegmentAnythingModels`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`InsertAnythingInferencer`、`CR Prompt Text`、`LayerMask: SegmentAnythingUltra V3`、`LayerMask: LoadSegmentAnythingModels`、`InsertAnythingImageProcessor`、`MaskOption`、`LoadImage`、`SaveImage`、`InsertAnythingLoader`

**用到的条目**：LoadImage、CR Prompt Text、SaveImage、LayerMask: LoadSegmentAnythingModels、LayerMask: SegmentAnythingUltra V3、InsertAnythingImageProcessor、InsertAnythingInferencer、InsertAnythingLoader
