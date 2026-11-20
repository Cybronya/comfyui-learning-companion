---
key: 平台全量/图像编辑工作流（flux_kontext+gemini+icedit支持中文）_1938632768190341121.json
name: 图像编辑工作流（flux_kontext+gemini+icedit支持中文）_1938632768190341121
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/图像编辑工作流（flux_kontext+gemini+icedit支持中文）_1938632768190341121.json
hash: cd8d588cffb8b282
coverage: 0.944444
learned_at: 2026-11-14 01:53:42
nodes: [VAELoader, DualCLIPLoader, LoadImage, ConditioningZeroOut, FluxKontextImageScale, VAEEncode, ReferenceLatent, FluxGuidance, KSampler, VAEDecode, CLIPTextEncode, Google-Gemini-PL, SaveImage, LoadImage, UNETLoader, DualCLIPLoader, LoadImage, UNETLoader, FluxGuidance, VAELoader, FlexLoraLoaderModelOnly, InpaintModelConditioning, LmcqDeepLoader, Text, LmcqDeepGen, ImagePadForOutpaint, ConditioningZeroOut, KSampler, DifferentialDiffusion, StringFunction|pysssss, SaveImage, CLIPTextEncode, VAEDecode, SaveImage, Fast Groups Muter (rgthree), Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 148977929511327, "steps": 20}
---

# 平台全量/图像编辑工作流（flux_kontext+gemini+icedit支持中文）_1938632768190341121.json

> 来源文件 `comfyui_library/workflows/平台全量/图像编辑工作流（flux_kontext+gemini+icedit支持中文）_1938632768190341121.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `VAELoader`
- `DualCLIPLoader`
- `LoadImage`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `Google-Gemini-PL`
- `SaveImage`
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoadImage`
- `UNETLoader` ★核心
- `FluxGuidance`
- `VAELoader`
- `FlexLoraLoaderModelOnly` ★核心
- `InpaintModelConditioning`
- `LmcqDeepLoader`
- `Text`
- `LmcqDeepGen`
- `ImagePadForOutpaint`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `DifferentialDiffusion`
- `StringFunction|pysssss`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Muter (rgthree)`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `148977929511327`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`VAELoader`、`DualCLIPLoader`、`LoadImage`、`ConditioningZeroOut`、`FluxKontextImageScale`、`VAEEncode`、`ReferenceLatent`、`FluxGuidance`、`KSampler`、`VAEDecode`、`CLIPTextEncode`、`Google-Gemini-PL`、`SaveImage`、`UNETLoader`、`FlexLoraLoaderModelOnly`、`InpaintModelConditioning`、`LmcqDeepLoader`、`Text`、`LmcqDeepGen`、`ImagePadForOutpaint`、`DifferentialDiffusion`、`StringFunction|pysssss`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
