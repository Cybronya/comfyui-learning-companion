---
key: 视频生成/文生视频/LTX2.3_PromptRelay+DramaBoxTTS 音画同步视频生成工作流_2056252444816003074.json
name: LTX2.3_PromptRelay+DramaBoxTTS 音画同步视频生成工作流_2056252444816003074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3_PromptRelay+DramaBoxTTS 音画同步视频生成工作流_2056252444816003074.json
hash: 399670abadbb08bd
coverage: 0.495238
learned_at: 2026-10-10 23:00:23
nodes: [LTXVConditioning, LTXVSeparateAVLatent, GetNode, SetNode, ConditioningZeroOut, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, VAEDecode, SetNode, EmptyLTXVLatentVideo, GetNode, VisualizeSigmasKJ, GetNode, easy clearCacheAll, GetNode, easy cleanGpuUsed, KSamplerSelect, LTXVAudioVAEDecode, CR Float To Integer, SetNode, GetNode, SetNode, SetNode, easy cleanGpuUsed, easy clearCacheAll, LTX2SamplingPreviewOverride, Note, GetNode, GetNode, GetImageSize, GetNode, GetImageSize, GetNode, SetNode, BasicScheduler, PreviewImage, LTXVPreprocess, SetNode, PrimitiveInt, CFGGuider, CLIPTextEncode, LTXVConditioning, easy cleanGpuUsed, VAEEncodeTiled, LTXVLoopingSampler, ManualSigmas, RandomNoise, VisualizeSigmasKJ, KSamplerSelect, BasicScheduler, LTXVSpatioTemporalTiledVAEDecode, ImageScaleToMaxDimension, PreviewImage, GetNode, SolidMask, GetNode, PrimitiveFloat, SetNode, MathExpression|pysssss, SetNode, SetNode, LTXVAudioVAEEncode, SetNode, SetNode, SamplerCustom, GetNode, PreviewAudio, Audio Duration (mtb), MathExpression|pysssss, LTXVImgToVideoInplaceKJ, VHS_VideoCombine, VHS_VideoCombine, SetLatentNoiseMask, PathchSageAttentionKJ, SetNode, Any Switch (rgthree), ResizeImageMaskNode, SetNode, StringReplace, LTXVConcatAVLatent, PromptRelayEncode, LoadImageFromPath, PreviewImage, UnetLoaderGGUF, LoraLoaderModelOnly, VAELoader, LTXVAudioVAELoader, UNETLoader, DualCLIPLoader, PrimitiveStringMultiline, DramaBoxLoader, DramaBoxTTS, LoraLoaderModelOnly, AILab_QwenVL_Advanced, ShowText|pysssss, LoadAudio, DramaBoxVoiceClone, LoadImage]
patterns: []
missing: [Audio Duration (mtb), CR Float To Integer, MathExpression|pysssss, MathExpression|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, easy clearCacheAll]
discoveries: [次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Float To Integer` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
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

覆盖率 **50%**（52/105）

**有卡**：`LTXVConditioning`、`LTXVSeparateAVLatent`、`ConditioningZeroOut`、`VAEDecode`、`EmptyLTXVLatentVideo`、`VisualizeSigmasKJ`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`LTX2SamplingPreviewOverride`、`GetImageSize`、`BasicScheduler`、`LTXVPreprocess`、`CFGGuider`、`CLIPTextEncode`、`VAEEncodeTiled`、`LTXVLoopingSampler`、`ManualSigmas`、`RandomNoise`、`LTXVSpatioTemporalTiledVAEDecode`、`ImageScaleToMaxDimension`、`SolidMask`、`LTXVAudioVAEEncode`、`SamplerCustom`、`PreviewAudio`、`LTXVImgToVideoInplaceKJ`、`VHS_VideoCombine`、`SetLatentNoiseMask`、`PathchSageAttentionKJ`、`ResizeImageMaskNode`、`StringReplace`、`LTXVConcatAVLatent`、`PromptRelayEncode`、`LoadImageFromPath`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`VAELoader`、`LTXVAudioVAELoader`、`UNETLoader`、`DualCLIPLoader`、`DramaBoxLoader`、`DramaBoxTTS`、`AILab_QwenVL_Advanced`、`LoadAudio`、`DramaBoxVoiceClone`、`LoadImage`

**缺卡**（9）：`Audio Duration (mtb)`、`CR Float To Integer`、`MathExpression|pysssss`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy clearCacheAll`、`easy clearCacheAll`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider

## 学习发现

- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Float To Integer` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
