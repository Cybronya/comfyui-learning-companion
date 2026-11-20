---
key: 平台全量/Hoko Manga Style 1.5_1869937841319874562.json
name: Hoko Manga Style 1.5_1869937841319874562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Hoko Manga Style 1.5_1869937841319874562.json
hash: c9c2b6f7a1978c79
coverage: 0.826087
learned_at: 2026-11-14 00:32:03
nodes: [SaveImage, Image Comparer (rgthree), VAEDecode, easy imageSize, ShowText|pysssss, EmptyLatentImage, AlignYourStepsScheduler, KSamplerSelect, ImageScaleToTotalPixels, SamplerCustom, CLIPTextEncode, CLIPTextEncode, CR Text Concatenate, ControlNetApplyAdvanced, PreviewImage, easy positive, Note, LoadImage, ControlNetLoader, CheckpointLoaderSimple, LoraLoader, LayerColor: Brightness & Contrast, RH_Captioner]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "animagineXLV31_v31.safetensors", "controlnet_strength": 0.7000000000000001, "height": 512, "lora_name": "残照金 SDXL - Hoko Manga Style_Hoko v1.0.safetensors", "strength_clip": 1, "strength_model": 0.75, "width": 512}
---

# 平台全量/Hoko Manga Style 1.5_1869937841319874562.json

> 来源文件 `comfyui_library/workflows/平台全量/Hoko Manga Style 1.5_1869937841319874562.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `easy imageSize`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `AlignYourStepsScheduler`
- `KSamplerSelect` ★核心
- `ImageScaleToTotalPixels`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `easy positive`
- `Note`
- `LoadImage`
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `LayerColor: Brightness & Contrast`
- `RH_Captioner`

**识别到的模式**：lora

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `controlnet_strength` = `0.7000000000000001`
- `checkpoint` = `animagineXLV31_v31.safetensors`
- `lora_name` = `残照金 SDXL - Hoko Manga Style_Hoko v1.0.safetensors`
- `strength_model` = `0.75`
- `strength_clip` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`SaveImage`、`VAEDecode`、`easy imageSize`、`EmptyLatentImage`、`AlignYourStepsScheduler`、`KSamplerSelect`、`ImageScaleToTotalPixels`、`SamplerCustom`、`CLIPTextEncode`、`CR Text Concatenate`、`ControlNetApplyAdvanced`、`easy positive`、`LoadImage`、`ControlNetLoader`、`CheckpointLoaderSimple`、`LoraLoader`、`LayerColor: Brightness & Contrast`、`RH_Captioner`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、AlignYourStepsScheduler
