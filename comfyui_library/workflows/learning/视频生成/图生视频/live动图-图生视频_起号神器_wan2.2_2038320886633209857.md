---
key: 视频生成/图生视频/live动图-图生视频_起号神器_wan2.2_2038320886633209857.json
name: live动图-图生视频_起号神器_wan2.2_2038320886633209857.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038320886633209857.json
hash: e6209a0a26da06f3
coverage: 1
learned_at: 2026-10-15 22:36:02
nodes: [CLIPVisionEncode, WanImageToVideo, MathExpression|pysssss, CLIPLoader, LoadLatent, VAEDecode, VHS_VideoCombine, VAELoader, JWInteger, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, JWFloat, KSampler, ModelSamplingSD3, JWInteger, LoadImage, JWInteger, CheckpointLoaderSimple, LoraLoaderModelOnly, SaveImage, TwoWaySwitch, CR Prompt Text, Int, CLIPTextEncode, LoadImage, VHS_VideoCombine, VAEDecode, CLIPTextEncode, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 399207984471919, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/live动图-图生视频_起号神器_wan2.2_2038320886633209857.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038320886633209857.json`

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

- `seed` = `399207984471919`
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
