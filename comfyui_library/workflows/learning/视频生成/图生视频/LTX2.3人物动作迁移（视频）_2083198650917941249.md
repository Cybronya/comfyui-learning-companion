---
key: 视频生成/图生视频/LTX2.3人物动作迁移（视频）_2083198650917941249.json
name: LTX2.3人物动作迁移（视频）_2083198650917941249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3人物动作迁移（视频）_2083198650917941249.json
hash: eeb7f383be10eadc
coverage: 0.964286
learned_at: 2026-10-16 19:17:11
nodes: [LTXVConditioning, LTXVConcatAVLatent, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVCropGuides, LTXVSeparateAVLatent, DWPreprocessor, LTXVAudioVAELoader, CheckpointLoaderSimple, CLIPTextEncode, CFGGuider, GetVideoComponents, ImageScale, GetImageSize, SimpleMath+, PrimitiveBoolean, RandomNoise, ImageScale, KSamplerSelect, CLIPTextEncode, CannyEdgePreprocessor, LoraLoaderModelOnly, LTXVTiledVAEDecode, LTXVAudioVAEDecode, LTXFloatToInt, ImageScale, MaskToImage, LTXVDilateVideoMask, ImageScale, Note, GetVideoComponents, ImageToMask, LoadVideo, LoadVideo, LoadImage, LTXAVTextEncoderLoader, LTXICLoRALoaderModelOnly, GemmaAPITextEncode, PrimitiveString, GemmaAPITextEncode, ManualSigmas, LTXAddVideoICLoRAGuide, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTXVLaplacianPyramidBlend, CreateVideo, SaveVideo, ImageScale, ImageToMask, GetImageSize, ComfyMathExpression, ComfyMathExpression, ImageScale, LTXAddVideoICLoRAGuide, GetVideoComponents, LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3人物动作迁移（视频）_2083198650917941249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3人物动作迁移（视频）_2083198650917941249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `DWPreprocessor`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `GetVideoComponents`
- `ImageScale`
- `GetImageSize`
- `SimpleMath+`
- `PrimitiveBoolean`
- `RandomNoise`
- `ImageScale`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `CannyEdgePreprocessor`
- `LoraLoaderModelOnly` ★核心
- `LTXVTiledVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXFloatToInt`
- `ImageScale`
- `MaskToImage`
- `LTXVDilateVideoMask`
- `ImageScale`
- `Note`
- `GetVideoComponents`
- `ImageToMask`
- `LoadVideo`
- `LoadVideo`
- `LoadImage`
- `LTXAVTextEncoderLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `GemmaAPITextEncode`
- `PrimitiveString`
- `GemmaAPITextEncode`
- `ManualSigmas`
- `LTXAddVideoICLoRAGuide`
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVLaplacianPyramidBlend`
- `CreateVideo`
- `SaveVideo`
- `ImageScale`
- `ImageToMask`
- `GetImageSize`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageScale`
- `LTXAddVideoICLoRAGuide`
- `GetVideoComponents`
- `LoadVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（54/56）

**有卡**：`LTXVConditioning`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`DWPreprocessor`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`CFGGuider`、`GetVideoComponents`、`ImageScale`、`GetImageSize`、`SimpleMath+`、`PrimitiveBoolean`、`RandomNoise`、`KSamplerSelect`、`CannyEdgePreprocessor`、`LoraLoaderModelOnly`、`LTXVTiledVAEDecode`、`LTXVAudioVAEDecode`、`LTXFloatToInt`、`MaskToImage`、`LTXVDilateVideoMask`、`ImageToMask`、`LoadVideo`、`LoadImage`、`LTXAVTextEncoderLoader`、`LTXICLoRALoaderModelOnly`、`GemmaAPITextEncode`、`ManualSigmas`、`LTXAddVideoICLoRAGuide`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTXVLaplacianPyramidBlend`、`CreateVideo`、`SaveVideo`、`ComfyMathExpression`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CannyEdgePreprocessor、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
