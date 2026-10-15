---
key: 视频生成/文生视频/LTXV2.0文生视频-点PLUS运行_2009517391662813186.json
name: LTXV2.0文生视频-点PLUS运行_2009517391662813186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTXV2.0文生视频-点PLUS运行_2009517391662813186.json
hash: 6c7a1ab845937916
coverage: 0.773585
learned_at: 2026-10-15 22:45:18
nodes: [GetImageSize, MarkdownNote, KSamplerSelect, LTXVConditioning, SamplerCustomAdvanced, KSamplerSelect, Reroute, Reroute, LTXVScheduler, LTXVConcatAVLatent, MarkdownNote, CLIPTextEncode, LTXVSeparateAVLatent, Reroute, Reroute, Reroute, VAEDecodeTiled, LTXVAudioVAEDecode, RandomNoise, CFGGuider, CFGGuider, ImageScaleBy, EmptyImage, PrimitiveInt, PrimitiveFloat, EmptyLTXVLatentVideo, PrimitiveInt, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LatentUpscaleModelLoader, ManualSigmas, RandomNoise, LTXVAudioVAEDecode, VAEDecodeTiled, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, LTXVAudioVAELoader, CLIPTextEncode, VHS_VideoCombine, VRAMReserver, LTXAVTextEncoderLoader, CR Text, CR Text, easy showAnything, RH_LLMAPI_NODE, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTXV2.0文生视频-点PLUS运行_2009517391662813186.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTXV2.0文生视频-点PLUS运行_2009517391662813186.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（53 个）：
- `GetImageSize`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `Reroute`
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `CFGGuider`
- `CFGGuider`
- `ImageScaleBy`
- `EmptyImage`
- `PrimitiveInt`
- `PrimitiveFloat`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VRAMReserver`
- `LTXAVTextEncoderLoader`
- `CR Text`
- `CR Text`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **77%**（41/53）

**有卡**：`GetImageSize`、`KSamplerSelect`、`LTXVConditioning`、`SamplerCustomAdvanced`、`LTXVScheduler`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`RandomNoise`、`CFGGuider`、`ImageScaleBy`、`EmptyImage`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`ManualSigmas`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`VRAMReserver`、`LTXAVTextEncoderLoader`、`CR Text`、`RH_LLMAPI_NODE`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
