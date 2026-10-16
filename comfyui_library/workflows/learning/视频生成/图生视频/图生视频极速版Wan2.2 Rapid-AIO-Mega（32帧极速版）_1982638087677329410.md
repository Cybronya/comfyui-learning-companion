---
key: 视频生成/图生视频/图生视频极速版Wan2.2 Rapid-AIO-Mega（32帧极速版）_1982638087677329410.json
name: 图生视频极速版Wan2.2 Rapid-AIO-Mega（32帧极速版）_1982638087677329410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1982638087677329410.json
hash: ee0cae85668508af
coverage: 0.846154
learned_at: 2026-10-15 22:32:41
nodes: [CLIPTextEncode, ModelSamplingSD3, Note, WanVaceToVideo, WanVideoVACEStartToEndFrame, LayerUtility: ImageScaleByAspectRatio V2, KSampler, GIMMVFI_interpolate, SimpleMath+, VAEDecode, DownloadAndLoadGIMMVFIModel, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, CM_IntToFloat, JWInteger, Note, Note, ApplySageAttention, MathExpression|pysssss, JWInteger, JWInteger, JWInteger, LoadImage, CLIPTextEncode, PrimitiveNode, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v11.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 258531477796076, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/图生视频极速版Wan2.2 Rapid-AIO-Mega（32帧极速版）_1982638087677329410.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982638087677329410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `Note`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `GIMMVFI_interpolate`
- `SimpleMath+`
- `VAEDecode` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `CM_IntToFloat`
- `JWInteger`
- `Note`
- `Note`
- `ApplySageAttention`
- `MathExpression|pysssss`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `258531477796076`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v11.safetensors`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`GIMMVFI_interpolate`、`SimpleMath+`、`VAEDecode`、`DownloadAndLoadGIMMVFIModel`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`CM_IntToFloat`、`JWInteger`、`ApplySageAttention`、`MathExpression|pysssss`、`LoadImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CM_IntToFloat、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
