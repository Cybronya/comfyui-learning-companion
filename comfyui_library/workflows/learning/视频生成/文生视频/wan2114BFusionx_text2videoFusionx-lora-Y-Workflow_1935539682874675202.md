---
key: 视频生成/文生视频/wan2114BFusionx_text2videoFusionx-lora-Y-Workflow_1935539682874675202.json
name: wan2114BFusionx_text2videoFusionx-lora-Y-Workflow_1935539682874675202.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1935539682874675202.json
hash: f7062624776dd6b2
coverage: 0.846154
learned_at: 2026-10-15 22:43:28
nodes: [CLIPTextEncode, UNETLoader, VAELoader, MarkdownNote, VAEDecode, MarkdownNote, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, ModelSamplingSD3, KSampler, EmptyHunyuanLatentVideo, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "normal", "seed": 134051876466274, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2114BFusionx_text2videoFusionx-lora-Y-Workflow_1935539682874675202.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1935539682874675202.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `MarkdownNote`
- `VAEDecode` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `EmptyHunyuanLatentVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `134051876466274`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`VAEDecode`、`CLIPLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSampler`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
