---
key: 图片生成/图生图/开源最强图片模型_Qwen-image2.1_指定抠图模式_2105107851831234562.json
name: 开源最强图片模型_Qwen-image2.1_指定抠图模式_2105107851831234562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/开源最强图片模型_Qwen-image2.1_指定抠图模式_2105107851831234562.json
hash: ca4128e3a0d90af6
coverage: 0.846154
learned_at: 2026-10-21 00:52:28
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, LoadImage, VAEDecode, CR Text, SaveImage, TextEncodeQwenImage21, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 440178444168320, "steps": 25, "width": 1024}
---

# 图片生成/图生图/开源最强图片模型_Qwen-image2.1_指定抠图模式_2105107851831234562.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/开源最强图片模型_Qwen-image2.1_指定抠图模式_2105107851831234562.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `LoadImage`
- `VAEDecode` ★核心
- `CR Text`
- `SaveImage`
- `TextEncodeQwenImage21`
- `孤海注释`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `440178444168320`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`VAEDecode`、`CR Text`、`SaveImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
