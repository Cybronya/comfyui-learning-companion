---
key: 图片生成/图生图/Fill flux OneReward-image expansion扩图_1966338160613601281.json
name: Fill flux OneReward-image expansion扩图_1966338160613601281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Fill flux OneReward-image expansion扩图_1966338160613601281.json
hash: 0ed0f403691c0cab
coverage: 0.95
learned_at: 2026-10-23 10:55:19
nodes: [DifferentialDiffusion, InpaintModelConditioning, DualCLIPLoader, VAELoader, VAEDecode, KSampler, FluxGuidance, CLIPTextEncode, CLIPTextEncode, InvertMask, LayerUtility: ExtendCanvas, LayerUtility: ImageScaleByAspectRatio V2, GrowMask, SaveImage, RH_Translator, LayerUtility: TextBox, UNETLoader, SaveImage, LoadImage, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 928442777897807, "steps": 20}
---

# 图片生成/图生图/Fill flux OneReward-image expansion扩图_1966338160613601281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Fill flux OneReward-image expansion扩图_1966338160613601281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `InvertMask`
- `LayerUtility: ExtendCanvas`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMask`
- `SaveImage`
- `RH_Translator`
- `LayerUtility: TextBox`
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `Note`

## 关键参数

- `seed` = `928442777897807`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`DifferentialDiffusion`、`InpaintModelConditioning`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`KSampler`、`FluxGuidance`、`CLIPTextEncode`、`InvertMask`、`LayerUtility: ExtendCanvas`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMask`、`SaveImage`、`RH_Translator`、`LayerUtility: TextBox`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
