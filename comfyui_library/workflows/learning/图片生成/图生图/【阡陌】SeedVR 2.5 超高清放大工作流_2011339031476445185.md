---
key: 图片生成/图生图/【阡陌】SeedVR 2.5 超高清放大工作流_2011339031476445185.json
name: 【阡陌】SeedVR 2.5 超高清放大工作流_2011339031476445185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【阡陌】SeedVR 2.5 超高清放大工作流_2011339031476445185.json
hash: 5c550e3bd62cbf8d
coverage: 0.764706
learned_at: 2026-10-23 11:52:47
nodes: [SaveImage, SaveImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), KOOK_ImageCompression, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, Note, LoadImage, JoinImageWithAlpha, SaveImage, SeedVR2LoadDiTModel, LoadImage, SeedVR2LoadDiTModel]
patterns: []
missing: []
---

# 图片生成/图生图/【阡陌】SeedVR 2.5 超高清放大工作流_2011339031476445185.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【阡陌】SeedVR 2.5 超高清放大工作流_2011339031476445185.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（17 个）：
- `SaveImage`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `KOOK_ImageCompression`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `Note`
- `LoadImage`
- `JoinImageWithAlpha`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `SeedVR2LoadDiTModel`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`KOOK_ImageCompression`、`LoadImage`、`JoinImageWithAlpha`、`SeedVR2LoadDiTModel`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、JoinImageWithAlpha、KOOK_ImageCompression、sd15-t2i-basic
