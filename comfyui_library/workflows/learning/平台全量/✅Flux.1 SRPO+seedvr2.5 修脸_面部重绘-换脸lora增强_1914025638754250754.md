---
key: 平台全量/✅Flux.1 SRPO+seedvr2.5 修脸_面部重绘-换脸lora增强_1914025638754250754.json
name: ✅Flux.1 SRPO+seedvr2.5 修脸_面部重绘-换脸lora增强_1914025638754250754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/✅Flux.1 SRPO+seedvr2.5 修脸_面部重绘-换脸lora增强_1914025638754250754.json
hash: e2db93f092d8d871
coverage: 0.483516
learned_at: 2026-11-14 01:21:05
nodes: [FluxGuidance, VAELoader, PreviewImage, CLIPTextEncode, SetUnionControlNetType, GetNode, GetNode, GetNode, ControlNetLoader, SetNode, SetNode, DWPreprocessor, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, ImageSmartSharpen+, SetNode, SetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, SamplerCustom, VAEDecode, SetNode, SetNode, CLIPTextEncode, ConditioningZeroOut, SetNode, UNETLoader, DifferentialDiffusion, DifferentialDiffusion, DetailDaemonSamplerNode, PreviewImage, SetNode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LayerMask: MaskPreview, SetNode, SetNode, TilePreprocessor, LoraLoaderModelOnly, KSamplerSelect, InjectLatentNoise+, ImpactSwitch, GetNode, ImpactSwitch, GetNode, ControlNetApplySD3, SeedVR2VideoUpscaler, SaveImage, CR Text, LoraLoaderModelOnly, EasyCache, InpaintModelConditioning, BasicScheduler, LoraLoaderModelOnly, PreviewImage, LoadImage, LoraLoaderModelOnly, SetNode, SetNode, SetNode, SetNode, SaveImage, LayerMask: PersonMaskUltra V2, InpaintStitchImproved, InpaintCropImproved, SetNode, GetNode, GetNode, InpaintStitchImproved, SaveImage, SaveImage, GetNode, GetNode, Image Comparer (rgthree), GetNode, InjectLatentNoise+, KSampler, DualCLIPLoader, GetNode, SetNode]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.8000000000000002, "denoise": 0.5000000000000001, "sampler_name": "deis", "scheduler": "beta", "seed": 111382123497273, "steps": 10}
---

# 平台全量/✅Flux.1 SRPO+seedvr2.5 修脸_面部重绘-换脸lora增强_1914025638754250754.json

> 来源文件 `comfyui_library/workflows/平台全量/✅Flux.1 SRPO+seedvr2.5 修脸_面部重绘-换脸lora增强_1914025638754250754.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `FluxGuidance`
- `VAELoader`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `SetUnionControlNetType`
- `GetNode`
- `GetNode`
- `GetNode`
- `ControlNetLoader`
- `SetNode`
- `SetNode`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageSmartSharpen+`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SetNode`
- `UNETLoader` ★核心
- `DifferentialDiffusion`
- `DifferentialDiffusion`
- `DetailDaemonSamplerNode` ★核心
- `PreviewImage`
- `SetNode`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LayerMask: MaskPreview`
- `SetNode`
- `SetNode`
- `TilePreprocessor`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `InjectLatentNoise+`
- `ImpactSwitch`
- `GetNode`
- `ImpactSwitch`
- `GetNode`
- `ControlNetApplySD3` ★核心
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `EasyCache`
- `InpaintModelConditioning`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SaveImage`
- `LayerMask: PersonMaskUltra V2`
- `InpaintStitchImproved`
- `InpaintCropImproved`
- `SetNode`
- `GetNode`
- `GetNode`
- `InpaintStitchImproved`
- `SaveImage`
- `SaveImage`
- `GetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `GetNode`
- `InjectLatentNoise+`
- `KSampler` ★核心
- `DualCLIPLoader`
- `GetNode`
- `SetNode`

## 关键参数

- `controlnet_strength` = `0.8000000000000002`
- `seed` = `111382123497273`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **48%**（44/91）

**有卡**：`FluxGuidance`、`VAELoader`、`CLIPTextEncode`、`SetUnionControlNetType`、`ControlNetLoader`、`DWPreprocessor`、`ImageSmartSharpen+`、`VAEDecode`、`SamplerCustom`、`ConditioningZeroOut`、`UNETLoader`、`DifferentialDiffusion`、`DetailDaemonSamplerNode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`LayerMask: MaskPreview`、`TilePreprocessor`、`LoraLoaderModelOnly`、`KSamplerSelect`、`InjectLatentNoise+`、`ControlNetApplySD3`、`SeedVR2VideoUpscaler`、`SaveImage`、`CR Text`、`EasyCache`、`InpaintModelConditioning`、`BasicScheduler`、`LoadImage`、`LayerMask: PersonMaskUltra V2`、`InpaintStitchImproved`、`InpaintCropImproved`、`KSampler`、`DualCLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
