---
key: 视频生成/图生视频/Wan2.2 动态海报工作流 LIXOAXIAO_1956058743224061953.json
name: Wan2.2 动态海报工作流 LIXOAXIAO_1956058743224061953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 动态海报工作流 LIXOAXIAO_1956058743224061953.json
hash: d89253921a20ed84
coverage: 0.8125
learned_at: 2026-10-15 22:31:11
nodes: [UNETLoader, CLIPLoader, PrimitiveInt, PrimitiveInt, Primitive integer [Crystools], VAELoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, VAEDecode, KSampler, MathExpression|pysssss, VHS_VideoCombine, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 1, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 动态海报工作流 LIXOAXIAO_1956058743224061953.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956058743224061953.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `Primitive integer [Crystools]`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `1`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`Primitive integer [Crystools]`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`WanImageToVideo`、`VAEDecode`、`KSampler`、`MathExpression|pysssss`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
