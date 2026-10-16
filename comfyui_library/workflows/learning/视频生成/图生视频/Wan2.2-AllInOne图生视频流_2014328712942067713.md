---
key: 视频生成/图生视频/Wan2.2-AllInOne图生视频流_2014328712942067713.json
name: Wan2.2-AllInOne图生视频流_2014328712942067713.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2014328712942067713.json
hash: d719e2403e404c9e
coverage: 0.928571
learned_at: 2026-10-15 22:34:34
nodes: [CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, VAEDecode, PreviewImage, ModelSamplingSD3, WanImageToVideo, LayerUtility: PurgeVRAM, KSampler, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, CheckpointLoaderSimple, LoadImage, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 192054346835137, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-AllInOne图生视频流_2014328712942067713.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2014328712942067713.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `PreviewImage`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `192054346835137`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`VAEDecode`、`ModelSamplingSD3`、`WanImageToVideo`、`LayerUtility: PurgeVRAM`、`KSampler`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`CheckpointLoaderSimple`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、CLIPVisionLoader、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
