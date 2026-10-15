---
key: 视频生成/文生视频/图生视频自动提示词 Remix V2.1+PainterI2V 一致性加强版_2037406985737478145.json
name: 图生视频自动提示词 Remix V2.1+PainterI2V 一致性加强版_2037406985737478145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/图生视频自动提示词 Remix V2.1+PainterI2V 一致性加强版_2037406985737478145.json
hash: c492db5ccd4af107
coverage: 0.921053
learned_at: 2026-10-15 22:48:24
nodes: [CLIPVisionEncode, CLIPVisionLoader, VAELoader, Note, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, RH_LLMAPI_NODE, Reroute, easy showAnything, MathExpression|pysssss, Seed (rgthree), LayerUtility: PurgeVRAM, Float, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, VAEDecode, easy cleanGpuUsed, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, PathchSageAttentionKJ, UNETLoader, UNETLoader, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, ImageResizeKJv2, ImageFromBatch+, RunningHub Deepcleaner, AILab_QwenVL, easy anythingIndexSwitch, JWInteger, CR Prompt Text, CR Prompt Text, LoadImage, JWInteger, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/图生视频自动提示词 Remix V2.1+PainterI2V 一致性加强版_2037406985737478145.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/图生视频自动提示词 Remix V2.1+PainterI2V 一致性加强版_2037406985737478145.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `VAELoader`
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_LLMAPI_NODE`
- `Reroute`
- `easy showAnything`
- `MathExpression|pysssss`
- `Seed (rgthree)`
- `LayerUtility: PurgeVRAM`
- `Float`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ImageResizeKJv2`
- `ImageFromBatch+`
- `RunningHub Deepcleaner`
- `AILab_QwenVL`
- `easy anythingIndexSwitch`
- `JWInteger`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadImage`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`KSamplerAdvanced`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_LLMAPI_NODE`、`MathExpression|pysssss`、`Seed (rgthree)`、`LayerUtility: PurgeVRAM`、`Float`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`VAEDecode`、`easy cleanGpuUsed`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`ModelSamplingSD3`、`ImageResizeKJv2`、`ImageFromBatch+`、`RunningHub Deepcleaner`、`AILab_QwenVL`、`easy anythingIndexSwitch`、`JWInteger`、`CR Prompt Text`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
