---
key: 平台全量/✅Flux Kontext+Union Pro2.0深度迁移_2003351711626428418.json
name: ✅Flux Kontext+Union Pro2.0深度迁移_2003351711626428418
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/✅Flux Kontext+Union Pro2.0深度迁移_2003351711626428418.json
hash: 985b1539dc763784
coverage: 0.9375
learned_at: 2026-11-14 01:21:05
nodes: [LoadImage, LoadImage, VAELoader, DualCLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, FluxKontextImageScale, DF_Get_image_size, VAEEncode, EmptySD3LatentImage, CLIPTextEncode, JWInteger, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, PreviewImage, UNETLoader, CR Prompt Text, ControlNetLoader, SetUnionControlNetType, CLIPTextEncode, ReferenceLatent, FluxGuidance, ControlNetApplySD3, KSampler, VAEDecode, PurgeVRAM_UTK, SeedVR2GGUF, ImageConcatMulti, PDImageResizeV2, SaveImage, SaveImage, SaveImage, Anything Everywhere3]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 351694158957741, "steps": 20}
---

# 平台全量/✅Flux Kontext+Union Pro2.0深度迁移_2003351711626428418.json

> 来源文件 `comfyui_library/workflows/平台全量/✅Flux Kontext+Union Pro2.0深度迁移_2003351711626428418.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `DualCLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxKontextImageScale`
- `DF_Get_image_size`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `PreviewImage`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `ControlNetApplySD3` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PurgeVRAM_UTK`
- `SeedVR2GGUF`
- `ImageConcatMulti`
- `PDImageResizeV2`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Anything Everywhere3`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `seed` = `351694158957741`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`LoadImage`、`VAELoader`、`DualCLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`FluxKontextImageScale`、`DF_Get_image_size`、`VAEEncode`、`EmptySD3LatentImage`、`CLIPTextEncode`、`JWInteger`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`UNETLoader`、`CR Prompt Text`、`ControlNetLoader`、`SetUnionControlNetType`、`ReferenceLatent`、`FluxGuidance`、`ControlNetApplySD3`、`KSampler`、`VAEDecode`、`PurgeVRAM_UTK`、`SeedVR2GGUF`、`ImageConcatMulti`、`PDImageResizeV2`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、ControlNetApplySD3
