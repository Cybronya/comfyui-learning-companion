---
key: 平台全量/LTX2.3 视频配音_2080277383072014337.json
name: LTX2.3 视频配音_2080277383072014337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3 视频配音_2080277383072014337.json
hash: db090cdcb9a1efcf
coverage: 0.892857
learned_at: 2026-11-14 00:37:48
nodes: [LTXVConcatAVLatent, CLIPTextEncode, LTXVAudioVAEDecode, EmptyLTXVLatentVideo, LTXVCropGuides, LTXVSeparateAVLatent, VAEDecodeTiled, VHS_GetImageCount, PainterLTX2Vomni, PainterFrameExtractor, RIFEInterpolation, KSamplerAdvanced, SimpleMath+, PromptRelayEncode, PrimitiveInt, PrimitiveInt, LTXVEmptyLatentAudio, VHS_VideoInfo, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, PrimitiveStringMultiline, VHS_LoadVideo, VHS_VideoCombine, LayerUtility: PurgeVRAM V2]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 9, "denoise": "linear_quadratic", "height": 30, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 1}
---

# 平台全量/LTX2.3 视频配音_2080277383072014337.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3 视频配音_2080277383072014337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（28 个）：
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `VHS_GetImageCount`
- `PainterLTX2Vomni`
- `PainterFrameExtractor`
- `RIFEInterpolation`
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `PromptRelayEncode`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `VHS_VideoInfo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `linear_quadratic`
- `width` = `1`
- `height` = `30`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`VHS_GetImageCount`、`PainterLTX2Vomni`、`PainterFrameExtractor`、`RIFEInterpolation`、`KSamplerAdvanced`、`SimpleMath+`、`PromptRelayEncode`、`LTXVEmptyLatentAudio`、`VHS_VideoInfo`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`DualCLIPLoader`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、KSamplerAdvanced、EmptyLTXVLatentVideo、LTXVAudioVAEDecode、LTXVConcatAVLatent、LTXVEmptyLatentAudio
