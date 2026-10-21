---
key: 图片生成/图生图/高度一致性人物写真 +Krea+2+turbo++Character+Portraits_+High_2107627484991803394.json
name: 高度一致性人物写真 +Krea+2+turbo++Character+Portraits_+High_2107627484991803394
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/高度一致性人物写真 +Krea+2+turbo++Character+Portraits_+High_2107627484991803394.json
hash: acbe2a1c40d0ecbd
coverage: 0.897436
learned_at: 2026-10-21 00:56:53
nodes: [VAEDecode, CLIPTextEncode, EmptyLatentImage, Dapao_LlamaCaptionOptions, ImpactInt, ImpactInt, CR Prompt List, easy showAnything, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageConcatMulti, ImageConcatMulti, ImageFromBatch, ImageConcatMulti, SaveImage, CR Batch Images From List, SaveImage, Dapao_LlamaCaption, KSampler, RegexReplace, easy showAnything, easy showAnything, RegexReplace, llama_cpp_instruct_adv, RegexReplace, llama_cpp_model_loader, llama_cpp_parameters, ConditioningZeroOut, UNETLoader, VAELoader, CLIPLoader, PixaromaLoraLoader, CR Text, String Literal, RegexReplace, Fast Groups Bypasser (rgthree), CR Text, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 720, "sampler_name": "er_sde", "scheduler": "simple", "seed": 5, "steps": 8, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/高度一致性人物写真 +Krea+2+turbo++Character+Portraits_+High_2107627484991803394.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/高度一致性人物写真 +Krea+2+turbo++Character+Portraits_+High_2107627484991803394.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `Dapao_LlamaCaptionOptions`
- `ImpactInt`
- `ImpactInt`
- `CR Prompt List`
- `easy showAnything`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageConcatMulti`
- `SaveImage`
- `CR Batch Images From List`
- `SaveImage`
- `Dapao_LlamaCaption`
- `KSampler` ★核心
- `RegexReplace`
- `easy showAnything`
- `easy showAnything`
- `RegexReplace`
- `llama_cpp_instruct_adv`
- `RegexReplace`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `PixaromaLoraLoader` ★核心
- `CR Text`
- `String Literal`
- `RegexReplace`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `seed` = `5`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（35/39）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`EmptyLatentImage`、`Dapao_LlamaCaptionOptions`、`ImpactInt`、`CR Prompt List`、`ImageFromBatch`、`ImageConcatMulti`、`SaveImage`、`CR Batch Images From List`、`Dapao_LlamaCaption`、`KSampler`、`RegexReplace`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`ConditioningZeroOut`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`PixaromaLoraLoader`、`CR Text`、`String Literal`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
