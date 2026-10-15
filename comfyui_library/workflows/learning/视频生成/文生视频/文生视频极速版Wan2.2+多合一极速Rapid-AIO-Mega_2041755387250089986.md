---
key: 视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_2041755387250089986.json
name: 文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_2041755387250089986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_2041755387250089986.json
hash: 5bfea4be76835d92
coverage: 0.85
learned_at: 2026-10-15 22:48:44
nodes: [Primitive integer [Crystools], Primitive integer [Crystools], INTConstant, MathExpression|pysssss, INTConstant, VAEDecode, Int, CheckpointLoaderSimple, CLIPTextEncode, SetNode, WanVaceToVideo, LayerUtility: PurgeVRAM V2, ModelSamplingSD3, Note, KSampler, GetNode, LayerUtility: PurgeVRAM V2, DF_Int_to_Float, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_2041755387250089986.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_2041755387250089986.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（20 个）：
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `INTConstant`
- `MathExpression|pysssss`
- `INTConstant`
- `VAEDecode` ★核心
- `Int`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `WanVaceToVideo`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingSD3`
- `Note`
- `KSampler` ★核心
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `DF_Int_to_Float`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

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

**有卡**：`Primitive integer [Crystools]`、`INTConstant`、`MathExpression|pysssss`、`VAEDecode`、`Int`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`WanVaceToVideo`、`LayerUtility: PurgeVRAM V2`、`ModelSamplingSD3`、`KSampler`、`DF_Int_to_Float`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、Int、INTConstant、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
