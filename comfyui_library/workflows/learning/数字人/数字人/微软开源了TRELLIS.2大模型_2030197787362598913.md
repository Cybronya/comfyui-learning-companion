---
key: 数字人/数字人/微软开源了TRELLIS.2大模型_2030197787362598913.json
name: 微软开源了TRELLIS.2大模型_2030197787362598913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/微软开源了TRELLIS.2大模型_2030197787362598913.json
hash: bf81bc28072392d9
coverage: 0.818182
learned_at: 2026-10-26 02:02:09
nodes: [CLIPLoader, VAELoader, ConditioningZeroOut, UNETLoader, KSampler, ModelSamplingAuraFlow, MarkdownNote, LoraLoaderModelOnly, Note, SaveImage, VAEDecode, Trellis2LoadModel, Trellis2SimplifyMesh, Trellis2PostProcessAndUnWrapAndRasterizer, TrimeshToMESH, EmptySD3LatentImage, Note, SaveGLB, RMBG, PreviewImage, Trellis2MeshWithVoxelGenerator, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 300400635547121, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/微软开源了TRELLIS.2大模型_2030197787362598913.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/微软开源了TRELLIS.2大模型_2030197787362598913.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `SaveImage`
- `VAEDecode` ★核心
- `Trellis2LoadModel`
- `Trellis2SimplifyMesh`
- `Trellis2PostProcessAndUnWrapAndRasterizer`
- `TrimeshToMESH`
- `EmptySD3LatentImage`
- `Note`
- `SaveGLB`
- `RMBG`
- `PreviewImage`
- `Trellis2MeshWithVoxelGenerator`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `300400635547121`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`UNETLoader`、`KSampler`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`SaveImage`、`VAEDecode`、`Trellis2LoadModel`、`Trellis2SimplifyMesh`、`Trellis2PostProcessAndUnWrapAndRasterizer`、`TrimeshToMESH`、`EmptySD3LatentImage`、`SaveGLB`、`RMBG`、`Trellis2MeshWithVoxelGenerator`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
