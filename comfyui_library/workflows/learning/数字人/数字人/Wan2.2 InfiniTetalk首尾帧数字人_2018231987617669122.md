---
key: 数字人/数字人/Wan2.2 InfiniTetalk首尾帧数字人_2018231987617669122.json
name: Wan2.2 InfiniTetalk首尾帧数字人_2018231987617669122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 InfiniTetalk首尾帧数字人_2018231987617669122.json
hash: 7fad54e0cab76dfd
coverage: 0.944444
learned_at: 2026-10-26 01:57:53
nodes: [UNETLoader, VAELoader, AudioEncoderLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, PainterAI2V, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, AudioEncoderEncode, PainterAudioCut, Audio Duration (mtb), SimpleMath+, VAEDecode, ColorMatch, SimpleMath+, CLIPTextEncode, CLIPTextEncode, SimpleMath+, AudioBeforeAfterSilence, KSamplerAdvanced, KSamplerAdvanced, AudioCrop, easy showAnything, ImageFromBatch+, MarkdownNote, ImageResizeKJv2, ModelPatchLoader, LoadImage, LoadAudio, UNETLoader, CR Text, VHS_VideoCombine, RunningHub Deepcleaner, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 数字人/数字人/Wan2.2 InfiniTetalk首尾帧数字人_2018231987617669122.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 InfiniTetalk首尾帧数字人_2018231987617669122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `AudioEncoderLoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PainterAI2V`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `AudioEncoderEncode`
- `PainterAudioCut`
- `Audio Duration (mtb)`
- `SimpleMath+`
- `VAEDecode` ★核心
- `ColorMatch`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `AudioBeforeAfterSilence`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `AudioCrop`
- `easy showAnything`
- `ImageFromBatch+`
- `MarkdownNote`
- `ImageResizeKJv2`
- `ModelPatchLoader`
- `LoadImage`
- `LoadAudio`
- `UNETLoader` ★核心
- `CR Text`
- `VHS_VideoCombine`
- `RunningHub Deepcleaner`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`UNETLoader`、`VAELoader`、`AudioEncoderLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`PainterAI2V`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`AudioEncoderEncode`、`PainterAudioCut`、`Audio Duration (mtb)`、`SimpleMath+`、`VAEDecode`、`ColorMatch`、`CLIPTextEncode`、`AudioBeforeAfterSilence`、`KSamplerAdvanced`、`AudioCrop`、`ImageFromBatch+`、`ImageResizeKJv2`、`ModelPatchLoader`、`LoadImage`、`LoadAudio`、`CR Text`、`VHS_VideoCombine`、`RunningHub Deepcleaner`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
