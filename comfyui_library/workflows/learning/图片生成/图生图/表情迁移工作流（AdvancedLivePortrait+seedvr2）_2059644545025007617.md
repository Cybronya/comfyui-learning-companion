---
key: 图片生成/图生图/表情迁移工作流（AdvancedLivePortrait+seedvr2）_2059644545025007617.json
name: 表情迁移工作流（AdvancedLivePortrait+seedvr2）_2059644545025007617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/表情迁移工作流（AdvancedLivePortrait+seedvr2）_2059644545025007617.json
hash: 50ef8955118d8aff
coverage: 0.85
learned_at: 2026-10-23 13:25:32
nodes: [SeedVR2LoadVAEModel, SaveImage, Image Comparer (rgthree), easy int, ImageResize+, Image Comparer (rgthree), easy int, easy int, SeedVR2LoadDiTModel, PreviewImage, ImageResize+, easy cleanGpuUsed, easy clearCacheAll, ImageResize+, SeedVR2VideoUpscaler, LoadImage, ExpressionEditor, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/表情迁移工作流（AdvancedLivePortrait+seedvr2）_2059644545025007617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/表情迁移工作流（AdvancedLivePortrait+seedvr2）_2059644545025007617.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（20 个）：
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `Image Comparer (rgthree)`
- `easy int`
- `ImageResize+`
- `Image Comparer (rgthree)`
- `easy int`
- `easy int`
- `SeedVR2LoadDiTModel`
- `PreviewImage`
- `ImageResize+`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `ImageResize+`
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `ExpressionEditor`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`SeedVR2LoadVAEModel`、`SaveImage`、`easy int`、`ImageResize+`、`SeedVR2LoadDiTModel`、`easy cleanGpuUsed`、`easy clearCacheAll`、`SeedVR2VideoUpscaler`、`LoadImage`、`ExpressionEditor`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、ImageResize+、SaveImage、ExpressionEditor、easy cleanGpuUsed
