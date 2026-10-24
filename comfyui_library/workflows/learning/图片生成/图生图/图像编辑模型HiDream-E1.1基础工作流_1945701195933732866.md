---
key: 图片生成/图生图/图像编辑模型HiDream-E1.1基础工作流_1945701195933732866.json
name: 图像编辑模型HiDream-E1.1基础工作流_1945701195933732866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像编辑模型HiDream-E1.1基础工作流_1945701195933732866.json
hash: 74d10d13da89e81b
coverage: 0.916667
learned_at: 2026-10-23 12:39:07
nodes: [CLIPTextEncode, VAELoader, QuadrupleCLIPLoader, SaveImage, UNETLoader, workflow>IP2PSampler, ImageScale, PreviewImage, easy cleanGpuUsed, VAEDecode, LoadImage, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/图像编辑模型HiDream-E1.1基础工作流_1945701195933732866.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像编辑模型HiDream-E1.1基础工作流_1945701195933732866.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `QuadrupleCLIPLoader`
- `SaveImage`
- `UNETLoader` ★核心
- `workflow>IP2PSampler` ★核心
- `ImageScale`
- `PreviewImage`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **92%**（11/12）

**有卡**：`CLIPTextEncode`、`VAELoader`、`QuadrupleCLIPLoader`、`SaveImage`、`UNETLoader`、`workflow>IP2PSampler`、`ImageScale`、`easy cleanGpuUsed`、`VAEDecode`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、workflow>IP2PSampler、QuadrupleCLIPLoader、SaveImage
