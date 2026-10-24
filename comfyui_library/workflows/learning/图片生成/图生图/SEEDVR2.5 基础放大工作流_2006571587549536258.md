---
key: 图片生成/图生图/SEEDVR2.5 基础放大工作流_2006571587549536258.json
name: SEEDVR2.5 基础放大工作流_2006571587549536258
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SEEDVR2.5 基础放大工作流_2006571587549536258.json
hash: 3f348b92250224e8
coverage: 0.833333
learned_at: 2026-10-23 11:24:02
nodes: [SeedVR2LoadVAEModel, SaveImage, SeedVR2VideoUpscaler, PreviewImage, SeedVR2LoadVAEModel, SaveImage, SeedVR2VideoUpscaler, PreviewImage, LoadImage, LoadImage, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel]
patterns: []
missing: []
---

# 图片生成/图生图/SEEDVR2.5 基础放大工作流_2006571587549536258.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SEEDVR2.5 基础放大工作流_2006571587549536258.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（12 个）：
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadDiTModel`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`SeedVR2LoadVAEModel`、`SaveImage`、`SeedVR2VideoUpscaler`、`LoadImage`、`SeedVR2LoadDiTModel`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
