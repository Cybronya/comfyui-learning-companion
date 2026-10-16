---
key: 视频生成/图生视频/LTX-2.3_Gemini3补全分镜提示词+自定义音频+首尾帧+多图段子视频生成_2055962684570521602.json
name: LTX-2.3_Gemini3补全分镜提示词+自定义音频+首尾帧+多图段子视频生成_2055962684570521602.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2055962684570521602.json
hash: 9b06b50a723bf3b7
coverage: 0.496063
learned_at: 2026-10-15 22:37:59
nodes: [UNETLoader, SetNode, SoundFlow_GetLength, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, CFGGuider, SetNode, easy imageSize, SetNode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEEncode, GetNode, GetNode, GetNode, GetNode, SimpleMath+, GetNode, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, LTXVConditioning, FL_IntToFloat, RandomNoise, GetNode, GetNode, GetNode, LoadImage, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, GetImageRangeFromBatch, GetNode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, GetNode, ShowText|pysssss, SetNode, GetNode, easy int, GetNode, GetNode, easy imageSize, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, SetNode, SetNode, GetNode, SimpleMath+, GetNode, GetNode, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, GetNode, LTXVSeparateAVLatent, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, LoadImage, LTXVPreprocess, GetNode, SetNode, VAEDecode, LTXVAudioVAEDecode, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, CLIPTextEncode, SetNode, CR Text, SetNode, SetNode, SetNode, GetNode, LTXVPreprocess, GetNode, GetNode, GetNode, GetNode, VAEDecodeTiled, CLIPTextEncode, LTXVConditioning, LTXVCropGuides, GetNode, LTXVAudioVAEDecode, SamplerCustomAdvanced, SamplerCustomAdvanced, VHS_VideoCombine, VHS_VideoCombine, easy int, CR Text, LoraLoaderModelOnly, DualCLIPLoader, LoadAudio, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, DapaoGeminiInstructionZhenzhenNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 361}
---

# 视频生成/图生视频/LTX-2.3_Gemini3补全分镜提示词+自定义音频+首尾帧+多图段子视频生成_2055962684570521602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055962684570521602.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（127 个）：
- `UNETLoader` ★核心
- `SetNode`
- `SoundFlow_GetLength`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `SetNode`
- `easy imageSize`
- `SetNode`
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `FL_IntToFloat`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `GetNode`
- `ShowText|pysssss`
- `SetNode`
- `GetNode`
- `easy int`
- `GetNode`
- `GetNode`
- `easy imageSize`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LTXVPreprocess`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CR Text`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVCropGuides`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy int`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LoadAudio`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `DapaoGeminiInstructionZhenzhenNode`

## 关键参数

- `width` = `361`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（63/127）

**有卡**：`UNETLoader`、`SoundFlow_GetLength`、`VAELoaderKJ`、`CFGGuider`、`easy imageSize`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVConditioning`、`FL_IntToFloat`、`RandomNoise`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageRangeFromBatch`、`easy int`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`VAEDecode`、`LTXVAudioVAEDecode`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`CR Text`、`VAEDecodeTiled`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`LoadAudio`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplaceKJ`、`DapaoGeminiInstructionZhenzhenNode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
