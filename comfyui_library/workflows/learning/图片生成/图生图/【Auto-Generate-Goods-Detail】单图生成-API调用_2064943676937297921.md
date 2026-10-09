---
key: 图片生成/图生图/【Auto-Generate-Goods-Detail】单图生成-API调用_2064943676937297921.json
name: 【Auto-Generate-Goods-Detail】单图生成-API调用_2064943676937297921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Auto-Generate-Goods-Detail】单图生成-API调用_2064943676937297921.json
hash: 9b8b02274d2b79c8
coverage: 0.692308
learned_at: 2026-10-09 22:36:21
nodes: [LoadImagesFromURL, LoadImagesFromURL, LoadImagesFromURL, LoadImagesFromURL, LoadImagesFromURL, LoadImagesFromURL, Note, PrimitiveString, CR String To Combo, PrimitiveStringMultiline, LoadMultiImage, RH_RhartImageG2ImageToImage, SaveImage]
patterns: []
missing: [CR String To Combo]
discoveries: [次要节点 `CR String To Combo` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/【Auto-Generate-Goods-Detail】单图生成-API调用_2064943676937297921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2064943676937297921.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（13 个）：
- `LoadImagesFromURL`
- `LoadImagesFromURL`
- `LoadImagesFromURL`
- `LoadImagesFromURL`
- `LoadImagesFromURL`
- `LoadImagesFromURL`
- `Note`
- `PrimitiveString`
- `CR String To Combo`
- `PrimitiveStringMultiline`
- `LoadMultiImage`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`

## 知识

覆盖率 **69%**（9/13）

**有卡**：`LoadImagesFromURL`、`LoadMultiImage`、`RH_RhartImageG2ImageToImage`、`SaveImage`

**缺卡**（1）：`CR String To Combo`

**用到的条目**：SaveImage、RH_RhartImageG2ImageToImage、LoadImagesFromURL、LoadMultiImage、sd15-t2i-basic、sd15-t2i-lora、LoadImage、String

## 学习发现

- 次要节点 `CR String To Combo` 知识库中没有该节点类型的任何知识
