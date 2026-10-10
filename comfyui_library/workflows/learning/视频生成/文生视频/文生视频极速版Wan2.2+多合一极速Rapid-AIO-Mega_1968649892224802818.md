---
key: 视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_1968649892224802818.json
name: 文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_1968649892224802818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_1968649892224802818.json
hash: 18ae0af3c35d4c91
coverage: 0.6
learned_at: 2026-10-10 23:13:13
nodes: [Note, WanVaceToVideo, Primitive integer [Crystools], Primitive integer [Crystools], CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, INTConstant, MathExpression|pysssss, INTConstant, SetNode, GetNode, DF_Int_to_Float, VHS_VideoCombine, VAEDecode, KSampler, LayerUtility: PurgeVRAM V2, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, Int]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, Primitive integer [Crystools], Primitive integer [Crystools]]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_1968649892224802818.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_1968649892224802818.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（20 个）：
- `Note`
- `WanVaceToVideo`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `MathExpression|pysssss`
- `INTConstant`
- `SetNode`
- `GetNode`
- `DF_Int_to_Float`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `Int`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`
- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **60%**（12/20）

**有卡**：`WanVaceToVideo`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`INTConstant`、`DF_Int_to_Float`、`VHS_VideoCombine`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`Int`

**缺卡**（5）：`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、Int、INTConstant、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
