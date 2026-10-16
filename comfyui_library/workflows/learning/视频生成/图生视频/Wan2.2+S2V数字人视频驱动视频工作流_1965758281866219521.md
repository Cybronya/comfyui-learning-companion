---
key: 视频生成/图生视频/Wan2.2+S2V数字人视频驱动视频工作流_1965758281866219521.json
name: Wan2.2+S2V数字人视频驱动视频工作流_1965758281866219521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1965758281866219521.json
hash: 0ec0ba5a6ffa2cc2
coverage: 0.875
learned_at: 2026-10-15 22:31:38
nodes: [Note, Note, LayerUtility: PurgeVRAM V2, ModelSamplingSD3, PreviewAudio, Note, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VHS_VideoCombine, PreviewImage, AudioCropProcessUTK, JWFloat, KSampler, CR Float To Integer, UnetLoaderGGUF, PathchSageAttentionKJ, wanBlockSwap, LoraLoaderModelOnly, CLIPTextEncode, ContextWindowsManual, ImageFromBatch+, AudioEncoderEncode, SimpleMath+, VHS_LoadVideo, LoadImage, LoadAudio, VAEDecode, WanSoundImageToVideo, VAELoader, CLIPTextEncode, CLIPLoader, AudioEncoderLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1736, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2+S2V数字人视频驱动视频工作流_1965758281866219521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1965758281866219521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `Note`
- `Note`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingSD3`
- `PreviewAudio`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VHS_VideoCombine`
- `PreviewImage`
- `AudioCropProcessUTK`
- `JWFloat`
- `KSampler` ★核心
- `CR Float To Integer`
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ContextWindowsManual`
- `ImageFromBatch+`
- `AudioEncoderEncode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadAudio`
- `VAEDecode` ★核心
- `WanSoundImageToVideo`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `AudioEncoderLoader`

## 关键参数

- `seed` = `1736`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`LayerUtility: PurgeVRAM V2`、`ModelSamplingSD3`、`PreviewAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`VHS_VideoCombine`、`AudioCropProcessUTK`、`JWFloat`、`KSampler`、`CR Float To Integer`、`UnetLoaderGGUF`、`PathchSageAttentionKJ`、`wanBlockSwap`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ContextWindowsManual`、`ImageFromBatch+`、`AudioEncoderEncode`、`SimpleMath+`、`VHS_LoadVideo`、`LoadImage`、`LoadAudio`、`VAEDecode`、`WanSoundImageToVideo`、`VAELoader`、`CLIPLoader`、`AudioEncoderLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、AudioEncoderLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
