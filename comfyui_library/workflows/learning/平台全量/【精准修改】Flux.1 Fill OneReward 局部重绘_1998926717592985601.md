---
key: 平台全量/【精准修改】Flux.1 Fill OneReward 局部重绘_1998926717592985601.json
name: 【精准修改】Flux.1 Fill OneReward 局部重绘_1998926717592985601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【精准修改】Flux.1 Fill OneReward 局部重绘_1998926717592985601.json
hash: e2693ae1008186e8
coverage: 0.84375
learned_at: 2026-11-14 01:24:50
nodes: [孤海图像缩放按像素, ToBinaryMask, Mask Fill Holes, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, CLIPTextEncode, FluxGuidance, VAELoader, DifferentialDiffusion, VAEDecode, InpaintModelConditioning, PreviewImage, GrowMaskWithBlur, CLIPTextEncode, PreviewImage, LayerUtility: CropByMask V2, ImpactInt, LayerMask: MaskPreview, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: RestoreCropBox, CR Text Concatenate, SaveImage, Image Comparer (rgthree), LoadImage, Note, Note, KSamplerAdvanced, LoraLoaderModelOnly, Text Multiline, RH_Translator]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_cfg_pp", "seed": "enable", "steps": "randomize"}
---

# 平台全量/【精准修改】Flux.1 Fill OneReward 局部重绘_1998926717592985601.json

> 来源文件 `comfyui_library/workflows/平台全量/【精准修改】Flux.1 Fill OneReward 局部重绘_1998926717592985601.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（32 个）：
- `孤海图像缩放按像素`
- `ToBinaryMask`
- `Mask Fill Holes`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `VAELoader`
- `DifferentialDiffusion`
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `PreviewImage`
- `GrowMaskWithBlur`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `LayerUtility: CropByMask V2`
- `ImpactInt`
- `LayerMask: MaskPreview`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: RestoreCropBox`
- `CR Text Concatenate`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Note`
- `Note`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `RH_Translator`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_cfg_pp`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`孤海图像缩放按像素`、`ToBinaryMask`、`Mask Fill Holes`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`CLIPTextEncode`、`FluxGuidance`、`VAELoader`、`DifferentialDiffusion`、`VAEDecode`、`InpaintModelConditioning`、`GrowMaskWithBlur`、`LayerUtility: CropByMask V2`、`ImpactInt`、`LayerMask: MaskPreview`、`LayerMask: MaskGrow`、`LayerUtility: RestoreCropBox`、`CR Text Concatenate`、`SaveImage`、`LoadImage`、`KSamplerAdvanced`、`Text Multiline`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerAdvanced
