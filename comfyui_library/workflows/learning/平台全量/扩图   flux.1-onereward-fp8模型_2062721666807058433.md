---
key: 平台全量/扩图   flux.1-onereward-fp8模型_2062721666807058433.json
name: 扩图   flux.1-onereward-fp8模型_2062721666807058433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/扩图   flux.1-onereward-fp8模型_2062721666807058433.json
hash: a15f26aa78fca437
coverage: 0.954545
learned_at: 2026-11-14 02:05:07
nodes: [LoraLoaderModelOnly, DualCLIPLoader, UNETLoader, CLIPTextEncode, DifferentialDiffusion, FluxGuidance, VAELoader, InpaintModelConditioning, KSamplerAdvanced, ImageComposite+, MemoryCleaner, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, LayerMask: MaskGrow, ImagePadForOutpaint, easy clearCacheAll, SaveImage, ConditioningZeroOut, Image Comparer (rgthree), GrowMaskWithBlur, easy seed, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "er_sde", "seed": "enable", "steps": "randomize"}
---

# 平台全量/扩图   flux.1-onereward-fp8模型_2062721666807058433.json

> 来源文件 `comfyui_library/workflows/平台全量/扩图   flux.1-onereward-fp8模型_2062721666807058433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `DifferentialDiffusion`
- `FluxGuidance`
- `VAELoader`
- `InpaintModelConditioning`
- `KSamplerAdvanced` ★核心
- `ImageComposite+`
- `MemoryCleaner`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `LayerMask: MaskGrow`
- `ImagePadForOutpaint`
- `easy clearCacheAll`
- `SaveImage`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `GrowMaskWithBlur`
- `easy seed`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `er_sde`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`LoraLoaderModelOnly`、`DualCLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`DifferentialDiffusion`、`FluxGuidance`、`VAELoader`、`InpaintModelConditioning`、`KSamplerAdvanced`、`ImageComposite+`、`MemoryCleaner`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`LayerMask: MaskGrow`、`ImagePadForOutpaint`、`easy clearCacheAll`、`SaveImage`、`ConditioningZeroOut`、`GrowMaskWithBlur`、`easy seed`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、easy seed
