---
key: 视频生成/文生视频/图生视频自动提示词 Remix V2.1+PainterI2V 一致性加强版_2037406985737478145.json
name: 图生视频自动提示词 Remix V2.1+PainterI2V 一致性加强版_2037406985737478145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/图生视频自动提示词 Remix V2.1+PainterI2V 一致性加强版_2037406985737478145.json
hash: c492db5ccd4af107
coverage: 0.605263
learned_at: 2026-10-11 03:48:40
nodes: [CLIPVisionEncode, CLIPVisionLoader, VAELoader, Note, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, RH_LLMAPI_NODE, Reroute, easy showAnything, MathExpression|pysssss, Seed (rgthree), LayerUtility: PurgeVRAM, Float, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, VAEDecode, easy cleanGpuUsed, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, PathchSageAttentionKJ, UNETLoader, UNETLoader, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, ImageResizeKJv2, ImageFromBatch+, RunningHub Deepcleaner, AILab_QwenVL, easy anythingIndexSwitch, JWInteger, CR Prompt Text, CR Prompt Text, LoadImage, JWInteger, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: [ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, MathExpression|pysssss, RunningHub Deepcleaner, easy anythingIndexSwitch, easy cleanGpuUsed, CR Prompt Text, CR Prompt Text, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, Seed (rgthree)]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **61%**（23/38）

**有卡**：`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`KSamplerAdvanced`、`CLIPTextEncode`、`RH_LLMAPI_NODE`、`Float`、`VAEDecode`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`ModelSamplingSD3`、`ImageResizeKJv2`、`AILab_QwenVL`、`JWInteger`、`LoadImage`、`VHS_VideoCombine`

**缺卡**（12）：`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`RunningHub Deepcleaner`、`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`CR Prompt Text`、`CR Prompt Text`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
