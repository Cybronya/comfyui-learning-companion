---
key: 图片生成/文生图/【遇见AI】qwen image 2.1 官方turbo加速lora文生图基础流_2108863647031320578.json
name: 【遇见AI】qwen image 2.1 官方turbo加速lora文生图基础流_2108863647031320578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【遇见AI】qwen image 2.1 官方turbo加速lora文生图基础流_2108863647031320578.json
hash: 3af08bbb05dbba56
coverage: 0.923077
learned_at: 2026-10-21 02:58:09
nodes: [ResolutionSelector, EmptyLatentImage, KSampler, LoadImage, MarkdownNote, LoadImage, CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, TextEncodeQwenImage21, VAEDecode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 631754555976064, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【遇见AI】qwen image 2.1 官方turbo加速lora文生图基础流_2108863647031320578.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【遇见AI】qwen image 2.1 官方turbo加速lora文生图基础流_2108863647031320578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `631754555976064`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`LoadImage`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
