---
key: 视频生成/文生视频/LTX2.3_PromptRelay+DramaBoxTTS 音画同步视频生成工作流_2056252444816003074.json
name: LTX2.3_PromptRelay+DramaBoxTTS 音画同步视频生成工作流_2056252444816003074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3_PromptRelay+DramaBoxTTS 音画同步视频生成工作流_2056252444816003074.json
hash: 399670abadbb08bd
coverage: 0.580952
learned_at: 2026-10-15 22:45:05
nodes: [LTXVConditioning, LTXVSeparateAVLatent, GetNode, SetNode, ConditioningZeroOut, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, VAEDecode, SetNode, EmptyLTXVLatentVideo, GetNode, VisualizeSigmasKJ, GetNode, easy clearCacheAll, GetNode, easy cleanGpuUsed, KSamplerSelect, LTXVAudioVAEDecode, CR Float To Integer, SetNode, GetNode, SetNode, SetNode, easy cleanGpuUsed, easy clearCacheAll, LTX2SamplingPreviewOverride, Note, GetNode, GetNode, GetImageSize, GetNode, GetImageSize, GetNode, SetNode, BasicScheduler, PreviewImage, LTXVPreprocess, SetNode, PrimitiveInt, CFGGuider, CLIPTextEncode, LTXVConditioning, easy cleanGpuUsed, VAEEncodeTiled, LTXVLoopingSampler, ManualSigmas, RandomNoise, VisualizeSigmasKJ, KSamplerSelect, BasicScheduler, LTXVSpatioTemporalTiledVAEDecode, ImageScaleToMaxDimension, PreviewImage, GetNode, SolidMask, GetNode, PrimitiveFloat, SetNode, MathExpression|pysssss, SetNode, SetNode, LTXVAudioVAEEncode, SetNode, SetNode, SamplerCustom, GetNode, PreviewAudio, Audio Duration (mtb), MathExpression|pysssss, LTXVImgToVideoInplaceKJ, VHS_VideoCombine, VHS_VideoCombine, SetLatentNoiseMask, PathchSageAttentionKJ, SetNode, Any Switch (rgthree), ResizeImageMaskNode, SetNode, StringReplace, LTXVConcatAVLatent, PromptRelayEncode, LoadImageFromPath, PreviewImage, UnetLoaderGGUF, LoraLoaderModelOnly, VAELoader, LTXVAudioVAELoader, UNETLoader, DualCLIPLoader, PrimitiveStringMultiline, DramaBoxLoader, DramaBoxTTS, LoraLoaderModelOnly, AILab_QwenVL_Advanced, ShowText|pysssss, LoadAudio, DramaBoxVoiceClone, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX2.3_PromptRelay+DramaBoxTTS 音画同步视频生成工作流_2056252444816003074.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3_PromptRelay+DramaBoxTTS 音画同步视频生成工作流_2056252444816003074.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（105 个）：
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `VAEDecode` ★核心
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `VisualizeSigmasKJ`
- `GetNode`
- `easy clearCacheAll`
- `GetNode`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CR Float To Integer`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `LTX2SamplingPreviewOverride`
- `Note`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `SetNode`
- `BasicScheduler`
- `PreviewImage`
- `LTXVPreprocess`
- `SetNode`
- `PrimitiveInt`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `easy cleanGpuUsed`
- `VAEEncodeTiled` ★核心
- `LTXVLoopingSampler` ★核心
- `ManualSigmas`
- `RandomNoise`
- `VisualizeSigmasKJ`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `ImageScaleToMaxDimension`
- `PreviewImage`
- `GetNode`
- `SolidMask`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `SetNode`
- `SamplerCustom` ★核心
- `GetNode`
- `PreviewAudio`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `LTXVImgToVideoInplaceKJ`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetLatentNoiseMask`
- `PathchSageAttentionKJ`
- `SetNode`
- `Any Switch (rgthree)`
- `ResizeImageMaskNode`
- `SetNode`
- `StringReplace`
- `LTXVConcatAVLatent`
- `PromptRelayEncode`
- `LoadImageFromPath`
- `PreviewImage`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LTXVAudioVAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `PrimitiveStringMultiline`
- `DramaBoxLoader`
- `DramaBoxTTS`
- `LoraLoaderModelOnly` ★核心
- `AILab_QwenVL_Advanced`
- `ShowText|pysssss`
- `LoadAudio`
- `DramaBoxVoiceClone`
- `LoadImage`

## 知识

覆盖率 **58%**（61/105）

**有卡**：`LTXVConditioning`、`LTXVSeparateAVLatent`、`ConditioningZeroOut`、`VAEDecode`、`EmptyLTXVLatentVideo`、`VisualizeSigmasKJ`、`easy clearCacheAll`、`easy cleanGpuUsed`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`CR Float To Integer`、`LTX2SamplingPreviewOverride`、`GetImageSize`、`BasicScheduler`、`LTXVPreprocess`、`CFGGuider`、`CLIPTextEncode`、`VAEEncodeTiled`、`LTXVLoopingSampler`、`ManualSigmas`、`RandomNoise`、`LTXVSpatioTemporalTiledVAEDecode`、`ImageScaleToMaxDimension`、`SolidMask`、`MathExpression|pysssss`、`LTXVAudioVAEEncode`、`SamplerCustom`、`PreviewAudio`、`Audio Duration (mtb)`、`LTXVImgToVideoInplaceKJ`、`VHS_VideoCombine`、`SetLatentNoiseMask`、`PathchSageAttentionKJ`、`ResizeImageMaskNode`、`StringReplace`、`LTXVConcatAVLatent`、`PromptRelayEncode`、`LoadImageFromPath`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`VAELoader`、`LTXVAudioVAELoader`、`UNETLoader`、`DualCLIPLoader`、`DramaBoxLoader`、`DramaBoxTTS`、`AILab_QwenVL_Advanced`、`LoadAudio`、`DramaBoxVoiceClone`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider
