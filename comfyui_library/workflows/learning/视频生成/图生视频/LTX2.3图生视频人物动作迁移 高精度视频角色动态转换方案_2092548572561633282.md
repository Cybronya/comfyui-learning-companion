---
key: 视频生成/图生视频/LTX2.3图生视频人物动作迁移 高精度视频角色动态转换方案_2092548572561633282.json
name: LTX2.3图生视频人物动作迁移 高精度视频角色动态转换方案_2092548572561633282
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频人物动作迁移 高精度视频角色动态转换方案_2092548572561633282.json
hash: e451b5d3cac4d5c3
coverage: 0.939024
learned_at: 2026-10-16 22:59:03
nodes: [LTXVConditioning, LTXVConcatAVLatent, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVCropGuides, LTXVSeparateAVLatent, DWPreprocessor, LTXVAudioVAELoader, CheckpointLoaderSimple, CLIPTextEncode, CFGGuider, GetVideoComponents, ImageScale, GetImageSize, SimpleMath+, PrimitiveBoolean, RandomNoise, ImageScale, KSamplerSelect, CLIPTextEncode, CannyEdgePreprocessor, LoraLoaderModelOnly, LTXVTiledVAEDecode, LTXVAudioVAEDecode, LTXFloatToInt, ImageScale, MaskToImage, LTXVDilateVideoMask, ImageScale, GetVideoComponents, ImageToMask, LoadVideo, LoadVideo, LoadImage, LTXAVTextEncoderLoader, LTXICLoRALoaderModelOnly, GemmaAPITextEncode, PrimitiveString, GemmaAPITextEncode, ManualSigmas, LTXAddVideoICLoRAGuide, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTXVLaplacianPyramidBlend, CreateVideo, SaveVideo, ImageScale, ImageToMask, GetImageSize, ComfyMathExpression, ComfyMathExpression, ImageScale, LTXAddVideoICLoRAGuide, GetVideoComponents, LoadVideo, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3图生视频人物动作迁移 高精度视频角色动态转换方案_2092548572561633282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频人物动作迁移 高精度视频角色动态转换方案_2092548572561633282.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **94%**（77/82）

**有卡**：`LTXVConditioning`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`DWPreprocessor`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`CFGGuider`、`GetVideoComponents`、`ImageScale`、`GetImageSize`、`SimpleMath+`、`PrimitiveBoolean`、`RandomNoise`、`KSamplerSelect`、`CannyEdgePreprocessor`、`LoraLoaderModelOnly`、`LTXVTiledVAEDecode`、`LTXVAudioVAEDecode`、`LTXFloatToInt`、`MaskToImage`、`LTXVDilateVideoMask`、`ImageToMask`、`LoadVideo`、`LoadImage`、`LTXAVTextEncoderLoader`、`LTXICLoRALoaderModelOnly`、`GemmaAPITextEncode`、`ManualSigmas`、`LTXAddVideoICLoRAGuide`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTXVLaplacianPyramidBlend`、`CreateVideo`、`SaveVideo`、`ComfyMathExpression`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
