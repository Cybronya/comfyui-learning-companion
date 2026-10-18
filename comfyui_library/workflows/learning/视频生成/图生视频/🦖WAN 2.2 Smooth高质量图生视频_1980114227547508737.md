---
key: 视频生成/图生视频/🦖WAN 2.2 Smooth高质量图生视频_1980114227547508737.json
name: 🦖WAN 2.2 Smooth高质量图生视频_1980114227547508737.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🦖WAN 2.2 Smooth高质量图生视频_1980114227547508737.json
hash: 8665ccf3c939609d
coverage: 0.787234
learned_at: 2026-10-15 22:32:27
nodes: [Note, ImageScaleBy, Note, CLIPTextEncode, StringConcatenate, ImageResizeKJv2, easy cleanGpuUsed, easy showAnything, Note, Seed (rgthree), Note, Note, WanImageToVideo, KSamplerAdvanced, JWInteger, Bjornulf_ShowInt, VAEDecode, CLIPLoader, UNETLoader, UNETLoader, VAELoader, CLIPVisionLoader, CLIPVisionEncode, ModelSamplingSD3, ModelSamplingSD3, Note, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, VHS_VideoCombine, PrimitiveStringMultiline, CLIPTextEncode, RIFE VFI, easy cleanGpuUsed, Pick From Batch (mtb), KSamplerAdvanced, JWInteger, CR Prompt Text, ColorMatch, ImageScaleBy, LoadImage, JWInteger, RH_Captioner, ImpactSwitch, CR Prompt Text, VHS_VideoCombine, PreviewImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/🦖WAN 2.2 Smooth高质量图生视频_1980114227547508737.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980114227547508737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `Note`
- `ImageScaleBy`
- `Note`
- `CLIPTextEncode` ★核心
- `StringConcatenate`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `easy showAnything`
- `Note`
- `Seed (rgthree)`
- `Note`
- `Note`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `Bjornulf_ShowInt`
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `RIFE VFI`
- `easy cleanGpuUsed`
- `Pick From Batch (mtb)`
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `CR Prompt Text`
- `ColorMatch`
- `ImageScaleBy`
- `LoadImage`
- `JWInteger`
- `RH_Captioner`
- `ImpactSwitch`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（37/47）

**有卡**：`ImageScaleBy`、`CLIPTextEncode`、`StringConcatenate`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`Seed (rgthree)`、`WanImageToVideo`、`KSamplerAdvanced`、`JWInteger`、`Bjornulf_ShowInt`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`VHS_VideoCombine`、`RIFE VFI`、`Pick From Batch (mtb)`、`CR Prompt Text`、`ColorMatch`、`LoadImage`、`RH_Captioner`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
