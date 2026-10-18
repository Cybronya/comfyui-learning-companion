---
key: 视频生成/图生视频/首尾帧图生视频加速版（Wan2.2）_1959534134572036097.json
name: 首尾帧图生视频加速版（Wan2.2）_1959534134572036097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧图生视频加速版（Wan2.2）_1959534134572036097.json
hash: 8fb78fef8bb34edd
coverage: 0.964286
learned_at: 2026-10-15 22:31:24
nodes: [CLIPTextEncode, WanVideoNAG, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, UnetLoaderGGUF, UnetLoaderGGUF, Power Lora Loader (rgthree), ImageScale, ImageScale, Power Lora Loader (rgthree), LoadImage, LoadImage, WanVideoNAG, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, PrimitiveStringMultiline, WanFirstLastFrameToVideo, easy int, easy int, easy int, VHS_VideoCombine, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/首尾帧图生视频加速版（Wan2.2）_1959534134572036097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1959534134572036097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Power Lora Loader (rgthree)`
- `ImageScale`
- `ImageScale`
- `Power Lora Loader (rgthree)`
- `LoadImage`
- `LoadImage`
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `WanFirstLastFrameToVideo`
- `easy int`
- `easy int`
- `easy int`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`CLIPTextEncode`、`WanVideoNAG`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`UnetLoaderGGUF`、`Power Lora Loader (rgthree)`、`ImageScale`、`LoadImage`、`PathchSageAttentionKJ`、`WanFirstLastFrameToVideo`、`easy int`、`VHS_VideoCombine`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、Power Lora Loader (rgthree)、ImageScale
