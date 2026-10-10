---
key: 视频生成/文生视频/Wan2.2 Dyno+Remix 新模型1.0文生视频V2（官方采样器）_1975847969142517762.json
name: Wan2.2 Dyno+Remix 新模型1.0文生视频V2（官方采样器）_1975847969142517762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Dyno+Remix 新模型1.0文生视频V2（官方采样器）_1975847969142517762.json
hash: 98a143dde132c61f
coverage: 0.961538
learned_at: 2026-10-10 23:06:47
nodes: [CLIPTextEncode, PathchSageAttentionKJ, EmptyHunyuanLatentVideo, INTConstant, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, VAELoader, CLIPLoader, INTConstant, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, JWInteger, JWInteger, JWInteger, KSamplerAdvanced, TT_img_enc, SaveImage, UNETLoader, VHS_VideoCombine, KSamplerAdvanced, UNETLoader, VAEDecode, ImageFromBatch+, VHS_VideoCombine]
patterns: []
missing: [ImageFromBatch+]
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2 Dyno+Remix 新模型1.0文生视频V2（官方采样器）_1975847969142517762.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Dyno+Remix 新模型1.0文生视频V2（官方采样器）_1975847969142517762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAELoader`
- `CLIPLoader`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `TT_img_enc`
- `SaveImage`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`INTConstant`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`JWInteger`、`KSamplerAdvanced`、`TT_img_enc`、`SaveImage`、`UNETLoader`、`VHS_VideoCombine`、`VAEDecode`

**缺卡**（1）：`ImageFromBatch+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
