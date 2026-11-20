---
key: 平台全量/Turn your photo to line drawing style!_1867148737771700225.json
name: Turn your photo to line drawing style!_1867148737771700225
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Turn your photo to line drawing style!_1867148737771700225.json
hash: ab4ffb867cc97fee
coverage: 0.589286
learned_at: 2026-11-14 01:01:58
nodes: [VAEDecode, CLIPTextEncode, CLIPTextEncode, PreviewImage, ImageBatch, ImageBatch, Seed Generator, PreviewImage, GetNode, SetNode, SetNode, GetNode, GetNode, Prompts Everywhere, Anything Everywhere, Anything Everywhere, SaveImage, easy promptReplace, easy promptConcat, KSampler, ShowText|pysssss, ShowText|pysssss, LoadImage, LoadImage, LoadImage, WD14Tagger|pysssss, EmptyLatentImage, ImageBatch, GetNode, AV_ControlNetPreprocessor, CheckpointLoaderSimple, Note, GetImageSize+, LayerUtility: ImageRemoveAlpha, ImageDesaturate+, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, ImageScaleToMegapixels, MaskToImage, SetNode, String Literal, PreviewImage, PreviewImage, ControlNetApplyAdvanced, GetNode, Anything Everywhere, LoraLoader, Note, Note, SetNode, GetNode, LoadImage, Note, ControlNetLoader, AV_IPAdapter, LoadImage]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 5.4, "checkpoint": "leosamsHelloworldXL_helloworldXL70.safetensors", "controlnet_strength": 0.65, "denoise": 1, "height": 512, "lora_name": "araminta_k_midsommar_cartoon.safetensors", "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 461232078965532, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 512}
---

# 平台全量/Turn your photo to line drawing style!_1867148737771700225.json

> 来源文件 `comfyui_library/workflows/平台全量/Turn your photo to line drawing style!_1867148737771700225.json`

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
- `PreviewImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Prompts Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `SaveImage`
- `easy promptReplace`
- `easy promptConcat`
- `KSampler` ★核心
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WD14Tagger|pysssss`
- `EmptyLatentImage` ★核心
- `ImageBatch`
- `GetNode`
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
- `LoraLoader` ★核心
- `Note`
- `Note`
- `SetNode`
- `GetNode`
- `LoadImage`
- `Note`
- `ControlNetLoader`
- `AV_IPAdapter`
- `LoadImage`

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `461232078965532`
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

**有卡**：`VAEDecode`、`CLIPTextEncode`、`ImageBatch`、`Seed Generator`、`Prompts Everywhere`、`SaveImage`、`easy promptReplace`、`easy promptConcat`、`KSampler`、`LoadImage`、`WD14Tagger|pysssss`、`EmptyLatentImage`、`AV_ControlNetPreprocessor`、`CheckpointLoaderSimple`、`GetImageSize+`、`LayerUtility: ImageRemoveAlpha`、`ImageDesaturate+`、`LayerMask: BiRefNetUltraV2`、`LayerMask: LoadBiRefNetModel`、`ImageScaleToMegapixels`、`MaskToImage`、`String Literal`、`ControlNetApplyAdvanced`、`LoraLoader`、`ControlNetLoader`、`AV_IPAdapter`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、AV_ControlNetPreprocessor、ControlNetApplyAdvanced
