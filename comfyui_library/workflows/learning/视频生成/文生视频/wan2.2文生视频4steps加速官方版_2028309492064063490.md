---
key: 视频生成/文生视频/wan2.2文生视频4steps加速官方版_2028309492064063490.json
name: wan2.2文生视频4steps加速官方版_2028309492064063490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频4steps加速官方版_2028309492064063490.json
hash: 1892c39b1d2b8e5d
coverage: 0.827586
learned_at: 2026-10-11 03:16:51
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEDecode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, EmptyHunyuanLatentVideo, CreateVideo, SaveVideo, ModelSamplingSD3, UNETLoader, LayerUtility: PurgeVRAM V2, MarkdownNote, KSamplerAdvanced, KSamplerAdvanced, Int, Int, MathExpression|pysssss, CM_IntToFloat, MathExpression|pysssss, CLIPTextEncode, Int, Int, CM_IntToFloat, Int, MarkdownNote, Int]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, MathExpression|pysssss, MathExpression|pysssss]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2文生视频4steps加速官方版_2028309492064063490.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频4steps加速官方版_2028309492064063490.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（29 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `CreateVideo`
- `SaveVideo`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Int`
- `Int`
- `MathExpression|pysssss`
- `CM_IntToFloat`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `CM_IntToFloat`
- `Int`
- `MarkdownNote`
- `Int`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`CreateVideo`、`SaveVideo`、`KSamplerAdvanced`、`Int`、`CM_IntToFloat`

**缺卡**（3）：`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
