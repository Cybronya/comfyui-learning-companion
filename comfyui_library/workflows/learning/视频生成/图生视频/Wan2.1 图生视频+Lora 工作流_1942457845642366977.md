---
key: 视频生成/图生视频/Wan2.1 图生视频+Lora 工作流_1942457845642366977.json
name: Wan2.1 图生视频+Lora 工作流_1942457845642366977.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 图生视频+Lora 工作流_1942457845642366977.json
hash: 2bdb37178ee6e89c
coverage: 1
learned_at: 2026-10-15 22:30:36
nodes: [CLIPTextEncode, CLIPVisionEncode, WanImageToVideo, VAEDecode, KSampler, VHS_VideoCombine, CLIPLoader, CLIPVisionLoader, VAELoader, UNETLoader, WanVideoTeaCacheKJ, LoraLoaderModelOnly, LoadImage, ImageResizeKJ, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 692898559916565, "steps": 20}
---

# 视频生成/图生视频/Wan2.1 图生视频+Lora 工作流_1942457845642366977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1942457845642366977.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（15 个）：
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `WanVideoTeaCacheKJ`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ImageResizeKJ`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `692898559916565`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`CLIPTextEncode`、`CLIPVisionEncode`、`WanImageToVideo`、`VAEDecode`、`KSampler`、`VHS_VideoCombine`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`UNETLoader`、`WanVideoTeaCacheKJ`、`LoraLoaderModelOnly`、`LoadImage`、`ImageResizeKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
