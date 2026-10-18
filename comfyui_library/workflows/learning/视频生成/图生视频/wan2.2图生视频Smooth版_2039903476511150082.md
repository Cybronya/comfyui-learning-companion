---
key: 视频生成/图生视频/wan2.2图生视频Smooth版_2039903476511150082.json
name: wan2.2图生视频Smooth版_2039903476511150082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频Smooth版_2039903476511150082.json
hash: 1bd7ea9afee8d0e9
coverage: 0.804878
learned_at: 2026-10-15 22:36:12
nodes: [Note, ImageScaleBy, Note, ImageResizeKJv2, easy cleanGpuUsed, CLIPVisionEncode, Note, Note, KSamplerAdvanced, VAEDecode, LayerUtility: PurgeVRAM, KSamplerAdvanced, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, RunningHub Deepcleaner, Reroute, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, Note, Note, CLIPVisionLoader, VAELoader, CLIPLoader, CLIPTextEncode, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, JWInteger, easy anythingIndexSwitch, CLIPTextEncode, JWInteger, Seed (rgthree), Note, Float, VHS_VideoCombine, VHS_VideoCombine, Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频Smooth版_2039903476511150082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039903476511150082.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（41 个）：
- `Note`
- `ImageScaleBy`
- `Note`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `Note`
- `Note`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `RunningHub Deepcleaner`
- `Reroute`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `JWInteger`
- `easy anythingIndexSwitch`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `Seed (rgthree)`
- `Note`
- `Float`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（33/41）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`KSamplerAdvanced`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`RunningHub Deepcleaner`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`JWInteger`、`easy anythingIndexSwitch`、`Seed (rgthree)`、`Float`、`VHS_VideoCombine`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
