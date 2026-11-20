---
key: 平台全量/Seamless 360° Flux Image Generator_1891331746825379841.json
name: Seamless 360° Flux Image Generator_1891331746825379841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Seamless 360° Flux Image Generator_1891331746825379841.json
hash: 6bca83e20d5e9600
coverage: 1
learned_at: 2026-11-14 00:58:22
nodes: [Cut By Mask, Cut By Mask, ImageCompositeAbsolute, ImageCompositeAbsolute, AlphaChanelRemove, VAEDecode, DifferentialDiffusion, AlphaChanelRemove, InpaintModelConditioning, JjkShowText, CLIPTextEncode, KSampler, UNETLoader, Florence2ModelLoader, ImageUpscaleWithModel, SaveImage, EmptySD3LatentImage, GlobalSeed //Inspire, UNETLoader, UpscaleModelLoader, VAELoader, LoraLoaderModelOnly, DualCLIPLoader, ConditioningZeroOut, FluxGuidance, VAEDecode, InjectNoiseToLatent, KSamplerAdvanced, KSamplerAdvanced, ETN_CropImage, CR Color Bars, ETN_CropImage, Paste By Mask, Paste By Mask, ImageInvert, CR Color Bars, ImageBlur, Image To Mask, Florence2Run, FluxGuidance, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 平台全量/Seamless 360° Flux Image Generator_1891331746825379841.json

> 来源文件 `comfyui_library/workflows/平台全量/Seamless 360° Flux Image Generator_1891331746825379841.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `Cut By Mask`
- `Cut By Mask`
- `ImageCompositeAbsolute`
- `ImageCompositeAbsolute`
- `AlphaChanelRemove`
- `VAEDecode` ★核心
- `DifferentialDiffusion`
- `AlphaChanelRemove`
- `InpaintModelConditioning`
- `JjkShowText`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `Florence2ModelLoader`
- `ImageUpscaleWithModel`
- `SaveImage`
- `EmptySD3LatentImage`
- `GlobalSeed //Inspire`
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAEDecode` ★核心
- `InjectNoiseToLatent`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ETN_CropImage`
- `CR Color Bars`
- `ETN_CropImage`
- `Paste By Mask`
- `Paste By Mask`
- `ImageInvert`
- `CR Color Bars`
- `ImageBlur`
- `Image To Mask`
- `Florence2Run`
- `FluxGuidance`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（41/41）

**有卡**：`Cut By Mask`、`ImageCompositeAbsolute`、`AlphaChanelRemove`、`VAEDecode`、`DifferentialDiffusion`、`InpaintModelConditioning`、`JjkShowText`、`CLIPTextEncode`、`KSampler`、`UNETLoader`、`Florence2ModelLoader`、`ImageUpscaleWithModel`、`SaveImage`、`EmptySD3LatentImage`、`GlobalSeed //Inspire`、`UpscaleModelLoader`、`VAELoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`ConditioningZeroOut`、`FluxGuidance`、`InjectNoiseToLatent`、`KSamplerAdvanced`、`ETN_CropImage`、`CR Color Bars`、`Paste By Mask`、`ImageInvert`、`ImageBlur`、`Image To Mask`、`Florence2Run`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、FluxGuidance
