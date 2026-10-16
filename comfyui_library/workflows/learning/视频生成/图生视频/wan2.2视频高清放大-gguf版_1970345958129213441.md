---
key: 视频生成/图生视频/wan2.2视频高清放大-gguf版_1970345958129213441.json
name: wan2.2视频高清放大-gguf版_1970345958129213441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1970345958129213441.json
hash: 84bf336be0e2b400
coverage: 1
learned_at: 2026-10-15 22:31:53
nodes: [PathchSageAttentionKJ, KSampler, VHS_VideoCombine, VAEDecode, LoraLoaderModelOnly, VHS_LoadVideo, UnetLoaderGGUF, ImageUpscaleWithModel, CLIPLoader, CLIPTextEncode, VAEEncode, VAELoader, ModelSamplingSD3, CLIPTextEncode, ImageScaleBy, UpscaleModelLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.2, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 713853677764099, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.2视频高清放大-gguf版_1970345958129213441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1970345958129213441.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`
- `UnetLoaderGGUF` ★核心
- `ImageUpscaleWithModel`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `ImageScaleBy`
- `UpscaleModelLoader`

## 关键参数

- `seed` = `713853677764099`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.2`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`PathchSageAttentionKJ`、`KSampler`、`VHS_VideoCombine`、`VAEDecode`、`LoraLoaderModelOnly`、`VHS_LoadVideo`、`UnetLoaderGGUF`、`ImageUpscaleWithModel`、`CLIPLoader`、`CLIPTextEncode`、`VAEEncode`、`VAELoader`、`ModelSamplingSD3`、`ImageScaleBy`、`UpscaleModelLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、VAEEncode、ImageUpscaleWithModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
