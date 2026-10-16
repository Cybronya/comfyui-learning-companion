---
key: 视频生成/图生视频/极速图生视频 保留真实细节生视频 Wan2.2 Rapid-AIO-Mega 超级加速版_2026459324947632130.json
name: 极速图生视频 保留真实细节生视频 Wan2.2 Rapid-AIO-Mega 超级加速版_2026459324947632130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2026459324947632130.json
hash: 68e51a1b79db729a
coverage: 1
learned_at: 2026-10-15 22:35:14
nodes: [WanVaceToVideo, WanVideoVACEStartToEndFrame, KSampler, VHS_VideoCombine, PDIMAGE_LongerSize, VAEDecode, ImageConcanate, JWInteger, LoadImage, JWInteger, JWInteger, MathExpression|pysssss, JWInteger, CheckpointLoaderSimple, ApplySageAttention, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 969351200151193, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/极速图生视频 保留真实细节生视频 Wan2.2 Rapid-AIO-Mega 超级加速版_2026459324947632130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2026459324947632130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `VAEDecode` ★核心
- `ImageConcanate`
- `JWInteger`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `MathExpression|pysssss`
- `JWInteger`
- `CheckpointLoaderSimple` ★核心
- `ApplySageAttention`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `969351200151193`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`KSampler`、`VHS_VideoCombine`、`PDIMAGE_LongerSize`、`VAEDecode`、`ImageConcanate`、`JWInteger`、`LoadImage`、`MathExpression|pysssss`、`CheckpointLoaderSimple`、`ApplySageAttention`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、PDIMAGE_LongerSize、ImageConcanate、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
