---
key: 视频生成/图生视频/Aiwood-wan2.2Funvace官流_1966707596608647169.json
name: Aiwood-wan2.2Funvace官流_1966707596608647169.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1966707596608647169.json
hash: 643d4bd2bf5f671a
coverage: 0.866667
learned_at: 2026-10-15 22:31:39
nodes: [MaskToImage, CLIPTextEncode, ImageBatch, ImageBatch, ImageBatch, ImageToMask, SolidMask, MaskToImage, SolidMask, PrimitiveInt, ImageBatch, WanVaceToVideo, PrimitiveNode, PrimitiveNode, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, TorchCompileModelWanVideoV2, TrimVideoLatent, VAEDecode, KSamplerAdvanced, ImageScaleToMegapixels, ImageScaleToMegapixels, VAEDecode, ImageStitch, ImageStitch, VHS_VideoCombine, PrimitiveInt, PreviewImage, PreviewImage, RepeatImageBatch, LoadImage, VHS_VideoCombine, INTConstant, INTConstant, PathchSageAttentionKJ, TorchCompileModelWanVideoV2, UNETLoader, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, LoadImage, VAELoader, CLIPLoader, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Aiwood-wan2.2Funvace官流_1966707596608647169.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966707596608647169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `MaskToImage`
- `CLIPTextEncode` ★核心
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageToMask`
- `SolidMask`
- `MaskToImage`
- `SolidMask`
- `PrimitiveInt`
- `ImageBatch`
- `WanVaceToVideo`
- `PrimitiveNode`
- `PrimitiveNode`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `ImageScaleToMegapixels`
- `ImageScaleToMegapixels`
- `VAEDecode` ★核心
- `ImageStitch`
- `ImageStitch`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PreviewImage`
- `PreviewImage`
- `RepeatImageBatch`
- `LoadImage`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideoV2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（39/45）

**有卡**：`MaskToImage`、`CLIPTextEncode`、`ImageBatch`、`ImageToMask`、`SolidMask`、`WanVaceToVideo`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`TorchCompileModelWanVideoV2`、`TrimVideoLatent`、`VAEDecode`、`KSamplerAdvanced`、`ImageScaleToMegapixels`、`ImageStitch`、`VHS_VideoCombine`、`RepeatImageBatch`、`LoadImage`、`INTConstant`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
