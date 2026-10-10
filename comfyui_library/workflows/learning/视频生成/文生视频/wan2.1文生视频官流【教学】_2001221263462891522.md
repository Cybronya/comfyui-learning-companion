---
key: 视频生成/文生视频/wan2.1文生视频官流【教学】_2001221263462891522.json
name: wan2.1文生视频官流【教学】_2001221263462891522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1文生视频官流【教学】_2001221263462891522.json
hash: 0fa59e34b2312197
coverage: 0.866667
learned_at: 2026-10-11 02:57:39
nodes: [VHS_VideoCombine, LoraLoaderModelOnly, ApplySageAttention, Int, ModelSamplingSD3, CLIPLoader, CLIPTextEncode, CLIPTextEncode, KSampler, EmptyHunyuanLatentVideo, SimpleMath+, VAELoader, UNETLoader, VAEDecode, PreviewImage]
patterns: []
missing: [SimpleMath+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 946223056963374, "steps": 6}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.1文生视频官流【教学】_2001221263462891522.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.1文生视频官流【教学】_2001221263462891522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `ApplySageAttention`
- `Int`
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyHunyuanLatentVideo`
- `SimpleMath+`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `PreviewImage`

## 关键参数

- `seed` = `946223056963374`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`VHS_VideoCombine`、`LoraLoaderModelOnly`、`ApplySageAttention`、`Int`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`KSampler`、`EmptyHunyuanLatentVideo`、`VAELoader`、`UNETLoader`、`VAEDecode`

**缺卡**（1）：`SimpleMath+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
