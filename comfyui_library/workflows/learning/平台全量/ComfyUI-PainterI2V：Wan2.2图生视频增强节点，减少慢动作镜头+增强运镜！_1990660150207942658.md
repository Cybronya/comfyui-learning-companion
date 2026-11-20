---
key: 平台全量/ComfyUI-PainterI2V：Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜！_1990660150207942658.json
name: ComfyUI-PainterI2V：Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜！_1990660150207942658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI-PainterI2V：Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜！_1990660150207942658.json
hash: 57e46a770207909f
coverage: 0.977778
learned_at: 2026-11-14 00:22:22
nodes: [PathchSageAttentionKJ, VAELoader, PathchSageAttentionKJ, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, KSamplerAdvanced, CLIPLoader, KSamplerAdvanced, VAEDecode, CLIPTextEncode, VAELoader, VHS_VideoCombine, AddLabel, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, easy seed, easy int, ModelSamplingSD3, ModelSamplingSD3, WanImageToVideo, CLIPTextEncode, ImageConcanate, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, easy int, easy int, AddLabel, PrimitiveStringMultiline, CLIPTextEncode, CLIPLoader, WanImageToVideo, LoadImage, PainterI2V, VHS_VideoCombine, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 平台全量/ComfyUI-PainterI2V：Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜！_1990660150207942658.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI-PainterI2V：Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜！_1990660150207942658.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（45 个）：
- `PathchSageAttentionKJ`
- `VAELoader`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VHS_VideoCombine`
- `AddLabel`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy seed`
- `easy int`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy int`
- `easy int`
- `AddLabel`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `WanImageToVideo`
- `LoadImage`
- `PainterI2V`
- `VHS_VideoCombine`
- `Label (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（44/45）

**有卡**：`PathchSageAttentionKJ`、`VAELoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`VHS_VideoCombine`、`AddLabel`、`LoraLoaderModelOnly`、`UNETLoader`、`easy seed`、`easy int`、`WanImageToVideo`、`ImageConcanate`、`LoadImage`、`PainterI2V`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、easy seed
