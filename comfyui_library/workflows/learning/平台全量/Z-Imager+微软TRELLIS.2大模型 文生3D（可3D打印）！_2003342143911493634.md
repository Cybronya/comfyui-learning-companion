---
key: 平台全量/Z-Imager+微软TRELLIS.2大模型 文生3D（可3D打印）！_2003342143911493634.json
name: Z-Imager+微软TRELLIS.2大模型 文生3D（可3D打印）！_2003342143911493634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Z-Imager+微软TRELLIS.2大模型 文生3D（可3D打印）！_2003342143911493634.json
hash: 112e46aa5de93bea
coverage: 0.84
learned_at: 2026-11-14 01:08:15
nodes: [CLIPLoader, VAELoader, ConditioningZeroOut, UNETLoader, KSampler, ModelSamplingAuraFlow, MarkdownNote, LoraLoaderModelOnly, Note, SaveImage, VAEDecode, Trellis2LoadModel, Trellis2SimplifyMesh, EmptySD3LatentImage, Note, RMBG, PreviewImage, Trellis2ExportMesh, Trellis2PostProcessAndUnWrapAndRasterizer, SaveGLB, TrimeshToMESH, Trellis2ExportMesh, CLIPTextEncode, Trellis2MeshWithVoxelGenerator, Preview3D]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 556353273321965, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Z-Imager+微软TRELLIS.2大模型 文生3D（可3D打印）！_2003342143911493634.json

> 来源文件 `comfyui_library/workflows/平台全量/Z-Imager+微软TRELLIS.2大模型 文生3D（可3D打印）！_2003342143911493634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
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
- `EmptySD3LatentImage`
- `Note`
- `RMBG`
- `PreviewImage`
- `Trellis2ExportMesh`
- `Trellis2PostProcessAndUnWrapAndRasterizer`
- `SaveGLB`
- `TrimeshToMESH`
- `Trellis2ExportMesh`
- `CLIPTextEncode` ★核心
- `Trellis2MeshWithVoxelGenerator`
- `Preview3D`

## 关键参数

- `seed` = `556353273321965`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`UNETLoader`、`KSampler`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`SaveImage`、`VAEDecode`、`Trellis2LoadModel`、`Trellis2SimplifyMesh`、`EmptySD3LatentImage`、`RMBG`、`Trellis2ExportMesh`、`Trellis2PostProcessAndUnWrapAndRasterizer`、`SaveGLB`、`TrimeshToMESH`、`CLIPTextEncode`、`Trellis2MeshWithVoxelGenerator`、`Preview3D`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
