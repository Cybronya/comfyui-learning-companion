---
key: 平台全量/磨皮大师 EKKIVOK - REAL SKIN FINAL_1851168136954531842.json
name: 磨皮大师 EKKIVOK - REAL SKIN FINAL_1851168136954531842
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/磨皮大师 EKKIVOK - REAL SKIN FINAL_1851168136954531842.json
hash: ce95e31fae8d7994
coverage: 0.735294
learned_at: 2026-11-14 02:27:17
nodes: [LoadImage, Florence2Run, DownloadAndLoadFlorence2Model, Anything Everywhere, CR Combine Prompt, ShowText|pysssss, LayerMask: PersonMaskUltra V2, VAEEncode, SetLatentNoiseMask, CLIPTextEncode, VAEDecode, KSampler, MaskPreview+, PreviewImage, FaceParsingProcessorLoader(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParse(FaceParsing), FaceParsingResultsParser(FaceParsing), GrowMaskWithBlur, PreviewImage, Reroute, Cut By Mask, PreviewImage, MaskToImage, ImageCompositeMasked, Image Comparer (rgthree), CR Simple Image Compare, PreviewImage, Reroute, SaveImage, Power Lora Loader (rgthree), LoraLoader, CheckpointLoaderSimple, CLIPTextEncode]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 0.7000000000000001, "checkpoint": "epicrealismXL_v8Kiss.safetensors", "denoise": 0.3, "lora_name": "real-humans-PublicPrompts.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 1012533537766516, "steps": 30, "strength_clip": 1, "strength_model": 1}
---

# 平台全量/磨皮大师 EKKIVOK - REAL SKIN FINAL_1851168136954531842.json

> 来源文件 `comfyui_library/workflows/平台全量/磨皮大师 EKKIVOK - REAL SKIN FINAL_1851168136954531842.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LoadImage`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `Anything Everywhere`
- `CR Combine Prompt`
- `ShowText|pysssss`
- `LayerMask: PersonMaskUltra V2`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `MaskPreview+`
- `PreviewImage`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParse(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `GrowMaskWithBlur`
- `PreviewImage`
- `Reroute`
- `Cut By Mask`
- `PreviewImage`
- `MaskToImage`
- `ImageCompositeMasked`
- `Image Comparer (rgthree)`
- `CR Simple Image Compare`
- `PreviewImage`
- `Reroute`
- `SaveImage`
- `Power Lora Loader (rgthree)`
- `LoraLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `1012533537766516`
- `steps` = `30`
- `cfg` = `0.7000000000000001`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.3`
- `lora_name` = `real-humans-PublicPrompts.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `epicrealismXL_v8Kiss.safetensors`

## 知识

覆盖率 **74%**（25/34）

**有卡**：`LoadImage`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`CR Combine Prompt`、`LayerMask: PersonMaskUltra V2`、`VAEEncode`、`SetLatentNoiseMask`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`MaskPreview+`、`FaceParsingProcessorLoader(FaceParsing)`、`FaceParsingModelLoader(FaceParsing)`、`FaceParse(FaceParsing)`、`FaceParsingResultsParser(FaceParsing)`、`GrowMaskWithBlur`、`Cut By Mask`、`MaskToImage`、`ImageCompositeMasked`、`CR Simple Image Compare`、`SaveImage`、`Power Lora Loader (rgthree)`、`LoraLoader`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SetLatentNoiseMask、VAEEncode、LoraLoader
