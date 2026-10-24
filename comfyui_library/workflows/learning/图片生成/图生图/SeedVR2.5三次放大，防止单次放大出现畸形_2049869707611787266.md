---
key: 图片生成/图生图/SeedVR2.5三次放大，防止单次放大出现畸形_2049869707611787266.json
name: SeedVR2.5三次放大，防止单次放大出现畸形_2049869707611787266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5三次放大，防止单次放大出现畸形_2049869707611787266.json
hash: eac731880edb375a
coverage: 0.52381
learned_at: 2026-10-23 11:25:06
nodes: [SaveImage, INTConstant, Note, Note, Image Comparer (rgthree), Image Comparer (rgthree), SeedVR2VideoUpscaler, SeedVR2VideoUpscaler, Note, Image Comparer (rgthree), Image Comparer (rgthree), LoadImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Note, Note, INTConstant, Note, INTConstant, INTConstant]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5三次放大，防止单次放大出现畸形_2049869707611787266.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5三次放大，防止单次放大出现畸形_2049869707611787266.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（21 个）：
- `SaveImage`
- `INTConstant`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `SeedVR2VideoUpscaler`
- `Note`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Note`
- `Note`
- `INTConstant`
- `Note`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **52%**（11/21）

**有卡**：`SaveImage`、`INTConstant`、`SeedVR2VideoUpscaler`、`LoadImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、INTConstant、sd15-t2i-basic、sd15-t2i-lora
