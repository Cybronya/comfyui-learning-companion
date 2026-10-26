---
key: 图片生成/文生图/Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2114257373773778946.json
name: Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2114257373773778946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2114257373773778946.json
hash: 2e63bc30a2c1941d
coverage: 0.842105
learned_at: 2026-10-26 22:08:43
nodes: [TextEncodeQwenImage21, ResolutionSelector, QwenPERewriteT8, easy showAnything, UNETLoader, EmptyLatentImage, ComfySwitchNode, CLIPLoader, VAELoader, QwenImage21Cache, LoraLoaderModelOnly, CR Prompt Text, VAEDecode, SaveImage, Color Grading JK, LoraLoaderModelOnly, KSampler, LoadImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 768944667022360, "steps": 7, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2114257373773778946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2114257373773778946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `QwenPERewriteT8`
- `easy showAnything`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `VAEDecode` ★核心
- `SaveImage`
- `Color Grading JK`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `768944667022360`
- `steps` = `7`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`TextEncodeQwenImage21`、`ResolutionSelector`、`QwenPERewriteT8`、`UNETLoader`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`CR Prompt Text`、`VAEDecode`、`SaveImage`、`Color Grading JK`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
