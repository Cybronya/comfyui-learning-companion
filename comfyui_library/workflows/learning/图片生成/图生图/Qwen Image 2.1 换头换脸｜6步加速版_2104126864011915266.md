---
key: 图片生成/图生图/Qwen Image 2.1 换头换脸｜6步加速版_2104126864011915266.json
name: Qwen Image 2.1 换头换脸｜6步加速版_2104126864011915266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 换头换脸｜6步加速版_2104126864011915266.json
hash: ee740af8f6382e3e
coverage: 0.85
learned_at: 2026-10-21 00:42:14
nodes: [CLIPLoader, VAELoader, ConcatTextOfUtils, CR Prompt Text, TextEncodeQwenImage21, UNETLoader, LoraLoaderModelOnly, QwenImage21SageAttentionT8, LoraLoaderBypassModelOnly, KSampler, VAELoader, LoadImage, EmptyLatentImage, LoadImage, ComfySwitchNode, 孤海注释, SaveImage, VAEDecode, PreviewImage, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1600, "sampler_name": "euler", "scheduler": "simple", "seed": 454056675809629, "steps": 6, "width": 1200}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 换头换脸｜6步加速版_2104126864011915266.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 换头换脸｜6步加速版_2104126864011915266.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `ConcatTextOfUtils`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21SageAttentionT8`
- `LoraLoaderBypassModelOnly` ★核心
- `KSampler` ★核心
- `VAELoader`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ComfySwitchNode`
- `孤海注释`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `CR Text`

## 关键参数

- `seed` = `454056675809629`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1200`
- `height` = `1600`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CLIPLoader`、`VAELoader`、`ConcatTextOfUtils`、`CR Prompt Text`、`TextEncodeQwenImage21`、`UNETLoader`、`LoraLoaderModelOnly`、`QwenImage21SageAttentionT8`、`LoraLoaderBypassModelOnly`、`KSampler`、`LoadImage`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
