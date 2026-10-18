---
key: 视频生成/文生视频/Wan2.2大一统文生视频-RAPID-AIO_1949761106275426305.json
name: Wan2.2大一统文生视频-RAPID-AIO_1949761106275426305.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2大一统文生视频-RAPID-AIO_1949761106275426305.json
hash: 1458a07567ffd31a
coverage: 0.95
learned_at: 2026-10-15 22:43:33
nodes: [UNETLoader, CLIPTextEncode, CLIPTextEncode, MathExpression|pysssss, ModelSamplingSD3, VAELoader, EmptyHunyuanLatentVideo, DF_Integer, DF_Integer, DF_Integer, KSampler, VHS_VideoCombine, easy cleanGpuUsed, VAEDecode, easy clearCacheAll, UNETLoader, easy clearCacheAll, easy cleanGpuUsed, CLIPLoader, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 292719160495675, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2大一统文生视频-RAPID-AIO_1949761106275426305.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949761106275426305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（20 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `DF_Integer`
- `DF_Integer`
- `DF_Integer`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy clearCacheAll`
- `UNETLoader` ★核心
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `292719160495675`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`MathExpression|pysssss`、`ModelSamplingSD3`、`VAELoader`、`EmptyHunyuanLatentVideo`、`DF_Integer`、`KSampler`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`VAEDecode`、`easy clearCacheAll`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、DF_Integer

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
