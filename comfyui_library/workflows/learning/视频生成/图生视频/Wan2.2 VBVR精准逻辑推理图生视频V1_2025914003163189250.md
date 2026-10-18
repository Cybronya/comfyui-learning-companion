---
key: 视频生成/图生视频/Wan2.2 VBVR精准逻辑推理图生视频V1_2025914003163189250.json
name: Wan2.2 VBVR精准逻辑推理图生视频V1_2025914003163189250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 VBVR精准逻辑推理图生视频V1_2025914003163189250.json
hash: 561027797454bd1e
coverage: 0.75
learned_at: 2026-10-15 22:35:13
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, VHS_VideoCombine, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, CLIPTextEncode, VHS_VideoCombine, Reroute, Note, Reroute, RunningHub Deepcleaner, ImageFromBatch+, LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, Float, Note, PathchSageAttentionKJ, JWInteger, JWInteger, CR Prompt Text, LoadImage, Seed (rgthree), PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 VBVR精准逻辑推理图生视频V1_2025914003163189250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2025914003163189250.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `ImageResizeKJv2`
- `SaveImage`
- `ColorMatch`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `Note`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `Pick From Batch (mtb)`
- `VAEDecode` ★核心
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `Reroute`
- `Note`
- `Reroute`
- `RunningHub Deepcleaner`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `Float`
- `Note`
- `PathchSageAttentionKJ`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `LoadImage`
- `Seed (rgthree)`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（39/52）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`VHS_VideoCombine`、`Pick From Batch (mtb)`、`VAEDecode`、`PainterI2V`、`RunningHub Deepcleaner`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`Float`、`PathchSageAttentionKJ`、`JWInteger`、`LoadImage`、`Seed (rgthree)`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
