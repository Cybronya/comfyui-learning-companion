---
key: 视频生成/文生视频/Wan MoE KSampler_万相_Wan2.2 文生视频加速 官方版_1955876808312979457.json
name: Wan MoE KSampler_万相_Wan2.2 文生视频加速 官方版_1955876808312979457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1955876808312979457.json
hash: 04e2e207e8fc974d
coverage: 0.869565
learned_at: 2026-10-15 22:43:40
nodes: [CLIPLoader, easy int, Reroute, VAEDecode, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, Anything Everywhere, MathExpression|pysssss, VAELoader, LayerUtility: PurgeVRAM, easy clearCacheAll, ImpactSwitch, VHS_VideoCombine, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, easy float, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, JjkText, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, RH_LLMAPI_NODE, VHS_VideoCombine, VHS_VideoCombine, TorchCompileModelWanVideoV2, VHS_VideoCombine, easy int, Note, easy int, WanMoeKSampler, easy int]
patterns: []
missing: []
parameters: {"cfg": 15, "denoise": "uni_pc", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/文生视频/Wan MoE KSampler_万相_Wan2.2 文生视频加速 官方版_1955876808312979457.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1955876808312979457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（46 个）：
- `CLIPLoader`
- `easy int`
- `Reroute`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `Anything Everywhere`
- `MathExpression|pysssss`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `easy clearCacheAll`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy float`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JjkText`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `TorchCompileModelWanVideoV2`
- `VHS_VideoCombine`
- `easy int`
- `Note`
- `easy int`
- `WanMoeKSampler` ★核心
- `easy int`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `15`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `uni_pc`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`CLIPLoader`、`easy int`、`VAEDecode`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`MathExpression|pysssss`、`VAELoader`、`LayerUtility: PurgeVRAM`、`easy clearCacheAll`、`VHS_VideoCombine`、`easy float`、`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`RH_LLMAPI_NODE`、`TorchCompileModelWanVideoV2`、`WanMoeKSampler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、EmptyHunyuanLatentVideo
