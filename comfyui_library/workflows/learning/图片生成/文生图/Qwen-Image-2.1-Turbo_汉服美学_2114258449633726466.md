---
key: 图片生成/文生图/Qwen-Image-2.1-Turbo_汉服美学_2114258449633726466.json
name: Qwen-Image-2.1-Turbo_汉服美学_2114258449633726466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-Turbo_汉服美学_2114258449633726466.json
hash: 8ad815bdd7a4606d
coverage: 0.882353
learned_at: 2026-10-26 22:08:43
nodes: [TextEncodeQwenImage21, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, CLIPLoader, VAELoader, QwenImage21Cache, VAEDecode, KSampler, LoraLoaderModelOnly, UNETLoader, Color Grading JK, SaveImage, CR Prompt Text, LoraLoaderModelOnly, LoadImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 420174175766165, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-2.1-Turbo_汉服美学_2114258449633726466.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-Turbo_汉服美学_2114258449633726466.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Color Grading JK`
- `SaveImage`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `420174175766165`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`Color Grading JK`、`SaveImage`、`CR Prompt Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
