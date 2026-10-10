---
key: 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_1983515933761314818.json
name: 图生视频Wan2.2+All-in-one极速版_1983515933761314818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_1983515933761314818.json
hash: 378df726f5196b54
coverage: 0.888889
learned_at: 2026-10-10 22:54:58
nodes: [CLIPVisionEncode, WanImageToVideo, SaveImage, CLIPTextEncode, MathExpression|pysssss, CLIPLoader, CLIPTextEncode, LoadImage, LoadLatent, VAEDecode, VHS_VideoCombine, VAELoader, CR Prompt Text, CheckpointLoaderSimple, LoadImage, JWInteger, JWInteger, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, JWFloat, VAEDecode, KSampler, ModelSamplingSD3, VHS_VideoCombine, JWInteger]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 448766640178835, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_1983515933761314818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_1983515933761314818.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPVisionEncode`
- `WanImageToVideo`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `CR Prompt Text`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
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
- `VHS_VideoCombine`
- `JWInteger`

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`
- `seed` = `448766640178835`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`SaveImage`、`CLIPTextEncode`、`CLIPLoader`、`LoadImage`、`LoadLatent`、`VAEDecode`、`VHS_VideoCombine`、`VAELoader`、`CheckpointLoaderSimple`、`JWInteger`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPVisionLoader`、`JWFloat`、`KSampler`、`ModelSamplingSD3`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
