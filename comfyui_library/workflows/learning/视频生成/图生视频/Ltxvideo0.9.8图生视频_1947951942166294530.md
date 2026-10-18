---
key: 视频生成/图生视频/Ltxvideo0.9.8图生视频_1947951942166294530.json
name: Ltxvideo0.9.8图生视频_1947951942166294530.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltxvideo0.9.8图生视频_1947951942166294530.json
hash: 6c3931a71c139dd1
coverage: 1
learned_at: 2026-10-15 22:30:46
nodes: [LoadImage, CLIPLoader, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, Int, LTXVImgToVideo, LTXVScheduler, KSamplerSelect, LTXVConditioning, SamplerCustom, VAEDecode, VHS_VideoCombine, ImageResizeKJ, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.8-distilled-fp8.safetensors"}
---

# 视频生成/图生视频/Ltxvideo0.9.8图生视频_1947951942166294530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1947951942166294530.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（15 个）：
- `LoadImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `Int`
- `LTXVImgToVideo`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.8-distilled-fp8.safetensors`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`LoadImage`、`CLIPLoader`、`CLIPTextEncode`、`LTXVPreprocess`、`Int`、`LTXVImgToVideo`、`LTXVScheduler`、`KSamplerSelect`、`LTXVConditioning`、`SamplerCustom`、`VAEDecode`、`VHS_VideoCombine`、`ImageResizeKJ`、`CheckpointLoaderSimple`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、LTXVConditioning
