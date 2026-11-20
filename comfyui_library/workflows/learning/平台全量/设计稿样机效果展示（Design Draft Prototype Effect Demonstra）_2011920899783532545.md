---
key: 平台全量/设计稿样机效果展示（Design Draft Prototype Effect Demonstra）_2011920899783532545.json
name: 设计稿样机效果展示（Design Draft Prototype Effect Demonstra）_2011920899783532545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/设计稿样机效果展示（Design Draft Prototype Effect Demonstra）_2011920899783532545.json
hash: bb66e8e1d19bd867
coverage: 0.909091
learned_at: 2026-11-14 02:44:16
nodes: [RH_Nano_Banana_Image2Image, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, UpscaleModelLoader, SaveImage, LoadImage, ImageUpscaleWithModel, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 平台全量/设计稿样机效果展示（Design Draft Prototype Effect Demonstra）_2011920899783532545.json

> 来源文件 `comfyui_library/workflows/平台全量/设计稿样机效果展示（Design Draft Prototype Effect Demonstra）_2011920899783532545.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（11 个）：
- `RH_Nano_Banana_Image2Image`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UpscaleModelLoader`
- `SaveImage`
- `LoadImage`
- `ImageUpscaleWithModel`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`RH_Nano_Banana_Image2Image`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LayerUtility: PurgeVRAM`、`UpscaleModelLoader`、`SaveImage`、`ImageUpscaleWithModel`

**用到的条目**：LoadImage、ImageUpscaleWithModel、UpscaleModelLoader、SaveImage、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、RH_Nano_Banana_Image2Image、image_to_image_controlnet_face_detailer_lora
