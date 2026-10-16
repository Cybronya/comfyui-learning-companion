---
key: 视频生成/图生视频/Bernini + LTX2.3 参考生视频+自定义音频_2079522335211745282.json
name: Bernini + LTX2.3 参考生视频+自定义音频_2079522335211745282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2079522335211745282.json
hash: f4f1d1084823c38f
coverage: 0.771429
learned_at: 2026-10-15 22:42:03
nodes: [CLIPTextEncode, SplitSigmas, KSamplerSelect, LoraLoaderModelOnly, BasicScheduler, SamplerCustom, CLIPTextEncode, PrimitiveFloat, SamplerCustom, BerniniConditioning, PrimitiveInt, easy promptConcat, easy promptConcat, PrimitiveStringMultiline, PrimitiveStringMultiline, SetLatentNoiseMask, MelBandRoFormerSampler, CLIPTextEncode, DualCLIPLoader, Fast Groups Bypasser (rgthree), Note, Note, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoadImage, LoadAudio, MelBandRoFormerModelLoader, SimpleComparison+, easy ifElse, LoadImage, VAELoaderKJ, SimpleMath+, LTXVSeparateAVLatent, LTXVAudioVAEDecode, PrimitiveStringMultiline, PainterFrameExtractor, LTXVAudioVAEEncode, TrimAudioDuration, LTXVCropGuides, VAELoaderKJ, LTXVConcatAVLatent, SolidMask, SimpleMath+, SimpleComparison+, PrimitiveInt, PrimitiveInt, VAEDecodeTiled, SimpleComparison+, PrimitiveInt, PrimitiveInt, easy ifElse, easy ifElse, PrimitiveStringMultiline, VHS_GetImageCount, RIFEInterpolation, PainterLTX2Vomni, VHS_VideoCombine, VHS_VideoCombine, EmptyLTXVLatentVideo, PromptRelayEncode, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, VAEDecodeTiled, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 9, "denoise": "linear_quadratic", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Bernini + LTX2.3 参考生视频+自定义音频_2079522335211745282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079522335211745282.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（70 个）：
- `CLIPTextEncode` ★核心
- `SplitSigmas`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `SamplerCustom` ★核心
- `BerniniConditioning`
- `PrimitiveInt`
- `easy promptConcat`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SetLatentNoiseMask`
- `MelBandRoFormerSampler` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `SimpleComparison+`
- `easy ifElse`
- `LoadImage`
- `VAELoaderKJ`
- `SimpleMath+`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveStringMultiline`
- `PainterFrameExtractor`
- `LTXVAudioVAEEncode` ★核心
- `TrimAudioDuration`
- `LTXVCropGuides`
- `VAELoaderKJ`
- `LTXVConcatAVLatent`
- `SolidMask`
- `SimpleMath+`
- `SimpleComparison+`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `SimpleComparison+`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy ifElse`
- `easy ifElse`
- `PrimitiveStringMultiline`
- `VHS_GetImageCount`
- `RIFEInterpolation`
- `PainterLTX2Vomni`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `EmptyLTXVLatentVideo`
- `PromptRelayEncode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecodeTiled` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `linear_quadratic`

## 知识

覆盖率 **77%**（54/70）

**有卡**：`CLIPTextEncode`、`SplitSigmas`、`KSamplerSelect`、`LoraLoaderModelOnly`、`BasicScheduler`、`SamplerCustom`、`BerniniConditioning`、`easy promptConcat`、`SetLatentNoiseMask`、`MelBandRoFormerSampler`、`DualCLIPLoader`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`LoadAudio`、`MelBandRoFormerModelLoader`、`SimpleComparison+`、`VAELoaderKJ`、`SimpleMath+`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`PainterFrameExtractor`、`LTXVAudioVAEEncode`、`TrimAudioDuration`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`SolidMask`、`VAEDecodeTiled`、`VHS_GetImageCount`、`RIFEInterpolation`、`PainterLTX2Vomni`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`PromptRelayEncode`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、KSamplerSelect
