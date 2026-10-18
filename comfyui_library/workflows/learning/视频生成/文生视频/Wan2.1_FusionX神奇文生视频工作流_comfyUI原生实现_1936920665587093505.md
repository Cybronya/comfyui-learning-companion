---
key: 视频生成/文生视频/Wan2.1_FusionX神奇文生视频工作流_comfyUI原生实现_1936920665587093505.json
name: Wan2.1_FusionX神奇文生视频工作流_comfyUI原生实现_1936920665587093505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1_FusionX神奇文生视频工作流_comfyUI原生实现_1936920665587093505.json
hash: 976c8367d073e615
coverage: 0.888889
learned_at: 2026-10-15 22:43:29
nodes: [UNETLoader, VAELoader, Prompts Everywhere, EmptyHunyuanLatentVideo, ApplySageAttention, CLIPLoader, Anything Everywhere3, ModelSamplingSD3, Int, CLIPTextEncode, Int, Seed (rgthree), PrimitiveFloat, UpscaleModelLoader, ImageUpscaleWithModel, VAEDecode, KSamplerAdvanced, CLIPTextEncode, PlaySound|pysssss, RHHiddenNodes, RHHiddenNodes, VHS_VideoCombine, Note, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 9, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.1_FusionX神奇文生视频工作流_comfyUI原生实现_1936920665587093505.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1936920665587093505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `Prompts Everywhere`
- `EmptyHunyuanLatentVideo`
- `ApplySageAttention`
- `CLIPLoader`
- `Anything Everywhere3`
- `ModelSamplingSD3`
- `Int`
- `CLIPTextEncode` ★核心
- `Int`
- `Seed (rgthree)`
- `PrimitiveFloat`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PlaySound|pysssss`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `Note`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`UNETLoader`、`VAELoader`、`Prompts Everywhere`、`EmptyHunyuanLatentVideo`、`ApplySageAttention`、`CLIPLoader`、`ModelSamplingSD3`、`Int`、`CLIPTextEncode`、`Seed (rgthree)`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VAEDecode`、`KSamplerAdvanced`、`PlaySound|pysssss`、`RHHiddenNodes`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、EmptyHunyuanLatentVideo
