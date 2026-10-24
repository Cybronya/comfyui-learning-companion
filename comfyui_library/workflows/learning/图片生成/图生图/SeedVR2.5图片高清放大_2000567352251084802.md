---
key: 图片生成/图生图/SeedVR2.5图片高清放大_2000567352251084802.json
name: SeedVR2.5图片高清放大_2000567352251084802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5图片高清放大_2000567352251084802.json
hash: 3a62d098e7415f4b
coverage: 0.8
learned_at: 2026-10-23 11:25:08
nodes: [SeedVR2LoadVAEModel, SimpleMath+, easy cleanGpuUsed, easy imageSizeBySide, PrimitiveFloat, SaveImage, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, LoadImage, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5图片高清放大_2000567352251084802.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5图片高清放大_2000567352251084802.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `SeedVR2LoadVAEModel`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `easy imageSizeBySide`
- `PrimitiveFloat`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **80%**（8/10）

**有卡**：`SeedVR2LoadVAEModel`、`SimpleMath+`、`easy cleanGpuUsed`、`easy imageSizeBySide`、`SaveImage`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、easy imageSizeBySide、SaveImage、easy cleanGpuUsed、SimpleMath+
