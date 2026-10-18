---
key: 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega图生视频极速版_2052639403599773698.json
name: Wan2.2 Rapid-AIO-Mega图生视频极速版_2052639403599773698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Rapid-AIO-Mega图生视频极速版_2052639403599773698.json
hash: 6ecbd415c046f869
coverage: 0.875
learned_at: 2026-10-15 22:37:31
nodes: [CLIPTextEncode, Note, ModelSamplingSD3, Note, CheckpointLoaderSimple, ApplySageAttention, Note, WanVaceToVideo, JWInteger, MathExpression|pysssss, JWInteger, WanVideoVACEStartToEndFrame, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, KSampler, VHS_VideoCombine, PDIMAGE_LongerSize, VAEDecode, LayerUtility: PurgeVRAM V2, ImageConcanate, VHS_VideoCombine, JWInteger, LoadImage, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 162326267882810, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega图生视频极速版_2052639403599773698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052639403599773698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `ModelSamplingSD3`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `ApplySageAttention`
- `Note`
- `WanVaceToVideo`
- `JWInteger`
- `MathExpression|pysssss`
- `JWInteger`
- `WanVideoVACEStartToEndFrame`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageConcanate`
- `VHS_VideoCombine`
- `JWInteger`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`
- `seed` = `162326267882810`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`ApplySageAttention`、`WanVaceToVideo`、`JWInteger`、`MathExpression|pysssss`、`WanVideoVACEStartToEndFrame`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`VHS_VideoCombine`、`PDIMAGE_LongerSize`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`ImageConcanate`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、PDIMAGE_LongerSize、ImageConcanate、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
