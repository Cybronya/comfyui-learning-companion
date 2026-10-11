---
key: 视频生成/文生视频/LTX2.3 In​gredients IC LORA全能参考_2070747298736463873.json
name: LTX2.3 In​gredients IC LORA全能参考_2070747298736463873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 In​gredients IC LORA全能参考_2070747298736463873.json
hash: 2bad783e3ed4876a
coverage: 0.492958
learned_at: 2026-10-11 20:21:25
nodes: [LTXVConditioning, KSamplerSelect, LTXFloatToInt, PrimitiveBoolean, SetNode, ResizeImageMaskNode, CreateVideo, GetVideoComponents, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, ManualSigmas, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VAELoaderKJ, LTXVPreprocess, GetNode, Int, SetNode, LTXAVTextEncoderLoader, easy showAnything, RepeatImageBatch, GetNode, SimpleMath+, LTXVImgToVideoConditionOnly, GetImageSize, GetNode, LTXAddVideoICLoRAGuide, GetNode, SaveVideo, CLIPTextEncode, CLIPTextEncode, GetNode, LTXVEmptyLatentAudio, GetNode, GetNode, SetNode, CFGGuider, LTXVTiledVAEDecode, LTXVAudioVAEDecode, CreateVideo, UNETLoader, LTXVSeparateAVLatent, LTXVCropGuides, LTXICLoRALoaderModelOnly, SetNode, VAELoaderKJ, RandomNoise, GetNode, LoadImage, Int, SetNode, PrimitiveFloat, Note, CR Text, SamplerCustomAdvanced, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConcatAVLatent]
patterns: []
missing: [CR Text, SimpleMath+]
parameters: {"batch_size": 1, "height": 24, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 In​gredients IC LORA全能参考_2070747298736463873.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 In​gredients IC LORA全能参考_2070747298736463873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXFloatToInt`
- `PrimitiveBoolean`
- `SetNode`
- `ResizeImageMaskNode`
- `CreateVideo`
- `GetVideoComponents`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `LTXVPreprocess`
- `GetNode`
- `Int`
- `SetNode`
- `LTXAVTextEncoderLoader`
- `easy showAnything`
- `RepeatImageBatch`
- `GetNode`
- `SimpleMath+`
- `LTXVImgToVideoConditionOnly`
- `GetImageSize`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `CFGGuider`
- `LTXVTiledVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `UNETLoader` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXICLoRALoaderModelOnly` ★核心
- `SetNode`
- `VAELoaderKJ`
- `RandomNoise`
- `GetNode`
- `LoadImage`
- `Int`
- `SetNode`
- `PrimitiveFloat`
- `Note`
- `CR Text`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **49%**（35/71）

**有卡**：`LTXVConditioning`、`KSamplerSelect`、`LTXFloatToInt`、`PrimitiveBoolean`、`ResizeImageMaskNode`、`CreateVideo`、`GetVideoComponents`、`ManualSigmas`、`VAELoaderKJ`、`LTXVPreprocess`、`Int`、`LTXAVTextEncoderLoader`、`RepeatImageBatch`、`LTXVImgToVideoConditionOnly`、`GetImageSize`、`LTXAddVideoICLoRAGuide`、`SaveVideo`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`CFGGuider`、`LTXVTiledVAEDecode`、`LTXVAudioVAEDecode`、`UNETLoader`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXICLoRALoaderModelOnly`、`RandomNoise`、`LoadImage`、`SamplerCustomAdvanced`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`

**缺卡**（2）：`CR Text`、`SimpleMath+`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
