---
key: 视频生成/文生视频/无限时长视频转绘Lynx+InfiniteTalk+VACE_1976202797450428418.json
name: 无限时长视频转绘Lynx+InfiniteTalk+VACE_1976202797450428418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/无限时长视频转绘Lynx+InfiniteTalk+VACE_1976202797450428418.json
hash: 1f7fcc2747fca0db
coverage: 0.828283
learned_at: 2026-10-10 23:13:16
nodes: [ImageResizeKJv2, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoVAELoader, GetImageSizeAndCount, ImageResizeKJv2, GetNode, VHS_VideoCombine, WanVideoDecode, GetNode, GetNode, GetImageRangeFromBatch, WanVideoVACEStartToEndFrame, WanVideoSampler, easy batchAnything, ImageBatch, GetNode, GetImageSizeAndCount, SimpleMath+, WanVideoDecode, GetImageRangeFromBatch, GetImageRangeFromBatch, SetNode, INTConstant, VHS_BatchManager, GetImageRangeFromBatch, MathExpression|pysssss, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, LoadLynxResampler, LynxEncodeFaceIP, WanVideoTextEncodeCached, LoadLynxResampler, LynxEncodeFaceIP, WanVideoTextEncodeCached, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoExtraModelSelect, WanVideoSetBlockSwap, WanVideoExtraModelSelect, LynxInsightFaceCrop, WanVideoAddLynxEmbeds, LynxInsightFaceCrop, WanVideoModelLoader, JWInteger, AudioSeparation, AudioSeparation, Wav2VecModelLoader, MultiTalkWav2VecEmbeds, MultiTalkModelLoader, MathExpression|pysssss, ACE_AudioCrop, floatToText _O, floatToText _O, MultiTalkModelLoader, LoadAudio, Wav2VecModelLoader, MultiTalkWav2VecEmbeds, WanVideoVAELoader, LoadWanVideoT5TextEncoder, VHS_VideoCombine, VHS_VideoCombine, WanVideoTextEncode, WanVideoTextEncode, ImageResizeKJv2, WanVideoVACEEncode, ImageResizeKJv2, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoModelLoader, easy forLoopEnd, easy seed, DWPreprocessor, DWPreprocessor, easy forLoopStart, VHS_VideoCombine, String Literal, LoadImage, VHS_LoadVideo, Int, Int, WanVideoSampler, WanVideoVACEEncode, WanVideoAddLynxEmbeds, GetImageRangeFromBatch, VHS_LoadVideo, ACE_AudioCrop, MathExpression|pysssss, MathExpression|pysssss, VHS_VideoCombine]
patterns: []
missing: [MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, String Literal, easy batchAnything, easy forLoopEnd, easy forLoopStart, floatToText _O, floatToText _O, easy seed]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `floatToText _O` 知识库中没有该节点类型的任何知识, 次要节点 `floatToText _O` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/无限时长视频转绘Lynx+InfiniteTalk+VACE_1976202797450428418.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/无限时长视频转绘Lynx+InfiniteTalk+VACE_1976202797450428418.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（99 个）：
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `WanVideoVACEStartToEndFrame`
- `WanVideoSampler` ★核心
- `easy batchAnything`
- `ImageBatch`
- `GetNode`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `WanVideoDecode`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `SetNode`
- `INTConstant`
- `VHS_BatchManager`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `LoadLynxResampler` ★核心
- `LynxEncodeFaceIP`
- `WanVideoTextEncodeCached`
- `LoadLynxResampler` ★核心
- `LynxEncodeFaceIP`
- `WanVideoTextEncodeCached`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoExtraModelSelect`
- `WanVideoSetBlockSwap`
- `WanVideoExtraModelSelect`
- `LynxInsightFaceCrop`
- `WanVideoAddLynxEmbeds`
- `LynxInsightFaceCrop`
- `WanVideoModelLoader`
- `JWInteger`
- `AudioSeparation`
- `AudioSeparation`
- `Wav2VecModelLoader`
- `MultiTalkWav2VecEmbeds`
- `MultiTalkModelLoader`
- `MathExpression|pysssss`
- `ACE_AudioCrop`
- `floatToText _O`
- `floatToText _O`
- `MultiTalkModelLoader`
- `LoadAudio`
- `Wav2VecModelLoader`
- `MultiTalkWav2VecEmbeds`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `WanVideoVACEEncode`
- `ImageResizeKJv2`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `easy forLoopEnd`
- `easy seed`
- `DWPreprocessor`
- `DWPreprocessor`
- `easy forLoopStart`
- `VHS_VideoCombine`
- `String Literal`
- `LoadImage`
- `VHS_LoadVideo`
- `Int`
- `Int`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `WanVideoAddLynxEmbeds`
- `GetImageRangeFromBatch`
- `VHS_LoadVideo`
- `ACE_AudioCrop`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_VideoCombine`

## 知识

覆盖率 **83%**（82/99）

**有卡**：`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoDecode`、`GetImageRangeFromBatch`、`WanVideoSampler`、`ImageBatch`、`INTConstant`、`VHS_BatchManager`、`WanVideoExtraModelSelect`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LoadLynxResampler`、`LynxEncodeFaceIP`、`WanVideoTextEncodeCached`、`LynxInsightFaceCrop`、`WanVideoAddLynxEmbeds`、`WanVideoModelLoader`、`JWInteger`、`AudioSeparation`、`Wav2VecModelLoader`、`MultiTalkWav2VecEmbeds`、`MultiTalkModelLoader`、`ACE_AudioCrop`、`LoadAudio`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`DWPreprocessor`、`LoadImage`、`VHS_LoadVideo`、`Int`

**缺卡**（12）：`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`String Literal`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`floatToText _O`、`floatToText _O`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `floatToText _O` 知识库中没有该节点类型的任何知识
- 次要节点 `floatToText _O` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
