---
key: 视频生成/文生视频/LTX2.3-OmniNFT-RL-Lora 文_图生视频_2057113427591647233.json
name: LTX2.3-OmniNFT-RL-Lora 文_图生视频_2057113427591647233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-OmniNFT-RL-Lora 文_图生视频_2057113427591647233.json
hash: 1c7078ef369fb581
coverage: 0.694444
learned_at: 2026-10-11 19:49:37
nodes: [LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVCropGuides, easy getNode, CFGGuider, RandomNoise, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, easy getNode, VAEDecode, LTXVAudioVAEDecode, VisualizeSigmasKJ, VAELoader, KSamplerSelect, easy getNode, LTXVSeparateAVLatent, easy getNode, VAEDecode, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, easy getNode, LTXVEmptyLatentAudio, easy getNode, easy setNode, ConditioningZeroOut, easy getNode, BasicScheduler, CLIPTextEncode, ModelSamplingSD3, LoraLoaderModelOnly, easy setNode, easy setNode, easy setNode, PathchSageAttentionKJ, PrimitiveInt, Int, Int, Int, PrimitiveBoolean, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, easy setNode, PrimitiveInt, LTXVPreprocess, ImageResizeKJv2, UNETLoader, VRAMReserver, LoraLoaderModelOnly, easy getNode, LoadImage, DF_Int_to_Float, Fast Groups Bypasser (rgthree), easy getNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, ManualSigmas, easy getNode, Reroute, VHS_VideoCombine, CR Prompt Text, LTX2_NAG, LTXVConditioning, LTX2SamplingPreviewOverride, SamplerCustom, CLIPTextEncode, SimpleMath+, easy getNode, LTXVConcatAVLatent, LTXVAudioVAEDecode, VHS_VideoCombine]
patterns: []
missing: [SimpleMath+, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, easy setNode, easy setNode, CR Prompt Text]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3-OmniNFT-RL-Lora 文_图生视频_2057113427591647233.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-OmniNFT-RL-Lora 文_图生视频_2057113427591647233.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（72 个）：
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `easy getNode`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `easy getNode`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VisualizeSigmasKJ`
- `VAELoader`
- `KSamplerSelect` ★核心
- `easy getNode`
- `LTXVSeparateAVLatent`
- `easy getNode`
- `VAEDecode` ★核心
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `easy getNode`
- `LTXVEmptyLatentAudio` ★核心
- `easy getNode`
- `easy setNode`
- `ConditioningZeroOut`
- `easy getNode`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `Int`
- `Int`
- `Int`
- `PrimitiveBoolean`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `easy setNode`
- `PrimitiveInt`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `easy getNode`
- `LoadImage`
- `DF_Int_to_Float`
- `Fast Groups Bypasser (rgthree)`
- `easy getNode`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `easy getNode`
- `Reroute`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `LTX2_NAG`
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `easy getNode`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（50/72）

**有卡**：`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`VisualizeSigmasKJ`、`VAELoader`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ConditioningZeroOut`、`BasicScheduler`、`CLIPTextEncode`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`Int`、`PrimitiveBoolean`、`DualCLIPLoader`、`VAELoaderKJ`、`LTXVPreprocess`、`ImageResizeKJv2`、`UNETLoader`、`VRAMReserver`、`LoadImage`、`DF_Int_to_Float`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`ManualSigmas`、`VHS_VideoCombine`、`LTX2_NAG`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`SamplerCustom`

**缺卡**（18）：`SimpleMath+`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
