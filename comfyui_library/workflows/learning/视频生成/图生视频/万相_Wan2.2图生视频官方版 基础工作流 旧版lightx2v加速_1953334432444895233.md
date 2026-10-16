---
key: 视频生成/图生视频/万相_Wan2.2图生视频官方版 基础工作流 旧版lightx2v加速_1953334432444895233.json
name: 万相_Wan2.2图生视频官方版 基础工作流 旧版lightx2v加速_1953334432444895233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953334432444895233.json
hash: 1033ab57a56d4160
coverage: 0.871795
learned_at: 2026-10-15 22:31:04
nodes: [VAEDecode, easy seed, easy int, MathExpression|pysssss, WanImageToVideo, MathExpression|pysssss, ImpactSwitch, easy clearCacheAll, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, UNETLoader, VAELoader, Anything Everywhere, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, KSamplerAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM, RH_LLMAPI_NODE, JjkText, easy int, easy int, easy float, LoadImage, easy int, CLIPTextEncode, CLIPTextEncode, easy showAnything, Reroute, PathchSageAttentionKJ, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "normal", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/万相_Wan2.2图生视频官方版 基础工作流 旧版lightx2v加速_1953334432444895233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953334432444895233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `VAEDecode` ★核心
- `easy seed`
- `easy int`
- `MathExpression|pysssss`
- `WanImageToVideo`
- `MathExpression|pysssss`
- `ImpactSwitch`
- `easy clearCacheAll`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `VAELoader`
- `Anything Everywhere`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `RH_LLMAPI_NODE`
- `JjkText`
- `easy int`
- `easy int`
- `easy float`
- `LoadImage`
- `easy int`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `Reroute`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `normal`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`VAEDecode`、`easy seed`、`easy int`、`MathExpression|pysssss`、`WanImageToVideo`、`easy clearCacheAll`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`RH_LLMAPI_NODE`、`easy float`、`LoadImage`、`CLIPTextEncode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
