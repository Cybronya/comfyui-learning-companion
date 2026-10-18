---
key: 视频生成/图生视频/wan2.1 fusionx vace 首尾帧 官方工作流（gguf版）_1937092855930458113.json
name: wan2.1 fusionx vace 首尾帧 官方工作流（gguf版）_1937092855930458113.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1 fusionx vace 首尾帧 官方工作流（gguf版）_1937092855930458113.json
hash: 0723afdeef738de6
coverage: 0.882353
learned_at: 2026-10-15 22:30:28
nodes: [ImageBatch, ImageToMask, ImageBatch, TrimVideoLatent, RepeatImageBatch, MaskToImage, SolidMask, ImageBatch, SolidMask, MaskToImage, ImageBatch, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, PrimitiveInt, MathExpression|pysssss, CR Text, VAEDecode, WanVaceToVideo, CLIPLoader, VAELoader, PathchSageAttentionKJ, KSampler, UnetLoaderGGUF, VHS_VideoCombine, PrimitiveInt, PreviewImage, PreviewImage, TorchCompileModelWanVideoV2, PatchModelPatcherOrder]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1058793506303570, "steps": 10}
---

# 视频生成/图生视频/wan2.1 fusionx vace 首尾帧 官方工作流（gguf版）_1937092855930458113.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937092855930458113.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `ImageBatch`
- `ImageToMask`
- `ImageBatch`
- `TrimVideoLatent`
- `RepeatImageBatch`
- `MaskToImage`
- `SolidMask`
- `ImageBatch`
- `SolidMask`
- `MaskToImage`
- `ImageBatch`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `CR Text`
- `VAEDecode` ★核心
- `WanVaceToVideo`
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `UnetLoaderGGUF` ★核心
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PreviewImage`
- `PreviewImage`
- `TorchCompileModelWanVideoV2`
- `PatchModelPatcherOrder`

## 关键参数

- `seed` = `1058793506303570`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`ImageBatch`、`ImageToMask`、`TrimVideoLatent`、`RepeatImageBatch`、`MaskToImage`、`SolidMask`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`MathExpression|pysssss`、`CR Text`、`VAEDecode`、`WanVaceToVideo`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`KSampler`、`UnetLoaderGGUF`、`VHS_VideoCombine`、`TorchCompileModelWanVideoV2`、`PatchModelPatcherOrder`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、TrimVideoLatent
