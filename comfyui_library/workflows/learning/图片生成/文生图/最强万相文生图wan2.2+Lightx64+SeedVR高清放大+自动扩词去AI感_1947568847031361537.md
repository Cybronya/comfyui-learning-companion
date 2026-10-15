---
key: 图片生成/文生图/最强万相文生图wan2.2+Lightx64+SeedVR高清放大+自动扩词去AI感_1947568847031361537.json
name: 最强万相文生图wan2.2+Lightx64+SeedVR高清放大+自动扩词去AI感_1947568847031361537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/最强万相文生图wan2.2+Lightx64+SeedVR高清放大+自动扩词去AI感_1947568847031361537.json
hash: 6a21520736c1ce5a
coverage: 0.903226
learned_at: 2026-10-10 20:59:50
nodes: [CLIPTextEncode, ModelSamplingSD3, UNETLoader, UNETLoader, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, CR Text, Int, Int, RH_LLMAPI_NODE, EmptyHunyuanLatentVideo, VAEDecode, SeedVR2BlockSwap, LayerUtility: PurgeVRAM V2, SeedVR2, KSampler, KSampler, Bjornulf_TextToStringAndSeed, CFGZeroStar, CFGZeroStar, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Image Comparer (rgthree), SaveImage, SaveImage, PathchSageAttentionKJ, PathchSageAttentionKJ]
patterns: []
missing: [CR Text, LayerUtility: PurgeVRAM V2]
parameters: {"cfg": 1, "denoise": 0.3500000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 965369974524576, "steps": 10}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/最强万相文生图wan2.2+Lightx64+SeedVR高清放大+自动扩词去AI感_1947568847031361537.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/最强万相文生图wan2.2+Lightx64+SeedVR高清放大+自动扩词去AI感_1947568847031361537.json`

## 结构

**节点**（31 个）：
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `UNETLoader`
- `UNETLoader`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `CR Text`
- `Int`
- `Int`
- `RH_LLMAPI_NODE`
- `EmptyHunyuanLatentVideo`
- `VAEDecode`
- `SeedVR2BlockSwap`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2`
- `KSampler`
- `KSampler`
- `Bjornulf_TextToStringAndSeed`
- `CFGZeroStar`
- `CFGZeroStar`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`

## 关键参数

- `cfg` = `1`
- `denoise` = `0.3500000000000001`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `965369974524576`
- `steps` = `10`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CR Text`、`Int`、`RH_LLMAPI_NODE`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`SeedVR2BlockSwap`、`LayerUtility: PurgeVRAM V2`、`SeedVR2`、`KSampler`、`Bjornulf_TextToStringAndSeed`、`CFGZeroStar`、`LoraLoaderModelOnly`、`Image Comparer (rgthree)`、`SaveImage`

**缺卡**（2）：`CR Text`、`LayerUtility: PurgeVRAM V2`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
