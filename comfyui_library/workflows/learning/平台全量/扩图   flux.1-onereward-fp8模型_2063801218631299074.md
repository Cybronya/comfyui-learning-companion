---
key: 平台全量/扩图   flux.1-onereward-fp8模型_2063801218631299074.json
name: 扩图   flux.1-onereward-fp8模型_2063801218631299074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/扩图   flux.1-onereward-fp8模型_2063801218631299074.json
hash: 050797dc67db25d0
coverage: 0.791667
learned_at: 2026-11-14 02:05:07
nodes: [VAELoader, InpaintModelConditioning, easy seed, ConditioningZeroOut, GrowMaskWithBlur, ImageComposite+, SaveImage, UNETLoader, DualCLIPLoader, DifferentialDiffusion, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, SetNode, ImagePadForOutpaint, LayerMask: MaskGrow, GetNode, GetNode, SetNode, FluxGuidance, CLIPTextEncode, Image Comparer (rgthree), LoadImage, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "er_sde", "seed": "enable", "steps": "randomize"}
---

# 平台全量/扩图   flux.1-onereward-fp8模型_2063801218631299074.json

> 来源文件 `comfyui_library/workflows/平台全量/扩图   flux.1-onereward-fp8模型_2063801218631299074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAELoader`
- `InpaintModelConditioning`
- `easy seed`
- `ConditioningZeroOut`
- `GrowMaskWithBlur`
- `ImageComposite+`
- `SaveImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `DifferentialDiffusion`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `SetNode`
- `ImagePadForOutpaint`
- `LayerMask: MaskGrow`
- `GetNode`
- `GetNode`
- `SetNode`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `er_sde`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`VAELoader`、`InpaintModelConditioning`、`easy seed`、`ConditioningZeroOut`、`GrowMaskWithBlur`、`ImageComposite+`、`SaveImage`、`UNETLoader`、`DualCLIPLoader`、`DifferentialDiffusion`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`ImagePadForOutpaint`、`LayerMask: MaskGrow`、`FluxGuidance`、`CLIPTextEncode`、`LoadImage`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、easy seed
