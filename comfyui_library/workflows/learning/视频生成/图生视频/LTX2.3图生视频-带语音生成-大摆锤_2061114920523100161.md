---
key: 视频生成/图生视频/LTX2.3图生视频-带语音生成-大摆锤_2061114920523100161.json
name: LTX2.3图生视频-带语音生成-大摆锤_2061114920523100161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频-带语音生成-大摆锤_2061114920523100161.json
hash: 20c1da7eed13425b
coverage: 0.822581
learned_at: 2026-10-15 22:38:51
nodes: [VAELoaderKJ, GetNode, LTXVSeparateAVLatent, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, Int, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, LTXVPreprocess, ModelSamplingSD3, SetNode, ConditioningZeroOut, SimpleMath+, ImageResizeKJv2, LTXVImgToVideoInplaceKJ, easy positive, GetNode, VAEDecode, PathchSageAttentionKJ, DF_Int_to_Float, LTXVAudioVAEDecode, GetNode, PrimitiveInt, Int, easy cleanGpuUsed, VAELoader, easy cleanGpuUsed, SamplerCustom, easy cleanGpuUsed, KSamplerSelect, GetNode, PrimitiveInt, easy cleanGpuUsed, SetNode, GetNode, StringFunction|pysssss, AILab_QwenVL_Advanced, ShowText|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, LTX2SamplingPreviewOverride, LTX2_NAG, UNETLoader, DualCLIPLoader, SetNode, easy cleanGpuUsed, SaveImage, TT_img_enc_v2, text-util-prompt-join, easy positive, LoadImage, CLIPTextEncode, CLIPTextEncode, easy positive, LoraLoader|pysssss, PrimitiveBoolean, easy cleanGpuUsed, ZML_SwitchOutput, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "lora_name": "LTX-2.3-Phut honV2.0.safetensors", "strength_clip": 1, "strength_model": 1, "width": 305}
---

# 视频生成/图生视频/LTX2.3图生视频-带语音生成-大摆锤_2061114920523100161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061114920523100161.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `VAELoaderKJ`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `Int`
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
- `DF_Int_to_Float`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `PrimitiveInt`
- `Int`
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
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `SetNode`
- `easy cleanGpuUsed`
- `SaveImage`
- `TT_img_enc_v2`
- `text-util-prompt-join`
- `easy positive`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy positive`
- `LoraLoader|pysssss` ★核心
- `PrimitiveBoolean`
- `easy cleanGpuUsed`
- `ZML_SwitchOutput`
- `VHS_VideoCombine`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`
- `lora_name` = `LTX-2.3-Phut honV2.0.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **82%**（51/62）

**有卡**：`VAELoaderKJ`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`Int`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`LTXVPreprocess`、`ModelSamplingSD3`、`ConditioningZeroOut`、`SimpleMath+`、`ImageResizeKJv2`、`LTXVImgToVideoInplaceKJ`、`easy positive`、`VAEDecode`、`PathchSageAttentionKJ`、`DF_Int_to_Float`、`LTXVAudioVAEDecode`、`easy cleanGpuUsed`、`VAELoader`、`SamplerCustom`、`KSamplerSelect`、`StringFunction|pysssss`、`AILab_QwenVL_Advanced`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`UNETLoader`、`DualCLIPLoader`、`SaveImage`、`TT_img_enc_v2`、`text-util-prompt-join`、`LoadImage`、`CLIPTextEncode`、`LoraLoader|pysssss`、`PrimitiveBoolean`、`ZML_SwitchOutput`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、UNETLoader、KSamplerSelect
