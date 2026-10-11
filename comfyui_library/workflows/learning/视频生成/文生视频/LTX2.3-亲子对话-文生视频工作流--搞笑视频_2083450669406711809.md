---
key: 视频生成/文生视频/LTX2.3-亲子对话-文生视频工作流--搞笑视频_2083450669406711809.json
name: LTX2.3-亲子对话-文生视频工作流--搞笑视频_2083450669406711809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-亲子对话-文生视频工作流--搞笑视频_2083450669406711809.json
hash: de9a0fe4b003c165
coverage: 0.690909
learned_at: 2026-10-11 20:38:35
nodes: [easy setNode, easy setNode, easy setNode, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, easy setNode, easy getNode, Int, easy setNode, LTXVPreprocess, CLIPTextEncode, easy getNode, EmptyLTXVLatentVideo, SimpleMath+, easy getNode, easy getNode, easy getNode, ImageResizeKJv2, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, ConditioningZeroOut, BasicScheduler, LTXVConditioning, LTX2SamplingPreviewOverride, DF_Int_to_Float, LTXVSeparateAVLatent, PrimitiveInt, VAEDecode, ModelSamplingSD3, PathchSageAttentionKJ, VRAMReserver, LTX2_NAG, VisualizeSigmasKJ, VAELoader, KSamplerSelect, LTXVConcatAVLatent, easy getNode, easy getNode, LTXVAudioVAEDecode, VHS_VideoCombine, SamplerCustom, PrimitiveInt, Int, Int, CLIPTextEncode, CLIPTextEncode, MarkdownNote, LoadImage, PrimitiveBoolean, CLIPTextEncode, MarkdownNote]
patterns: []
missing: [SimpleMath+, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, easy setNode, easy setNode]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3-亲子对话-文生视频工作流--搞笑视频_2083450669406711809.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-亲子对话-文生视频工作流--搞笑视频_2083450669406711809.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy setNode`
- `easy getNode`
- `Int`
- `easy setNode`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `ImageResizeKJv2`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoConditionOnly`
- `ConditioningZeroOut`
- `BasicScheduler`
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `DF_Int_to_Float`
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VRAMReserver`
- `LTX2_NAG`
- `VisualizeSigmasKJ`
- `VAELoader`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `easy getNode`
- `easy getNode`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `SamplerCustom` ★核心
- `PrimitiveInt`
- `Int`
- `Int`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoadImage`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（38/55）

**有卡**：`DualCLIPLoader`、`VAELoaderKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`Int`、`LTXVPreprocess`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoConditionOnly`、`ConditioningZeroOut`、`BasicScheduler`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`DF_Int_to_Float`、`LTXVSeparateAVLatent`、`VAEDecode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`VRAMReserver`、`LTX2_NAG`、`VisualizeSigmasKJ`、`VAELoader`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`SamplerCustom`、`LoadImage`、`PrimitiveBoolean`

**缺卡**（13）：`SimpleMath+`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
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
