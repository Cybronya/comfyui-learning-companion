---
key: 图片生成/图生图/Krea2超细节增强洗图生图二合一 Qwen3.5自由切换构图控制_2098636397501575170.json
name: Krea2超细节增强洗图生图二合一 Qwen3.5自由切换构图控制_2098636397501575170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea2超细节增强洗图生图二合一 Qwen3.5自由切换构图控制_2098636397501575170.json
hash: a499b1e930324a74
coverage: 0.883333
learned_at: 2026-10-21 00:41:23
nodes: [EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Text Multiline, INTConstant, ResolutionSelector, CLIPTextEncode, VAELoader, EmptyLatentImage, UNETLoader, ConditioningKrea2Rebalance, VAEDecode, LatentUpscaleBy, ConditioningZeroOut, KSampler, Text Multiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, SaveImage, ShowText|pysssss, Switch any [Crystools], PrimitiveStringMultiline, PrimitiveStringMultiline, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, LoadImage, KSampler, easy seed, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Krea2超细节增强洗图生图二合一 Qwen3.5自由切换构图控制_2098636397501575170.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea2超细节增强洗图生图二合一 Qwen3.5自由切换构图控制_2098636397501575170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `Text Multiline`
- `INTConstant`
- `ResolutionSelector`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `ConditioningKrea2Rebalance`
- `VAEDecode` ★核心
- `LatentUpscaleBy`
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
- `llama_cpp_instruct_adv`
- `LoadImage`
- `KSampler` ★核心
- `easy seed`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（53/60）

**有卡**：`EmptyImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`Text Multiline`、`INTConstant`、`ResolutionSelector`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`UNETLoader`、`ConditioningKrea2Rebalance`、`VAEDecode`、`LatentUpscaleBy`、`ConditioningZeroOut`、`KSampler`、`LoraLoaderModelOnly`、`SaveImage`、`Switch any [Crystools]`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`LoadImage`、`easy seed`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
