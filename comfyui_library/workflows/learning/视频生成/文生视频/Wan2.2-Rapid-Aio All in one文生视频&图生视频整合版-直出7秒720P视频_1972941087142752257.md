---
key: 视频生成/文生视频/Wan2.2-Rapid-Aio All in one文生视频&图生视频整合版-直出7秒720P视频_1972941087142752257.json
name: Wan2.2-Rapid-Aio All in one文生视频&图生视频整合版-直出7秒720P视频_1972941087142752257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-Rapid-Aio All in one文生视频&图生视频整合版-直出7秒720P视频_1972941087142752257.json
hash: fec0a7d7de6ea953
coverage: 0.809524
learned_at: 2026-10-10 23:07:09
nodes: [CLIPTextEncode, LoadImage, CLIPTextEncode, LoraLoader, Fast Groups Bypasser (rgthree), Lora Loader Stack (rgthree), Int, Int, MathExpression_UTK, Int, ModelSamplingSD3, RHHiddenNodes, EmptyHunyuanLatentVideo, LayerUtility: PurgeVRAM, Int, Int, MathExpression_UTK, Int, CLIPVisionLoader, RHHiddenNodes, TorchCompileModelWanVideoV2, CLIPVisionEncode, ModelSamplingSD3, VAEDecode, WanImageToVideo, ColorMatch, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, CR Text Concatenate, CR Text, CR Text, Note, KSampler, SaveLatent, Note, KSampler, VAEDecode, SaveLatent, CheckpointLoaderSimple, CheckpointLoaderSimple, VHS_VideoCombine]
patterns: [lora]
missing: [CR Text, CR Text, CR Text Concatenate, LayerUtility: PurgeVRAM, Lora Loader Stack (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10.safetensors", "denoise": 1, "lora_name": "Wan2.1_I2V_14B_FusionX_LoRA.safetensors", "sampler_name": "sa_solver", "scheduler": "beta", "seed": 641247312301013, "steps": 6, "strength_clip": 1, "strength_model": 0.8}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2-Rapid-Aio All in one文生视频&图生视频整合版-直出7秒720P视频_1972941087142752257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-Rapid-Aio All in one文生视频&图生视频整合版-直出7秒720P视频_1972941087142752257.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（42 个）：
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Lora Loader Stack (rgthree)`
- `Int`
- `Int`
- `MathExpression_UTK`
- `Int`
- `ModelSamplingSD3`
- `RHHiddenNodes`
- `EmptyHunyuanLatentVideo`
- `LayerUtility: PurgeVRAM`
- `Int`
- `Int`
- `MathExpression_UTK`
- `Int`
- `CLIPVisionLoader`
- `RHHiddenNodes`
- `TorchCompileModelWanVideoV2`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `WanImageToVideo`
- `ColorMatch`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `CR Text`
- `CR Text`
- `Note`
- `KSampler` ★核心
- `SaveLatent`
- `Note`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveLatent`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Wan2.1_I2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `seed` = `641247312301013`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10.safetensors`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`CLIPTextEncode`、`LoadImage`、`LoraLoader`、`Int`、`MathExpression_UTK`、`ModelSamplingSD3`、`RHHiddenNodes`、`EmptyHunyuanLatentVideo`、`CLIPVisionLoader`、`TorchCompileModelWanVideoV2`、`CLIPVisionEncode`、`VAEDecode`、`WanImageToVideo`、`ColorMatch`、`VHS_VideoCombine`、`KSampler`、`SaveLatent`、`CheckpointLoaderSimple`

**缺卡**（5）：`CR Text`、`CR Text`、`CR Text Concatenate`、`LayerUtility: PurgeVRAM`、`Lora Loader Stack (rgthree)`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveLatent、CLIPVisionEncode、EmptyHunyuanLatentVideo

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
