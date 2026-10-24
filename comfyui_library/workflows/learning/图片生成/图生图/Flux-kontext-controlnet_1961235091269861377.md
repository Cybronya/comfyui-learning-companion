---
key: 图片生成/图生图/Flux-kontext-controlnet_1961235091269861377.json
name: Flux-kontext-controlnet_1961235091269861377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux-kontext-controlnet_1961235091269861377.json
hash: f31d882b52f954e7
coverage: 0.869565
learned_at: 2026-10-23 10:58:35
nodes: [SaveImage, EmptySD3LatentImage, LoadImage, DualCLIPLoader, LayerUtility: TextJoin, SetUnionControlNetType, AIO_Preprocessor, ReferenceLatent, Seed_, PreviewImage, RH_Translator, ControlNetLoader, LoraLoaderModelOnly, VAEEncode, VAELoader, CLIPTextEncodeFlux, ConditioningZeroOut, UNETLoader, ControlNetApplySD3, LoadImage, KSampler (Efficient), PreviewImage, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 185795086895352, "steps": 30}
---

# 图片生成/图生图/Flux-kontext-controlnet_1961235091269861377.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux-kontext-controlnet_1961235091269861377.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Process → Output → Other

**节点**（23 个）：
- `SaveImage`
- `EmptySD3LatentImage`
- `LoadImage`
- `DualCLIPLoader`
- `LayerUtility: TextJoin`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `ReferenceLatent`
- `Seed_`
- `PreviewImage`
- `RH_Translator`
- `ControlNetLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPTextEncodeFlux` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `ControlNetApplySD3` ★核心
- `LoadImage`
- `KSampler (Efficient)` ★核心
- `PreviewImage`
- `Note`

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `seed` = `185795086895352`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`SaveImage`、`EmptySD3LatentImage`、`LoadImage`、`DualCLIPLoader`、`LayerUtility: TextJoin`、`SetUnionControlNetType`、`AIO_Preprocessor`、`ReferenceLatent`、`Seed_`、`RH_Translator`、`ControlNetLoader`、`LoraLoaderModelOnly`、`VAEEncode`、`VAELoader`、`CLIPTextEncodeFlux`、`ConditioningZeroOut`、`UNETLoader`、`ControlNetApplySD3`、`KSampler (Efficient)`

**用到的条目**：VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、ControlNetLoader、SetUnionControlNetType、ControlNetApplySD3
