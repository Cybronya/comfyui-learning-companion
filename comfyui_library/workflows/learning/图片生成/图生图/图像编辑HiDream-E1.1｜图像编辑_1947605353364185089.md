---
key: 图片生成/图生图/图像编辑HiDream-E1.1｜图像编辑_1947605353364185089.json
name: 图像编辑HiDream-E1.1｜图像编辑_1947605353364185089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像编辑HiDream-E1.1｜图像编辑_1947605353364185089.json
hash: 84319ee10574f027
coverage: 0.857143
learned_at: 2026-10-23 12:39:03
nodes: [CLIPTextEncode, VAELoader, QuadrupleCLIPLoader, SaveImage, UNETLoader, workflow>IP2PSampler, PreviewImage, easy cleanGpuUsed, LoadImage, CLIPTextEncode, ImageScale, VAEDecode, PIP_图像联结, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/图像编辑HiDream-E1.1｜图像编辑_1947605353364185089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像编辑HiDream-E1.1｜图像编辑_1947605353364185089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `QuadrupleCLIPLoader`
- `SaveImage`
- `UNETLoader` ★核心
- `workflow>IP2PSampler` ★核心
- `PreviewImage`
- `easy cleanGpuUsed`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ImageScale`
- `VAEDecode` ★核心
- `PIP_图像联结`
- `PreviewImage`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CLIPTextEncode`、`VAELoader`、`QuadrupleCLIPLoader`、`SaveImage`、`UNETLoader`、`workflow>IP2PSampler`、`easy cleanGpuUsed`、`LoadImage`、`ImageScale`、`VAEDecode`、`PIP_图像联结`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、workflow>IP2PSampler、QuadrupleCLIPLoader、SaveImage
