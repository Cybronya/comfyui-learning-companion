---
key: 视频生成/图生视频/LTXvideo0.9.6图生视频秒出提示词反推_1922122988903399425.json
name: LTXvideo0.9.6图生视频秒出提示词反推_1922122988903399425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1922122988903399425.json
hash: 4dd61a70c85b9d46
coverage: 1
learned_at: 2026-10-15 22:29:44
nodes: [LoadImage, ImageResizeKJ, CheckpointLoaderSimple, CLIPLoader, LayerMask: LoadFlorence2Model, Florence2, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, Int, LTXVConditioning, KSamplerSelect, LTXVScheduler, LTXVImgToVideo, SamplerCustom, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-2b-0.9.6-dev-04-25-v1.safetensors"}
---

# 视频生成/图生视频/LTXvideo0.9.6图生视频秒出提示词反推_1922122988903399425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1922122988903399425.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `LoadImage`
- `ImageResizeKJ`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `LayerMask: LoadFlorence2Model`
- `Florence2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `Int`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVImgToVideo`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltxv-2b-0.9.6-dev-04-25-v1.safetensors`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`LoadImage`、`ImageResizeKJ`、`CheckpointLoaderSimple`、`CLIPLoader`、`LayerMask: LoadFlorence2Model`、`Florence2`、`CLIPTextEncode`、`LTXVPreprocess`、`Int`、`LTXVConditioning`、`KSamplerSelect`、`LTXVScheduler`、`LTXVImgToVideo`、`SamplerCustom`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、LTXVConditioning
