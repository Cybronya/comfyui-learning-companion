---
key: 视频生成/图生视频/(官方版)Wan2.2 S2V数字人骨骼驱动视频工作流V1_1961257200578707457.json
name: (官方版)Wan2.2 S2V数字人骨骼驱动视频工作流V1_1961257200578707457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(官方版)Wan2.2 S2V数字人骨骼驱动视频工作流V1_1961257200578707457.json
hash: 7e3e960796e3f249
coverage: 0.857143
learned_at: 2026-10-15 22:31:28
nodes: [CLIPTextEncode, AudioEncoderEncode, AudioEncoderLoader, CR Float To Integer, ModelSamplingSD3, PathchSageAttentionKJ, wanBlockSwap, UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAELoader, AudioCropProcessUTK, PreviewAudio, ContextWindowsManual, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, SimpleMath+, PreviewImage, WanSoundImageToVideo, LoadImage, JWInteger, LoadAudio, JWFloat, Note, Note, Note, Note, VHS_VideoCombine, VAEDecode, ImageFromBatch+, OpenposePreprocessor, KSampler, SaveLatent, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1736, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/(官方版)Wan2.2 S2V数字人骨骼驱动视频工作流V1_1961257200578707457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961257200578707457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `CLIPTextEncode` ★核心
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CR Float To Integer`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `AudioCropProcessUTK`
- `PreviewAudio`
- `ContextWindowsManual`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `PreviewImage`
- `WanSoundImageToVideo`
- `LoadImage`
- `JWInteger`
- `LoadAudio`
- `JWFloat`
- `Note`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `OpenposePreprocessor`
- `KSampler` ★核心
- `SaveLatent`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1736`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`CLIPTextEncode`、`AudioEncoderEncode`、`AudioEncoderLoader`、`CR Float To Integer`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`wanBlockSwap`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`AudioCropProcessUTK`、`PreviewAudio`、`ContextWindowsManual`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`WanSoundImageToVideo`、`LoadImage`、`JWInteger`、`LoadAudio`、`JWFloat`、`VHS_VideoCombine`、`VAEDecode`、`ImageFromBatch+`、`OpenposePreprocessor`、`KSampler`、`SaveLatent`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
