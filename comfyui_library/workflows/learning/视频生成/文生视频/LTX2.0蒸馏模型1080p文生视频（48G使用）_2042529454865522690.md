---
key: 视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2042529454865522690.json
name: LTX2.0蒸馏模型1080p文生视频（48G使用）_2042529454865522690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2042529454865522690.json
hash: 2970ab10c8131daf
coverage: 0.777778
learned_at: 2026-10-15 22:44:55
nodes: [MarkdownNote, SaveVideo, MarkdownNote, MarkdownNote, b7c2d337-c38d-4c04-922b-2d638449d13e, PrimitiveInt, PrimitiveFloat, LTXVEmptyLatentAudio, ImageScaleBy, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, RandomNoise, EmptyLTXVLatentVideo, CFGGuider, KSamplerSelect, GetImageSize, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, CFGGuider, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, LTXVConditioning, CLIPTextEncode, MarkdownNote, PrimitiveInt, LTXVLatentUpsampler, SamplerCustomAdvanced, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVAudioVAEDecode, VAEDecodeTiled, VHS_VideoCombine, LTXVSeparateAVLatent, VHS_VideoCombine, RandomNoise, CheckpointLoaderSimple, EmptyImage, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-distilled-fp8.safetensors", "height": 25, "width": 121}
---

# 视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2042529454865522690.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2042529454865522690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `MarkdownNote`
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `b7c2d337-c38d-4c04-922b-2d638449d13e`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `EmptyLTXVLatentVideo`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `GetImageSize`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `PrimitiveInt`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAELoader`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `EmptyImage`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **78%**（35/45）

**有卡**：`SaveVideo`、`b7c2d337-c38d-4c04-922b-2d638449d13e`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`ManualSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`RandomNoise`、`EmptyLTXVLatentVideo`、`CFGGuider`、`KSamplerSelect`、`GetImageSize`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVAudioVAELoader`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`EmptyImage`、`LoraLoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
