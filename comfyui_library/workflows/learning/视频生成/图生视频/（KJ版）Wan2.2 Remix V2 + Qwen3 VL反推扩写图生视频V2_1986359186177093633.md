---
key: 视频生成/图生视频/（KJ版）Wan2.2 Remix V2 + Qwen3 VL反推扩写图生视频V2_1986359186177093633.json
name: （KJ版）Wan2.2 Remix V2 + Qwen3 VL反推扩写图生视频V2_1986359186177093633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1986359186177093633.json
hash: 7c1050253fc6af10
coverage: 0.741379
learned_at: 2026-10-15 22:32:55
nodes: [UnetLoaderGGUF, UnetLoaderGGUF, Note, Note, Note, CLIPTextEncode, ImageResizeKJv2, CLIPVisionEncode, ModelSamplingSD3, Note, VAELoader, Seed (rgthree), WanImageToVideo, Note, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, ModelSamplingSD3, CLIPVisionLoader, KSamplerAdvanced, easy showAnything, CLIPLoader, KSamplerAdvanced, Pick From Batch (mtb), easy cleanGpuUsed, VAEDecode, ImageScaleBy, Note, LoadImage, VHS_SelectFilename, VHS_VideoCombine, easy showAnything, Any To Any, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, Note, Note, CLIPTextEncode, easy cleanGpuUsed, TT_img_enc, TT_img_enc_v2, SaveImage, SaveImage, Note, CR Prompt Text, CR Prompt Text, CR Prompt Text, JWInteger, Text Concatenate, CR Prompt Text, VHS_VideoCombine, JWInteger, Qwen3_VQA, Text Concatenate, easy showAnything, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/（KJ版）Wan2.2 Remix V2 + Qwen3 VL反推扩写图生视频V2_1986359186177093633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986359186177093633.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `Note`
- `VAELoader`
- `Seed (rgthree)`
- `WanImageToVideo`
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `ModelSamplingSD3`
- `CLIPVisionLoader`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `Note`
- `LoadImage`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy showAnything`
- `Any To Any`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `TT_img_enc`
- `TT_img_enc_v2`
- `SaveImage`
- `SaveImage`
- `Note`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `JWInteger`
- `Text Concatenate`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `JWInteger`
- `Qwen3_VQA`
- `Text Concatenate`
- `easy showAnything`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（43/58）

**有卡**：`UnetLoaderGGUF`、`CLIPTextEncode`、`ImageResizeKJv2`、`CLIPVisionEncode`、`ModelSamplingSD3`、`VAELoader`、`Seed (rgthree)`、`WanImageToVideo`、`LoraLoaderModelOnly`、`CLIPVisionLoader`、`KSamplerAdvanced`、`CLIPLoader`、`Pick From Batch (mtb)`、`easy cleanGpuUsed`、`VAEDecode`、`ImageScaleBy`、`LoadImage`、`VHS_SelectFilename`、`VHS_VideoCombine`、`Any To Any`、`LayerUtility: ImageScaleByAspectRatio V2`、`TT_img_enc`、`TT_img_enc_v2`、`SaveImage`、`CR Prompt Text`、`JWInteger`、`Text Concatenate`、`Qwen3_VQA`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
