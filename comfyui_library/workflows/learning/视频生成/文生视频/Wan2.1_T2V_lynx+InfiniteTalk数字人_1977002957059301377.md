---
key: 视频生成/文生视频/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977002957059301377.json
name: Wan2.1_T2V_lynx+InfiniteTalk数字人_1977002957059301377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977002957059301377.json
hash: 5c70bd038bec5c79
coverage: 0.803279
learned_at: 2026-10-15 22:47:08
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, LoadLynxResampler, Wan22PromptSelector, JWInteger, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, SetNode, ImpactSwitch, Text Concatenate, easy showAnything, Note, MarkdownNote, RH_LLMAPI_NODE, WanVideoExtraModelSelect, WanVideoDecode, ImageFromBatch+, ImageConcatMulti, CR Text, WanVideoSampler, JWInteger, JWInteger, GetNode, LynxEncodeFaceIP, LynxInsightFaceCrop, SetNode, ImageResize+, WanVideoTextEncodeCached, Note, Note, PreviewImage, CR Integer To String, AudioCrop, SoundFlow_GetLength, ToInt, MathExpression|pysssss, AudioSeparation, MathExpression|pysssss, SaveAudio, LoadAudio, Int, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, WanVideoVAELoader, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkModelLoader, easy cleanGpuUsed, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, WanVideoTextEncodeCached, PreviewImage, WanVideoEncode, WanVideoAddLynxEmbeds, WanVideoEmptyEmbeds]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977002957059301377.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977002957059301377.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（61 个）：
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoExtraModelSelect`
- `LoadLynxResampler` ★核心
- `Wan22PromptSelector`
- `JWInteger`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `ImpactSwitch`
- `Text Concatenate`
- `easy showAnything`
- `Note`
- `MarkdownNote`
- `RH_LLMAPI_NODE`
- `WanVideoExtraModelSelect`
- `WanVideoDecode`
- `ImageFromBatch+`
- `ImageConcatMulti`
- `CR Text`
- `WanVideoSampler` ★核心
- `JWInteger`
- `JWInteger`
- `GetNode`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `SetNode`
- `ImageResize+`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `PreviewImage`
- `CR Integer To String`
- `AudioCrop`
- `SoundFlow_GetLength`
- `ToInt`
- `MathExpression|pysssss`
- `AudioSeparation`
- `MathExpression|pysssss`
- `SaveAudio`
- `LoadAudio`
- `Int`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoVAELoader`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkModelLoader`
- `easy cleanGpuUsed`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `WanVideoTextEncodeCached`
- `PreviewImage`
- `WanVideoEncode`
- `WanVideoAddLynxEmbeds`
- `WanVideoEmptyEmbeds`

## 知识

覆盖率 **80%**（49/61）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`、`LoadLynxResampler`、`Wan22PromptSelector`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`Text Concatenate`、`RH_LLMAPI_NODE`、`WanVideoDecode`、`ImageFromBatch+`、`ImageConcatMulti`、`CR Text`、`WanVideoSampler`、`LynxEncodeFaceIP`、`LynxInsightFaceCrop`、`ImageResize+`、`WanVideoTextEncodeCached`、`CR Integer To String`、`AudioCrop`、`SoundFlow_GetLength`、`ToInt`、`MathExpression|pysssss`、`AudioSeparation`、`SaveAudio`、`LoadAudio`、`Int`、`VHS_VideoCombine`、`LoadImage`、`WanVideoVAELoader`、`MultiTalkModelLoader`、`easy cleanGpuUsed`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`WanVideoEncode`、`WanVideoAddLynxEmbeds`、`WanVideoEmptyEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、LynxEncodeFaceIP
