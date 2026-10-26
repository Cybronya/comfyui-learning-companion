---
key: 数字人/数字人/ltx2.3数字人_2029843228320600065.json
name: ltx2.3数字人_2029843228320600065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/ltx2.3数字人_2029843228320600065.json
hash: 1b25c49ee1493612
coverage: 0.833333
learned_at: 2026-10-26 01:59:05
nodes: [VAEDecode, LTXVConcatAVLatent, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVAudioVAELoader, GetImageSize, LTXVAudioVAEEncode, ImagePadForOutpaint, PreviewImage, MelBandRoFormerSampler, SimpleMath+, easy showAnything, Audio Duration (mtb), ImageResizeKJv2, LTXVConditioning, CheckpointLoaderSimple, VHS_VideoCombine, CLIPTextEncode, PreviewAudio, MarkdownNote, CLIPTextEncode, LoadImage, Fast Groups Bypasser (rgthree), LoadAudio, TrimAudioDuration, MarkdownNote, MarkdownNote, SolidMask, SetLatentNoiseMask, GetImageSize, EmptyImage, LTXAVTextEncoderLoader, LoraLoaderModelOnly, KSampler, MelBandRoFormerModelLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 147746554818774, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/ltx2.3数字人_2029843228320600065.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/ltx2.3数字人_2029843228320600065.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVAudioVAELoader`
- `GetImageSize`
- `LTXVAudioVAEEncode` ★核心
- `ImagePadForOutpaint`
- `PreviewImage`
- `MelBandRoFormerSampler` ★核心
- `SimpleMath+`
- `easy showAnything`
- `Audio Duration (mtb)`
- `ImageResizeKJv2`
- `LTXVConditioning`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `PreviewAudio`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `TrimAudioDuration`
- `MarkdownNote`
- `MarkdownNote`
- `SolidMask`
- `SetLatentNoiseMask`
- `GetImageSize`
- `EmptyImage`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `MelBandRoFormerModelLoader`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `147746554818774`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`VAEDecode`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVAudioVAELoader`、`GetImageSize`、`LTXVAudioVAEEncode`、`ImagePadForOutpaint`、`MelBandRoFormerSampler`、`SimpleMath+`、`Audio Duration (mtb)`、`ImageResizeKJv2`、`LTXVConditioning`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`CLIPTextEncode`、`PreviewAudio`、`LoadImage`、`LoadAudio`、`TrimAudioDuration`、`SolidMask`、`SetLatentNoiseMask`、`EmptyImage`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`KSampler`、`MelBandRoFormerModelLoader`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、MelBandRoFormerSampler、LTXVConcatAVLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
