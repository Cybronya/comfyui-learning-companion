---
key: 图片生成/图生图/krea2 超细节增强-构图多样性 洗图生图2合1工作流V2（Qwen3.5自由切换版）😼_2095467409154072577.json
name: krea2 超细节增强-构图多样性 洗图生图2合1工作流V2（Qwen3.5自由切换版）😼_2095467409154072577
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/krea2 超细节增强-构图多样性 洗图生图2合1工作流V2（Qwen3.5自由切换版）😼_2095467409154072577.json
hash: 39472deede3f53a9
coverage: 0.833333
learned_at: 2026-10-21 00:45:46
nodes: [EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, MarkdownNote, MarkdownNote, Text Multiline, INTConstant, ResolutionSelector, MarkdownNote, CLIPTextEncode, VAELoader, EmptyLatentImage, UNETLoader, ConditioningKrea2Rebalance, VAEDecode, LatentUpscaleBy, Label (rgthree), ConditioningZeroOut, KSampler, Text Multiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, SaveImage, ShowText|pysssss, Switch any [Crystools], PrimitiveStringMultiline, PrimitiveStringMultiline, llama_cpp_model_loader, llama_cpp_parameters, Label (rgthree), llama_cpp_instruct_adv, LoadImage, KSampler, easy seed]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 1646172312039, "steps": 3, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/krea2 超细节增强-构图多样性 洗图生图2合1工作流V2（Qwen3.5自由切换版）😼_2095467409154072577.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/krea2 超细节增强-构图多样性 洗图生图2合1工作流V2（Qwen3.5自由切换版）😼_2095467409154072577.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `Text Multiline`
- `INTConstant`
- `ResolutionSelector`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `ConditioningKrea2Rebalance`
- `VAEDecode` ★核心
- `LatentUpscaleBy`
- `Label (rgthree)`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ShowText|pysssss`
- `Switch any [Crystools]`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `Label (rgthree)`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `KSampler` ★核心
- `easy seed`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `1646172312039`
- `steps` = `3`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`EmptyImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`Text Multiline`、`INTConstant`、`ResolutionSelector`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`UNETLoader`、`ConditioningKrea2Rebalance`、`VAEDecode`、`LatentUpscaleBy`、`Label (rgthree)`、`ConditioningZeroOut`、`KSampler`、`LoraLoaderModelOnly`、`SaveImage`、`Switch any [Crystools]`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`LoadImage`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
