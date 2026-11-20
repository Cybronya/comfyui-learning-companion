---
key: 平台全量/【update】Hand-drawn illustration workflow _ 手绘插画工作流_1862384348501835778.json
name: 【update】Hand-drawn illustration workflow _ 手绘插画工作流_1862384348501835778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【update】Hand-drawn illustration workflow _ 手绘插画工作流_1862384348501835778.json
hash: 85d5fd915bc03261
coverage: 0.764706
learned_at: 2026-11-14 01:22:30
nodes: [SaveImage, Simple String, ImpactInt, EmptyLatentImage, Prompts Everywhere, CM_NearestSDXLResolution, CM_SDXLResolution, ImageBatch, ImageBatch, LoadImage, Anything Everywhere, PreviewImage, Anything Everywhere, LayerUtility: ImageBlendAdvance V2, KSampler, ImageBatch, ImageResize+, CLIPSetLastLayer, CR Color Gradient, PreviewImage, MiniCPM_VQA, ImageBatch, ImageBatch, ImageBatch, ImageBatch, ImageBatch, ImageBatch, ShowText|pysssss, easy promptReplace, ShowText|pysssss, Simple String, LayerUtility: TextJoin, CR Text Input Switch, CR Text Concatenate, LayerMask: SegmentAnythingUltra V2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Note, Note, Note, Note, Note, ImpactSwitch, LoraLoader, AV_ControlNetPreprocessor, ACN_ControlNet++LoaderSingle, ControlNetApplyAdvanced, AV_IPAdapter, Anything Everywhere, CheckpointLoaderSimple, ImpactSwitch, VAEDecode, Seed Generator, ImpactSwitch, Anything Everywhere, CLIPTextEncode, CLIPTextEncode, ImpactInt]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "checkpoint": "albedobaseXLPre_v21preBeta.safetensors", "controlnet_strength": 0.8, "denoise": 1, "height": 512, "lora_name": "araminta_k_midsommar_cartoon.safetensors", "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 167716666794083, "steps": 25, "strength_clip": 1, "strength_model": 0.5, "width": 512}
---

# 平台全量/【update】Hand-drawn illustration workflow _ 手绘插画工作流_1862384348501835778.json

> 来源文件 `comfyui_library/workflows/平台全量/【update】Hand-drawn illustration workflow _ 手绘插画工作流_1862384348501835778.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `SaveImage`
- `Simple String`
- `ImpactInt`
- `EmptyLatentImage` ★核心
- `Prompts Everywhere`
- `CM_NearestSDXLResolution`
- `CM_SDXLResolution`
- `ImageBatch`
- `ImageBatch`
- `LoadImage`
- `Anything Everywhere`
- `PreviewImage`
- `Anything Everywhere`
- `LayerUtility: ImageBlendAdvance V2`
- `KSampler` ★核心
- `ImageBatch`
- `ImageResize+`
- `CLIPSetLastLayer`
- `CR Color Gradient`
- `PreviewImage`
- `MiniCPM_VQA`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ShowText|pysssss`
- `easy promptReplace`
- `ShowText|pysssss`
- `Simple String`
- `LayerUtility: TextJoin`
- `CR Text Input Switch`
- `CR Text Concatenate`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `ImpactSwitch`
- `LoraLoader` ★核心
- `AV_ControlNetPreprocessor`
- `ACN_ControlNet++LoaderSingle`
- `ControlNetApplyAdvanced` ★核心
- `AV_IPAdapter`
- `Anything Everywhere`
- `CheckpointLoaderSimple` ★核心
- `ImpactSwitch`
- `VAEDecode` ★核心
- `Seed Generator`
- `ImpactSwitch`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImpactInt`

**识别到的模式**：text_to_image、lora

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `167716666794083`
- `steps` = `25`
- `cfg` = `3.5`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `lora_name` = `araminta_k_midsommar_cartoon.safetensors`
- `strength_model` = `0.5`
- `strength_clip` = `1`
- `controlnet_strength` = `0.8`
- `checkpoint` = `albedobaseXLPre_v21preBeta.safetensors`

## 知识

覆盖率 **76%**（52/68）

**有卡**：`SaveImage`、`Simple String`、`ImpactInt`、`EmptyLatentImage`、`Prompts Everywhere`、`CM_NearestSDXLResolution`、`CM_SDXLResolution`、`ImageBatch`、`LoadImage`、`LayerUtility: ImageBlendAdvance V2`、`KSampler`、`ImageResize+`、`CLIPSetLastLayer`、`CR Color Gradient`、`MiniCPM_VQA`、`easy promptReplace`、`LayerUtility: TextJoin`、`CR Text Input Switch`、`CR Text Concatenate`、`LayerMask: SegmentAnythingUltra V2`、`LoraLoader`、`AV_ControlNetPreprocessor`、`ACN_ControlNet++LoaderSingle`、`ControlNetApplyAdvanced`、`AV_IPAdapter`、`CheckpointLoaderSimple`、`VAEDecode`、`Seed Generator`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ACN_ControlNet++LoaderSingle、AV_ControlNetPreprocessor
