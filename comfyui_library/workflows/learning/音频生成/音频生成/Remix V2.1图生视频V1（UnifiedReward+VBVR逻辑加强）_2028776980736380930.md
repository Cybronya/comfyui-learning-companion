---
key: 音频生成/音频生成/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028776980736380930.json
name: Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028776980736380930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028776980736380930.json
hash: 06645c013d5cff56
coverage: 0.730159
learned_at: 2026-10-18 02:28:43
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, VHS_VideoCombine, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, AILab_QwenVL, CLIPTextEncode, Reroute, Note, Note, Note, easy anythingIndexSwitch, Note, Seed (rgthree), Reroute, LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, Float, CR Prompt Text, JWInteger, easy showAnything, CR Prompt Text, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageFromBatch+, RunningHub Deepcleaner, UNETLoader, UNETLoader, RH_LLMAPI_NODE, easy cleanGpuUsed, LoraLoaderModelOnly, JWInteger, VHS_VideoCombine, easy showAnything, LayerUtility: PurgeVRAM, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 音频生成/音频生成/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028776980736380930.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028776980736380930.json`

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
- `easy showAnything`
- `CR Prompt Text`
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
- `JWInteger`
- `VHS_VideoCombine`
- `easy showAnything`
- `LayerUtility: PurgeVRAM`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **73%**（46/63）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`VHS_VideoCombine`、`Pick From Batch (mtb)`、`VAEDecode`、`PainterI2V`、`AILab_QwenVL`、`easy anythingIndexSwitch`、`Seed (rgthree)`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`Float`、`CR Prompt Text`、`JWInteger`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ImageFromBatch+`、`RunningHub Deepcleaner`、`UNETLoader`、`RH_LLMAPI_NODE`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
