---
key: 图片生成/图生图/Nunchaku_InsertAnything换脸_1922491323624935426.json
name: Nunchaku_InsertAnything换脸_1922491323624935426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku_InsertAnything换脸_1922491323624935426.json
hash: a30f71312a0629a0
coverage: 0.823529
learned_at: 2026-10-23 11:10:05
nodes: [InsertAnythingInferencer, LoadImage, LoadImage, PreviewImage, PreviewImage, SaveImage, InsertAnythingImageProcessor, ImageConcatMulti, LayerMask: PersonMaskUltra V2, ImageConcatMulti, MaskOption, MaskOption, InsertAnythingLoader, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, LayerMask: PersonMaskUltra V2]
patterns: []
missing: []
---

# 图片生成/图生图/Nunchaku_InsertAnything换脸_1922491323624935426.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku_InsertAnything换脸_1922491323624935426.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（17 个）：
- `InsertAnythingInferencer`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `InsertAnythingImageProcessor`
- `ImageConcatMulti`
- `LayerMask: PersonMaskUltra V2`
- `ImageConcatMulti`
- `MaskOption`
- `MaskOption`
- `InsertAnythingLoader`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `LayerMask: PersonMaskUltra V2`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`InsertAnythingInferencer`、`LoadImage`、`SaveImage`、`InsertAnythingImageProcessor`、`ImageConcatMulti`、`LayerMask: PersonMaskUltra V2`、`MaskOption`、`InsertAnythingLoader`、`FaceAnalysisModels`、`FaceEmbedDistance`

**用到的条目**：LoadImage、SaveImage、ImageConcatMulti、FaceAnalysisModels、FaceEmbedDistance、LayerMask: PersonMaskUltra V2、InsertAnythingImageProcessor、InsertAnythingInferencer
