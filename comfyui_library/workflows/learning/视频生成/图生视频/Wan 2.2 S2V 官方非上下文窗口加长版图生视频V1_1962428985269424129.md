---
key: 视频生成/图生视频/Wan 2.2 S2V 官方非上下文窗口加长版图生视频V1_1962428985269424129.json
name: Wan 2.2 S2V 官方非上下文窗口加长版图生视频V1_1962428985269424129.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.2 S2V 官方非上下文窗口加长版图生视频V1_1962428985269424129.json
hash: 3176ec6b888996e3
coverage: 0.794872
learned_at: 2026-10-15 22:31:30
nodes: [CLIPLoader, VAEDecode, CLIPTextEncode, VAELoader, AudioEncoderLoader, WanSoundImageToVideo, ModelSamplingSD3, LatentConcat, LatentCut, Note, PrimitiveInt, PrimitiveInt, MarkdownNote, AudioEncoderEncode, PrimitiveInt, PrimitiveFloat, MarkdownNote, MarkdownNote, KSampler, LatentConcat, KSampler, WanSoundImageToVideoExtend, LatentConcat, WanSoundImageToVideoExtend, KSampler, LoadAudio, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, UNETLoader, PathchSageAttentionKJ, CLIPTextEncode, ImageFromBatch, VHS_VideoCombine, WanSoundImageToVideoExtend, KSampler, LatentConcat, AudioCrop, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1, "steps": 10}
---

# 视频生成/图生视频/Wan 2.2 S2V 官方非上下文窗口加长版图生视频V1_1962428985269424129.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962428985269424129.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `AudioEncoderLoader`
- `WanSoundImageToVideo`
- `ModelSamplingSD3`
- `LatentConcat`
- `LatentCut`
- `Note`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `AudioEncoderEncode`
- `PrimitiveInt`
- `PrimitiveFloat`
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `LatentConcat`
- `KSampler` ★核心
- `WanSoundImageToVideoExtend`
- `LatentConcat`
- `WanSoundImageToVideoExtend`
- `KSampler` ★核心
- `LoadAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `ImageFromBatch`
- `VHS_VideoCombine`
- `WanSoundImageToVideoExtend`
- `KSampler` ★核心
- `LatentConcat`
- `AudioCrop`
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `seed` = `1`
- `steps` = `10`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（31/39）

**有卡**：`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`AudioEncoderLoader`、`WanSoundImageToVideo`、`ModelSamplingSD3`、`LatentConcat`、`LatentCut`、`AudioEncoderEncode`、`KSampler`、`WanSoundImageToVideoExtend`、`LoadAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`UNETLoader`、`PathchSageAttentionKJ`、`ImageFromBatch`、`VHS_VideoCombine`、`AudioCrop`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、AudioEncoderLoader
