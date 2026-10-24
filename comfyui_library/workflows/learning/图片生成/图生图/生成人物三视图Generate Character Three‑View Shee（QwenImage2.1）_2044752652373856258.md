---
key: 图片生成/图生图/生成人物三视图Generate Character Three‑View Shee（QwenImage2.1）_2044752652373856258.json
name: 生成人物三视图Generate Character Three‑View Shee（QwenImage2.1）_2044752652373856258
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生成人物三视图Generate Character Three‑View Shee（QwenImage2.1）_2044752652373856258.json
hash: 140f3c5368dfa6a8
coverage: 0.935484
learned_at: 2026-10-23 13:15:27
nodes: [VAEDecode, Anything Everywhere3, SaveImage, UNETLoader, CLIPLoader, VAELoader, VAEDecode, ConditioningZeroOut, KSampler, LoraLoaderModelOnly, Anything Everywhere3, LoadImage, Int, Int, ResizeAndPadImage, SaveImage, CR Text, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, ResolutionSelector, LoadImage, LoadImage, TextEncodeQwenImage21]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 446451417821415, "steps": 25, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/生成人物三视图Generate Character Three‑View Shee（QwenImage2.1）_2044752652373856258.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生成人物三视图Generate Character Three‑View Shee（QwenImage2.1）_2044752652373856258.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `VAEDecode` ★核心
- `Anything Everywhere3`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `LoadImage`
- `Int`
- `Int`
- `ResizeAndPadImage`
- `SaveImage`
- `CR Text`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `446451417821415`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`VAEDecode`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`KSampler`、`LoraLoaderModelOnly`、`LoadImage`、`Int`、`ResizeAndPadImage`、`CR Text`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
