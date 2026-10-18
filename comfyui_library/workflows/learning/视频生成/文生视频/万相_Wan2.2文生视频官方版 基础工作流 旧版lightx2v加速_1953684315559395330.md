---
key: 视频生成/文生视频/万相_Wan2.2文生视频官方版 基础工作流 旧版lightx2v加速_1953684315559395330.json
name: 万相_Wan2.2文生视频官方版 基础工作流 旧版lightx2v加速_1953684315559395330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/万相_Wan2.2文生视频官方版 基础工作流 旧版lightx2v加速_1953684315559395330.json
hash: 2d0e41b89b7ff848
coverage: 0.871795
learned_at: 2026-10-15 22:43:39
nodes: [VAEDecode, easy seed, easy int, MathExpression|pysssss, ImpactSwitch, easy clearCacheAll, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, Anything Everywhere, CLIPLoader, KSamplerAdvanced, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM, VHS_VideoCombine, easy int, easy float, Reroute, PathchSageAttentionKJ, KSamplerAdvanced, EmptyHunyuanLatentVideo, MathExpression|pysssss, easy int, easy int, UNETLoader, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, ModelSamplingSD3, RH_LLMAPI_NODE, easy showAnything, CLIPTextEncode, VAELoader, JjkText, easy int, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "normal", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/万相_Wan2.2文生视频官方版 基础工作流 旧版lightx2v加速_1953684315559395330.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1953684315559395330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（39 个）：
- `VAEDecode` ★核心
- `easy seed`
- `easy int`
- `MathExpression|pysssss`
- `ImpactSwitch`
- `easy clearCacheAll`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `Anything Everywhere`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `easy int`
- `easy float`
- `Reroute`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `MathExpression|pysssss`
- `easy int`
- `easy int`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `JjkText`
- `easy int`
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

**有卡**：`VAEDecode`、`easy seed`、`easy int`、`MathExpression|pysssss`、`easy clearCacheAll`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPLoader`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`easy float`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`CLIPTextEncode`、`RH_LLMAPI_NODE`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、easy seed
