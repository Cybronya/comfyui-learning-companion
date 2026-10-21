---
key: 图片生成/图生图/FLUX+WAN2.2高清放大修复细节_2064895041612632065.json
name: FLUX+WAN2.2高清放大修复细节_2064895041612632065
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX+WAN2.2高清放大修复细节_2064895041612632065.json
hash: 71773e4b8733b5ba
coverage: 0.9
learned_at: 2026-10-21 00:39:04
nodes: [DualCLIPLoader, ConditioningZeroOut, FluxGuidance, VAEEncode, UNETLoader, LoraLoaderModelOnly, PreviewAny, ConditioningZeroOut, KSampler, LayerUtility: PurgeVRAM V2, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SeedVR2VideoUpscaler, VHS_VAEEncodeBatched, JDCN_StringToList, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, ReferenceLatent, VAEDecode, VAEDecode, ModelSamplingSD3, CLIPLoader, VAELoader, KSampler, VAELoader, easy int, Image Comparer (rgthree), SaveImage, PreviewImage, Float, CLIPTextEncode, CLIPTextEncode, AILab_QwenVL, NunchakuFluxLoraLoader, LayerUtility: PurgeVRAM V2, NunchakuFluxDiTLoader, LayerUtility: PurgeVRAM V2, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 852435369943954, "steps": 10}
---

# 图片生成/图生图/FLUX+WAN2.2高清放大修复细节_2064895041612632065.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX+WAN2.2高清放大修复细节_2064895041612632065.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2VideoUpscaler`
- `VHS_VAEEncodeBatched` ★核心
- `JDCN_StringToList`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAELoader`
- `easy int`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `Float`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AILab_QwenVL`
- `NunchakuFluxLoraLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `NunchakuFluxDiTLoader`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `852435369943954`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（36/40）

**有卡**：`DualCLIPLoader`、`ConditioningZeroOut`、`FluxGuidance`、`VAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`VHS_VAEEncodeBatched`、`JDCN_StringToList`、`LayerUtility: ImageScaleByAspectRatio V2`、`ReferenceLatent`、`VAEDecode`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`easy int`、`SaveImage`、`Float`、`CLIPTextEncode`、`AILab_QwenVL`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
