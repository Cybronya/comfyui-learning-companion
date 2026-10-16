---
key: 视频生成/图生视频/首尾帧双帧对口型数字人——Wan2.2 与 Qwen3TTS 的破壁合奏！_2016877597203894274.json
name: 首尾帧双帧对口型数字人——Wan2.2 与 Qwen3TTS 的破壁合奏！_2016877597203894274.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2016877597203894274.json
hash: a3d70db964b1d21c
coverage: 0.895833
learned_at: 2026-10-15 22:34:44
nodes: [KSamplerAdvanced, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, MathExpression|pysssss, MathExpression|pysssss, PainterAI2V, JjkText, LoadAudio, LoadImage, LoadImage, PathchSageAttentionKJ, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, wanBlockSwap, UNETLoader, UNETLoader, ModelSamplingSD3, Qwen3TTSVoiceClone, Qwen3TTSModelLoader, AudioSeparation, SaveAudioMP3, Audio Duration (mtb), easy showAnything, PainterAudioCut, PreviewAny, CR Prompt Text, VAELoader, AudioEncoderEncode, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, KSamplerAdvanced, VAEDecode, GetImageSizeAndCount, MathExpression|pysssss, PreviewImage, ImageFromBatch, ImageConcanate, ImageConcanate, CLIPTextEncode, VHS_VideoCombine, ModelPatchLoader, PreviewImage, ColorMatch, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧双帧对口型数字人——Wan2.2 与 Qwen3TTS 的破壁合奏！_2016877597203894274.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016877597203894274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `KSamplerAdvanced` ★核心
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PainterAI2V`
- `JjkText`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `Qwen3TTSVoiceClone`
- `Qwen3TTSModelLoader`
- `AudioSeparation`
- `SaveAudioMP3`
- `Audio Duration (mtb)`
- `easy showAnything`
- `PainterAudioCut`
- `PreviewAny`
- `CR Prompt Text`
- `VAELoader`
- `AudioEncoderEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `PreviewImage`
- `ImageFromBatch`
- `ImageConcanate`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `ModelPatchLoader`
- `PreviewImage`
- `ColorMatch`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（43/48）

**有卡**：`KSamplerAdvanced`、`AudioEncoderLoader`、`CLIPLoader`、`CLIPTextEncode`、`MathExpression|pysssss`、`PainterAI2V`、`LoadAudio`、`LoadImage`、`PathchSageAttentionKJ`、`wanBlockSwap`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`UNETLoader`、`Qwen3TTSVoiceClone`、`Qwen3TTSModelLoader`、`AudioSeparation`、`SaveAudioMP3`、`Audio Duration (mtb)`、`PainterAudioCut`、`CR Prompt Text`、`VAELoader`、`AudioEncoderEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`VAEDecode`、`GetImageSizeAndCount`、`ImageFromBatch`、`ImageConcanate`、`VHS_VideoCombine`、`ModelPatchLoader`、`ColorMatch`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
