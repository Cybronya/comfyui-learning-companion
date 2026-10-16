---
key: 视频生成/图生视频/Ltx2.3视频配音+自定义音频_2080444148519362561.json
name: Ltx2.3视频配音+自定义音频_2080444148519362561.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2080444148519362561.json
hash: 27c02ed08bb3124e
coverage: 0.866667
learned_at: 2026-10-15 22:42:13
nodes: [PainterFrameExtractor, EmptyLTXVLatentVideo, VHS_GetImageCount, LTXVConcatAVLatent, LTXVCropGuides, LayerUtility: PurgeVRAM V2, LTXVSeparateAVLatent, CLIPTextEncode, PrimitiveInt, PrimitiveInt, RIFEInterpolation, TrimAudioDuration, MelBandRoFormerSampler, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, PrimitiveInt, SimpleMath+, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadAudio, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, MelBandRoFormerModelLoader, PromptRelayEncode, LTXVAudioVAEDecode, VHS_VideoInfo, SimpleMath+, PainterLTX2Vomni, KSamplerAdvanced, VAEDecodeTiled, TDQwen3TTSModelLoader, Apply Whisper, PreviewAny, MarkdownNote, Text, LoadAudio, SaveAudio, VHS_LoadVideo, PrimitiveStringMultiline, TDQwen3TTSVoiceClone, easy clearCacheAll, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 9, "denoise": "linear_quadratic", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Ltx2.3视频配音+自定义音频_2080444148519362561.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080444148519362561.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `PainterFrameExtractor`
- `EmptyLTXVLatentVideo`
- `VHS_GetImageCount`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LayerUtility: PurgeVRAM V2`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `RIFEInterpolation`
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
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `MelBandRoFormerModelLoader`
- `PromptRelayEncode`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoInfo`
- `SimpleMath+`
- `PainterLTX2Vomni`
- `KSamplerAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `TDQwen3TTSModelLoader`
- `Apply Whisper`
- `PreviewAny`
- `MarkdownNote`
- `Text`
- `LoadAudio`
- `SaveAudio`
- `VHS_LoadVideo`
- `PrimitiveStringMultiline`
- `TDQwen3TTSVoiceClone`
- `easy clearCacheAll`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `linear_quadratic`

## 知识

覆盖率 **87%**（39/45）

**有卡**：`PainterFrameExtractor`、`EmptyLTXVLatentVideo`、`VHS_GetImageCount`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LayerUtility: PurgeVRAM V2`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`RIFEInterpolation`、`TrimAudioDuration`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`SimpleMath+`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadAudio`、`VAELoaderKJ`、`DualCLIPLoader`、`MelBandRoFormerModelLoader`、`PromptRelayEncode`、`LTXVAudioVAEDecode`、`VHS_VideoInfo`、`PainterLTX2Vomni`、`KSamplerAdvanced`、`VAEDecodeTiled`、`TDQwen3TTSModelLoader`、`Apply Whisper`、`Text`、`SaveAudio`、`VHS_LoadVideo`、`TDQwen3TTSVoiceClone`、`easy clearCacheAll`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、KSamplerAdvanced、MelBandRoFormerSampler、LTXVConcatAVLatent、LTXVSeparateAVLatent、SetLatentNoiseMask
