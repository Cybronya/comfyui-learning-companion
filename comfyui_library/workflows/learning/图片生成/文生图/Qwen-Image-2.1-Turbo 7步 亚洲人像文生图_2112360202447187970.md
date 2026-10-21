---
key: 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112360202447187970.json
name: Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112360202447187970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112360202447187970.json
hash: fe2bb9507f3d7ca3
coverage: 0.882353
learned_at: 2026-10-21 02:54:27
nodes: [TextEncodeQwenImage21, ResolutionSelector, QwenPERewriteT8, easy showAnything, UNETLoader, EmptyLatentImage, ComfySwitchNode, CLIPLoader, VAELoader, QwenImage21Cache, LoraLoaderModelOnly, VAEDecode, SaveImage, Color Grading JK, LoraLoaderModelOnly, KSampler, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 567494346953410, "steps": 7, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112360202447187970.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112360202447187970.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
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
- `VAEDecode` ★核心
- `SaveImage`
- `Color Grading JK`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `567494346953410`
- `steps` = `7`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`TextEncodeQwenImage21`、`ResolutionSelector`、`QwenPERewriteT8`、`UNETLoader`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`Color Grading JK`、`KSampler`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
