---
key: 视频生成/图生视频/（自用）Wan2.2 Smooth Mix高低噪模型高动态图生视频V1（KJ版）_1979918269014511617.json
name: （自用）Wan2.2 Smooth Mix高低噪模型高动态图生视频V1（KJ版）_1979918269014511617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979918269014511617.json
hash: 546518119de9a993
coverage: 0.782609
learned_at: 2026-10-15 22:32:27
nodes: [UnetLoaderGGUF, UnetLoaderGGUF, Note, Note, Note, CLIPTextEncode, StringConcatenate, ImageResizeKJv2, CLIPVisionEncode, ModelSamplingSD3, Note, VAELoader, CLIPTextEncode, Seed (rgthree), WanImageToVideo, Note, Note, JWInteger, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, Note, PrimitiveStringMultiline, UNETLoader, ModelSamplingSD3, CR Prompt Text, CLIPVisionLoader, KSamplerAdvanced, LoadImage, easy showAnything, CLIPLoader, RIFE VFI, SaveImage, TT_img_enc_v2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, Pick From Batch (mtb), easy cleanGpuUsed, VAEDecode, ImageScaleBy, SaveImage, Note, TT_img_enc, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/（自用）Wan2.2 Smooth Mix高低噪模型高动态图生视频V1（KJ版）_1979918269014511617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979918269014511617.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `StringConcatenate`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `Note`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `WanImageToVideo`
- `Note`
- `Note`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CR Prompt Text`
- `CLIPVisionLoader`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `easy showAnything`
- `CLIPLoader`
- `RIFE VFI`
- `SaveImage`
- `TT_img_enc_v2`
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `SaveImage`
- `Note`
- `TT_img_enc`
- `CR Prompt Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`UnetLoaderGGUF`、`CLIPTextEncode`、`StringConcatenate`、`ImageResizeKJv2`、`CLIPVisionEncode`、`ModelSamplingSD3`、`VAELoader`、`Seed (rgthree)`、`WanImageToVideo`、`JWInteger`、`LoraLoaderModelOnly`、`UNETLoader`、`CR Prompt Text`、`CLIPVisionLoader`、`KSamplerAdvanced`、`LoadImage`、`CLIPLoader`、`RIFE VFI`、`SaveImage`、`TT_img_enc_v2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`Pick From Batch (mtb)`、`VAEDecode`、`ImageScaleBy`、`TT_img_enc`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
