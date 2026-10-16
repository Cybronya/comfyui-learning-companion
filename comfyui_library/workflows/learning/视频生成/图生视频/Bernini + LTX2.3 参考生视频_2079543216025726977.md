---
key: 视频生成/图生视频/Bernini + LTX2.3 参考生视频_2079543216025726977.json
name: Bernini + LTX2.3 参考生视频_2079543216025726977.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2079543216025726977.json
hash: e60d870e3deb77d2
coverage: 0.714286
learned_at: 2026-10-15 22:42:04
nodes: [CLIPTextEncode, CLIPTextEncode, SamplerCustom, KSamplerSelect, easy promptConcat, PrimitiveStringMultiline, PrimitiveFloat, SamplerCustom, LTXVCropGuides, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VAELoaderKJ, Reroute, Reroute, PainterFrameExtractor, RIFEInterpolation, LayerUtility: PurgeVRAM V2, SplitSigmas, BasicScheduler, PrimitiveStringMultiline, DualCLIPLoader, easy promptConcat, Note, Note, PromptRelayEncode, CLIPTextEncode, SimpleMath+, PrimitiveInt, SimpleMath+, VHS_GetImageCount, LTXVConcatAVLatent, VAELoaderKJ, VAEDecodeTiled, SimpleComparison+, PrimitiveInt, SimpleComparison+, SimpleComparison+, PrimitiveInt, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, LTXVEmptyLatentAudio, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPLoader, VAELoader, UNETLoader, LoadImage, LoadImage, PrimitiveInt, easy ifElse, BerniniConditioning, PainterLTX2Vomni, PrimitiveInt, easy ifElse, easy ifElse, EmptyLTXVLatentVideo, KSamplerAdvanced, VAEDecodeTiled, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 9, "denoise": "linear_quadratic", "height": 30, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 1}
---

# 视频生成/图生视频/Bernini + LTX2.3 参考生视频_2079543216025726977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079543216025726977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（63 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `SamplerCustom` ★核心
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VAELoaderKJ`
- `Reroute`
- `Reroute`
- `PainterFrameExtractor`
- `RIFEInterpolation`
- `LayerUtility: PurgeVRAM V2`
- `SplitSigmas`
- `BasicScheduler`
- `PrimitiveStringMultiline`
- `DualCLIPLoader`
- `easy promptConcat`
- `Note`
- `Note`
- `PromptRelayEncode`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `PrimitiveInt`
- `SimpleMath+`
- `VHS_GetImageCount`
- `LTXVConcatAVLatent`
- `VAELoaderKJ`
- `VAEDecodeTiled` ★核心
- `SimpleComparison+`
- `PrimitiveInt`
- `SimpleComparison+`
- `SimpleComparison+`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `LTXVEmptyLatentAudio` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `easy ifElse`
- `BerniniConditioning`
- `PainterLTX2Vomni`
- `PrimitiveInt`
- `easy ifElse`
- `easy ifElse`
- `EmptyLTXVLatentVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1`
- `height` = `30`
- `batch_size` = `1`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `linear_quadratic`

## 知识

覆盖率 **71%**（45/63）

**有卡**：`CLIPTextEncode`、`SamplerCustom`、`KSamplerSelect`、`easy promptConcat`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAELoaderKJ`、`PainterFrameExtractor`、`RIFEInterpolation`、`LayerUtility: PurgeVRAM V2`、`SplitSigmas`、`BasicScheduler`、`DualCLIPLoader`、`PromptRelayEncode`、`SimpleMath+`、`VHS_GetImageCount`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`SimpleComparison+`、`VHS_VideoCombine`、`LTXVEmptyLatentAudio`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`BerniniConditioning`、`PainterLTX2Vomni`、`EmptyLTXVLatentVideo`、`KSamplerAdvanced`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、KSamplerSelect
