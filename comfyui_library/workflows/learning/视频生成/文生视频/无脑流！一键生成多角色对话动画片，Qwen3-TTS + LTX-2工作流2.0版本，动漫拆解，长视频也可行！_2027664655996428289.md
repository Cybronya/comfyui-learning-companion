---
key: 视频生成/文生视频/无脑流！一键生成多角色对话动画片，Qwen3-TTS + LTX-2工作流2.0版本，动漫拆解，长视频也可行！_2027664655996428289.json
name: 无脑流！一键生成多角色对话动画片，Qwen3-TTS + LTX-2工作流2.0版本，动漫拆解，长视频也可行！_2027664655996428289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/无脑流！一键生成多角色对话动画片，Qwen3-TTS + LTX-2工作流2.0版本，动漫拆解，长视频也可行！_2027664655996428289.json
hash: bf4fba89d11b9998
coverage: 0.50495
learned_at: 2026-10-11 03:16:52
nodes: [GetNode, GetNode, GetNode, MarkdownNote, MarkdownNote, SetNode, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, SetLatentNoiseMask, SetNode, LTXVAudioVAEEncode, easy showAnything, Audio Duration (mtb), GetNode, VRAM_Debug, SimpleCalculatorKJ, GetNode, LTXVConcatAVLatent, MarkdownNote, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, CFGGuider, SamplerCustomAdvanced, GetNode, GetNode, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVSeparateAVLatent, GetNode, KSamplerSelect, LTXVSeparateAVLatent, GetImageSize, ManualSigmas, VHS_VideoCombine, SimpleCalculatorKJ, LTXVScheduler, GetNode, GetNode, LTXVEmptyLatentAudio, EmptyImage, LayerUtility: PurgeVRAM V2, LTXVChunkFeedForward, LoraLoaderModelOnly, DualCLIPLoaderGGUF, VAELoader, VAELoaderKJ, LatentUpscaleModelLoader, GetNode, CLIPTextEncode, GetNode, KSamplerSelect, LTX2AudioLatentNormalizingSampling, CFGGuider, SetNode, ImageScaleBy, LayerUtility: PurgeVRAM V2, SolidMask, RandomNoise, RandomNoise, FB_Qwen3TTSVoiceClonePrompt, UnetLoaderGGUF, GetNode, SetNode, SetNode, LTXVConditioning, FB_Qwen3TTSDialogueInference, CLIPTextEncode, FB_Qwen3TTSVoiceDesign, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, PreviewAudio, FB_Qwen3TTSRoleBank, CR Text, CR Text, CR Text, PreviewAudio, CR Text, CR Text, INTConstant, INTConstant, PrimitiveFloat, PreviewAudio]
patterns: []
missing: [Audio Duration (mtb), CR Text, CR Text, CR Text, CR Text, CR Text, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2]
parameters: {"batch_size": 1, "height": 25, "width": 121}
discoveries: [次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/无脑流！一键生成多角色对话动画片，Qwen3-TTS + LTX-2工作流2.0版本，动漫拆解，长视频也可行！_2027664655996428289.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/无脑流！一键生成多角色对话动画片，Qwen3-TTS + LTX-2工作流2.0版本，动漫拆解，长视频也可行！_2027664655996428289.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（101 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetLatentNoiseMask`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `easy showAnything`
- `Audio Duration (mtb)`
- `GetNode`
- `VRAM_Debug`
- `SimpleCalculatorKJ`
- `GetNode`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `GetImageSize`
- `ManualSigmas`
- `VHS_VideoCombine`
- `SimpleCalculatorKJ`
- `LTXVScheduler`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyImage`
- `LayerUtility: PurgeVRAM V2`
- `LTXVChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoaderGGUF`
- `VAELoader`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `LTX2AudioLatentNormalizingSampling`
- `CFGGuider`
- `SetNode`
- `ImageScaleBy`
- `LayerUtility: PurgeVRAM V2`
- `SolidMask`
- `RandomNoise`
- `RandomNoise`
- `FB_Qwen3TTSVoiceClonePrompt`
- `UnetLoaderGGUF` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `FB_Qwen3TTSDialogueInference`
- `CLIPTextEncode` ★核心
- `FB_Qwen3TTSVoiceDesign`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `PreviewAudio`
- `FB_Qwen3TTSRoleBank`
- `CR Text`
- `CR Text`
- `CR Text`
- `PreviewAudio`
- `CR Text`
- `CR Text`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `PreviewAudio`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（51/101）

**有卡**：`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`VRAM_Debug`、`SimpleCalculatorKJ`、`CFGGuider`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`GetImageSize`、`ManualSigmas`、`VHS_VideoCombine`、`LTXVScheduler`、`LTXVEmptyLatentAudio`、`EmptyImage`、`LTXVChunkFeedForward`、`LoraLoaderModelOnly`、`DualCLIPLoaderGGUF`、`VAELoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`LTX2AudioLatentNormalizingSampling`、`ImageScaleBy`、`SolidMask`、`RandomNoise`、`FB_Qwen3TTSVoiceClonePrompt`、`UnetLoaderGGUF`、`LTXVConditioning`、`FB_Qwen3TTSDialogueInference`、`FB_Qwen3TTSVoiceDesign`、`PreviewAudio`、`FB_Qwen3TTSRoleBank`、`INTConstant`

**缺卡**（8）：`Audio Duration (mtb)`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
