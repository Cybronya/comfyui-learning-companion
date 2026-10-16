---
key: 视频生成/图生视频/Wan2.2 Moe Lightx2v图生视频v1_1978387992047931393.json
name: Wan2.2 Moe Lightx2v图生视频v1_1978387992047931393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1978387992047931393.json
hash: 7ef126ae59698618
coverage: 0.970588
learned_at: 2026-10-15 22:32:19
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, WanImageToVideo, CLIPVisionEncode, PathchSageAttentionKJ, TorchCompileModel, LoraLoaderModelOnly, CLIPTextEncode, CLIPVisionLoader, PathchSageAttentionKJ, TorchCompileModel, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageFromBatch+, ModelSamplingSD3, ModelSamplingSD3, Note, UNETLoader, UNETLoader, JWInteger, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, RIFE VFI, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, VHS_VideoCombine, JWInteger, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Moe Lightx2v图生视频v1_1978387992047931393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978387992047931393.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageFromBatch+`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `RIFE VFI`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LoraLoaderModelOnly`、`WanImageToVideo`、`CLIPVisionEncode`、`PathchSageAttentionKJ`、`TorchCompileModel`、`CLIPVisionLoader`、`ImageFromBatch+`、`ModelSamplingSD3`、`UNETLoader`、`JWInteger`、`KSamplerAdvanced`、`VAEDecode`、`RIFE VFI`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
