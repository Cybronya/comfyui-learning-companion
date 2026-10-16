---
key: 视频生成/图生视频/Ltxvideo0.9.6图生视频_1920704880137142273.json
name: Ltxvideo0.9.6图生视频_1920704880137142273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1920704880137142273.json
hash: ebacfb616e1c5b7e
coverage: 1
learned_at: 2026-10-15 22:29:42
nodes: [KSamplerSelect, LTXVConditioning, SamplerCustom, CheckpointLoaderSimple, LTXVImgToVideo, CLIPTextEncode, VAEDecode, LTXVScheduler, CLIPTextEncode, ImageResizeKJ, LTXVPreprocess, LoadImage, CLIPLoader, VHS_VideoCombine, Int]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-2b-0.9.6-dev-04-25-v1.safetensors"}
---

# 视频生成/图生视频/Ltxvideo0.9.6图生视频_1920704880137142273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1920704880137142273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（15 个）：
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVImgToVideo`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LTXVScheduler`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `LTXVPreprocess`
- `LoadImage`
- `CLIPLoader`
- `VHS_VideoCombine`
- `Int`

## 关键参数

- `checkpoint` = `ltxv-2b-0.9.6-dev-04-25-v1.safetensors`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`KSamplerSelect`、`LTXVConditioning`、`SamplerCustom`、`CheckpointLoaderSimple`、`LTXVImgToVideo`、`CLIPTextEncode`、`VAEDecode`、`LTXVScheduler`、`ImageResizeKJ`、`LTXVPreprocess`、`LoadImage`、`CLIPLoader`、`VHS_VideoCombine`、`Int`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、LTXVConditioning
