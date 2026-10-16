---
key: 视频生成/图生视频/LTX2.3图生视频KJ优化版！_2031926967917879297.json
name: LTX2.3图生视频KJ优化版！_2031926967917879297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031926967917879297.json
hash: d5de194205e352ee
coverage: 0.76087
learned_at: 2026-10-15 22:35:33
nodes: [VAELoaderKJ, LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, UNETLoader, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoader, DualCLIPLoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, PathchSageAttentionKJ, SetNode, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, LTXVPreprocess, ModelSamplingSD3, SetNode, ConditioningZeroOut, SamplerCustom, VHS_VideoCombine, VAEDecode, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, PrimitiveInt, SimpleMath+, ImageResizeKJv2, LTXVImgToVideoInplaceKJ, easy positive, StringFunction|pysssss, SetNode, DF_Int_to_Float, GetNode, GetNode, AILab_QwenVL_Advanced, GetNode, LoadImage, ShowText|pysssss, PrimitiveInt, easy positive, Int]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3图生视频KJ优化版！_2031926967917879297.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031926967917879297.json`

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
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
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
- `LoadImage`
- `ShowText|pysssss`
- `PrimitiveInt`
- `easy positive`
- `Int`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（35/46）

**有卡**：`VAELoaderKJ`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`UNETLoader`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAELoader`、`DualCLIPLoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`LTXVPreprocess`、`ModelSamplingSD3`、`ConditioningZeroOut`、`SamplerCustom`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerSelect`、`CLIPTextEncode`、`SimpleMath+`、`ImageResizeKJv2`、`LTXVImgToVideoInplaceKJ`、`easy positive`、`StringFunction|pysssss`、`DF_Int_to_Float`、`AILab_QwenVL_Advanced`、`LoadImage`、`Int`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
