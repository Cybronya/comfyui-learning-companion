---
key: 视频生成/图生视频/视频-Remix V2.1建筑图生视频V1工作流_2029118702054023169.json
name: 视频-Remix V2.1建筑图生视频V1工作流_2029118702054023169.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2029118702054023169.json
hash: 996e208b9ebb6f52
coverage: 0.75
learned_at: 2026-10-15 22:35:21
nodes: [ImageScaleBy, ImageResizeKJv2, easy cleanGpuUsed, CLIPVisionEncode, CLIPVisionLoader, VAELoader, Note, CLIPLoader, Note, KSamplerAdvanced, KSamplerAdvanced, Reroute, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, UNETLoader, LoraLoaderModelOnly, Note, JWInteger, JWInteger, Note, Seed (rgthree), Float, easy cleanGpuUsed, Reroute, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, MathExpression|pysssss, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, Note, LayerUtility: PurgeVRAM, ImageFromBatch+, RunningHub Deepcleaner, PathchSageAttentionKJ, PathchSageAttentionKJ, LoadImage, VAEDecode, PainterI2V, Note, Note, PreviewImage, SaveImage, ImageScaleBy, Pick From Batch (mtb), ColorMatch, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, MarkdownNote, CR Prompt Text, easy anythingIndexSwitch, RH_LLMAPI_NODE, LayerUtility: PurgeVRAM, AILab_QwenVL, easy showAnything, Note, Note, CR Prompt Text, easy showAnything, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/视频-Remix V2.1建筑图生视频V1工作流_2029118702054023169.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029118702054023169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `ImageScaleBy`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `VAELoader`
- `Note`
- `CLIPLoader`
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `JWInteger`
- `JWInteger`
- `Note`
- `Seed (rgthree)`
- `Float`
- `easy cleanGpuUsed`
- `Reroute`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `LayerUtility: PurgeVRAM`
- `ImageFromBatch+`
- `RunningHub Deepcleaner`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoadImage`
- `VAEDecode` ★核心
- `PainterI2V`
- `Note`
- `Note`
- `PreviewImage`
- `SaveImage`
- `ImageScaleBy`
- `Pick From Batch (mtb)`
- `ColorMatch`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `CR Prompt Text`
- `easy anythingIndexSwitch`
- `RH_LLMAPI_NODE`
- `LayerUtility: PurgeVRAM`
- `AILab_QwenVL`
- `easy showAnything`
- `Note`
- `Note`
- `CR Prompt Text`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（48/64）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`LoraLoaderModelOnly`、`JWInteger`、`Seed (rgthree)`、`Float`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`MathExpression|pysssss`、`CLIPTextEncode`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`ImageFromBatch+`、`RunningHub Deepcleaner`、`PathchSageAttentionKJ`、`LoadImage`、`VAEDecode`、`PainterI2V`、`SaveImage`、`Pick From Batch (mtb)`、`ColorMatch`、`CR Prompt Text`、`easy anythingIndexSwitch`、`RH_LLMAPI_NODE`、`AILab_QwenVL`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
