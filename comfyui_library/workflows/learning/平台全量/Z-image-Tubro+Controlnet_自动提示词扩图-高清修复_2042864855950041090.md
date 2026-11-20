---
key: 平台全量/Z-image-Tubro+Controlnet_自动提示词扩图-高清修复_2042864855950041090.json
name: Z-image-Tubro+Controlnet_自动提示词扩图-高清修复_2042864855950041090
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Z-image-Tubro+Controlnet_自动提示词扩图-高清修复_2042864855950041090.json
hash: 97f3e818d3332da6
coverage: 0.520833
learned_at: 2026-11-14 01:08:22
nodes: [llama_cpp_instruct_adv, LayerUtility: PurgeVRAM V2, VAELoader, CLIPLoader, SetNode, SetNode, ShowText|pysssss, SetNode, GetNode, GetNode, GetNode, ZImageFunControlnet, GetNode, VAEEncode, GetNode, Reroute, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, GetNode, Reroute, Note, SetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, Reroute, LayerUtility: PurgeVRAM V2, SeedVR2LoadDiTModel, Image Comparer (rgthree), ImageScaleToTotalPixels, SeedVR2LoadVAEModel, llama_cpp_model_loader, KSampler, VAEDecode, ImagePadForOutpaint, UNETLoader, ModelPatchLoader, LoadImage, LanPaint_MaskBlend, SetNode, SetNode, SaveImage, SeedVR2VideoUpscaler, Reroute, ImageAndMaskPreview, GetNode, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 1, "steps": 12}
---

# 平台全量/Z-image-Tubro+Controlnet_自动提示词扩图-高清修复_2042864855950041090.json

> 来源文件 `comfyui_library/workflows/平台全量/Z-image-Tubro+Controlnet_自动提示词扩图-高清修复_2042864855950041090.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM V2`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `ShowText|pysssss`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ZImageFunControlnet`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `Reroute`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `GetNode`
- `Reroute`
- `Note`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `llama_cpp_model_loader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImagePadForOutpaint`
- `UNETLoader` ★核心
- `ModelPatchLoader`
- `LoadImage`
- `LanPaint_MaskBlend`
- `SetNode`
- `SetNode`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `ImageAndMaskPreview`
- `GetNode`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **52%**（25/48）

**有卡**：`llama_cpp_instruct_adv`、`LayerUtility: PurgeVRAM V2`、`VAELoader`、`CLIPLoader`、`ZImageFunControlnet`、`VAEEncode`、`CLIPTextEncode`、`ConditioningZeroOut`、`DifferentialDiffusion`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`llama_cpp_model_loader`、`KSampler`、`VAEDecode`、`ImagePadForOutpaint`、`UNETLoader`、`ModelPatchLoader`、`LoadImage`、`LanPaint_MaskBlend`、`SaveImage`、`SeedVR2VideoUpscaler`、`ImageAndMaskPreview`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader
