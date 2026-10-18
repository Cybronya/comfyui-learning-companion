---
key: 视频生成/图生视频/Qwen_2.1超细节洗图生图二合一，支持Qwen_3.5自由切换的反推提示词工作流_2105120232384851969.json
name: Qwen_2.1超细节洗图生图二合一，支持Qwen_3.5自由切换的反推提示词工作流_2105120232384851969
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_2.1超细节洗图生图二合一，支持Qwen_3.5自由切换的反推提示词工作流_2105120232384851969.json
hash: 0f299f9d3223550a
coverage: 0.872727
learned_at: 2026-10-17 22:18:52
nodes: [TextEncodeQwenImage21, EmptyLatentImage, KSampler, TextGenerateLTX2Prompt, easy showAnything, ResolutionSelector, EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, VAEDecode, SaveImage, Text Multiline, CLIPLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, easy seed, ShowText|pysssss, PrimitiveStringMultiline, llama_cpp_model_loader, llama_cpp_parameters, LoadImage, PrimitiveStringMultiline, Switch any [Crystools], llama_cpp_instruct_adv, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_2.1超细节洗图生图二合一，支持Qwen_3.5自由切换的反推提示词工作流_2105120232384851969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_2.1超细节洗图生图二合一，支持Qwen_3.5自由切换的反推提示词工作流_2105120232384851969.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `ResolutionSelector`
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `VAEDecode` ★核心
- `SaveImage`
- `Text Multiline`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `easy seed`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Switch any [Crystools]`
- `llama_cpp_instruct_adv`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **87%**（48/55）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`EmptyImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`VAEDecode`、`SaveImage`、`Text Multiline`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`easy seed`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LoadImage`、`Switch any [Crystools]`、`llama_cpp_instruct_adv`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
