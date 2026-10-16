---
key: 视频生成/图生视频/wan2.1首尾帧视频【教学】_2000392269180137473.json
name: wan2.1首尾帧视频【教学】_2000392269180137473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2000392269180137473.json
hash: abe177b0ee18a592
coverage: 0.954545
learned_at: 2026-10-15 22:33:40
nodes: [VAEDecode, VHS_VideoCombine, PreviewImage, LoraLoaderModelOnly, VAELoader, KSampler, ApplySageAttention, WanFirstLastFrameToVideo, CLIPVisionEncode, Int, CLIPVisionEncode, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, SimpleMath+, UNETLoader, ModelSamplingSD3, CLIPTextEncode, CLIPLoader, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 443679702370205, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.1首尾帧视频【教学】_2000392269180137473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000392269180137473.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSampler` ★核心
- `ApplySageAttention`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `Int`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `SimpleMath+`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `443679702370205`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`VAEDecode`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`ApplySageAttention`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`Int`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`SimpleMath+`、`UNETLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
