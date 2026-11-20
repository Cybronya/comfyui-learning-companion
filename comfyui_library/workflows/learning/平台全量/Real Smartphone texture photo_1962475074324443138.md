---
key: 平台全量/Real Smartphone texture photo_1962475074324443138.json
name: Real Smartphone texture photo_1962475074324443138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Real Smartphone texture photo_1962475074324443138.json
hash: c5a392835209f7f7
coverage: 0.647059
learned_at: 2026-11-14 00:54:33
nodes: [AILab_MiniCPM_4_V, ShowText|pysssss, ShowText|pysssss, RH_Translator, CR Text, ShowText|pysssss, ShowText|pysssss, RH_Translator, CR Text, Note, UNETLoader, UNETLoader, LoraLoaderModelOnly, ImpactInt, Note, ImpactInt, ImpactInt, Note, Note, GetNode, SetNode, GetNode, Note, KSamplerAdvanced, CLIPLoader, Note, Seed Everywhere, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPTextEncode, CLIPTextEncode, CR Text Concatenate, ImpactInt, CR Text, Switch any [Crystools], SetNode, LayerUtility: PurgeVRAM, easy cleanGpuUsed, KSamplerAdvanced, SeedVR2, SeedVR2BlockSwap, PreviewImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), VAEDecode, SaveImage, RH_LLMAPI_NODE, PreviewImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "enable", "steps": "randomize"}
---

# 平台全量/Real Smartphone texture photo_1962475074324443138.json

> 来源文件 `comfyui_library/workflows/平台全量/Real Smartphone texture photo_1962475074324443138.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（51 个）：
- `AILab_MiniCPM_4_V`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `RH_Translator`
- `CR Text`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `RH_Translator`
- `CR Text`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImpactInt`
- `Note`
- `ImpactInt`
- `ImpactInt`
- `Note`
- `Note`
- `GetNode`
- `SetNode`
- `GetNode`
- `Note`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `Note`
- `Seed Everywhere`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `ImpactInt`
- `CR Text`
- `Switch any [Crystools]`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `SeedVR2`
- `SeedVR2BlockSwap`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `RH_LLMAPI_NODE`
- `PreviewImage`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **65%**（33/51）

**有卡**：`AILab_MiniCPM_4_V`、`RH_Translator`、`CR Text`、`UNETLoader`、`LoraLoaderModelOnly`、`ImpactInt`、`KSamplerAdvanced`、`CLIPLoader`、`Seed Everywhere`、`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPTextEncode`、`CR Text Concatenate`、`Switch any [Crystools]`、`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`SeedVR2`、`SeedVR2BlockSwap`、`VAEDecode`、`SaveImage`、`RH_LLMAPI_NODE`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced
