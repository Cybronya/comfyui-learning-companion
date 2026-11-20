---
key: 平台全量/一键毛坯房装修+flux+kontext+wan2.1高清洗图_1967073041094152194.json
name: 一键毛坯房装修+flux+kontext+wan2.1高清洗图_1967073041094152194
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键毛坯房装修+flux+kontext+wan2.1高清洗图_1967073041094152194.json
hash: 07e7568d2dc2eb56
coverage: 0.921053
learned_at: 2026-11-14 01:29:01
nodes: [ConditioningZeroOut, VAEEncode, ReferenceLatent, FluxGuidance, KSampler, DualCLIPLoader, Image Comparer (rgthree), SaveImage, VAEEncode, easy cleanGpuUsed, easy cleanGpuUsed, UNETLoader, VAELoader, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, KSampler, VAEDecode, ColorMatch, VAEDecode, SaveImage, LoadImage, CLIPTextEncode, PreviewImage, easy imageConcat, easy imageConcat, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RH_LLMAPI_NODE, ShowText, RH_Translator, easy showAnything, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 1072469613203564, "steps": 10}
---

# 平台全量/一键毛坯房装修+flux+kontext+wan2.1高清洗图_1967073041094152194.json

> 来源文件 `comfyui_library/workflows/平台全量/一键毛坯房装修+flux+kontext+wan2.1高清洗图_1967073041094152194.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `KSampler` ★核心
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ColorMatch`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `easy imageConcat`
- `easy imageConcat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `ShowText`
- `RH_Translator`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1072469613203564`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`FluxGuidance`、`KSampler`、`DualCLIPLoader`、`SaveImage`、`easy cleanGpuUsed`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAEDecode`、`ColorMatch`、`LoadImage`、`easy imageConcat`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_LLMAPI_NODE`、`ShowText`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut
