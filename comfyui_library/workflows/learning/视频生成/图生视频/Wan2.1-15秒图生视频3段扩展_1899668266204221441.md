---
key: 视频生成/图生视频/Wan2.1-15秒图生视频3段扩展_1899668266204221441.json
name: Wan2.1-15秒图生视频3段扩展_1899668266204221441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1899668266204221441.json
hash: fdddc8573fc424fb
coverage: 0.954545
learned_at: 2026-10-15 22:29:21
nodes: [ModelSamplingSD3, VAEDecode, CLIPVisionEncode, GetImageSizeAndCount, MathExpression|pysssss, ImageFromBatch, CLIPVisionEncode, WanImageToVideo, MathExpression|pysssss, ImageFromBatch, GetImageSizeAndCount, ImpactInt, PathchSageAttentionKJ, VAEDecode, ImageBatch, WanImageToVideo, CLIPVisionEncode, KSampler, VAEDecode, ImageBatch, KSampler, KSampler, WanImageToVideo, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, PreviewImage, UNETLoader, UnetLoaderGGUF, WanVideoTeaCacheKJ, CLIPLoader, VAELoader, CLIPVisionLoader, TorchCompileModelWanVideo, LoadImage, ImpactInt, ImpactInt, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPVisionLoader, CLIPVisionLoader, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 249152997625579, "steps": 20}
---

# 视频生成/图生视频/Wan2.1-15秒图生视频3段扩展_1899668266204221441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1899668266204221441.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `CLIPVisionEncode`
- `WanImageToVideo`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `ImpactInt`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `ImageBatch`
- `WanImageToVideo`
- `CLIPVisionEncode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageBatch`
- `KSampler` ★核心
- `KSampler` ★核心
- `WanImageToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `WanVideoTeaCacheKJ`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `TorchCompileModelWanVideo`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `249152997625579`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（42/44）

**有卡**：`ModelSamplingSD3`、`VAEDecode`、`CLIPVisionEncode`、`GetImageSizeAndCount`、`MathExpression|pysssss`、`ImageFromBatch`、`WanImageToVideo`、`ImpactInt`、`PathchSageAttentionKJ`、`ImageBatch`、`KSampler`、`VHS_VideoCombine`、`UNETLoader`、`UnetLoaderGGUF`、`WanVideoTeaCacheKJ`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`TorchCompileModelWanVideo`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
