---
key: 图片生成/图生图/LTX2.3图生视频-带语音生成-摇动版_2047251943105503234.json
name: LTX2.3图生视频-带语音生成-摇动版_2047251943105503234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LTX2.3图生视频-带语音生成-摇动版_2047251943105503234.json
hash: e49990ac83a4ebec
coverage: 0.810345
learned_at: 2026-10-23 11:08:53
nodes: [VAELoaderKJ, GetNode, LTXVSeparateAVLatent, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, Int, SetNode, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, LTXVPreprocess, ModelSamplingSD3, SetNode, ConditioningZeroOut, SimpleMath+, ImageResizeKJv2, LTXVImgToVideoInplaceKJ, easy positive, GetNode, VAEDecode, PathchSageAttentionKJ, LTXVAudioVAEDecode, GetNode, PrimitiveInt, Int, CLIPTextEncode, easy cleanGpuUsed, VAELoader, easy cleanGpuUsed, SamplerCustom, easy cleanGpuUsed, KSamplerSelect, GetNode, PrimitiveInt, easy cleanGpuUsed, SetNode, GetNode, StringFunction|pysssss, AILab_QwenVL_Advanced, ShowText|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, LTX2SamplingPreviewOverride, LTX2_NAG, CLIPTextEncode, UNETLoader, DualCLIPLoader, easy cleanGpuUsed, SaveImage, DF_Int_to_Float, VHS_VideoCombine, easy cleanGpuUsed, TT_img_enc_v2, LoraLoader|pysssss, easy positive, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "lora_name": "LTX2.3 - Doggy Style Sex.safetensors", "strength_clip": 1, "strength_model": 1, "width": 305}
---

# 图片生成/图生图/LTX2.3图生视频-带语音生成-摇动版_2047251943105503234.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LTX2.3图生视频-带语音生成-摇动版_2047251943105503234.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `VAELoaderKJ`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `Int`
- `SetNode`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `BasicScheduler`
- `LTXVPreprocess`
- `ModelSamplingSD3`
- `SetNode`
- `ConditioningZeroOut`
- `SimpleMath+`
- `ImageResizeKJv2`
- `LTXVImgToVideoInplaceKJ`
- `easy positive`
- `GetNode`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `PrimitiveInt`
- `Int`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `VAELoader`
- `easy cleanGpuUsed`
- `SamplerCustom` ★核心
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `GetNode`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `StringFunction|pysssss`
- `AILab_QwenVL_Advanced`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `easy cleanGpuUsed`
- `SaveImage`
- `DF_Int_to_Float`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `TT_img_enc_v2`
- `LoraLoader|pysssss` ★核心
- `easy positive`
- `LoadImage`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`
- `lora_name` = `LTX2.3 - Doggy Style Sex.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **81%**（47/58）

**有卡**：`VAELoaderKJ`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`Int`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`LTXVPreprocess`、`ModelSamplingSD3`、`ConditioningZeroOut`、`SimpleMath+`、`ImageResizeKJv2`、`LTXVImgToVideoInplaceKJ`、`easy positive`、`VAEDecode`、`PathchSageAttentionKJ`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`easy cleanGpuUsed`、`VAELoader`、`SamplerCustom`、`KSamplerSelect`、`StringFunction|pysssss`、`AILab_QwenVL_Advanced`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`UNETLoader`、`DualCLIPLoader`、`SaveImage`、`DF_Int_to_Float`、`VHS_VideoCombine`、`TT_img_enc_v2`、`LoraLoader|pysssss`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
