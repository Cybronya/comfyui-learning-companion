---
key: 平台全量/EKKIVOK - REAL SKIN FINAL_1868944134554951682.json
name: EKKIVOK - REAL SKIN FINAL_1868944134554951682
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/EKKIVOK - REAL SKIN FINAL_1868944134554951682.json
hash: 7b291523de6be9fe
coverage: 0.735294
learned_at: 2026-11-14 00:23:52
nodes: [LoadImage, Florence2Run, DownloadAndLoadFlorence2Model, Anything Everywhere, LayerMask: PersonMaskUltra V2, CLIPTextEncode, VAEEncode, SetLatentNoiseMask, CLIPTextEncode, VAEDecode, MaskPreview+, FaceParsingProcessorLoader(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParse(FaceParsing), FaceParsingResultsParser(FaceParsing), GrowMaskWithBlur, PreviewImage, Reroute, Cut By Mask, PreviewImage, MaskToImage, Image Comparer (rgthree), Reroute, SaveImage, ImageCompositeMasked, ShowText|pysssss, LoraLoader, CR Combine Prompt, CheckpointLoaderSimple, CR Simple Image Compare, SaveImage, PreviewImage, KSampler, PreviewImage]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 0.7000000000000001, "checkpoint": "epicrealismXL_v8Kiss.safetensors", "denoise": 0.3, "lora_name": "epiCRealLife.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 344932621520769, "steps": 30, "strength_clip": 1, "strength_model": 1}
---

# 平台全量/EKKIVOK - REAL SKIN FINAL_1868944134554951682.json

> 来源文件 `comfyui_library/workflows/平台全量/EKKIVOK - REAL SKIN FINAL_1868944134554951682.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LoadImage`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `Anything Everywhere`
- `LayerMask: PersonMaskUltra V2`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `MaskPreview+`
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
- `Image Comparer (rgthree)`
- `Reroute`
- `SaveImage`
- `ImageCompositeMasked`
- `ShowText|pysssss`
- `LoraLoader` ★核心
- `CR Combine Prompt`
- `CheckpointLoaderSimple` ★核心
- `CR Simple Image Compare`
- `SaveImage`
- `PreviewImage`
- `KSampler` ★核心
- `PreviewImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `epiCRealLife.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `epicrealismXL_v8Kiss.safetensors`
- `seed` = `344932621520769`
- `steps` = `30`
- `cfg` = `0.7000000000000001`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.3`

## 知识

覆盖率 **74%**（25/34）

**有卡**：`LoadImage`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`LayerMask: PersonMaskUltra V2`、`CLIPTextEncode`、`VAEEncode`、`SetLatentNoiseMask`、`VAEDecode`、`MaskPreview+`、`FaceParsingProcessorLoader(FaceParsing)`、`FaceParsingModelLoader(FaceParsing)`、`FaceParse(FaceParsing)`、`FaceParsingResultsParser(FaceParsing)`、`GrowMaskWithBlur`、`Cut By Mask`、`MaskToImage`、`SaveImage`、`ImageCompositeMasked`、`LoraLoader`、`CR Combine Prompt`、`CheckpointLoaderSimple`、`CR Simple Image Compare`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SetLatentNoiseMask、VAEEncode、LoraLoader
