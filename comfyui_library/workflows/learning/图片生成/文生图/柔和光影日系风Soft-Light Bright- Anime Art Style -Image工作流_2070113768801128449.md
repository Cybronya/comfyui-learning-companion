---
key: 图片生成/文生图/柔和光影日系风Soft-Light Bright- Anime Art Style -Image工作流_2070113768801128449.json
name: 柔和光影日系风Soft-Light Bright- Anime Art Style -Image工作流_2070113768801128449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/柔和光影日系风Soft-Light Bright- Anime Art Style -Image工作流_2070113768801128449.json
hash: e60f563a3bc1d651
coverage: 1
learned_at: 2026-10-19 23:43:32
nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, VAEDecode, KSamplerAdvanced, SaveImage, LoraLoaderModelOnly, VAELoader, UNETLoader, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 9, "denoise": "simple", "height": 1856, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 1280}
---

# 图片生成/文生图/柔和光影日系风Soft-Light Bright- Anime Art Style -Image工作流_2070113768801128449.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/柔和光影日系风Soft-Light Bright- Anime Art Style -Image工作流_2070113768801128449.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（10 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `1280`
- `height` = `1856`
- `batch_size` = `1`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAEDecode`、`KSamplerAdvanced`、`SaveImage`、`LoraLoaderModelOnly`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
