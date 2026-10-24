---
key: 图片生成/图生图/Flux最新多重控制EasyControl Depth_1909501750808555521.json
name: Flux最新多重控制EasyControl Depth_1909501750808555521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux最新多重控制EasyControl Depth_1909501750808555521.json
hash: 39057dda5ab57cec
coverage: 1
learned_at: 2026-10-23 11:02:11
nodes: [EasyControlLoadFlux, easy cleanGpuUsed, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, CR Prompt Text, SaveImage, EasyControlLoadLora, EasyControlGenerate]
patterns: []
missing: []
---

# 图片生成/图生图/Flux最新多重控制EasyControl Depth_1909501750808555521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux最新多重控制EasyControl Depth_1909501750808555521.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（9 个）：
- `EasyControlLoadFlux`
- `easy cleanGpuUsed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `CR Prompt Text`
- `SaveImage`
- `EasyControlLoadLora`
- `EasyControlGenerate`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`EasyControlLoadFlux`、`easy cleanGpuUsed`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`LoadImage`、`CR Prompt Text`、`SaveImage`、`EasyControlLoadLora`、`EasyControlGenerate`

**用到的条目**：LoadImage、EasyControlLoadLora、EasyControlLoadFlux、CR Prompt Text、SaveImage、EasyControlGenerate、easy cleanGpuUsed、LayerUtility: ImageScaleByAspectRatio V2
