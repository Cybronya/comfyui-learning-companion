---
key: 视频生成/文生视频/【阡陌】 Wan2.2 Fun Control 视频控制生成_1969656393957601281.json
name: 【阡陌】 Wan2.2 Fun Control 视频控制生成_1969656393957601281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【阡陌】 Wan2.2 Fun Control 视频控制生成_1969656393957601281.json
hash: 9b5ac4094199ee17
coverage: 1
learned_at: 2026-10-15 22:43:47
nodes: [SaveVideo, CLIPLoader, LoadImage, LoraLoaderModelOnly, KSamplerAdvanced, CreateVideo, VAEDecode, VHS_VideoCombine, VHS_VideoCombine, ImageConcanate, VHS_LoadVideo, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, UNETLoader, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, VAELoader, LoadImage, DWPreprocessor, Wan22FunControlToVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/【阡陌】 Wan2.2 Fun Control 视频控制生成_1969656393957601281.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1969656393957601281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `SaveVideo`
- `CLIPLoader`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcanate`
- `VHS_LoadVideo`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `DWPreprocessor`
- `Wan22FunControlToVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`SaveVideo`、`CLIPLoader`、`LoadImage`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`CreateVideo`、`VAEDecode`、`VHS_VideoCombine`、`ImageConcanate`、`VHS_LoadVideo`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`DWPreprocessor`、`Wan22FunControlToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
