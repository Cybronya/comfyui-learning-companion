---
key: 图片生成/图生图/InfiniteYou StoryDiffusion_1904953215173971969.json
name: InfiniteYou StoryDiffusion_1904953215173971969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/InfiniteYou StoryDiffusion_1904953215173971969.json
hash: a68628c24944bfa6
coverage: 1
learned_at: 2026-10-23 11:03:38
nodes: [EasyFunction_Lite, Storydiffusion_Sampler, Storydiffusion_Model_Loader, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/InfiniteYou StoryDiffusion_1904953215173971969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/InfiniteYou StoryDiffusion_1904953215173971969.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（5 个）：
- `EasyFunction_Lite`
- `Storydiffusion_Sampler` ★核心
- `Storydiffusion_Model_Loader`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **100%**（5/5）

**有卡**：`EasyFunction_Lite`、`Storydiffusion_Sampler`、`Storydiffusion_Model_Loader`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、Storydiffusion_Sampler、SaveImage、EasyFunction_Lite、Storydiffusion_Model_Loader、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
