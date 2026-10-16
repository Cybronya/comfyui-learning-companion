---
key: 视频生成/图生视频/（CLK V2.1（自用））N版运动增强图生视频V1（官方流，不支持KJ）_1975896909040758785.json
name: （CLK V2.1（自用））N版运动增强图生视频V1（官方流，不支持KJ）_1975896909040758785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1975896909040758785.json
hash: d792d74624ec02bf
coverage: 0.894737
learned_at: 2026-10-15 22:32:10
nodes: [MarkdownNote, VAELoader, MarkdownNote, ImageFromBatch+, Note, LoraLoaderModelOnly, WanImageToVideo, CLIPVisionEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, TorchCompileModel, LayerUtility: ImageScaleByAspectRatio V2, Note, JWInteger, UNETLoader, UNETLoader, CLIPTextEncode, TorchCompileModel, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, CLIPTextEncode, VAEDecode, LoraLoaderModelOnly, TT_img_enc, CLIPLoader, CR Prompt Text, LoadImage, CLIPVisionLoader, JWInteger, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/（CLK V2.1（自用））N版运动增强图生视频V1（官方流，不支持KJ）_1975896909040758785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975896909040758785.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `MarkdownNote`
- `VAELoader`
- `MarkdownNote`
- `ImageFromBatch+`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `JWInteger`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `TorchCompileModel`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `TT_img_enc`
- `CLIPLoader`
- `CR Prompt Text`
- `LoadImage`
- `CLIPVisionLoader`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`VAELoader`、`ImageFromBatch+`、`LoraLoaderModelOnly`、`WanImageToVideo`、`CLIPVisionEncode`、`PathchSageAttentionKJ`、`TorchCompileModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`UNETLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`TT_img_enc`、`CLIPLoader`、`CR Prompt Text`、`LoadImage`、`CLIPVisionLoader`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
