---
key: 图片生成/图生图/大言出法随Flux-Kontext-max+pmrf+invsr双重高清修复放大图像编辑_1929939831818764290.json
name: 大言出法随Flux-Kontext-max+pmrf+invsr双重高清修复放大图像编辑_1929939831818764290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/大言出法随Flux-Kontext-max+pmrf+invsr双重高清修复放大图像编辑_1929939831818764290.json
hash: 500d525cf4dc74f5
coverage: 0.888889
learned_at: 2026-10-23 12:46:34
nodes: [RH_ComfyFluxKontext, SaveImage, LoadImage, InvSRSampler, LoadInvSRModels, PrimitiveStringMultiline, PMRF, LayerUtility: PurgeVRAM V2, ColorMatch]
patterns: []
missing: []
---

# 图片生成/图生图/大言出法随Flux-Kontext-max+pmrf+invsr双重高清修复放大图像编辑_1929939831818764290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/大言出法随Flux-Kontext-max+pmrf+invsr双重高清修复放大图像编辑_1929939831818764290.json`

## 结构

**生成流程**：Sampling → Output → Other

**节点**（9 个）：
- `RH_ComfyFluxKontext`
- `SaveImage`
- `LoadImage`
- `InvSRSampler` ★核心
- `LoadInvSRModels`
- `PrimitiveStringMultiline`
- `PMRF`
- `LayerUtility: PurgeVRAM V2`
- `ColorMatch`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`RH_ComfyFluxKontext`、`SaveImage`、`LoadImage`、`InvSRSampler`、`LoadInvSRModels`、`PMRF`、`LayerUtility: PurgeVRAM V2`、`ColorMatch`

**用到的条目**：LoadImage、InvSRSampler、RH_ComfyFluxKontext、SaveImage、ColorMatch、PMRF、LoadInvSRModels、LayerUtility: PurgeVRAM V2
