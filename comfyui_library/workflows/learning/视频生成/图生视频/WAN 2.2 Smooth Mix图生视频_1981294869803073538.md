---
key: 视频生成/图生视频/WAN 2.2 Smooth Mix图生视频_1981294869803073538.json
name: WAN 2.2 Smooth Mix图生视频_1981294869803073538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN 2.2 Smooth Mix图生视频_1981294869803073538.json
hash: a1e816ef9fd6a76b
coverage: 0.75
learned_at: 2026-10-15 22:32:37
nodes: [Note, ImageScaleBy, Note, CLIPTextEncode, StringConcatenate, ImageResizeKJv2, easy cleanGpuUsed, RIFE VFI, SaveImage, ColorMatch, ImageScaleBy, Pick From Batch (mtb), easy cleanGpuUsed, CLIPVisionEncode, ModelSamplingSD3, Note, CLIPVisionLoader, VAEDecode, VAELoader, easy showAnything, Note, CLIPTextEncode, Seed (rgthree), WanImageToVideo, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, CLIPLoader, UNETLoader, PreviewImage, Note, PrimitiveStringMultiline, UNETLoader, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, CR Prompt Text, JWInteger, ShowText|pysssss, Qwen3_VQA, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN 2.2 Smooth Mix图生视频_1981294869803073538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981294869803073538.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `Note`
- `ImageScaleBy`
- `Note`
- `CLIPTextEncode` ★核心
- `StringConcatenate`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `SaveImage`
- `ColorMatch`
- `ImageScaleBy`
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `Note`
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `easy showAnything`
- `Note`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `WanImageToVideo`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PreviewImage`
- `Note`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `CR Prompt Text`
- `JWInteger`
- `ShowText|pysssss`
- `Qwen3_VQA`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（33/44）

**有卡**：`ImageScaleBy`、`CLIPTextEncode`、`StringConcatenate`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`RIFE VFI`、`SaveImage`、`ColorMatch`、`Pick From Batch (mtb)`、`CLIPVisionEncode`、`ModelSamplingSD3`、`CLIPVisionLoader`、`VAEDecode`、`VAELoader`、`Seed (rgthree)`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`CLIPLoader`、`UNETLoader`、`KSamplerAdvanced`、`VHS_VideoCombine`、`CR Prompt Text`、`Qwen3_VQA`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
