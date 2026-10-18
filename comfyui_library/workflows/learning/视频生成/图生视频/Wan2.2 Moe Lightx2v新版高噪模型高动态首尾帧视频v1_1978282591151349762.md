---
key: 视频生成/图生视频/Wan2.2 Moe Lightx2v新版高噪模型高动态首尾帧视频v1_1978282591151349762.json
name: Wan2.2 Moe Lightx2v新版高噪模型高动态首尾帧视频v1_1978282591151349762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Moe Lightx2v新版高噪模型高动态首尾帧视频v1_1978282591151349762.json
hash: f4c1ecafb22a8925
coverage: 0.875
learned_at: 2026-10-15 22:32:18
nodes: [MarkdownNote, CLIPLoader, CLIPTextEncode, VAELoader, MarkdownNote, Note, PathchSageAttentionKJ, TorchCompileModel, Note, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, JWInteger, VAEDecode, ImageFromBatch+, VHS_VideoCombine, ModelSamplingSD3, ModelSamplingSD3, Note, UNETLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, TorchCompileModel, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, WanFirstLastFrameToVideo, LoadImage, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, LoadImage, CLIPVisionEncode, CLIPVisionLoader, CLIPVisionEncode, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Moe Lightx2v新版高噪模型高动态首尾帧视频v1_1978282591151349762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978282591151349762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `MarkdownNote`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `MarkdownNote`
- `Note`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `LoadImage`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`PathchSageAttentionKJ`、`TorchCompileModel`、`LoraLoaderModelOnly`、`JWInteger`、`VAEDecode`、`ImageFromBatch+`、`VHS_VideoCombine`、`ModelSamplingSD3`、`UNETLoader`、`KSamplerAdvanced`、`WanFirstLastFrameToVideo`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
