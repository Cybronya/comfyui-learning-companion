---
key: 视频生成/图生视频/live动图-图生视频_wan2.2_2095005372602994689.json
name: live动图-图生视频_wan2.2_2095005372602994689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/live动图-图生视频_wan2.2_2095005372602994689.json
hash: e3cb0178468420f4
coverage: 0.933333
learned_at: 2026-10-17 00:02:46
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, JWInteger, PathchSageAttentionKJ, JWInteger, JWInteger, CR Prompt Text, CheckpointLoaderSimple, CLIPLoader, MathExpression|pysssss, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, WanImageToVideo, KSampler, VAEDecode, JWFloat, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, JoinStrings, easy showAnything, RH_Captioner, VHS_VideoCombine, Qwen3_VQA, ShowText|pysssss, TextInput_, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 1116447522038538, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/live动图-图生视频_wan2.2_2095005372602994689.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/live动图-图生视频_wan2.2_2095005372602994689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（30 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `PathchSageAttentionKJ`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `MathExpression|pysssss`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `WanImageToVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JWFloat`
- `ModelSamplingSD3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JoinStrings`
- `easy showAnything`
- `RH_Captioner`
- `VHS_VideoCombine`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `TextInput_`
- `LoadImage`
- `LoadImage`

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`
- `seed` = `1116447522038538`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`LoraLoaderModelOnly`、`JWInteger`、`PathchSageAttentionKJ`、`CR Prompt Text`、`CheckpointLoaderSimple`、`CLIPLoader`、`MathExpression|pysssss`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`WanImageToVideo`、`KSampler`、`VAEDecode`、`JWFloat`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`JoinStrings`、`RH_Captioner`、`VHS_VideoCombine`、`Qwen3_VQA`、`TextInput_`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
