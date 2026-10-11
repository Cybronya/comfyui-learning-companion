---
key: 视频生成/文生视频/LTX2.3图生视频KJ优化版_2034072375746105345.json
name: LTX2.3图生视频KJ优化版_2034072375746105345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频KJ优化版_2034072375746105345.json
hash: 3ef98bdfa5bdc51d
coverage: 0.673913
learned_at: 2026-10-11 03:48:36
nodes: [VAELoaderKJ, LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, UNETLoader, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoader, DualCLIPLoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, PathchSageAttentionKJ, SetNode, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, LTXVPreprocess, ModelSamplingSD3, SetNode, ConditioningZeroOut, SamplerCustom, VAEDecode, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, SimpleMath+, ImageResizeKJv2, LTXVImgToVideoInplaceKJ, easy positive, StringFunction|pysssss, SetNode, DF_Int_to_Float, GetNode, GetNode, AILab_QwenVL_Advanced, GetNode, Int, PrimitiveInt, ShowText|pysssss, PrimitiveInt, VHS_VideoCombine, LoadImage, easy positive]
patterns: []
missing: [SimpleMath+, StringFunction|pysssss, easy positive, easy positive]
parameters: {"batch_size": 1, "height": 24, "width": 305}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3图生视频KJ优化版_2034072375746105345.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频KJ优化版_2034072375746105345.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（46 个）：
- `VAELoaderKJ`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `SetNode`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `BasicScheduler`
- `LTXVPreprocess`
- `ModelSamplingSD3`
- `SetNode`
- `ConditioningZeroOut`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `ImageResizeKJv2`
- `LTXVImgToVideoInplaceKJ`
- `easy positive`
- `StringFunction|pysssss`
- `SetNode`
- `DF_Int_to_Float`
- `GetNode`
- `GetNode`
- `AILab_QwenVL_Advanced`
- `GetNode`
- `Int`
- `PrimitiveInt`
- `ShowText|pysssss`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LoadImage`
- `easy positive`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（31/46）

**有卡**：`VAELoaderKJ`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`UNETLoader`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAELoader`、`DualCLIPLoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`LTXVPreprocess`、`ModelSamplingSD3`、`ConditioningZeroOut`、`SamplerCustom`、`VAEDecode`、`KSamplerSelect`、`CLIPTextEncode`、`ImageResizeKJv2`、`LTXVImgToVideoInplaceKJ`、`DF_Int_to_Float`、`AILab_QwenVL_Advanced`、`Int`、`VHS_VideoCombine`、`LoadImage`

**缺卡**（4）：`SimpleMath+`、`StringFunction|pysssss`、`easy positive`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
