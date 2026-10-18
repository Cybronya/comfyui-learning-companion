---
key: 视频生成/图生视频/【阡陌】Qwen3-VL图片反推提示词wan2.2首尾帧视频生成_1983549760990846978.json
name: 【阡陌】Qwen3-VL图片反推提示词wan2.2首尾帧视频生成_1983549760990846978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【阡陌】Qwen3-VL图片反推提示词wan2.2首尾帧视频生成_1983549760990846978.json
hash: 9884260bfe80b78b
coverage: 0.931034
learned_at: 2026-10-15 22:32:45
nodes: [VAEDecode, ModelSamplingSD3, ModelSamplingSD3, CreateVideo, SaveVideo, CLIPLoader, ModelPatchTorchSettings, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, KSamplerAdvanced, CLIPTextEncode, WanFunInpaintToVideo, KSamplerAdvanced, VAELoader, UNETLoader, UNETLoader, MultiplePathsInput, Qwen3_VQA, CLIPTextEncode, LoadImage, ImageLoader, ImageLoader, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveNode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/【阡陌】Qwen3-VL图片反推提示词wan2.2首尾帧视频生成_1983549760990846978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983549760990846978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `WanFunInpaintToVideo`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MultiplePathsInput`
- `Qwen3_VQA`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageLoader`
- `ImageLoader`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveNode`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`VAEDecode`、`ModelSamplingSD3`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`CLIPTextEncode`、`WanFunInpaintToVideo`、`VAELoader`、`UNETLoader`、`MultiplePathsInput`、`Qwen3_VQA`、`LoadImage`、`ImageLoader`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
