---
key: 图片生成/文生图/krea2 风格之王 全能模型 Qwen3.5自动提示词文生图工作流（自由版）_2070756328192172034.json
name: krea2 风格之王 全能模型 Qwen3.5自动提示词文生图工作流（自由版）_2070756328192172034
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/krea2 风格之王 全能模型 Qwen3.5自动提示词文生图工作流（自由版）_2070756328192172034.json
hash: 4b1213cfb3bbf28f
coverage: 0.777778
learned_at: 2026-10-19 23:42:34
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyImage, ResolutionSelector, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, ConditioningZeroOut, EmptyLatentImage, MarkdownNote, Text Multiline, CLIPTextEncode, KSampler, MarkdownNote, Label (rgthree), MarkdownNote, PrimitiveStringMultiline, llama_cpp_instruct_adv, ShowText|pysssss, llama_cpp_parameters, easy seed, PrimitiveStringMultiline, Label (rgthree), llama_cpp_model_loader, LoraLoaderModelOnly, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "dpmpp_2s_ancestral", "scheduler": "bong_tangent", "seed": 1646172312039, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/krea2 风格之王 全能模型 Qwen3.5自动提示词文生图工作流（自由版）_2070756328192172034.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/krea2 风格之王 全能模型 Qwen3.5自动提示词文生图工作流（自由版）_2070756328192172034.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyImage`
- `ResolutionSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `Label (rgthree)`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `llama_cpp_parameters`
- `easy seed`
- `PrimitiveStringMultiline`
- `Label (rgthree)`
- `llama_cpp_model_loader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `1646172312039`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2s_ancestral`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **78%**（21/27）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyImage`、`ResolutionSelector`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`ConditioningZeroOut`、`EmptyLatentImage`、`Text Multiline`、`CLIPTextEncode`、`KSampler`、`Label (rgthree)`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`easy seed`、`llama_cpp_model_loader`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
