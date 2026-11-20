---
key: 平台全量/SeedVRv2.5高清放大_2018696865683873794.json
name: SeedVRv2.5高清放大_2018696865683873794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVRv2.5高清放大_2018696865683873794.json
hash: 5f49abd347fd4d0d
coverage: 0.727273
learned_at: 2026-11-14 01:00:12
nodes: [SeedVR2TorchCompileSettings, Note, JoinImageWithAlpha, Note, SeedVR2VideoUpscaler, Image Comparer (rgthree), LoadImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SaveImage, INTConstant]
patterns: []
missing: []
---

# 平台全量/SeedVRv2.5高清放大_2018696865683873794.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVRv2.5高清放大_2018696865683873794.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（11 个）：
- `SeedVR2TorchCompileSettings`
- `Note`
- `JoinImageWithAlpha`
- `Note`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `INTConstant`

## 知识

覆盖率 **73%**（8/11）

**有卡**：`SeedVR2TorchCompileSettings`、`JoinImageWithAlpha`、`SeedVR2VideoUpscaler`、`LoadImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SaveImage`、`INTConstant`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2TorchCompileSettings、SeedVR2VideoUpscaler、SaveImage、INTConstant、JoinImageWithAlpha
