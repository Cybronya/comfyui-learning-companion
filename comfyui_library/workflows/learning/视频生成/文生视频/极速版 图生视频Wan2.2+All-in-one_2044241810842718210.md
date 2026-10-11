---
key: 视频生成/文生视频/极速版 图生视频Wan2.2+All-in-one_2044241810842718210.json
name: 极速版 图生视频Wan2.2+All-in-one_2044241810842718210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/极速版 图生视频Wan2.2+All-in-one_2044241810842718210.json
hash: d565323051035d9b
coverage: 0.818182
learned_at: 2026-10-11 19:49:50
nodes: [CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, MathExpression|pysssss, CLIPLoader, CLIPTextEncode, JWInteger, JWInteger, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, JWFloat, VAEDecode, KSampler, ModelSamplingSD3, JWInteger, CheckpointLoaderSimple, LoadImage, CR Prompt Text, VHS_VideoCombine, Note]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 10952568152757, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/极速版 图生视频Wan2.2+All-in-one_2044241810842718210.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/极速版 图生视频Wan2.2+All-in-one_2044241810842718210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `CLIPVisionEncode`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `JWFloat`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `JWInteger`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `Note`

## 关键参数

- `seed` = `10952568152757`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`CLIPTextEncode`、`CLIPLoader`、`JWInteger`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPVisionLoader`、`JWFloat`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`LoadImage`、`VHS_VideoCombine`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
