---
key: 视频生成/文生视频/（Mega V11）Wan2.2 Rapid-AIO大一统多合一（文生视频、图生视频、首尾帧视频）_1975577828731301889.json
name: （Mega V11）Wan2.2 Rapid-AIO大一统多合一（文生视频、图生视频、首尾帧视频）_1975577828731301889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（Mega V11）Wan2.2 Rapid-AIO大一统多合一（文生视频、图生视频、首尾帧视频）_1975577828731301889.json
hash: 6526ac858970695e
coverage: 0.52
learned_at: 2026-10-10 23:14:27
nodes: [RH_LLMAPI_NODE, Text Concatenate, RH_LLMAPI_NODE, ImpactSwitch, CLIPTextEncode, CLIPTextEncode, LoadImage, JWInteger, ImageConcanate, easy showAnything, Wan22PromptSelector, Mute / Bypass Repeater (rgthree), PrimitiveInt, PrimitiveInt, Any Switch (rgthree), Any Switch (rgthree), Note, WanVaceToVideo, MathExpression|pysssss, PrimitiveFloat, PrimitiveFloat, Any Switch (rgthree), Mute / Bypass Relay (rgthree), LoadImage, RH_LLMAPI_NODE, Any Switch (rgthree), RH_LLMAPI_NODE, WanVideoVACEStartToEndFrame, ImageResizeKJ, ImageConcanate, Note, Mute / Bypass Relay (rgthree), ImpactInt, ImpactInt, ImageConcanate, Mute / Bypass Repeater (rgthree), wanBlockSwap, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, CR Text, Fast Groups Bypasser (rgthree), CR Text, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, VHS_VideoCombine, ImageFromBatch+, VHS_VideoCombine, KSampler, CheckpointLoaderSimple]
patterns: []
missing: [CR Text, CR Text, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, Mute / Bypass Relay (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Text Concatenate]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v11.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 573754122364118, "steps": 4}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Relay (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Relay (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/（Mega V11）Wan2.2 Rapid-AIO大一统多合一（文生视频、图生视频、首尾帧视频）_1975577828731301889.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（Mega V11）Wan2.2 Rapid-AIO大一统多合一（文生视频、图生视频、首尾帧视频）_1975577828731301889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（50 个）：
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `JWInteger`
- `ImageConcanate`
- `easy showAnything`
- `Wan22PromptSelector`
- `Mute / Bypass Repeater (rgthree)`
- `PrimitiveInt`
- `PrimitiveInt`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Note`
- `WanVaceToVideo`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `Any Switch (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `Any Switch (rgthree)`
- `RH_LLMAPI_NODE`
- `WanVideoVACEStartToEndFrame`
- `ImageResizeKJ`
- `ImageConcanate`
- `Note`
- `Mute / Bypass Relay (rgthree)`
- `ImpactInt`
- `ImpactInt`
- `ImageConcanate`
- `Mute / Bypass Repeater (rgthree)`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `573754122364118`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v11.safetensors`

## 知识

覆盖率 **52%**（26/50）

**有卡**：`RH_LLMAPI_NODE`、`CLIPTextEncode`、`LoadImage`、`JWInteger`、`ImageConcanate`、`Wan22PromptSelector`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`ImageResizeKJ`、`ImpactInt`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`CheckpointLoaderSimple`

**缺卡**（10）：`CR Text`、`CR Text`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`Mute / Bypass Relay (rgthree)`、`Mute / Bypass Relay (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Text Concatenate`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Wan22PromptSelector、ImageResizeKJ、ImageConcanate

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Relay (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Relay (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
