---
key: 视频生成/图生视频/Remix V2 PainterI2V Plus版  浮云 头发动画 图生视频 12.11_1998932620186673154.json
name: Remix V2 PainterI2V Plus版  浮云 头发动画 图生视频 12.11_1998932620186673154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Remix V2 PainterI2V Plus版  浮云 头发动画 图生视频 12.11_1998932620186673154.json
hash: 5a17074007192091
coverage: 0.777778
learned_at: 2026-10-15 22:33:34
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), VAEDecode, LayerUtility: PurgeVRAM, PainterI2V, CLIPTextEncode, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, UNETLoader, AddLabel, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, Seed (rgthree), JWInteger, JWInteger, CR Prompt Text, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Remix V2 PainterI2V Plus版  浮云 头发动画 图生视频 12.11_1998932620186673154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998932620186673154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `PainterI2V`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Reroute`
- `UNETLoader` ★核心
- `AddLabel`
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `Seed (rgthree)`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（35/45）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`PainterI2V`、`UNETLoader`、`PathchSageAttentionKJ`、`AddLabel`、`LayerUtility: ImageScaleByAspectRatio V2`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`Seed (rgthree)`、`JWInteger`、`CR Prompt Text`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
