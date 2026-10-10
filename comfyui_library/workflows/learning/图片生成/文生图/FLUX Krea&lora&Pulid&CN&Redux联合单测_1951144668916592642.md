---
key: FLUX Krea&lora&Pulid&CN&Redux联合单测_1951144668916592642.json
name: FLUX Krea&lora&Pulid&CN&Redux联合单测_1951144668916592642
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX Krea&lora&Pulid&CN&Redux联合单测_1951144668916592642.json
hash: a320e725f9112e16
coverage: 0.973333
learned_at: 2026-10-10 20:58:31
nodes: [LoraLoader, LoraLoader, SetUnionControlNetType, AIO_Preprocessor, BasicScheduler, KSamplerSelect, VAEEncode, RandomNoise, VAEDecode, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, ApplyPulidFlux, LoraLoader, CFGGuider, LoraLoader, StyleModelLoader, CLIPVisionLoader, CLIPVisionEncode, StyleModelApply, DualCLIPLoader, ImageResizeKJ, VAELoader, SamplerCustomAdvanced, UNETLoader, AIO_Preprocessor, ControlNetLoader, CLIPTextEncode, CLIPSetLastLayer, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetApplyAdvanced, SetUnionControlNetType, LoraLoader, LoraLoader, SetUnionControlNetType, AIO_Preprocessor, BasicScheduler, KSamplerSelect, RandomNoise, VAEDecode, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, CFGGuider, LoraLoader, StyleModelLoader, CLIPVisionLoader, CLIPVisionEncode, StyleModelApply, DualCLIPLoader, ImageResizeKJ, VAELoader, SamplerCustomAdvanced, UNETLoader, AIO_Preprocessor, ControlNetLoader, ControlNetApplyAdvanced, SetUnionControlNetType, PreviewImage, ApplyPulidFlux, LoadImage, CLIPTextEncode, LoraLoader, LoraLoader, SetUnionControlNetType, AIO_Preprocessor, BasicScheduler, KSamplerSelect, VAEEncode, RandomNoise, VAEDecode, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, LoraLoader, CFGGuider, LoraLoader, StyleModelLoader, DualCLIPLoader, ImageResizeKJ, VAELoader, UNETLoader, AIO_Preprocessor, ControlNetLoader, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetApplyAdvanced, SetUnionControlNetType, PreviewImage, ApplyPulidFlux, LoadImage, CLIPTextEncode, CLIPVisionEncode, LoadImage, StyleModelApply, CLIPVisionLoader, LoraLoader, SetUnionControlNetType, AIO_Preprocessor, BasicScheduler, KSamplerSelect, VAEEncode, RandomNoise, VAEDecode, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, LoraLoader, CFGGuider, LoraLoader, StyleModelLoader, DualCLIPLoader, ImageResizeKJ, VAELoader, SamplerCustomAdvanced, UNETLoader, AIO_Preprocessor, ControlNetLoader, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetApplyAdvanced, SetUnionControlNetType, PreviewImage, ApplyPulidFlux, LoadImage, CLIPVisionEncode, LoadImage, StyleModelApply, CLIPVisionLoader, SamplerCustomAdvanced, LoraLoader, CLIPTextEncode, LoadImage, PreviewImage, NAGCFGGuider, LoraLoader, VAEEncode, ControlNetApplyAdvanced, CLIPTextEncode, CLIPTextEncode, UNETLoader, DualCLIPLoader, VAELoader, EmptySD3LatentImage, ConditioningZeroOut, KSampler, VAEDecode, SaveImage, CLIPTextEncode]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.6000000000000001, "denoise": 1, "lora_name": "Shingeki no Kyojin (Attack on Titan) Anime Style LoRA-v1", "sampler_name": "euler", "scheduler": "simple", "seed": 82480346685211, "steps": 20, "strength_clip": 0.8, "strength_model": 0.8}
---

# FLUX Krea&lora&Pulid&CN&Redux联合单测_1951144668916592642.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX Krea&lora&Pulid&CN&Redux联合单测_1951144668916592642.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（150 个）：
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `ApplyPulidFlux`
- `LoraLoader` ★核心
- `CFGGuider`
- `LoraLoader` ★核心
- `StyleModelLoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelApply`
- `DualCLIPLoader`
- `ImageResizeKJ`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `CLIPSetLastLayer`
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `CFGGuider`
- `LoraLoader` ★核心
- `StyleModelLoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelApply`
- `DualCLIPLoader`
- `ImageResizeKJ`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `PreviewImage`
- `ApplyPulidFlux`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `LoraLoader` ★核心
- `CFGGuider`
- `LoraLoader` ★核心
- `StyleModelLoader`
- `DualCLIPLoader`
- `ImageResizeKJ`
- `VAELoader`
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `PreviewImage`
- `ApplyPulidFlux`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `LoadImage`
- `StyleModelApply`
- `CLIPVisionLoader`
- `LoraLoader` ★核心
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `LoraLoader` ★核心
- `CFGGuider`
- `LoraLoader` ★核心
- `StyleModelLoader`
- `DualCLIPLoader`
- `ImageResizeKJ`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `PreviewImage`
- `ApplyPulidFlux`
- `LoadImage`
- `CLIPVisionEncode`
- `LoadImage`
- `StyleModelApply`
- `CLIPVisionLoader`
- `SamplerCustomAdvanced` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PreviewImage`
- `NAGCFGGuider`
- `LoraLoader` ★核心
- `VAEEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Shingeki no Kyojin (Attack on Titan) Anime Style LoRA-v1`
- `strength_model` = `0.8`
- `strength_clip` = `0.8`
- `controlnet_strength` = `0.6000000000000001`
- `seed` = `82480346685211`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（146/150）

**有卡**：`LoraLoader`、`SetUnionControlNetType`、`AIO_Preprocessor`、`BasicScheduler`、`KSamplerSelect`、`VAEEncode`、`RandomNoise`、`VAEDecode`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`PulidFluxModelLoader`、`ApplyPulidFlux`、`CFGGuider`、`StyleModelLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`StyleModelApply`、`DualCLIPLoader`、`ImageResizeKJ`、`VAELoader`、`SamplerCustomAdvanced`、`UNETLoader`、`ControlNetLoader`、`CLIPTextEncode`、`CLIPSetLastLayer`、`ControlNetApplyAdvanced`、`LoadImage`、`NAGCFGGuider`、`EmptySD3LatentImage`、`ConditioningZeroOut`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplyAdvanced
