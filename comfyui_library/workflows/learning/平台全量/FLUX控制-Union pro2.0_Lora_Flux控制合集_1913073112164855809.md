---
key: 平台全量/FLUX控制-Union pro2.0_Lora_Flux控制合集_1913073112164855809.json
name: FLUX控制-Union pro2.0_Lora_Flux控制合集_1913073112164855809
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX控制-Union pro2.0_Lora_Flux控制合集_1913073112164855809.json
hash: b371c7655950fdc7
coverage: 0.755102
learned_at: 2026-11-14 00:26:01
nodes: [FluxGuidance, DualCLIPLoader, DualCLIPLoader, EmptyLatentImage, VAEDecode, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, KSampler, VAELoader, GetNode, GetImageSize, SetNode, ControlNetApplySD3, SetUnionControlNetType, ControlNetLoader, DifferentialDiffusion, Anything Everywhere, FluxGuidance, ConditioningZeroOut, SetNode, SetNode, GetNode, GetNode, AIO_Preprocessor, PreviewImage, SaveImage, Anything Everywhere, LoadImage, RH_Translator, KSampler, SaveImage, DifferentialDiffusion, LoraLoaderModelOnly, LoraLoaderModelOnly, ConditioningZeroOut, CLIPTextEncode, VAEDecode, InstructPixToPixConditioning, Anything Everywhere, VAELoader, RH_Translator, UNETLoader, CannyEdgePreprocessor, PreviewImage, LoadImage, DepthAnythingPreprocessor, PreviewImage, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.7000000000000002, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 387255478595980, "steps": 28, "width": 512}
---

# 平台全量/FLUX控制-Union pro2.0_Lora_Flux控制合集_1913073112164855809.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX控制-Union pro2.0_Lora_Flux控制合集_1913073112164855809.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `FluxGuidance`
- `DualCLIPLoader`
- `DualCLIPLoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAELoader`
- `GetNode`
- `GetImageSize`
- `SetNode`
- `ControlNetApplySD3` ★核心
- `SetUnionControlNetType`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `Anything Everywhere`
- `FluxGuidance`
- `ConditioningZeroOut`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `AIO_Preprocessor`
- `PreviewImage`
- `SaveImage`
- `Anything Everywhere`
- `LoadImage`
- `RH_Translator`
- `KSampler` ★核心
- `SaveImage`
- `DifferentialDiffusion`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `InstructPixToPixConditioning`
- `Anything Everywhere`
- `VAELoader`
- `RH_Translator`
- `UNETLoader` ★核心
- `CannyEdgePreprocessor`
- `PreviewImage`
- `LoadImage`
- `DepthAnythingPreprocessor`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `387255478595980`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000002`

## 知识

覆盖率 **76%**（37/49）

**有卡**：`FluxGuidance`、`DualCLIPLoader`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`KSampler`、`VAELoader`、`GetImageSize`、`ControlNetApplySD3`、`SetUnionControlNetType`、`ControlNetLoader`、`DifferentialDiffusion`、`ConditioningZeroOut`、`AIO_Preprocessor`、`SaveImage`、`LoadImage`、`RH_Translator`、`InstructPixToPixConditioning`、`CannyEdgePreprocessor`、`DepthAnythingPreprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
