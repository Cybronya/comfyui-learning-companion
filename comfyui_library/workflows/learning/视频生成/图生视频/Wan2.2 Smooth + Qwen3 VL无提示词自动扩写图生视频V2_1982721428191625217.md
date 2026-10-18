---
key: 视频生成/图生视频/Wan2.2 Smooth + Qwen3 VL无提示词自动扩写图生视频V2_1982721428191625217.json
name: Wan2.2 Smooth + Qwen3 VL无提示词自动扩写图生视频V2_1982721428191625217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Smooth + Qwen3 VL无提示词自动扩写图生视频V2_1982721428191625217.json
hash: ce8d3d6ec9eee222
coverage: 0.719298
learned_at: 2026-10-15 22:32:42
nodes: [UnetLoaderGGUF, UnetLoaderGGUF, Note, Note, Note, CLIPTextEncode, ImageResizeKJv2, CLIPVisionEncode, ModelSamplingSD3, Note, VAELoader, Seed (rgthree), WanImageToVideo, Note, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, UNETLoader, ModelSamplingSD3, CLIPVisionLoader, KSamplerAdvanced, easy showAnything, CLIPLoader, KSamplerAdvanced, Pick From Batch (mtb), easy cleanGpuUsed, VAEDecode, ImageScaleBy, Note, VHS_SelectFilename, VHS_VideoCombine, easy showAnything, Any To Any, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, Note, Note, CLIPTextEncode, easy cleanGpuUsed, TT_img_enc, TT_img_enc_v2, SaveImage, SaveImage, Note, CR Prompt Text, JWInteger, VHS_VideoCombine, JWInteger, CR Prompt Text, LoadImage, CR Prompt Text, UNETLoader, Qwen3_VQA, easy showAnything, easy showAnything, Text Concatenate]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Smooth + Qwen3 VL无提示词自动扩写图生视频V2_1982721428191625217.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982721428191625217.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
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
- `UNETLoader` ★核心
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
- `JWInteger`
- `VHS_VideoCombine`
- `JWInteger`
- `CR Prompt Text`
- `LoadImage`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `Qwen3_VQA`
- `easy showAnything`
- `easy showAnything`
- `Text Concatenate`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **72%**（41/57）

**有卡**：`UnetLoaderGGUF`、`CLIPTextEncode`、`ImageResizeKJv2`、`CLIPVisionEncode`、`ModelSamplingSD3`、`VAELoader`、`Seed (rgthree)`、`WanImageToVideo`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPVisionLoader`、`KSamplerAdvanced`、`CLIPLoader`、`Pick From Batch (mtb)`、`easy cleanGpuUsed`、`VAEDecode`、`ImageScaleBy`、`VHS_SelectFilename`、`VHS_VideoCombine`、`Any To Any`、`LayerUtility: ImageScaleByAspectRatio V2`、`TT_img_enc`、`TT_img_enc_v2`、`SaveImage`、`CR Prompt Text`、`JWInteger`、`LoadImage`、`Qwen3_VQA`、`Text Concatenate`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
