---
key: 图片生成/图生图/boogu_edit+Qwen3.5-完美洗图_2069637206297374722.json
name: boogu_edit+Qwen3.5-完美洗图_2069637206297374722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/boogu_edit+Qwen3.5-完美洗图_2069637206297374722.json
hash: 017018925a981c69
coverage: 0.72
learned_at: 2026-10-23 11:34:13
nodes: [llama_cpp_parameters, easy cleanGpuUsed, llama_cpp_instruct_adv, easy showAnything, VAELoader, CLIPLoader, UNETLoader, SamplerCustom, ModelSamplingAuraFlow, KSamplerSelect, BasicScheduler, VAEDecode, llama_cpp_model_loader, TextEncodeBooguEdit, JjkText, 孤海注释, 孤海注释, SaveImage, Image Comparer (rgthree), Text, ImageLoader, PreviewImage, EmptyLatentImage, LayerUtility: ImageScaleByAspectRatio V2, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1280, "width": 1280}
---

# 图片生成/图生图/boogu_edit+Qwen3.5-完美洗图_2069637206297374722.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/boogu_edit+Qwen3.5-完美洗图_2069637206297374722.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `llama_cpp_parameters`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustom` ★核心
- `ModelSamplingAuraFlow`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `llama_cpp_model_loader`
- `TextEncodeBooguEdit`
- `JjkText`
- `孤海注释`
- `孤海注释`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Text`
- `ImageLoader`
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`

## 关键参数

- `width` = `1280`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（18/25）

**有卡**：`llama_cpp_parameters`、`easy cleanGpuUsed`、`llama_cpp_instruct_adv`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`SamplerCustom`、`ModelSamplingAuraFlow`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`llama_cpp_model_loader`、`TextEncodeBooguEdit`、`SaveImage`、`Text`、`ImageLoader`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、KSamplerSelect、SamplerCustom、TextEncodeBooguEdit
