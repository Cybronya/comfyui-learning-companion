---
key: 图片生成/文生图/qwen_image_2.1图像反推文生图_2101924301023834113.json
name: qwen_image_2.1图像反推文生图_2101924301023834113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen_image_2.1图像反推文生图_2101924301023834113.json
hash: 5b02d501be3910c3
coverage: 0.85
learned_at: 2026-10-20 01:51:59
nodes: [VAELoader, KSampler, SaveImage, VAEDecode, TextEncodeQwenImage21, ReversalCaptionOptions, ReversalLlamaCaption, CR Text, easy showAnything, String Literal, CR Prompt List, easy showAnything, VAEDecodeTiled, SeedVR2Preprocess, VAEEncodeTiled, SeedVR2PostProcessing, ResizeImageMaskNode, KSampler, SeedVR2Conditioning, SaveImage, UNETLoader, Image Comparer (rgthree), VAELoader, easy showAnything, RegexReplace, RegexReplace, CR Text, llama_cpp_model_loader, llama_cpp_parameters, RegexReplace, Fast Groups Bypasser (rgthree), EmptyLatentImage, CR Text, Fast Groups Bypasser (rgthree), llama_cpp_instruct_adv, UNETLoader, CLIPLoader, LoadImage, ImpactInt, ImpactInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "er_sde", "scheduler": "bong_tangent", "seed": 979774322651229, "steps": 2, "width": 1680}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen_image_2.1图像反推文生图_2101924301023834113.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen_image_2.1图像反推文生图_2101924301023834113.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（40 个）：
- `VAELoader`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `ReversalCaptionOptions`
- `ReversalLlamaCaption`
- `CR Text`
- `easy showAnything`
- `String Literal`
- `CR Prompt List`
- `easy showAnything`
- `VAEDecodeTiled` ★核心
- `SeedVR2Preprocess`
- `VAEEncodeTiled` ★核心
- `SeedVR2PostProcessing`
- `ResizeImageMaskNode`
- `KSampler` ★核心
- `SeedVR2Conditioning`
- `SaveImage`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `VAELoader`
- `easy showAnything`
- `RegexReplace`
- `RegexReplace`
- `CR Text`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `RegexReplace`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`

## 关键参数

- `seed` = `979774322651229`
- `steps` = `2`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `1680`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`VAELoader`、`KSampler`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`ReversalCaptionOptions`、`ReversalLlamaCaption`、`CR Text`、`String Literal`、`CR Prompt List`、`VAEDecodeTiled`、`SeedVR2Preprocess`、`VAEEncodeTiled`、`SeedVR2PostProcessing`、`ResizeImageMaskNode`、`SeedVR2Conditioning`、`UNETLoader`、`RegexReplace`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`EmptyLatentImage`、`llama_cpp_instruct_adv`、`CLIPLoader`、`LoadImage`、`ImpactInt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
