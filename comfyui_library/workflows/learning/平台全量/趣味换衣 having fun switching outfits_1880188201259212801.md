---
key: 平台全量/趣味换衣 having fun switching outfits_1880188201259212801.json
name: 趣味换衣 having fun switching outfits_1880188201259212801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/趣味换衣 having fun switching outfits_1880188201259212801.json
hash: cfc3933f001b4ccd
coverage: 0.851351
learned_at: 2026-11-14 02:47:16
nodes: [Note, KSampler, StyleModelLoader, LoraLoaderModelOnly, DifferentialDiffusion, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, VAEDecode, SaveImage, FluxGuidance, StyleModelApply, CLIPVisionEncode, VAELoader, CLIPTextEncode, DualCLIPLoaderGGUF, CLIPVisionLoader, UnetLoaderGGUF, LoadImage, Image Comparer (rgthree), PreviewImage, GroundingDinoSAMSegment (segment anything), GroundingDinoSAMSegment (segment anything), MaskPreview+, AddMask, MaskPreview+, LayerMask: MaskGrow, MaskPreview+, InpaintModelConditioning, SAMLoader, GroundingDinoModelLoader (segment anything), VAEDecode, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, CLIPTextEncodeFlux, Reroute, Reroute, Reroute, Text Concatenate (JPS), CLIPTextEncodeFlux, EmptySD3LatentImage, CFGGuider, UnetLoaderGGUF, Note, LoraLoader, MaskPreview+, GroundingDinoSAMSegment (segment anything), SAMLoader, GroundingDinoModelLoader (segment anything), MaskPreview+, GroundingDinoSAMSegment (segment anything), MaskPreview+, AddMask, ControlNetLoader, ControlNetInpaintingAliMamaApply, InpaintModelConditioning, LayerMask: MaskGrow, LoadImage, UNETLoader, DualCLIPLoader, SaveImage, PreviewImage, ImageCompositeMasked, Image Comparer (rgthree), SaveImage, CR Text, RH_Captioner, SeargePromptCombiner, StringFunction|pysssss, ShowText|pysssss, RandomNoise, VAELoader, LoadImage]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "jinx-arcane-league-of-legends-season-1-v5.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 356524617621457, "steps": 8, "strength_clip": 1, "strength_model": 0.85}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/趣味换衣 having fun switching outfits_1880188201259212801.json

> 来源文件 `comfyui_library/workflows/平台全量/趣味换衣 having fun switching outfits_1880188201259212801.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `Note`
- `KSampler` ★核心
- `StyleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `DifferentialDiffusion`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `FluxGuidance`
- `StyleModelApply`
- `CLIPVisionEncode`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `DualCLIPLoaderGGUF`
- `CLIPVisionLoader`
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `GroundingDinoSAMSegment (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `MaskPreview+`
- `AddMask`
- `MaskPreview+`
- `LayerMask: MaskGrow`
- `MaskPreview+`
- `InpaintModelConditioning`
- `SAMLoader`
- `GroundingDinoModelLoader (segment anything)`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CLIPTextEncodeFlux` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Text Concatenate (JPS)`
- `CLIPTextEncodeFlux` ★核心
- `EmptySD3LatentImage`
- `CFGGuider`
- `UnetLoaderGGUF` ★核心
- `Note`
- `LoraLoader` ★核心
- `MaskPreview+`
- `GroundingDinoSAMSegment (segment anything)`
- `SAMLoader`
- `GroundingDinoModelLoader (segment anything)`
- `MaskPreview+`
- `GroundingDinoSAMSegment (segment anything)`
- `MaskPreview+`
- `AddMask`
- `ControlNetLoader`
- `ControlNetInpaintingAliMamaApply`
- `InpaintModelConditioning`
- `LayerMask: MaskGrow`
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `SaveImage`
- `PreviewImage`
- `ImageCompositeMasked`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CR Text`
- `RH_Captioner`
- `SeargePromptCombiner`
- `StringFunction|pysssss`
- `ShowText|pysssss`
- `RandomNoise`
- `VAELoader`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `356524617621457`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `lora_name` = `jinx-arcane-league-of-legends-season-1-v5.safetensors`
- `strength_model` = `0.85`
- `strength_clip` = `1`

## 知识

覆盖率 **85%**（63/74）

**有卡**：`KSampler`、`StyleModelLoader`、`LoraLoaderModelOnly`、`DifferentialDiffusion`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`SaveImage`、`FluxGuidance`、`StyleModelApply`、`CLIPVisionEncode`、`VAELoader`、`CLIPTextEncode`、`DualCLIPLoaderGGUF`、`CLIPVisionLoader`、`UnetLoaderGGUF`、`LoadImage`、`GroundingDinoSAMSegment (segment anything)`、`MaskPreview+`、`AddMask`、`LayerMask: MaskGrow`、`InpaintModelConditioning`、`SAMLoader`、`GroundingDinoModelLoader (segment anything)`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`CLIPTextEncodeFlux`、`Text Concatenate (JPS)`、`EmptySD3LatentImage`、`CFGGuider`、`LoraLoader`、`ControlNetLoader`、`ControlNetInpaintingAliMamaApply`、`UNETLoader`、`DualCLIPLoader`、`ImageCompositeMasked`、`CR Text`、`RH_Captioner`、`SeargePromptCombiner`、`StringFunction|pysssss`、`RandomNoise`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
