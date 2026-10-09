---
key: 图片生成/图生图/Qwen Image 2.1 Image Edit Viggle 4-Step 角色表生成工作流_2106005227299237889.json
name: Qwen Image 2.1 Image Edit Viggle 4-Step 角色表生成工作流_2106005227299237889.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Image Edit Viggle 4-Step 角色表生成工作流_2106005227299237889.json
hash: 65e0a521d9d9b555
coverage: 0.833333
learned_at: 2026-10-09 22:09:17
nodes: [ImageScale, MarkdownNote, PrimitiveInt, ImageScaleToTotalPixels, ComfyMathExpression, ComfySwitchNode, ImageScaleToTotalPixels, ComfyMathExpression, ComfySwitchNode, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, SaveImage, KSampler, ModelSamplingFlux, QwenImage21Cache, ModelAttentionBackend, VAEDecode, ResolutionSelector]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 385899894325001, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 Image Edit Viggle 4-Step 角色表生成工作流_2106005227299237889.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2106005227299237889.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ImageScale`
- `MarkdownNote`
- `PrimitiveInt`
- `ImageScaleToTotalPixels`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ImageScaleToTotalPixels`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `KSampler` ★核心
- `ModelSamplingFlux`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `VAEDecode` ★核心
- `ResolutionSelector`

## 关键参数

- `seed` = `385899894325001`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`ImageScale`、`ImageScaleToTotalPixels`、`ComfyMathExpression`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`KSampler`、`ModelSamplingFlux`、`QwenImage21Cache`、`ModelAttentionBackend`、`VAEDecode`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
