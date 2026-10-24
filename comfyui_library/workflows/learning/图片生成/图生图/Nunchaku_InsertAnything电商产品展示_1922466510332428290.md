---
key: 图片生成/图生图/Nunchaku_InsertAnything电商产品展示_1922466510332428290.json
name: Nunchaku_InsertAnything电商产品展示_1922466510332428290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku_InsertAnything电商产品展示_1922466510332428290.json
hash: 0c1d07aebc8ea915
coverage: 0.9
learned_at: 2026-10-23 11:10:05
nodes: [PreviewImage, ImageConcatMulti, LoadImage, PreviewImage, InsertAnythingInferencer, InsertAnythingImageProcessor, ImageConcatMulti, MaskOption, InsertAnythingLoader, MaskOption, LayerMask: MaskGrow, LoadImage, LayerMask: SegmentAnythingUltra V3, LayerMask: SegmentAnythingUltra V3, SaveImage, LayerMask: LoadSegmentAnythingModels, DeepTranslatorTextNode, DeepTranslatorTextNode, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/Nunchaku_InsertAnything电商产品展示_1922466510332428290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku_InsertAnything电商产品展示_1922466510332428290.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（20 个）：
- `PreviewImage`
- `ImageConcatMulti`
- `LoadImage`
- `PreviewImage`
- `InsertAnythingInferencer`
- `InsertAnythingImageProcessor`
- `ImageConcatMulti`
- `MaskOption`
- `InsertAnythingLoader`
- `MaskOption`
- `LayerMask: MaskGrow`
- `LoadImage`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerMask: SegmentAnythingUltra V3`
- `SaveImage`
- `LayerMask: LoadSegmentAnythingModels`
- `DeepTranslatorTextNode`
- `DeepTranslatorTextNode`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`ImageConcatMulti`、`LoadImage`、`InsertAnythingInferencer`、`InsertAnythingImageProcessor`、`MaskOption`、`InsertAnythingLoader`、`LayerMask: MaskGrow`、`LayerMask: SegmentAnythingUltra V3`、`SaveImage`、`LayerMask: LoadSegmentAnythingModels`、`DeepTranslatorTextNode`

**用到的条目**：LoadImage、SaveImage、ImageConcatMulti、DeepTranslatorTextNode、LayerMask: LoadSegmentAnythingModels、LayerMask: MaskGrow、LayerMask: SegmentAnythingUltra V3、InsertAnythingImageProcessor
