---
key: 平台全量/RealSkin Flux Enhancer_1878637014601080833.json
name: RealSkin Flux Enhancer_1878637014601080833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/RealSkin Flux Enhancer_1878637014601080833.json
hash: a2aa53a334998386
coverage: 0.695652
learned_at: 2026-11-14 00:54:35
nodes: [SamplerCustomAdvanced, VAEEncode, SetLatentNoiseMask, CheckpointLoaderSimple, BasicScheduler, KSamplerSelect, LoraLoader, MaskPreview+, FaceParsingProcessorLoader(FaceParsing), PreviewImage, MaskToImage, Cut By Mask, CLIPTextEncode, CLIPTextEncode, BasicGuider, PreviewImage, FaceParsingModelLoader(FaceParsing), VAEDecode, PreviewImage, FaceParsingResultsParser(FaceParsing), PreviewImage, FaceParse(FaceParsing), GrowMaskWithBlur, VAEDecode, Image Comparer (rgthree), CLIPTextEncode, SDXLEmptyLatentSizePicker+, RandomNoise, LayerMask: PersonMaskUltra V2, KSampler, Fast Groups Muter (rgthree), Reroute, Reroute, Reroute, Reroute, CR Text, Reroute, Note, Note, UNETLoader, DualCLIPLoader, LoraLoader, VAELoader, Note, ImageCompositeMasked, SaveImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 0, "cfg": 7, "checkpoint": "epicrealism_naturalSinRC1VAE.safetensors", "denoise": 0.25, "height": 1, "lora_name": "realism_lora.safetensors", "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 821625155047422, "steps": 25, "strength_clip": 1, "strength_model": 0.8, "width": "832x1152 (0.72)"}
---

# 平台全量/RealSkin Flux Enhancer_1878637014601080833.json

> 来源文件 `comfyui_library/workflows/平台全量/RealSkin Flux Enhancer_1878637014601080833.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `CheckpointLoaderSimple` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `LoraLoader` ★核心
- `MaskPreview+`
- `FaceParsingProcessorLoader(FaceParsing)`
- `PreviewImage`
- `MaskToImage`
- `Cut By Mask`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `PreviewImage`
- `FaceParsingModelLoader(FaceParsing)`
- `VAEDecode` ★核心
- `PreviewImage`
- `FaceParsingResultsParser(FaceParsing)`
- `PreviewImage`
- `FaceParse(FaceParsing)`
- `GrowMaskWithBlur`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心
- `RandomNoise`
- `LayerMask: PersonMaskUltra V2`
- `KSampler` ★核心
- `Fast Groups Muter (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CR Text`
- `Reroute`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `VAELoader`
- `Note`
- `ImageCompositeMasked`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `epicrealism_naturalSinRC1VAE.safetensors`
- `lora_name` = `realism_lora.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `width` = `832x1152 (0.72)`
- `height` = `1`
- `batch_size` = `0`
- `seed` = `821625155047422`
- `steps` = `25`
- `cfg` = `7`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.25`

## 知识

覆盖率 **70%**（32/46）

**有卡**：`SamplerCustomAdvanced`、`VAEEncode`、`SetLatentNoiseMask`、`CheckpointLoaderSimple`、`BasicScheduler`、`KSamplerSelect`、`LoraLoader`、`MaskPreview+`、`FaceParsingProcessorLoader(FaceParsing)`、`MaskToImage`、`Cut By Mask`、`CLIPTextEncode`、`BasicGuider`、`FaceParsingModelLoader(FaceParsing)`、`VAEDecode`、`FaceParsingResultsParser(FaceParsing)`、`FaceParse(FaceParsing)`、`GrowMaskWithBlur`、`SDXLEmptyLatentSizePicker+`、`RandomNoise`、`LayerMask: PersonMaskUltra V2`、`KSampler`、`CR Text`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ImageCompositeMasked`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、KSamplerSelect、SamplerCustomAdvanced
