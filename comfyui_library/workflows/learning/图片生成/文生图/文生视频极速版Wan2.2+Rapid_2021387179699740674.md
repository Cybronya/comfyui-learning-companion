---
key: 图片生成/文生图/文生视频极速版Wan2.2+Rapid_2021387179699740674.json
name: 文生视频极速版Wan2.2+Rapid_2021387179699740674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生视频极速版Wan2.2+Rapid_2021387179699740674.json
hash: f766533bc82e0fb9
coverage: 0.85
learned_at: 2026-10-19 22:30:33
nodes: [Note, WanVaceToVideo, Primitive integer [Crystools], Primitive integer [Crystools], CheckpointLoaderSimple, CLIPTextEncode, INTConstant, MathExpression|pysssss, INTConstant, SetNode, GetNode, VHS_VideoCombine, VAEDecode, KSampler, LayerUtility: PurgeVRAM V2, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, Int, CLIPTextEncode, DF_Int_to_Float]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/文生视频极速版Wan2.2+Rapid_2021387179699740674.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生视频极速版Wan2.2+Rapid_2021387179699740674.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（20 个）：
- `Note`
- `WanVaceToVideo`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `MathExpression|pysssss`
- `INTConstant`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `CLIPTextEncode` ★核心
- `DF_Int_to_Float`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`
- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`WanVaceToVideo`、`Primitive integer [Crystools]`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`INTConstant`、`MathExpression|pysssss`、`VHS_VideoCombine`、`VAEDecode`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`ModelSamplingSD3`、`Int`、`DF_Int_to_Float`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、Int、INTConstant、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
