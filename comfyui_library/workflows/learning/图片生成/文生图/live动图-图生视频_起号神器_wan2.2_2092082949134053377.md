---
key: 图片生成/文生图/live动图-图生视频_起号神器_wan2.2_2092082949134053377.json
name: live动图-图生视频_起号神器_wan2.2_2092082949134053377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/live动图-图生视频_起号神器_wan2.2_2092082949134053377.json
hash: 2d692503a5e17519
coverage: 1
learned_at: 2026-10-20 01:19:46
nodes: [CLIPVisionEncode, WanImageToVideo, MathExpression|pysssss, CLIPLoader, LoadLatent, VAEDecode, VHS_VideoCombine, VAELoader, JWInteger, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, JWFloat, KSampler, ModelSamplingSD3, JWInteger, LoadImage, JWInteger, CheckpointLoaderSimple, LoraLoaderModelOnly, SaveImage, TwoWaySwitch, CR Prompt Text, Int, CLIPTextEncode, LoadImage, VHS_VideoCombine, VAEDecode, CLIPTextEncode, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 346508688118809, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/live动图-图生视频_起号神器_wan2.2_2092082949134053377.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/live动图-图生视频_起号神器_wan2.2_2092082949134053377.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPVisionEncode`
- `WanImageToVideo`
- `MathExpression|pysssss`
- `CLIPLoader`
- `LoadLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `JWInteger`
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `JWFloat`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `JWInteger`
- `LoadImage`
- `JWInteger`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `TwoWaySwitch`
- `CR Prompt Text`
- `Int`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `346508688118809`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`MathExpression|pysssss`、`CLIPLoader`、`LoadLatent`、`VAEDecode`、`VHS_VideoCombine`、`VAELoader`、`JWInteger`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`JWFloat`、`KSampler`、`ModelSamplingSD3`、`LoadImage`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`SaveImage`、`TwoWaySwitch`、`CR Prompt Text`、`Int`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
