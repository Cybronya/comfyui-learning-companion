---
key: 视频生成/图生视频/wan2.2-动作迁移（WanVace版）_1969267205433159682.json
name: wan2.2-动作迁移（WanVace版）_1969267205433159682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1969267205433159682.json
hash: 07654ca70de71fe7
coverage: 0.869565
learned_at: 2026-10-15 22:31:48
nodes: [RH_Captioner, LayerUtility: TextJoin, CLIPTextEncode, CLIPTextEncode, ImageResizeKJv2, KSampler, PrimitiveInt, PrimitiveInt, ImageResizeKJv2, DWPreprocessor, GetImageSizeAndCount, Anything Everywhere3, PathchSageAttentionKJ, ModelSamplingSD3, Zoe-DepthMapPreprocessor, VHS_LoadVideo, WanVaceToVideo, CheckpointLoaderSimple, LoadImage, VAEDecode, ColorMatch, ImageBlend, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 147939141502779, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.2-动作迁移（WanVace版）_1969267205433159682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969267205433159682.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `RH_Captioner`
- `LayerUtility: TextJoin`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `KSampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `Anything Everywhere3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Zoe-DepthMapPreprocessor`
- `VHS_LoadVideo`
- `WanVaceToVideo`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `ColorMatch`
- `ImageBlend`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `147939141502779`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`RH_Captioner`、`LayerUtility: TextJoin`、`CLIPTextEncode`、`ImageResizeKJv2`、`KSampler`、`DWPreprocessor`、`GetImageSizeAndCount`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`Zoe-DepthMapPreprocessor`、`VHS_LoadVideo`、`WanVaceToVideo`、`CheckpointLoaderSimple`、`LoadImage`、`VAEDecode`、`ColorMatch`、`ImageBlend`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Zoe-DepthMapPreprocessor、GetImageSizeAndCount、ImageResizeKJv2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
