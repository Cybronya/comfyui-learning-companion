---
key: 平台全量/线绘风格 Turn your photo to line drawing style!_1840703002272288770.json
name: 线绘风格 Turn your photo to line drawing style!_1840703002272288770
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/线绘风格 Turn your photo to line drawing style!_1840703002272288770.json
hash: 7f43b8b440079afd
coverage: 0.589286
learned_at: 2026-11-14 02:29:01
nodes: [VAEDecode, CLIPTextEncode, CLIPTextEncode, PreviewImage, ImageBatch, ImageBatch, Seed Generator, GetNode, SetNode, SetNode, GetNode, GetNode, Prompts Everywhere, Anything Everywhere, Anything Everywhere, easy promptReplace, easy promptConcat, KSampler, ShowText|pysssss, ShowText|pysssss, LoadImage, WD14Tagger|pysssss, EmptyLatentImage, ImageBatch, GetNode, AV_IPAdapter, AV_ControlNetPreprocessor, CheckpointLoaderSimple, Note, GetImageSize+, LayerUtility: ImageRemoveAlpha, ImageDesaturate+, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, ImageScaleToMegapixels, MaskToImage, SetNode, String Literal, PreviewImage, PreviewImage, ControlNetApplyAdvanced, GetNode, Anything Everywhere, Note, LoraLoader, Note, Note, SetNode, GetNode, ACN_ControlNet++LoaderSingle, LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage, SaveImage]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 5.4, "checkpoint": "leosamsHelloworldXL_helloworldXL70.safetensors", "controlnet_strength": 0.65, "denoise": 1, "height": 512, "lora_name": "araminta_k_midsommar_cartoon.safetensors", "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 187849950591072, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 512}
---

# 平台全量/线绘风格 Turn your photo to line drawing style!_1840703002272288770.json

> 来源文件 `comfyui_library/workflows/平台全量/线绘风格 Turn your photo to line drawing style!_1840703002272288770.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ImageBatch`
- `ImageBatch`
- `Seed Generator`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Prompts Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `easy promptReplace`
- `easy promptConcat`
- `KSampler` ★核心
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LoadImage`
- `WD14Tagger|pysssss`
- `EmptyLatentImage` ★核心
- `ImageBatch`
- `GetNode`
- `AV_IPAdapter`
- `AV_ControlNetPreprocessor`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `GetImageSize+`
- `LayerUtility: ImageRemoveAlpha`
- `ImageDesaturate+`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `ImageScaleToMegapixels`
- `MaskToImage`
- `SetNode`
- `String Literal`
- `PreviewImage`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `GetNode`
- `Anything Everywhere`
- `Note`
- `LoraLoader` ★核心
- `Note`
- `Note`
- `SetNode`
- `GetNode`
- `ACN_ControlNet++LoaderSingle`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `SaveImage`

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `187849950591072`
- `steps` = `20`
- `cfg` = `5.4`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `checkpoint` = `leosamsHelloworldXL_helloworldXL70.safetensors`
- `controlnet_strength` = `0.65`
- `lora_name` = `araminta_k_midsommar_cartoon.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`

## 知识

覆盖率 **59%**（33/56）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`ImageBatch`、`Seed Generator`、`Prompts Everywhere`、`easy promptReplace`、`easy promptConcat`、`KSampler`、`LoadImage`、`WD14Tagger|pysssss`、`EmptyLatentImage`、`AV_IPAdapter`、`AV_ControlNetPreprocessor`、`CheckpointLoaderSimple`、`GetImageSize+`、`LayerUtility: ImageRemoveAlpha`、`ImageDesaturate+`、`LayerMask: BiRefNetUltraV2`、`LayerMask: LoadBiRefNetModel`、`ImageScaleToMegapixels`、`MaskToImage`、`String Literal`、`ControlNetApplyAdvanced`、`LoraLoader`、`ACN_ControlNet++LoaderSingle`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ACN_ControlNet++LoaderSingle、AV_ControlNetPreprocessor
