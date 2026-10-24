---
key: 图片生成/图生图/Flux.1 USO 风格迁移工作流，保持主题一致性_1994291088345284609.json
name: Flux.1 USO 风格迁移工作流，保持主题一致性_1994291088345284609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1 USO 风格迁移工作流，保持主题一致性_1994291088345284609.json
hash: 28685056c1cf7109
coverage: 1
learned_at: 2026-10-23 10:58:40
nodes: [RunningHub USO Loader, ImageStitch, LayerUtility: JoyCaptionBeta1, LoadImage, LoadImage, LayerUtility: LoadJoyCaptionBeta1Model, ImageStitch, SaveImage, SaveImage, RunningHub USO Sampler, ImageScaleToTotalPixels, ImageScaleToTotalPixels, GetImageSize]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.1 USO 风格迁移工作流，保持主题一致性_1994291088345284609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1 USO 风格迁移工作流，保持主题一致性_1994291088345284609.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（13 个）：
- `RunningHub USO Loader`
- `ImageStitch`
- `LayerUtility: JoyCaptionBeta1`
- `LoadImage`
- `LoadImage`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `ImageStitch`
- `SaveImage`
- `SaveImage`
- `RunningHub USO Sampler` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `GetImageSize`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`RunningHub USO Loader`、`ImageStitch`、`LayerUtility: JoyCaptionBeta1`、`LoadImage`、`LayerUtility: LoadJoyCaptionBeta1Model`、`SaveImage`、`RunningHub USO Sampler`、`ImageScaleToTotalPixels`、`GetImageSize`

**用到的条目**：LoadImage、RunningHub USO Sampler、GetImageSize、GetImageSize、SaveImage、ImageScaleToTotalPixels、ImageStitch、ImageStitch
