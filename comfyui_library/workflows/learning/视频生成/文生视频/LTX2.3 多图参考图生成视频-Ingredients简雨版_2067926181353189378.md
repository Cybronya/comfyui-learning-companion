---
key: 视频生成/文生视频/LTX2.3 多图参考图生成视频-Ingredients简雨版_2067926181353189378.json
name: LTX2.3 多图参考图生成视频-Ingredients简雨版_2067926181353189378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 多图参考图生成视频-Ingredients简雨版_2067926181353189378.json
hash: 583af97eaeae9094
coverage: 0.535714
learned_at: 2026-10-15 22:44:59
nodes: [LoraLoaderModelOnly, SetNode, LTXICLoRALoaderModelOnly, SetNode, VAELoaderKJ, Note, RepeatImageBatch, SetNode, LTXVAudioVAELoader, SetNode, PrimitiveFloat, SimpleCalculatorKJ, SetNode, Note, easy showAnything, Note, LTXVConditioning, GetNode, GetNode, GetNode, SetNode, SetNode, Note, LTXVImgToVideoConditionOnly, GetNode, GetNode, LTXAddVideoICLoRAGuide, GetNode, GetNode, GetNode, GetNode, CFGGuider, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, CreateVideo, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXFloatToInt, GetNode, GetNode, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, ManualSigmas, Note, Note, CLIPTextEncode, LTXVSeparateAVLatent, LTXVTiledVAEDecode, LTXVCropGuides, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, GetVideoComponents, CreateVideo, LoadImage, ImageBatchMultiple+, ResizeImageMaskNode, SaveVideo, ImageConcatFromBatch, PrimitiveFloat, EmptyLTXVLatentVideo, GetImageSize, LoadImage, LoadImage, LoadImage, LTXVPreprocess, INTConstant, GetNode, LoadImage, DualCLIPLoaderGGUF, UnetLoaderGGUFAdvanced, UNETLoader, LTXAVTextEncoderLoader, PreviewImage, LoadImage, easy positive]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/文生视频/LTX2.3 多图参考图生成视频-Ingredients简雨版_2067926181353189378.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 多图参考图生成视频-Ingredients简雨版_2067926181353189378.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `SetNode`
- `VAELoaderKJ`
- `Note`
- `RepeatImageBatch`
- `SetNode`
- `LTXVAudioVAELoader`
- `SetNode`
- `PrimitiveFloat`
- `SimpleCalculatorKJ`
- `SetNode`
- `Note`
- `easy showAnything`
- `Note`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXFloatToInt`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode` ★核心
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetVideoComponents`
- `CreateVideo`
- `LoadImage`
- `ImageBatchMultiple+`
- `ResizeImageMaskNode`
- `SaveVideo`
- `ImageConcatFromBatch`
- `PrimitiveFloat`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LTXVPreprocess`
- `INTConstant`
- `GetNode`
- `LoadImage`
- `DualCLIPLoaderGGUF`
- `UnetLoaderGGUFAdvanced` ★核心
- `UNETLoader` ★核心
- `LTXAVTextEncoderLoader`
- `PreviewImage`
- `LoadImage`
- `easy positive`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **54%**（45/84）

**有卡**：`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`VAELoaderKJ`、`RepeatImageBatch`、`LTXVAudioVAELoader`、`SimpleCalculatorKJ`、`LTXVConditioning`、`LTXVImgToVideoConditionOnly`、`LTXAddVideoICLoRAGuide`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`CreateVideo`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXFloatToInt`、`LTXVEmptyLatentAudio`、`ManualSigmas`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`LTXVTiledVAEDecode`、`LTXVCropGuides`、`GetVideoComponents`、`LoadImage`、`ImageBatchMultiple+`、`ResizeImageMaskNode`、`SaveVideo`、`ImageConcatFromBatch`、`EmptyLTXVLatentVideo`、`GetImageSize`、`LTXVPreprocess`、`INTConstant`、`DualCLIPLoaderGGUF`、`UnetLoaderGGUFAdvanced`、`UNETLoader`、`LTXAVTextEncoderLoader`、`easy positive`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
