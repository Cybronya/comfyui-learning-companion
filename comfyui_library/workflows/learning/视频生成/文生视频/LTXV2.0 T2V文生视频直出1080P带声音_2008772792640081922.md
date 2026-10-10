---
key: 视频生成/文生视频/LTXV2.0 T2V文生视频直出1080P带声音_2008772792640081922.json
name: LTXV2.0 T2V文生视频直出1080P带声音_2008772792640081922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTXV2.0 T2V文生视频直出1080P带声音_2008772792640081922.json
hash: 4a799ab79819f6b2
coverage: 0.833333
learned_at: 2026-10-11 03:07:10
nodes: [ManualSigmas, VAEDecode, CFGGuider, MarkdownNote, KSamplerSelect, KSamplerSelect, MarkdownNote, RandomNoise, LTXVConcatAVLatent, LoraLoaderModelOnly, Reroute, LTXVLatentUpsampler, LTXVCropGuides, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, ImageScaleBy, LTXVConditioning, SamplerCustomAdvanced, CheckpointLoaderSimple, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVAudioVAELoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, PrimitiveInt, LTXAVTextEncoderLoader, VHS_VideoCombine, CFGGuider, LoraLoaderModelOnly, LTXVScheduler, RandomNoise, LoraLoaderModelOnly, LTXVAudioVAEDecode, VAEDecode, VHS_VideoCombine, EmptyImage, PrimitiveInt, PrimitiveFloat, LoraLoaderModelOnly, MarkdownNote, CLIPTextEncode, RH_Translator, CR SDXL Aspect Ratio, CLIPTextEncode]
patterns: []
missing: [CR SDXL Aspect Ratio]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTXV2.0 T2V文生视频直出1080P带声音_2008772792640081922.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTXV2.0 T2V文生视频直出1080P带声音_2008772792640081922.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（48 个）：
- `ManualSigmas`
- `VAEDecode` ★核心
- `CFGGuider`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LatentUpscaleModelLoader`
- `ImageScaleBy`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAELoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `LTXAVTextEncoderLoader`
- `VHS_VideoCombine`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `EmptyImage`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `CR SDXL Aspect Ratio`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **83%**（40/48）

**有卡**：`ManualSigmas`、`VAEDecode`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`ImageScaleBy`、`LTXVConditioning`、`SamplerCustomAdvanced`、`CheckpointLoaderSimple`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`VAEDecodeTiled`、`LTXAVTextEncoderLoader`、`VHS_VideoCombine`、`LTXVScheduler`、`EmptyImage`、`CLIPTextEncode`、`RH_Translator`

**缺卡**（1）：`CR SDXL Aspect Ratio`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
