---
key: 视频生成/图生视频/满血版Wan2.2-S2V最新修复版-ComfyUI_1961703207414251521.json
name: 满血版Wan2.2-S2V最新修复版-ComfyUI_1961703207414251521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1961703207414251521.json
hash: 0e2214c42ba5fc04
coverage: 0.738095
learned_at: 2026-10-15 22:31:29
nodes: [CLIPLoader, VAEDecode, CLIPTextEncode, VAELoader, ModelSamplingSD3, LatentConcat, LatentCut, Note, MarkdownNote, PrimitiveInt, PrimitiveFloat, CLIPLoader, CLIPTextEncode, VAELoader, AudioEncoderLoader, KSampler, WanSoundImageToVideo, ModelSamplingSD3, MarkdownNote, MarkdownNote, KSampler, KSampler, LatentConcat, WanSoundImageToVideoExtend, KSampler, WanSoundImageToVideoExtend, PrimitiveInt, UNETLoader, WanSoundImageToVideo, AudioEncoderLoader, ImageResizeKJv2, LoraLoaderModelOnly, KSampler, LatentConcat, KSampler, LatentConcat, MarkdownNote, Note, AudioEncoderEncode, AudioCrop, ImageFromBatch, WanSoundImageToVideoExtend, WanSoundImageToVideoExtend, KSampler, LatentConcat, PrimitiveInt, WanSoundImageToVideoExtend, Note, CreateVideo, SaveVideo, LoadImage, LoadAudio, AudioEncoderEncode, MarkdownNote, MarkdownNote, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveFloat, LoadAudio, VHS_VideoCombine, AudioCrop, CLIPTextEncode, Fast Groups Bypasser (rgthree), UNETLoader, LoadImage, ImageResizeKJv2, CLIPTextEncode, MarkdownNote, Text Multiline, PrimitiveInt, PrimitiveInt, LatentConcat, Note, LatentCut, LatentConcat, VAEDecode, KSampler, LatentConcat, WanSoundImageToVideoExtend, ImageFromBatch, CreateVideo, VHS_VideoCombine, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1, "steps": 10}
---

# 视频生成/图生视频/满血版Wan2.2-S2V最新修复版-ComfyUI_1961703207414251521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961703207414251521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `LatentConcat`
- `LatentCut`
- `Note`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveFloat`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `AudioEncoderLoader`
- `KSampler` ★核心
- `WanSoundImageToVideo`
- `ModelSamplingSD3`
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `KSampler` ★核心
- `LatentConcat`
- `WanSoundImageToVideoExtend`
- `KSampler` ★核心
- `WanSoundImageToVideoExtend`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `WanSoundImageToVideo`
- `AudioEncoderLoader`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LatentConcat`
- `KSampler` ★核心
- `LatentConcat`
- `MarkdownNote`
- `Note`
- `AudioEncoderEncode`
- `AudioCrop`
- `ImageFromBatch`
- `WanSoundImageToVideoExtend`
- `WanSoundImageToVideoExtend`
- `KSampler` ★核心
- `LatentConcat`
- `PrimitiveInt`
- `WanSoundImageToVideoExtend`
- `Note`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `LoadAudio`
- `AudioEncoderEncode`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LoadAudio`
- `VHS_VideoCombine`
- `AudioCrop`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `Text Multiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `LatentConcat`
- `Note`
- `LatentCut`
- `LatentConcat`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LatentConcat`
- `WanSoundImageToVideoExtend`
- `ImageFromBatch`
- `CreateVideo`
- `VHS_VideoCombine`
- `SaveVideo`

## 关键参数

- `seed` = `1`
- `steps` = `10`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（62/84）

**有卡**：`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`LatentConcat`、`LatentCut`、`AudioEncoderLoader`、`KSampler`、`WanSoundImageToVideo`、`WanSoundImageToVideoExtend`、`UNETLoader`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`AudioEncoderEncode`、`AudioCrop`、`ImageFromBatch`、`CreateVideo`、`SaveVideo`、`LoadImage`、`LoadAudio`、`VHS_VideoCombine`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
