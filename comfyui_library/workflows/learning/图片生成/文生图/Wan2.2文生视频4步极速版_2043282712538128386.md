---
key: 图片生成/文生图/Wan2.2文生视频4步极速版_2043282712538128386.json
name: Wan2.2文生视频4步极速版_2043282712538128386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生视频4步极速版_2043282712538128386.json
hash: d78f4b9a7221ce43
coverage: 0.928571
learned_at: 2026-10-21 02:55:25
nodes: [ModelSamplingSD3, LayerUtility: PurgeVRAM V2, MarkdownNote, Int, Int, MathExpression|pysssss, CLIPTextEncode, Int, CM_IntToFloat, Int, Int, KSamplerAdvanced, MarkdownNote, LoraLoaderModelOnly, ModelSamplingSD3, EmptyHunyuanLatentVideo, VAELoader, CLIPLoader, CLIPTextEncode, MathExpression|pysssss, CM_IntToFloat, Int, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, UNETLoader, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/Wan2.2文生视频4步极速版_2043282712538128386.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生视频4步极速版_2043282712538128386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（28 个）：
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `MarkdownNote`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `Int`
- `CM_IntToFloat`
- `Int`
- `Int`
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `CM_IntToFloat`
- `Int`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`ModelSamplingSD3`、`LayerUtility: PurgeVRAM V2`、`Int`、`MathExpression|pysssss`、`CLIPTextEncode`、`CM_IntToFloat`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
