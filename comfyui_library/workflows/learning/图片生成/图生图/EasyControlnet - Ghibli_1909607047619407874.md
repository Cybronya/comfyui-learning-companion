---
key: 图片生成/图生图/EasyControlnet - Ghibli_1909607047619407874.json
name: EasyControlnet - Ghibli_1909607047619407874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/EasyControlnet - Ghibli_1909607047619407874.json
hash: bdd0433d55ae15d6
coverage: 0.9
learned_at: 2026-10-23 10:52:30
nodes: [EasyControlLoadFlux, easy cleanGpuUsed, SaveImage, LayerUtility: PurgeVRAM, GetImageSize, LoadImage, JjkText, EasyControlLoadLora, ConstrainImage|pysssss, EasyControlGenerate]
patterns: []
missing: []
---

# 图片生成/图生图/EasyControlnet - Ghibli_1909607047619407874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/EasyControlnet - Ghibli_1909607047619407874.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（10 个）：
- `EasyControlLoadFlux`
- `easy cleanGpuUsed`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `GetImageSize`
- `LoadImage`
- `JjkText`
- `EasyControlLoadLora`
- `ConstrainImage|pysssss`
- `EasyControlGenerate`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`EasyControlLoadFlux`、`easy cleanGpuUsed`、`SaveImage`、`LayerUtility: PurgeVRAM`、`GetImageSize`、`LoadImage`、`EasyControlLoadLora`、`ConstrainImage|pysssss`、`EasyControlGenerate`

**用到的条目**：LoadImage、EasyControlLoadLora、EasyControlLoadFlux、GetImageSize、GetImageSize、SaveImage、EasyControlGenerate、ConstrainImage|pysssss
