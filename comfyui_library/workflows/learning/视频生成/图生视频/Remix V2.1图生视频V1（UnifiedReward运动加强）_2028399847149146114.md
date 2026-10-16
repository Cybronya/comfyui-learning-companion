---
key: 视频生成/图生视频/Remix V2.1图生视频V1（UnifiedReward运动加强）_2028399847149146114.json
name: Remix V2.1图生视频V1（UnifiedReward运动加强）_2028399847149146114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2028399847149146114.json
hash: 9eda0bd66a44ba1a
coverage: 0.730159
learned_at: 2026-10-15 22:35:19
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, VHS_VideoCombine, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, LayerUtility: PurgeVRAM, AILab_QwenVL, CLIPTextEncode, Reroute, Note, Note, Note, easy anythingIndexSwitch, Note, Seed (rgthree), Reroute, LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, Float, CR Prompt Text, JWInteger, JWInteger, easy showAnything, CR Prompt Text, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, ImageFromBatch+, RunningHub Deepcleaner, VHS_VideoCombine, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, easy showAnything, easy cleanGpuUsed, RH_LLMAPI_NODE]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Remix V2.1图生视频V1（UnifiedReward运动加强）_2028399847149146114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2028399847149146114.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
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
- `LayerUtility: PurgeVRAM`
- `AILab_QwenVL`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Note`
- `Note`
- `Note`
- `easy anythingIndexSwitch`
- `Note`
- `Seed (rgthree)`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Float`
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`
- `easy showAnything`
- `CR Prompt Text`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ImageFromBatch+`
- `RunningHub Deepcleaner`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `easy showAnything`
- `easy cleanGpuUsed`
- `RH_LLMAPI_NODE`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **73%**（46/63）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`VHS_VideoCombine`、`Pick From Batch (mtb)`、`VAEDecode`、`PainterI2V`、`LayerUtility: PurgeVRAM`、`AILab_QwenVL`、`easy anythingIndexSwitch`、`Seed (rgthree)`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`Float`、`CR Prompt Text`、`JWInteger`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ImageFromBatch+`、`RunningHub Deepcleaner`、`UNETLoader`、`LoadImage`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
