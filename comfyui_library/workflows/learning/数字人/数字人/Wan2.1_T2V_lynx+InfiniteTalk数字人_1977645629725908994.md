---
key: 数字人/数字人/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977645629725908994.json
name: Wan2.1_T2V_lynx+InfiniteTalk数字人_1977645629725908994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977645629725908994.json
hash: 744a2116a7e3a93d
coverage: 0.770492
learned_at: 2026-10-26 01:57:47
nodes: [JWInteger, AudioCrop, Int, LoadLynxResampler, CR Integer To String, LoadAudio, JWInteger, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, WanVideoExtraModelSelect, MultiTalkModelLoader, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, MultiTalkWav2VecEmbeds, Note, MarkdownNote, SoundFlow_GetLength, ToInt, MathExpression|pysssss, SaveAudio, SetNode, Text Concatenate, RH_LLMAPI_NODE, easy showAnything, AudioSeparation, CR Text, Wan22PromptSelector, WanVideoEncode, SetNode, LynxInsightFaceCrop, Note, WanVideoEmptyEmbeds, ImageResize+, PreviewImage, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, GetNode, MathExpression|pysssss, Note, WanVideoTextEncodeCached, WanVideoAddLynxEmbeds, WanVideoTextEncodeCached, DownloadAndLoadWav2VecModel, easy cleanGpuUsed, WanVideoSampler, WanVideoDecode, ImageFromBatch+, ImageConcatMulti, GetNode, LoadImage, WanVideoVAELoader, SetNode, SetNode, MathExpression|pysssss, LynxEncodeFaceIP, JWInteger, ImpactSwitch]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977645629725908994.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977645629725908994.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（61 个）：
- `JWInteger`
- `AudioCrop`
- `Int`
- `LoadLynxResampler` ★核心
- `CR Integer To String`
- `LoadAudio`
- `JWInteger`
- `WanVideoTorchCompileSettings`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `MultiTalkModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `MultiTalkWav2VecEmbeds`
- `Note`
- `MarkdownNote`
- `SoundFlow_GetLength`
- `ToInt`
- `MathExpression|pysssss`
- `SaveAudio`
- `SetNode`
- `Text Concatenate`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `AudioSeparation`
- `CR Text`
- `Wan22PromptSelector`
- `WanVideoEncode`
- `SetNode`
- `LynxInsightFaceCrop`
- `Note`
- `WanVideoEmptyEmbeds`
- `ImageResize+`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `MathExpression|pysssss`
- `Note`
- `WanVideoTextEncodeCached`
- `WanVideoAddLynxEmbeds`
- `WanVideoTextEncodeCached`
- `DownloadAndLoadWav2VecModel`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageFromBatch+`
- `ImageConcatMulti`
- `GetNode`
- `LoadImage`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `LynxEncodeFaceIP`
- `JWInteger`
- `ImpactSwitch`

## 知识

覆盖率 **77%**（47/61）

**有卡**：`JWInteger`、`AudioCrop`、`Int`、`LoadLynxResampler`、`CR Integer To String`、`LoadAudio`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`、`MultiTalkModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`MultiTalkWav2VecEmbeds`、`SoundFlow_GetLength`、`ToInt`、`MathExpression|pysssss`、`SaveAudio`、`Text Concatenate`、`RH_LLMAPI_NODE`、`AudioSeparation`、`CR Text`、`Wan22PromptSelector`、`WanVideoEncode`、`LynxInsightFaceCrop`、`WanVideoEmptyEmbeds`、`ImageResize+`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`WanVideoAddLynxEmbeds`、`DownloadAndLoadWav2VecModel`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`、`ImageConcatMulti`、`LoadImage`、`WanVideoVAELoader`、`LynxEncodeFaceIP`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、LynxEncodeFaceIP
