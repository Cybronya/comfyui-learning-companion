---
key: 视频生成/图生视频/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028678704204881921.json
name: Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028678704204881921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2028678704204881921.json
hash: 5dc00f96645e9afa
coverage: 0.734375
learned_at: 2026-10-15 22:35:20
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, LayerUtility: PurgeVRAM, easy showAnything, AILab_QwenVL, CLIPTextEncode, Reroute, Seed (rgthree), Reroute, LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageFromBatch+, RunningHub Deepcleaner, UNETLoader, UNETLoader, RH_LLMAPI_NODE, easy cleanGpuUsed, LoraLoaderModelOnly, LoadImage, CR Prompt Text, Note, easy anythingIndexSwitch, Note, Note, CR Prompt Text, Note, Float, Int, JWInteger, JWInteger, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028678704204881921.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2028678704204881921.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
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
- `Pick From Batch (mtb)`
- `VAEDecode` ★核心
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `AILab_QwenVL`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Seed (rgthree)`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageFromBatch+`
- `RunningHub Deepcleaner`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `RH_LLMAPI_NODE`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CR Prompt Text`
- `Note`
- `easy anythingIndexSwitch`
- `Note`
- `Note`
- `CR Prompt Text`
- `Note`
- `Float`
- `Int`
- `JWInteger`
- `JWInteger`
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

覆盖率 **73%**（47/64）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`VAEDecode`、`PainterI2V`、`LayerUtility: PurgeVRAM`、`AILab_QwenVL`、`Seed (rgthree)`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ImageFromBatch+`、`RunningHub Deepcleaner`、`UNETLoader`、`RH_LLMAPI_NODE`、`LoadImage`、`CR Prompt Text`、`easy anythingIndexSwitch`、`Float`、`Int`、`JWInteger`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
