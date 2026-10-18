---
key: 视频生成/图生视频/Remix V2.1+PainterI2V图生视频自动提示词工作流V1（一致性加强版）_2010957966706479106.json
name: Remix V2.1+PainterI2V图生视频自动提示词工作流V1（一致性加强版）_2010957966706479106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Remix V2.1+PainterI2V图生视频自动提示词工作流V1（一致性加强版）_2010957966706479106.json
hash: df3eae267a7c5015
coverage: 0.721311
learned_at: 2026-10-15 22:34:19
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, VHS_VideoCombine, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, PathchSageAttentionKJ, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, easy showAnything, RH_LLMAPI_NODE, AILab_QwenVL, CLIPTextEncode, UNETLoader, UNETLoader, VHS_VideoCombine, Reroute, Note, Note, Note, easy anythingIndexSwitch, Note, Seed (rgthree), Reroute, RunningHub Deepcleaner, ImageFromBatch+, LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, Float, UNETLoader, UNETLoader, CR Prompt Text, JWInteger, JWInteger, easy showAnything, LoadImage, CR Prompt Text, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Remix V2.1+PainterI2V图生视频自动提示词工作流V1（一致性加强版）_2010957966706479106.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010957966706479106.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
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
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `AILab_QwenVL`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `Reroute`
- `Note`
- `Note`
- `Note`
- `easy anythingIndexSwitch`
- `Note`
- `Seed (rgthree)`
- `Reroute`
- `RunningHub Deepcleaner`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Float`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`
- `easy showAnything`
- `LoadImage`
- `CR Prompt Text`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **72%**（44/61）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`VHS_VideoCombine`、`Pick From Batch (mtb)`、`VAEDecode`、`PainterI2V`、`PathchSageAttentionKJ`、`LayerUtility: PurgeVRAM`、`RH_LLMAPI_NODE`、`AILab_QwenVL`、`UNETLoader`、`easy anythingIndexSwitch`、`Seed (rgthree)`、`RunningHub Deepcleaner`、`ImageFromBatch+`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`Float`、`CR Prompt Text`、`JWInteger`、`LoadImage`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
