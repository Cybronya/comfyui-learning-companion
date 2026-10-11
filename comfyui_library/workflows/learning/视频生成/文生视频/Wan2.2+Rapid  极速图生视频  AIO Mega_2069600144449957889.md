---
key: 视频生成/文生视频/Wan2.2+Rapid  极速图生视频  AIO Mega_2069600144449957889.json
name: Wan2.2+Rapid  极速图生视频  AIO Mega_2069600144449957889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2+Rapid  极速图生视频  AIO Mega_2069600144449957889.json
hash: 004410a11df7af10
coverage: 0.857143
learned_at: 2026-10-11 20:21:31
nodes: [WanVaceToVideo, WanVideoVACEStartToEndFrame, KSampler, VHS_VideoCombine, PDIMAGE_LongerSize, VAEDecode, ImageConcanate, JWInteger, JWInteger, JWInteger, MathExpression|pysssss, JWInteger, CheckpointLoaderSimple, ApplySageAttention, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, CLIPTextEncode, LoadImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, MathExpression|pysssss]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 134195933514968, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2+Rapid  极速图生视频  AIO Mega_2069600144449957889.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2+Rapid  极速图生视频  AIO Mega_2069600144449957889.json`

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
- `LoadImage`

## 关键参数

- `seed` = `134195933514968`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`KSampler`、`VHS_VideoCombine`、`PDIMAGE_LongerSize`、`VAEDecode`、`ImageConcanate`、`JWInteger`、`CheckpointLoaderSimple`、`ApplySageAttention`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、PDIMAGE_LongerSize、ImageConcanate、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
