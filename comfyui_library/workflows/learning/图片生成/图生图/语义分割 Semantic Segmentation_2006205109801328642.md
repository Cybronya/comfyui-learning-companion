---
key: 图片生成/图生图/语义分割 Semantic Segmentation_2006205109801328642.json
name: 语义分割 Semantic Segmentation_2006205109801328642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/语义分割 Semantic Segmentation_2006205109801328642.json
hash: e66af739203543b7
coverage: 0.777778
learned_at: 2026-10-23 13:27:57
nodes: [ColorPreprocessor, AIO_Preprocessor, PreviewImage, PreviewImage, LoadImage, OneFormer-COCO-SemSegPreprocessor, OneFormer-ADE20K-SemSegPreprocessor, SaveImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/语义分割 Semantic Segmentation_2006205109801328642.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/语义分割 Semantic Segmentation_2006205109801328642.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `ColorPreprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `OneFormer-COCO-SemSegPreprocessor`
- `OneFormer-ADE20K-SemSegPreprocessor`
- `SaveImage`
- `SaveImage`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`ColorPreprocessor`、`AIO_Preprocessor`、`LoadImage`、`OneFormer-COCO-SemSegPreprocessor`、`OneFormer-ADE20K-SemSegPreprocessor`、`SaveImage`

**用到的条目**：LoadImage、SaveImage、AIO_Preprocessor、ColorPreprocessor、OneFormer-COCO-SemSegPreprocessor、OneFormer-ADE20K-SemSegPreprocessor、sd15-t2i-basic、sd15-t2i-lora
