---
key: 平台全量/微软开源了TRELLIS.2大模型：可用于生产游戏3D模型，同时支持3D打印🎮！_2002627938883366914.json
name: 微软开源了TRELLIS.2大模型：可用于生产游戏3D模型，同时支持3D打印🎮！_2002627938883366914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/微软开源了TRELLIS.2大模型：可用于生产游戏3D模型，同时支持3D打印🎮！_2002627938883366914.json
hash: 1ebfd20b340a7b2f
coverage: 0.833333
learned_at: 2026-11-14 02:04:06
nodes: [CLIPLoader, VAELoader, ConditioningZeroOut, UNETLoader, KSampler, ModelSamplingAuraFlow, MarkdownNote, LoraLoaderModelOnly, Note, SaveImage, VAEDecode, Trellis2LoadModel, Trellis2SimplifyMesh, Trellis2PostProcessAndUnWrapAndRasterizer, TrimeshToMESH, EmptySD3LatentImage, Note, SaveGLB, RMBG, PreviewImage, Trellis2MeshWithVoxelGenerator, CLIPTextEncode, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 187729458352603, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/微软开源了TRELLIS.2大模型：可用于生产游戏3D模型，同时支持3D打印🎮！_2002627938883366914.json

> 来源文件 `comfyui_library/workflows/平台全量/微软开源了TRELLIS.2大模型：可用于生产游戏3D模型，同时支持3D打印🎮！_2002627938883366914.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
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
- `Label (rgthree)`
- `Label (rgthree)`

## 关键参数

- `seed` = `187729458352603`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`UNETLoader`、`KSampler`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`SaveImage`、`VAEDecode`、`Trellis2LoadModel`、`Trellis2SimplifyMesh`、`Trellis2PostProcessAndUnWrapAndRasterizer`、`TrimeshToMESH`、`EmptySD3LatentImage`、`SaveGLB`、`RMBG`、`Trellis2MeshWithVoxelGenerator`、`CLIPTextEncode`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
