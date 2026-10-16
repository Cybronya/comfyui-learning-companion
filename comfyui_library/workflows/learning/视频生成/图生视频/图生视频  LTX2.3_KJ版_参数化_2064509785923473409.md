---
key: 视频生成/图生视频/图生视频  LTX2.3_KJ版_参数化_2064509785923473409.json
name: 图生视频  LTX2.3_KJ版_参数化_2064509785923473409.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064509785923473409.json
hash: 4e97bf632868b085
coverage: 0.916667
learned_at: 2026-10-15 22:39:25
nodes: [Int, MathExpression|pysssss, JjkText, StringFunction|pysssss, ShowText|pysssss, UNETLoader, DualCLIPLoader, CLIPTextEncode, LTX2_NAG, VAELoader, LTX2SamplingPreviewOverride, CLIPTextEncode, ConditioningZeroOut, LTXVConditioning, KSamplerSelect, ModelSamplingSD3, BasicScheduler, VAELoaderKJ, ImageResizeKJv2, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVImgToVideoInplaceKJ, VAELoaderKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SamplerCustom, LTXVSeparateAVLatent, VAEDecode, Int, VisualizeSigmasKJ, VHS_VideoCombine, LTXVAudioVAEDecode, AILab_QwenVL_Advanced, Int, JjkText, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/图生视频  LTX2.3_KJ版_参数化_2064509785923473409.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064509785923473409.json`

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
- `CLIPTextEncode` ★核心
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
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（33/36）

**有卡**：`Int`、`MathExpression|pysssss`、`StringFunction|pysssss`、`UNETLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`LTX2_NAG`、`VAELoader`、`LTX2SamplingPreviewOverride`、`ConditioningZeroOut`、`LTXVConditioning`、`KSamplerSelect`、`ModelSamplingSD3`、`BasicScheduler`、`VAELoaderKJ`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVSeparateAVLatent`、`VAEDecode`、`VisualizeSigmasKJ`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`AILab_QwenVL_Advanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
