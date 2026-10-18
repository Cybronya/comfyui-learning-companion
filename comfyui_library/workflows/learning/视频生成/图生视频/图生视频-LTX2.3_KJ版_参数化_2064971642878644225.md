---
key: 视频生成/图生视频/图生视频-LTX2.3_KJ版_参数化_2064971642878644225.json
name: 图生视频-LTX2.3_KJ版_参数化_2064971642878644225.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频-LTX2.3_KJ版_参数化_2064971642878644225.json
hash: 67e875c88a671990
coverage: 0.916667
learned_at: 2026-10-15 22:39:32
nodes: [ShowText|pysssss, LTX2_NAG, LTX2SamplingPreviewOverride, ConditioningZeroOut, LTXVConditioning, BasicScheduler, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVImgToVideoInplaceKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SamplerCustom, LTXVSeparateAVLatent, VAEDecode, VisualizeSigmasKJ, VHS_VideoCombine, LTXVAudioVAEDecode, AILab_QwenVL_Advanced, Int, Int, MathExpression|pysssss, StringFunction|pysssss, JjkText, ModelSamplingSD3, CLIPTextEncode, DualCLIPLoader, ImageResizeKJv2, VAELoader, KSamplerSelect, VAELoaderKJ, Int, VAELoaderKJ, CLIPTextEncode, JjkText, LoadImage, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/图生视频-LTX2.3_KJ版_参数化_2064971642878644225.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064971642878644225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（36 个）：
- `ShowText|pysssss`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `ConditioningZeroOut`
- `LTXVConditioning`
- `BasicScheduler`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVImgToVideoInplaceKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VisualizeSigmasKJ`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `AILab_QwenVL_Advanced`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `StringFunction|pysssss`
- `JjkText`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `ImageResizeKJv2`
- `VAELoader`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `Int`
- `VAELoaderKJ`
- `CLIPTextEncode` ★核心
- `JjkText`
- `LoadImage`
- `UNETLoader` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（33/36）

**有卡**：`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`ConditioningZeroOut`、`LTXVConditioning`、`BasicScheduler`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVSeparateAVLatent`、`VAEDecode`、`VisualizeSigmasKJ`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`AILab_QwenVL_Advanced`、`Int`、`MathExpression|pysssss`、`StringFunction|pysssss`、`ModelSamplingSD3`、`CLIPTextEncode`、`DualCLIPLoader`、`ImageResizeKJv2`、`VAELoader`、`KSamplerSelect`、`VAELoaderKJ`、`LoadImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
