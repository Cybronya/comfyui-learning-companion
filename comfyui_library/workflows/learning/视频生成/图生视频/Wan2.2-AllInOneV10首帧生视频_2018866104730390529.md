---
key: 视频生成/图生视频/Wan2.2-AllInOneV10首帧生视频_2018866104730390529.json
name: Wan2.2-AllInOneV10首帧生视频_2018866104730390529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2018866104730390529.json
hash: 032530aace75aa88
coverage: 1
learned_at: 2026-10-15 22:34:59
nodes: [SaveVideo, CreateVideo, VAEDecode, LayerUtility: PurgeVRAM V2, KSampler, WanImageToVideo, CLIPVisionEncode, LoadImage, ModelSamplingSD3, CLIPTextEncode, CLIPVisionLoader, SimpleMath+, CLIPTextEncode, Int, Int, CM_IntToFloat, LayerUtility: ImageScaleByAspectRatio V2, CheckpointLoaderSimple, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 951880442708552, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-AllInOneV10首帧生视频_2018866104730390529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018866104730390529.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `SaveVideo`
- `CreateVideo`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `KSampler` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `LoadImage`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `CM_IntToFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CheckpointLoaderSimple` ★核心
- `Int`

## 关键参数

- `seed` = `951880442708552`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10.safetensors`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`SaveVideo`、`CreateVideo`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`KSampler`、`WanImageToVideo`、`CLIPVisionEncode`、`LoadImage`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPVisionLoader`、`SimpleMath+`、`Int`、`CM_IntToFloat`、`LayerUtility: ImageScaleByAspectRatio V2`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、CLIPVisionLoader、SaveVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
