---
key: 视频生成/文生视频/wan2.2-t2v-rapid-aio-最快文生视频_1950680019137941506.json
name: wan2.2-t2v-rapid-aio-最快文生视频_1950680019137941506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-t2v-rapid-aio-最快文生视频_1950680019137941506.json
hash: c325df1aa048c53a
coverage: 0.714286
learned_at: 2026-10-15 22:43:36
nodes: [CLIPTextEncode, VAELoader, CLIPLoader, EmptyHunyuanLatentVideo, UNETLoader, PrimitiveInt, CLIPTextEncode, KSampler, VAEDecode, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, ModelSamplingSD3, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 0, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2-t2v-rapid-aio-最快文生视频_1950680019137941506.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950680019137941506.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `ModelSamplingSD3`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `0`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **71%**（10/14）

**有卡**：`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`ModelSamplingSD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
