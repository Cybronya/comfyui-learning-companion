---
key: 图片生成/图生图/图像编辑HiDream-E1.1｜图像风格转换_1947604199786881026.json
name: 图像编辑HiDream-E1.1｜图像风格转换_1947604199786881026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像编辑HiDream-E1.1｜图像风格转换_1947604199786881026.json
hash: 8fae0affbaf6601b
coverage: 0.857143
learned_at: 2026-10-23 12:39:03
nodes: [CLIPTextEncode, VAELoader, QuadrupleCLIPLoader, UNETLoader, workflow>IP2PSampler, ImageScale, PreviewImage, easy cleanGpuUsed, CLIPTextEncode, LoadImage, VAEDecode, PIP_图像联结, SaveImage, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/图像编辑HiDream-E1.1｜图像风格转换_1947604199786881026.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像编辑HiDream-E1.1｜图像风格转换_1947604199786881026.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `QuadrupleCLIPLoader`
- `UNETLoader` ★核心
- `workflow>IP2PSampler` ★核心
- `ImageScale`
- `PreviewImage`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `PIP_图像联结`
- `SaveImage`
- `PreviewImage`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CLIPTextEncode`、`VAELoader`、`QuadrupleCLIPLoader`、`UNETLoader`、`workflow>IP2PSampler`、`ImageScale`、`easy cleanGpuUsed`、`LoadImage`、`VAEDecode`、`PIP_图像联结`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、workflow>IP2PSampler、QuadrupleCLIPLoader、SaveImage
