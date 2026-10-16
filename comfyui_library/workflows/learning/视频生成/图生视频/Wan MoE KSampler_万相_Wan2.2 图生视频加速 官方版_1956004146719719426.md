---
key: 视频生成/图生视频/Wan MoE KSampler_万相_Wan2.2 图生视频加速 官方版_1956004146719719426.json
name: Wan MoE KSampler_万相_Wan2.2 图生视频加速 官方版_1956004146719719426.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956004146719719426.json
hash: 7cd6ec8bb90103da
coverage: 0.787879
learned_at: 2026-10-15 22:31:11
nodes: [VAEDecode, MathExpression|pysssss, Anything Everywhere, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, easy int, easy int, easy int, CLIPTextEncode, LoadImage, WanImageToVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, VAELoader, Reroute, Note, UNETLoader, UNETLoader, WanMoeKSampler, JjkText, Note, VHS_VideoCombine, easy float, VHS_VideoCombine, VHS_VideoCombine, easy clearCacheAll, LayerUtility: PurgeVRAM, ImpactSwitch, CLIPTextEncode, RHHiddenNodes, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 15, "denoise": "uni_pc", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/Wan MoE KSampler_万相_Wan2.2 图生视频加速 官方版_1956004146719719426.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956004146719719426.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `VAEDecode` ★核心
- `MathExpression|pysssss`
- `Anything Everywhere`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `easy int`
- `easy int`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `WanImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAELoader`
- `Reroute`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanMoeKSampler` ★核心
- `JjkText`
- `Note`
- `VHS_VideoCombine`
- `easy float`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `LayerUtility: PurgeVRAM`
- `ImpactSwitch`
- `CLIPTextEncode` ★核心
- `RHHiddenNodes`
- `easy showAnything`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `15`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `uni_pc`

## 知识

覆盖率 **79%**（26/33）

**有卡**：`VAEDecode`、`MathExpression|pysssss`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`CLIPTextEncode`、`LoadImage`、`WanImageToVideo`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAELoader`、`UNETLoader`、`WanMoeKSampler`、`VHS_VideoCombine`、`easy float`、`easy clearCacheAll`、`LayerUtility: PurgeVRAM`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
