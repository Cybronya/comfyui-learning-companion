---
key: 平台全量/Ltx2.3视频配音+自定义音频_2080289592082784257.json
name: Ltx2.3视频配音+自定义音频_2080289592082784257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Ltx2.3视频配音+自定义音频_2080289592082784257.json
hash: 0275f5e7e1ba5025
coverage: 0.888889
learned_at: 2026-11-14 00:39:30
nodes: [PainterFrameExtractor, PainterLTX2Vomni, EmptyLTXVLatentVideo, VHS_GetImageCount, LTXVConcatAVLatent, VHS_VideoInfo, VAEDecodeTiled, LTXVCropGuides, LTXVAudioVAEDecode, LayerUtility: PurgeVRAM V2, LTXVSeparateAVLatent, CLIPTextEncode, PromptRelayEncode, KSamplerAdvanced, VHS_VideoCombine, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, RIFEInterpolation, SimpleMath+, TrimAudioDuration, MelBandRoFormerSampler, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, PrimitiveInt, SimpleMath+, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadAudio, VHS_LoadVideo, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, MelBandRoFormerModelLoader]
patterns: []
missing: []
parameters: {"cfg": 9, "denoise": "linear_quadratic", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 平台全量/Ltx2.3视频配音+自定义音频_2080289592082784257.json

> 来源文件 `comfyui_library/workflows/平台全量/Ltx2.3视频配音+自定义音频_2080289592082784257.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `PainterFrameExtractor`
- `PainterLTX2Vomni`
- `EmptyLTXVLatentVideo`
- `VHS_GetImageCount`
- `LTXVConcatAVLatent`
- `VHS_VideoInfo`
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `PromptRelayEncode`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `RIFEInterpolation`
- `SimpleMath+`
- `TrimAudioDuration`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `PrimitiveInt`
- `SimpleMath+`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadAudio`
- `VHS_LoadVideo`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `MelBandRoFormerModelLoader`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `linear_quadratic`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`PainterFrameExtractor`、`PainterLTX2Vomni`、`EmptyLTXVLatentVideo`、`VHS_GetImageCount`、`LTXVConcatAVLatent`、`VHS_VideoInfo`、`VAEDecodeTiled`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LayerUtility: PurgeVRAM V2`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`PromptRelayEncode`、`KSamplerAdvanced`、`VHS_VideoCombine`、`RIFEInterpolation`、`SimpleMath+`、`TrimAudioDuration`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadAudio`、`VHS_LoadVideo`、`VAELoaderKJ`、`DualCLIPLoader`、`MelBandRoFormerModelLoader`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、KSamplerAdvanced、MelBandRoFormerSampler、EmptyLTXVLatentVideo、LTXVAudioVAEDecode、LTXVAudioVAEEncode
