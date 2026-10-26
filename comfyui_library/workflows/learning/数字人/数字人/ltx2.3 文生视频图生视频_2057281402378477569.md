---
key: 数字人/数字人/ltx2.3 文生视频图生视频_2057281402378477569.json
name: ltx2.3 文生视频图生视频_2057281402378477569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/ltx2.3 文生视频图生视频_2057281402378477569.json
hash: e519b6228f60b80f
coverage: 0.90566
learned_at: 2026-10-26 01:59:05
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, Reroute, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVImgToVideoInplace, VAELoaderKJ, DualCLIPLoader, LTXVConcatAVLatent, ComfyMathExpression, VAELoaderKJ, MarkdownNote, LTXVImgToVideoInplace, CLIPTextEncode, RandomNoise, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, PrimitiveBoolean, LatentUpscaleModelLoader, CFGGuider, PrimitiveInt, SimpleMath+, SimpleMath+, LTXVEmptyLatentAudio, LTXVPreprocess, easy showAnything, SimpleMath+, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPTextEncode, LTXVConditioning, BasicScheduler, VisualizeSigmasKJ, CFGGuider, LTX2_NAG, ModelSamplingSD3, ManualSigmas, KSamplerSelect, VAEDecodeTiled, SaveImage, Vignette, LTXVAudioVAEDecode, ImageResizeKJv2, SaveVideoRGBA, LoadImage, PrimitiveStringMultiline, Int]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/ltx2.3 文生视频图生视频_2057281402378477569.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/ltx2.3 文生视频图生视频_2057281402378477569.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `VAELoaderKJ`
- `MarkdownNote`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `PrimitiveBoolean`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `PrimitiveInt`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `easy showAnything`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `CFGGuider`
- `LTX2_NAG`
- `ModelSamplingSD3`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `Vignette`
- `LTXVAudioVAEDecode` ★核心
- `ImageResizeKJv2`
- `SaveVideoRGBA`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Int`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（48/53）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`VAELoaderKJ`、`DualCLIPLoader`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`PrimitiveBoolean`、`LatentUpscaleModelLoader`、`CFGGuider`、`SimpleMath+`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`UNETLoader`、`LTXVConditioning`、`BasicScheduler`、`VisualizeSigmasKJ`、`LTX2_NAG`、`ModelSamplingSD3`、`VAEDecodeTiled`、`SaveImage`、`Vignette`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`SaveVideoRGBA`、`LoadImage`、`Int`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
