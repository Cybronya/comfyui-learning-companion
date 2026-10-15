---
key: 图片生成/文生图/Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297.json
name: Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297.json
hash: e26dcdccf78c9d57
coverage: 0.956522
learned_at: 2026-10-15 22:27:37
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, MarkdownNote, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, GetImageRangeFromBatch, VAEDecode, KSamplerAdvanced, UNETLoader, UNETLoader, LoraLoaderModelOnly, easy int, easy int, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, SaveImage, Text, Wan_video_prompt_generator]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `MarkdownNote`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `GetImageRangeFromBatch`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `easy int`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Text`
- `Wan_video_prompt_generator`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `14`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`GetImageRangeFromBatch`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`easy int`、`EmptyHunyuanLatentVideo`、`SaveImage`、`Text`、`Wan_video_prompt_generator`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
