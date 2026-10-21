---
key: 图片生成/图生图/一键制作人物风格信息图--Qwen image 2.1_2105302134995644418.json
name: 一键制作人物风格信息图--Qwen image 2.1_2105302134995644418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键制作人物风格信息图--Qwen image 2.1_2105302134995644418.json
hash: 58800a187ea1349e
coverage: 0.807692
learned_at: 2026-10-21 00:46:49
nodes: [Note, EmptyLatentImage, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, LayerUtility: PurgeVRAM V2, ModelAttentionBackend, PreviewImage, ImageResizeKJv2, LoadImage, llama_cpp_model_loader, SaveImage, ComfySwitchNode, VAELoader, CLIPLoader, UNETLoader, llama_cpp_parameters, PreviewAny, Text, KSampler, ResolutionSelector, llama_cpp_instruct_adv, Text, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 485494017043212, "steps": 30, "width": 1024}
---

# 图片生成/图生图/一键制作人物风格信息图--Qwen image 2.1_2105302134995644418.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键制作人物风格信息图--Qwen image 2.1_2105302134995644418.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `Note`
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LayerUtility: PurgeVRAM V2`
- `ModelAttentionBackend`
- `PreviewImage`
- `ImageResizeKJv2`
- `LoadImage`
- `llama_cpp_model_loader`
- `SaveImage`
- `ComfySwitchNode`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `llama_cpp_parameters`
- `PreviewAny`
- `Text`
- `KSampler` ★核心
- `ResolutionSelector`
- `llama_cpp_instruct_adv`
- `Text`
- `Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `485494017043212`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`LayerUtility: PurgeVRAM V2`、`ModelAttentionBackend`、`ImageResizeKJv2`、`LoadImage`、`llama_cpp_model_loader`、`SaveImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`llama_cpp_parameters`、`Text`、`KSampler`、`ResolutionSelector`、`llama_cpp_instruct_adv`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
