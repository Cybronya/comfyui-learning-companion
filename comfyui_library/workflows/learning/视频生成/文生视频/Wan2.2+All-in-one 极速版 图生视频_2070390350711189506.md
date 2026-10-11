---
key: 视频生成/文生视频/Wan2.2+All-in-one 极速版 图生视频_2070390350711189506.json
name: Wan2.2+All-in-one 极速版 图生视频_2070390350711189506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2+All-in-one 极速版 图生视频_2070390350711189506.json
hash: f0c2d87d07baf3f8
coverage: 0.818182
learned_at: 2026-10-11 20:21:31
nodes: [CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, MathExpression|pysssss, CLIPLoader, CLIPTextEncode, JWInteger, JWInteger, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, JWFloat, VAEDecode, KSampler, ModelSamplingSD3, JWInteger, CheckpointLoaderSimple, VHS_VideoCombine, Note, CR Prompt Text, LoadImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 482010572999044, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2+All-in-one 极速版 图生视频_2070390350711189506.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2+All-in-one 极速版 图生视频_2070390350711189506.json`

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
- `VHS_VideoCombine`
- `Note`
- `CR Prompt Text`
- `LoadImage`

## 关键参数

- `seed` = `482010572999044`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`CLIPTextEncode`、`CLIPLoader`、`JWInteger`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPVisionLoader`、`JWFloat`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`LoadImage`

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
