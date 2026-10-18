---
key: 视频生成/图生视频/（KJ版-（自用））Wan2.2 Remix V2 + Qwen VL3图生视频V2_1986359267705946114.json
name: （KJ版-（自用））Wan2.2 Remix V2 + Qwen VL3图生视频V2_1986359267705946114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（KJ版-（自用））Wan2.2 Remix V2 + Qwen VL3图生视频V2_1986359267705946114.json
hash: f59c7b23a14db83c
coverage: 0.714286
learned_at: 2026-10-15 22:32:55
nodes: [UnetLoaderGGUF, UnetLoaderGGUF, Note, Note, Note, ImageResizeKJv2, CLIPVisionEncode, ModelSamplingSD3, Note, VAELoader, Seed (rgthree), WanImageToVideo, Note, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, Pick From Batch (mtb), easy cleanGpuUsed, ImageScaleBy, VHS_SelectFilename, JWInteger, VHS_VideoCombine, easy showAnything, Any To Any, Note, Note, Note, JWInteger, CR Prompt Text, easy cleanGpuUsed, TT_img_enc_v2, SaveImage, SaveImage, TT_img_enc, VHS_VideoCombine, CR Prompt Text, CLIPLoader, VAEDecode, Note, easy showAnything, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, CLIPTextEncode, CLIPVisionLoader, Text Concatenate, easy showAnything, easy showAnything, LoadImage, Qwen3_VQA, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/（KJ版-（自用））Wan2.2 Remix V2 + Qwen VL3图生视频V2_1986359267705946114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986359267705946114.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Note`
- `Note`
- `Note`
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
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `VHS_SelectFilename`
- `JWInteger`
- `VHS_VideoCombine`
- `easy showAnything`
- `Any To Any`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `TT_img_enc_v2`
- `SaveImage`
- `SaveImage`
- `TT_img_enc`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Note`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `Text Concatenate`
- `easy showAnything`
- `easy showAnything`
- `LoadImage`
- `Qwen3_VQA`
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

覆盖率 **71%**（40/56）

**有卡**：`UnetLoaderGGUF`、`ImageResizeKJv2`、`CLIPVisionEncode`、`ModelSamplingSD3`、`VAELoader`、`Seed (rgthree)`、`WanImageToVideo`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`Pick From Batch (mtb)`、`easy cleanGpuUsed`、`ImageScaleBy`、`VHS_SelectFilename`、`JWInteger`、`VHS_VideoCombine`、`Any To Any`、`CR Prompt Text`、`TT_img_enc_v2`、`SaveImage`、`TT_img_enc`、`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`Text Concatenate`、`LoadImage`、`Qwen3_VQA`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
