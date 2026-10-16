---
key: 视频生成/图生视频/首尾帧生视频（解禁模型）：LTX2.3 Sulphur_2064603463413223426.json
name: 首尾帧生视频（解禁模型）：LTX2.3 Sulphur_2064603463413223426.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064603463413223426.json
hash: 05cf1e620afb1833
coverage: 1
learned_at: 2026-10-15 22:39:27
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LTXAVTextEncoderLoader, CheckpointLoaderSimple, ModelPatchTorchSettings, LTXVConditioning, LTXVPreprocess, LTXVAddGuide, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVAudioVAELoader, RandomNoise, CFGGuider, SamplerEulerAncestral, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVAudioVAEDecode, VAEDecodeTiled, LoadImage, GetImageSize, LoadImage, ResizeImageMaskNode, ResizeImageMaskNode, LTXVPreprocess, EmptyLTXVLatentVideo, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "sulphur_dev_fp8mixed.safetensors", "height": 25, "width": 201}
---

# 视频生成/图生视频/首尾帧生视频（解禁模型）：LTX2.3 Sulphur_2064603463413223426.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064603463413223426.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（32 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `ModelPatchTorchSettings`
- `LTXVConditioning`
- `LTXVPreprocess`
- `LTXVAddGuide`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAudioVAELoader`
- `RandomNoise`
- `CFGGuider`
- `SamplerEulerAncestral` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `GetImageSize`
- `LoadImage`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `sulphur_dev_fp8mixed.safetensors`
- `width` = `201`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（32/32）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`ModelPatchTorchSettings`、`LTXVConditioning`、`LTXVPreprocess`、`LTXVAddGuide`、`LTXVEmptyLatentAudio`、`LTXVAudioVAELoader`、`RandomNoise`、`CFGGuider`、`SamplerEulerAncestral`、`ManualSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LoadImage`、`GetImageSize`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`CLIPTextEncode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVConcatAVLatent
