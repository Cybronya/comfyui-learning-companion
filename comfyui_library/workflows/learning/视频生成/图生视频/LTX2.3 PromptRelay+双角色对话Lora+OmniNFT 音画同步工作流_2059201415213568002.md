---
key: 视频生成/图生视频/LTX2.3 PromptRelay+双角色对话Lora+OmniNFT 音画同步工作流_2059201415213568002.json
name: LTX2.3 PromptRelay+双角色对话Lora+OmniNFT 音画同步工作流_2059201415213568002.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2059201415213568002.json
hash: bc3340b0aebff587
coverage: 0.506494
learned_at: 2026-10-15 22:38:37
nodes: [LTXVSeparateAVLatent, GetNode, VAEDecode, SetNode, SetNode, EmptyLTXVLatentVideo, GetNode, LTXVAudioVAEDecode, CR Float To Integer, SetNode, SetNode, SetNode, SetNode, SetNode, easy cleanGpuUsed, easy clearCacheAll, PrimitiveInt, GetNode, GetNode, GetNode, LTXVAudioVAEEncode, GetNode, SolidMask, SetLatentNoiseMask, GetNode, GetImageSize, GetNode, VHS_LoadAudio, LTXVEmptyLatentAudio, GetImageSize, MathExpression|pysssss, GetNode, LTXVPreprocess, GetNode, LTXVConcatAVLatent, GetNode, PreviewImage, LTXVConditioning, GetNode, SamplerCustom, KSamplerSelect, GetNode, GetNode, VisualizeSigmasKJ, GetNode, BasicScheduler, PrimitiveInt, Any Switch (rgthree), ResizeImageMaskNode, CLIPTextEncode, GetNode, LoadImageFromPath, LTXVImgToVideoInplaceKJ, Any Switch (rgthree), SetNode, VHS_VideoCombine, PreviewImage, PrimitiveFloat, SetNode, GetNode, PrimitiveStringMultiline, LoraLoader, LTXVAudioVAELoader, SetNode, VAELoader, SetNode, SetNode, PathchSageAttentionKJ, SetNode, DualCLIPLoader, CheckpointLoaderSimple, UnetLoaderGGUF, Power Lora Loader (rgthree), PromptRelayEncode, LoadImage, ConditioningZeroOut, LTX2_NAG]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "lora_name": "LTX-2.3-OmniNFT-RL-Lora_bf16.safetensors", "strength_clip": 1, "strength_model": 0.9000000000000001, "width": 505}
---

# 视频生成/图生视频/LTX2.3 PromptRelay+双角色对话Lora+OmniNFT 音画同步工作流_2059201415213568002.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059201415213568002.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（77 个）：
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `CR Float To Integer`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `SetLatentNoiseMask`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `VHS_LoadAudio`
- `LTXVEmptyLatentAudio` ★核心
- `GetImageSize`
- `MathExpression|pysssss`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `PreviewImage`
- `LTXVConditioning`
- `GetNode`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `VisualizeSigmasKJ`
- `GetNode`
- `BasicScheduler`
- `PrimitiveInt`
- `Any Switch (rgthree)`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LoadImageFromPath`
- `LTXVImgToVideoInplaceKJ`
- `Any Switch (rgthree)`
- `SetNode`
- `VHS_VideoCombine`
- `PreviewImage`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `LoraLoader` ★核心
- `LTXVAudioVAELoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `UnetLoaderGGUF` ★核心
- `Power Lora Loader (rgthree)`
- `PromptRelayEncode`
- `LoadImage`
- `ConditioningZeroOut`
- `LTX2_NAG`

**识别到的模式**：lora

## 关键参数

- `width` = `505`
- `height` = `25`
- `batch_size` = `1`
- `lora_name` = `LTX-2.3-OmniNFT-RL-Lora_bf16.safetensors`
- `strength_model` = `0.9000000000000001`
- `strength_clip` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **51%**（39/77）

**有卡**：`LTXVSeparateAVLatent`、`VAEDecode`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`CR Float To Integer`、`easy cleanGpuUsed`、`easy clearCacheAll`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`GetImageSize`、`VHS_LoadAudio`、`LTXVEmptyLatentAudio`、`MathExpression|pysssss`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`LTXVConditioning`、`SamplerCustom`、`KSamplerSelect`、`VisualizeSigmasKJ`、`BasicScheduler`、`ResizeImageMaskNode`、`CLIPTextEncode`、`LoadImageFromPath`、`LTXVImgToVideoInplaceKJ`、`VHS_VideoCombine`、`LoraLoader`、`LTXVAudioVAELoader`、`VAELoader`、`PathchSageAttentionKJ`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`UnetLoaderGGUF`、`Power Lora Loader (rgthree)`、`PromptRelayEncode`、`LoadImage`、`ConditioningZeroOut`、`LTX2_NAG`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、KSamplerSelect、SamplerCustom
