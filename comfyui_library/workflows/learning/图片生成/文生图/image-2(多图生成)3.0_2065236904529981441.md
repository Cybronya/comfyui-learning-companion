---
key: 图片生成/文生图/image-2(多图生成)3.0_2065236904529981441.json
name: image-2(多图生成)3.0_2065236904529981441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/image-2(多图生成)3.0_2065236904529981441.json
hash: 8e77ea751f67606d
coverage: 0.809524
learned_at: 2026-10-19 23:22:29
nodes: [easy imageScaleDownToSize, SeedVR2LoadVAEModel, Image Comparer (rgthree), easy forLoopEnd, easy showAnything, easy forLoopStart, easy imageSplitGrid, LoadImage, LoadImage, LoadImage, LoadImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SaveImage, Note, SaveImage, easy positive, Note, ComfyUI_Image_Round__ImageCropAdvanced, easy seed, ComfyuiZhangyuAPIImage2Node]
patterns: []
missing: []
---

# 图片生成/文生图/image-2(多图生成)3.0_2065236904529981441.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/image-2(多图生成)3.0_2065236904529981441.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（21 个）：
- `easy imageScaleDownToSize`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `easy forLoopEnd`
- `easy showAnything`
- `easy forLoopStart`
- `easy imageSplitGrid`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Note`
- `SaveImage`
- `easy positive`
- `Note`
- `ComfyUI_Image_Round__ImageCropAdvanced`
- `easy seed`
- `ComfyuiZhangyuAPIImage2Node`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`easy imageScaleDownToSize`、`SeedVR2LoadVAEModel`、`easy forLoopEnd`、`easy forLoopStart`、`easy imageSplitGrid`、`LoadImage`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`easy positive`、`ComfyUI_Image_Round__ImageCropAdvanced`、`easy seed`、`ComfyuiZhangyuAPIImage2Node`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、easy seed、easy imageScaleDownToSize、SaveImage、ComfyUI_Image_Round__ImageCropAdvanced
