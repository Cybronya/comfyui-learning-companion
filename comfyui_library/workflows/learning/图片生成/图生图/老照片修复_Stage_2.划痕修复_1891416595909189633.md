---
key: 图片生成/图生图/老照片修复_Stage_2.划痕修复_1891416595909189633.json
name: 老照片修复_Stage_2.划痕修复_1891416595909189633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/老照片修复_Stage_2.划痕修复_1891416595909189633.json
hash: 578aba3759a237e6
coverage: 1
learned_at: 2026-10-23 13:22:57
nodes: [BOPBTL_ScratchMask, ComfyUI_Image_Round__ImageRoundAdvanced, BOPBTL_RestoreOldPhotos, ComfyUI_Image_Round__ImageCropAdvanced, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, BOPBTL_LoadScratchMaskModel, BOPBTL_LoadRestoreOldPhotosModel]
patterns: []
missing: []
---

# 图片生成/图生图/老照片修复_Stage_2.划痕修复_1891416595909189633.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/老照片修复_Stage_2.划痕修复_1891416595909189633.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `BOPBTL_ScratchMask`
- `ComfyUI_Image_Round__ImageRoundAdvanced`
- `BOPBTL_RestoreOldPhotos`
- `ComfyUI_Image_Round__ImageCropAdvanced`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `BOPBTL_LoadScratchMaskModel`
- `BOPBTL_LoadRestoreOldPhotosModel`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`BOPBTL_ScratchMask`、`ComfyUI_Image_Round__ImageRoundAdvanced`、`BOPBTL_RestoreOldPhotos`、`ComfyUI_Image_Round__ImageCropAdvanced`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`BOPBTL_LoadScratchMaskModel`、`BOPBTL_LoadRestoreOldPhotosModel`

**用到的条目**：LoadImage、SaveImage、BOPBTL_LoadRestoreOldPhotosModel、BOPBTL_LoadScratchMaskModel、BOPBTL_RestoreOldPhotos、BOPBTL_ScratchMask、ComfyUI_Image_Round__ImageCropAdvanced、ComfyUI_Image_Round__ImageRoundAdvanced
