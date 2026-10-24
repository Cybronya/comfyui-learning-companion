---
key: 图片生成/图生图/SEEDVR2放大 图像放大到2K  接入SD-PPP实现 SEEDVR2.5放大_2073377648025358338.json
name: SEEDVR2放大 图像放大到2K  接入SD-PPP实现 SEEDVR2.5放大_2073377648025358338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SEEDVR2放大 图像放大到2K  接入SD-PPP实现 SEEDVR2.5放大_2073377648025358338.json
hash: a64fe1b2f4c15a18
coverage: 0.833333
learned_at: 2026-10-23 11:24:02
nodes: [SaveImage, PreviewImage, SeedVR2LoadVAEModel, LoadImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler]
patterns: []
missing: []
---

# 图片生成/图生图/SEEDVR2放大 图像放大到2K  接入SD-PPP实现 SEEDVR2.5放大_2073377648025358338.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SEEDVR2放大 图像放大到2K  接入SD-PPP实现 SEEDVR2.5放大_2073377648025358338.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（6 个）：
- `SaveImage`
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`

## 知识

覆盖率 **83%**（5/6）

**有卡**：`SaveImage`、`SeedVR2LoadVAEModel`、`LoadImage`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
