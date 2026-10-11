---
key: 视频生成/文生视频/LTX2.3图生视频-KJ版-参数化_2069425308750671874.json
name: LTX2.3图生视频-KJ版-参数化_2069425308750671874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频-KJ版-参数化_2069425308750671874.json
hash: e5d4f4d79393bc80
coverage: 0.861111
learned_at: 2026-10-11 20:21:26
nodes: [Int, MathExpression|pysssss, JjkText, StringFunction|pysssss, ShowText|pysssss, UNETLoader, DualCLIPLoader, LTX2_NAG, VAELoader, LTX2SamplingPreviewOverride, CLIPTextEncode, ConditioningZeroOut, LTXVConditioning, KSamplerSelect, ModelSamplingSD3, BasicScheduler, VAELoaderKJ, ImageResizeKJv2, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVImgToVideoInplaceKJ, VAELoaderKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SamplerCustom, LTXVSeparateAVLatent, VAEDecode, Int, VisualizeSigmasKJ, VHS_VideoCombine, LTXVAudioVAEDecode, AILab_QwenVL_Advanced, Int, JjkText, CLIPTextEncode, LoadImage]
patterns: []
missing: [MathExpression|pysssss, StringFunction|pysssss]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3图生视频-KJ版-参数化_2069425308750671874.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频-KJ版-参数化_2069425308750671874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（36 个）：
- `Int`
- `MathExpression|pysssss`
- `JjkText`
- `StringFunction|pysssss`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LTX2_NAG`
- `VAELoader`
- `LTX2SamplingPreviewOverride`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `BasicScheduler`
- `VAELoaderKJ`
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVImgToVideoInplaceKJ`
- `VAELoaderKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `Int`
- `VisualizeSigmasKJ`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `AILab_QwenVL_Advanced`
- `Int`
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`Int`、`UNETLoader`、`DualCLIPLoader`、`LTX2_NAG`、`VAELoader`、`LTX2SamplingPreviewOverride`、`CLIPTextEncode`、`ConditioningZeroOut`、`LTXVConditioning`、`KSamplerSelect`、`ModelSamplingSD3`、`BasicScheduler`、`VAELoaderKJ`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVSeparateAVLatent`、`VAEDecode`、`VisualizeSigmasKJ`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`AILab_QwenVL_Advanced`、`LoadImage`

**缺卡**（2）：`MathExpression|pysssss`、`StringFunction|pysssss`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
