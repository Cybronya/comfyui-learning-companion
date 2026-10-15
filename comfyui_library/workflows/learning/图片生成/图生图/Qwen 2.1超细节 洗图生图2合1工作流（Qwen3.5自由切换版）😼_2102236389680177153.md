---
key: 图片生成/图生图/Qwen 2.1超细节 洗图生图2合1工作流（Qwen3.5自由切换版）😼_2102236389680177153.json
name: Qwen 2.1超细节 洗图生图2合1工作流（Qwen3.5自由切换版）😼_2102236389680177153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 2.1超细节 洗图生图2合1工作流（Qwen3.5自由切换版）😼_2102236389680177153.json
hash: b509384d89ba4af2
coverage: 0.774194
learned_at: 2026-10-15 22:25:10
nodes: [TextEncodeQwenImage21, EmptyLatentImage, KSampler, TextGenerateLTX2Prompt, easy showAnything, ResolutionSelector, EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, MarkdownNote, Label (rgthree), MarkdownNote, MarkdownNote, VAEDecode, SaveImage, Text Multiline, CLIPLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, easy seed, ShowText|pysssss, PrimitiveStringMultiline, llama_cpp_model_loader, llama_cpp_parameters, LoadImage, PrimitiveStringMultiline, Label (rgthree), Switch any [Crystools], llama_cpp_instruct_adv]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 905, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen 2.1超细节 洗图生图2合1工作流（Qwen3.5自由切换版）😼_2102236389680177153.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 2.1超细节 洗图生图2合1工作流（Qwen3.5自由切换版）😼_2102236389680177153.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `ResolutionSelector`
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `MarkdownNote`
- `Label (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
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
- `Label (rgthree)`
- `Switch any [Crystools]`
- `llama_cpp_instruct_adv`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `905`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`EmptyImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`Label (rgthree)`、`VAEDecode`、`SaveImage`、`Text Multiline`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`easy seed`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LoadImage`、`Switch any [Crystools]`、`llama_cpp_instruct_adv`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
