---
key: 视频生成/图生视频/Wan2.2+All-in-one图生视频极速版_2019656477216088065.json
name: Wan2.2+All-in-one图生视频极速版_2019656477216088065.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+All-in-one图生视频极速版_2019656477216088065.json
hash: 3f41739c2e9269fe
coverage: 1
learned_at: 2026-10-15 22:35:03
nodes: [CLIPVisionEncode, SaveImage, CLIPTextEncode, CLIPLoader, CLIPTextEncode, LoadImage, LoadLatent, VAEDecode, VHS_VideoCombine, VAELoader, CheckpointLoaderSimple, JWInteger, JWInteger, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, JWFloat, VAEDecode, KSampler, ModelSamplingSD3, VHS_VideoCombine, JWInteger, LoadImage, CR Prompt Text, MathExpression|pysssss, WanImageToVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 1009487704370414, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2+All-in-one图生视频极速版_2019656477216088065.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019656477216088065.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPVisionEncode`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
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
- `LoadImage`
- `CR Prompt Text`
- `MathExpression|pysssss`
- `WanImageToVideo`

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`
- `seed` = `1009487704370414`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`CLIPVisionEncode`、`SaveImage`、`CLIPTextEncode`、`CLIPLoader`、`LoadImage`、`LoadLatent`、`VAEDecode`、`VHS_VideoCombine`、`VAELoader`、`CheckpointLoaderSimple`、`JWInteger`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`JWFloat`、`KSampler`、`ModelSamplingSD3`、`CR Prompt Text`、`MathExpression|pysssss`、`WanImageToVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
