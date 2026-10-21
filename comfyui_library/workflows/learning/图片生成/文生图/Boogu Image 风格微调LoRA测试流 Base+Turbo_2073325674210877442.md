---
key: 图片生成/文生图/Boogu Image 风格微调LoRA测试流 Base+Turbo_2073325674210877442.json
name: Boogu Image 风格微调LoRA测试流 Base+Turbo_2073325674210877442
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Boogu Image 风格微调LoRA测试流 Base+Turbo_2073325674210877442.json
hash: e8343b7874e32bac
coverage: 0.939394
learned_at: 2026-10-20 00:01:05
nodes: [UNETLoader, VAELoader, CLIPLoader, ConditioningZeroOut, KSampler, CLIPLoader, UNETLoader, VAELoader, ConditioningZeroOut, KSampler, KSampler, EmptyLatentImage, EmptyLatentImage, SaveImage, SaveImage, SaveImage, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), VAEDecode, VAEDecode, VAEDecode, VAEDecode, LayerUtility: ImageReel, KSampler, PrimitiveNode, TTResolutionSelector, TTResolutionSelector, LayerUtility: ImageReelComposit, SaveImage, CLIPTextEncode, CLIPTextEncode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "lcm", "scheduler": "sgm_uniform", "seed": 812818686328483, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Boogu Image 风格微调LoRA测试流 Base+Turbo_2073325674210877442.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Boogu Image 风格微调LoRA测试流 Base+Turbo_2073325674210877442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `KSampler` ★核心
- `PrimitiveNode`
- `TTResolutionSelector`
- `TTResolutionSelector`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `812818686328483`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`ConditioningZeroOut`、`KSampler`、`EmptyLatentImage`、`SaveImage`、`LoraLoaderModelOnly`、`VAEDecode`、`LayerUtility: ImageReel`、`TTResolutionSelector`、`LayerUtility: ImageReelComposit`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
