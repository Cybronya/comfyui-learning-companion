---
key: 视频生成/文生视频/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977002957059301377.json
name: Wan2.1_T2V_lynx+InfiniteTalk数字人_1977002957059301377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977002957059301377.json
hash: 5c70bd038bec5c79
coverage: 0.655738
learned_at: 2026-10-10 23:06:35
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, LoadLynxResampler, Wan22PromptSelector, JWInteger, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, SetNode, ImpactSwitch, Text Concatenate, easy showAnything, Note, MarkdownNote, RH_LLMAPI_NODE, WanVideoExtraModelSelect, WanVideoDecode, ImageFromBatch+, ImageConcatMulti, CR Text, WanVideoSampler, JWInteger, JWInteger, GetNode, LynxEncodeFaceIP, LynxInsightFaceCrop, SetNode, ImageResize+, WanVideoTextEncodeCached, Note, Note, PreviewImage, CR Integer To String, AudioCrop, SoundFlow_GetLength, ToInt, MathExpression|pysssss, AudioSeparation, MathExpression|pysssss, SaveAudio, LoadAudio, Int, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, WanVideoVAELoader, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkModelLoader, easy cleanGpuUsed, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, WanVideoTextEncodeCached, PreviewImage, WanVideoEncode, WanVideoAddLynxEmbeds, WanVideoEmptyEmbeds]
patterns: []
missing: [CR Integer To String, CR Text, ImageFromBatch+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, Text Concatenate, easy cleanGpuUsed, ImageResize+]
discoveries: [次要节点 `CR Integer To String` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
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

覆盖率 **66%**（40/61）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`、`LoadLynxResampler`、`Wan22PromptSelector`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`RH_LLMAPI_NODE`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoSampler`、`LynxEncodeFaceIP`、`LynxInsightFaceCrop`、`WanVideoTextEncodeCached`、`AudioCrop`、`SoundFlow_GetLength`、`ToInt`、`AudioSeparation`、`SaveAudio`、`LoadAudio`、`Int`、`VHS_VideoCombine`、`LoadImage`、`WanVideoVAELoader`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`WanVideoEncode`、`WanVideoAddLynxEmbeds`、`WanVideoEmptyEmbeds`

**缺卡**（9）：`CR Integer To String`、`CR Text`、`ImageFromBatch+`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`Text Concatenate`、`easy cleanGpuUsed`、`ImageResize+`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、LynxEncodeFaceIP

## 学习发现

- 次要节点 `CR Integer To String` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
