---
key: 视频生成/图生视频/Wan2.2 + SVI2：三镜头带货lyan_2021226831017418753.json
name: Wan2.2 + SVI2：三镜头带货lyan_2021226831017418753.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 + SVI2：三镜头带货lyan_2021226831017418753.json
hash: b5659ddab0ba6133
coverage: 0.672897
learned_at: 2026-10-15 22:35:08
nodes: [WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSampler, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, WanVideoLoraSelect, WanVideoBlockSwap, SetNode, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, InvertMask, WanVideoLoraSelect, WanVideoImageToVideoEncode, GetNode, WanVideoSampler, INTConstant, INTConstant, GetNode, GetNode, GetNode, WanVideoTorchCompileSettings, GetNode, GetNode, DF_Int_to_Float, SetNode, SetNode, GetNode, SetNode, GetNode, WanVideoTextEncode, WanVideoDecode, RepeatImageBatch, WanVideoVACEStartToEndFrame, GetNode, MathExpression|pysssss, JWInteger, JWInteger, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, InvertMask, WanVideoImageToVideoEncode, GetNode, WanVideoSampler, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, RepeatImageBatch, WanVideoVACEStartToEndFrame, GetNode, MathExpression|pysssss, VHS_VideoCombine, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, InvertMask, WanVideoImageToVideoEncode, GetNode, WanVideoSampler, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncode, RepeatImageBatch, WanVideoVACEStartToEndFrame, GetNode, MathExpression|pysssss, VHS_VideoCombine, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, WanVideoDecode, WanVideoDecode, ImageBatchMulti, SaveAudioMP3, MarkdownNote, IndexTTSRun, VHS_VideoCombine, LoadAudio, JWInteger, MultiLinePromptIndex, LoadImage, LoadImage, LoadImage, CR Text, CR Text, JWInteger, JWInteger, CR Text, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 + SVI2：三镜头带货lyan_2021226831017418753.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021226831017418753.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（107 个）：
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `InvertMask`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `GetNode`
- `DF_Int_to_Float`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `RepeatImageBatch`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `MathExpression|pysssss`
- `JWInteger`
- `JWInteger`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `InvertMask`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `RepeatImageBatch`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `InvertMask`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncode`
- `RepeatImageBatch`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoDecode`
- `ImageBatchMulti`
- `SaveAudioMP3`
- `MarkdownNote`
- `IndexTTSRun`
- `VHS_VideoCombine`
- `LoadAudio`
- `JWInteger`
- `MultiLinePromptIndex`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `CR Text`
- `JWInteger`
- `JWInteger`
- `CR Text`
- `WanVideoTextEncode`

## 知识

覆盖率 **67%**（72/107）

**有卡**：`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`InvertMask`、`WanVideoImageToVideoEncode`、`INTConstant`、`WanVideoTorchCompileSettings`、`DF_Int_to_Float`、`WanVideoTextEncode`、`WanVideoDecode`、`RepeatImageBatch`、`WanVideoVACEStartToEndFrame`、`MathExpression|pysssss`、`JWInteger`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`ImageBatchMulti`、`SaveAudioMP3`、`IndexTTSRun`、`LoadAudio`、`MultiLinePromptIndex`、`LoadImage`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
