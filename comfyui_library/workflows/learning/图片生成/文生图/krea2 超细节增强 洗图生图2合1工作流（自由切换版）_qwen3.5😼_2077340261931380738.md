---
key: 图片生成/文生图/krea2 超细节增强 洗图生图2合1工作流（自由切换版）_qwen3.5😼_2077340261931380738.json
name: krea2 超细节增强 洗图生图2合1工作流（自由切换版）_qwen3.5😼_2077340261931380738
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/krea2 超细节增强 洗图生图2合1工作流（自由切换版）_qwen3.5😼_2077340261931380738.json
hash: f72939aae2c6e7bc
coverage: 0.828571
learned_at: 2026-10-20 00:20:37
nodes: [UNETLoader, EmptyImage, ResolutionSelector, LayerUtility: ImageScaleByAspectRatio V2, Label (rgthree), VAELoader, MarkdownNote, CLIPTextEncode, ConditioningZeroOut, ConditioningKrea2Rebalance, LoraLoaderModelOnly, VAEDecode, Text Multiline, EmptyLatentImage, INTConstant, MarkdownNote, LatentUpscaleBy, MarkdownNote, VAEDecode, SaveImage, CLIPLoader, Text Multiline, llama_cpp_parameters, llama_cpp_model_loader, PrimitiveStringMultiline, LoadImage, Switch any [Crystools], Label (rgthree), PrimitiveStringMultiline, ShowText|pysssss, LoraLoaderModelOnly, KSampler, KSampler, easy seed, llama_cpp_instruct_adv]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 1646172312039, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/krea2 超细节增强 洗图生图2合1工作流（自由切换版）_qwen3.5😼_2077340261931380738.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/krea2 超细节增强 洗图生图2合1工作流（自由切换版）_qwen3.5😼_2077340261931380738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `UNETLoader` ★核心
- `EmptyImage`
- `ResolutionSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Label (rgthree)`
- `VAELoader`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ConditioningKrea2Rebalance`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `Text Multiline`
- `EmptyLatentImage` ★核心
- `INTConstant`
- `MarkdownNote`
- `LatentUpscaleBy`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `Text Multiline`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `PrimitiveStringMultiline`
- `LoadImage`
- `Switch any [Crystools]`
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `easy seed`
- `llama_cpp_instruct_adv`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `1646172312039`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（29/35）

**有卡**：`UNETLoader`、`EmptyImage`、`ResolutionSelector`、`LayerUtility: ImageScaleByAspectRatio V2`、`Label (rgthree)`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`ConditioningKrea2Rebalance`、`LoraLoaderModelOnly`、`VAEDecode`、`Text Multiline`、`EmptyLatentImage`、`INTConstant`、`LatentUpscaleBy`、`SaveImage`、`CLIPLoader`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`LoadImage`、`Switch any [Crystools]`、`KSampler`、`easy seed`、`llama_cpp_instruct_adv`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
