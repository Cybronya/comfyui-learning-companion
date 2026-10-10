---
key: 视频生成/文生视频/多重参考生视频（WAN_BindWeave+TTS+MULTITALK）_1990350029464498177.json
name: 多重参考生视频（WAN_BindWeave+TTS+MULTITALK）_1990350029464498177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/多重参考生视频（WAN_BindWeave+TTS+MULTITALK）_1990350029464498177.json
hash: 10589cad4b1d7bfc
coverage: 0.69
learned_at: 2026-10-11 02:57:40
nodes: [WanVideoDecode, Int, ImageResizeKJv2, ImagePadKJ, ImageResizeKJv2, easy imageRemBg, PreviewImage, SolidMask, InvertMask, easy imageRemBg, InvertMask, PreviewImage, easy imageRemBg, TransparentBGSession+, ImageRemoveBackground+, InvertMask, InvertMask, WanVideoImageToVideoEncode, CLIPVisionLoader, WanVideoClipVisionEncode, MaskBatchMulti, ImageBatchMulti, DrawMaskOnImage, ImageBatchMulti, PreviewImage, PreviewImage, ImageBatchMulti, ImageRemoveBackground+, InvertMask, DrawMaskOnImage, InvertMask, ImageBatchMulti, WanVideoEncodeLatentBatch, TransparentBGSession+, VHS_VideoCombine, easy downloadIndexTTSAndLoadModel, easy indexTTSGenerateSimple, LayerUtility: PurgeVRAM, Reroute, CR Prompt Text, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, SetNode, PreviewAny, CLIPVisionLoader, AudioSeparation, Reroute, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, GetImageRangeFromBatch, WanVideoEncode, GetImageSizeAndCount, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoTextEncodeCached, WanVideoSampler, PrimitiveFloat, GetNode, VHS_VideoCombine, CR Prompt Text, LoadAudio, SaveAudio, LayerUtility: PurgeVRAM V2, WanVideoDecode, GetImageSizeAndCount, GetImageRangeFromBatch, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, WanVideoLoraSelect, PreviewAny, WanVideoSetBlockSwap, WanVideoBlockSwap, JWInteger, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoTextEncode, PreviewAny, WanVideoAddBindweaveEmbeds, LayerUtility: PurgeVRAM V2, GetImageSizeAndCount, VHS_VideoCombine, MathExpression|pysssss, WanVideoDecode, ImageResizeKJv2, TextImageEncodeQwenVL, PreviewImage, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, WanVideoSampler, CLIPLoader, LoadImage, LoadImage, WanVideoTorchCompileSettings, RMBG, TextInput_, LoadImage]
patterns: []
missing: [ImageFromBatch+, ImageRemoveBackground+, ImageRemoveBackground+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, TransparentBGSession+, TransparentBGSession+, easy downloadIndexTTSAndLoadModel, easy imageRemBg, easy imageRemBg, easy imageRemBg, easy indexTTSGenerateSimple, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageRemoveBackground+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageRemoveBackground+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `TransparentBGSession+` 知识库中没有该节点类型的任何知识, 次要节点 `TransparentBGSession+` 知识库中没有该节点类型的任何知识, 次要节点 `easy downloadIndexTTSAndLoadModel` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexTTSGenerateSimple` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/多重参考生视频（WAN_BindWeave+TTS+MULTITALK）_1990350029464498177.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/多重参考生视频（WAN_BindWeave+TTS+MULTITALK）_1990350029464498177.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（100 个）：
- `WanVideoDecode`
- `Int`
- `ImageResizeKJv2`
- `ImagePadKJ`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `PreviewImage`
- `SolidMask`
- `InvertMask`
- `easy imageRemBg`
- `InvertMask`
- `PreviewImage`
- `easy imageRemBg`
- `TransparentBGSession+`
- `ImageRemoveBackground+`
- `InvertMask`
- `InvertMask`
- `WanVideoImageToVideoEncode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `MaskBatchMulti`
- `ImageBatchMulti`
- `DrawMaskOnImage`
- `ImageBatchMulti`
- `PreviewImage`
- `PreviewImage`
- `ImageBatchMulti`
- `ImageRemoveBackground+`
- `InvertMask`
- `DrawMaskOnImage`
- `InvertMask`
- `ImageBatchMulti`
- `WanVideoEncodeLatentBatch`
- `TransparentBGSession+`
- `VHS_VideoCombine`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSGenerateSimple`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `PreviewAny`
- `CLIPVisionLoader`
- `AudioSeparation`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `GetImageSizeAndCount`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `PrimitiveFloat`
- `GetNode`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `LoadAudio`
- `SaveAudio`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoLoraSelect`
- `PreviewAny`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `JWInteger`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `PreviewAny`
- `WanVideoAddBindweaveEmbeds`
- `LayerUtility: PurgeVRAM V2`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `WanVideoDecode`
- `ImageResizeKJv2`
- `TextImageEncodeQwenVL`
- `PreviewImage`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `RMBG`
- `TextInput_`
- `LoadImage`

## 知识

覆盖率 **69%**（69/100）

**有卡**：`WanVideoDecode`、`Int`、`ImageResizeKJv2`、`ImagePadKJ`、`SolidMask`、`InvertMask`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`MaskBatchMulti`、`ImageBatchMulti`、`DrawMaskOnImage`、`WanVideoEncodeLatentBatch`、`VHS_VideoCombine`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`AudioSeparation`、`GetImageRangeFromBatch`、`WanVideoEncode`、`GetImageSizeAndCount`、`WanVideoImageToVideoMultiTalk`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`LoadAudio`、`SaveAudio`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`JWInteger`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`WanVideoAddBindweaveEmbeds`、`TextImageEncodeQwenVL`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`CLIPLoader`、`LoadImage`、`WanVideoTorchCompileSettings`、`RMBG`、`TextInput_`

**缺卡**（18）：`ImageFromBatch+`、`ImageRemoveBackground+`、`ImageRemoveBackground+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`TransparentBGSession+`、`TransparentBGSession+`、`easy downloadIndexTTSAndLoadModel`、`easy imageRemBg`、`easy imageRemBg`、`easy imageRemBg`、`easy indexTTSGenerateSimple`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：CLIPLoader、LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageRemoveBackground+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageRemoveBackground+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `TransparentBGSession+` 知识库中没有该节点类型的任何知识
- 次要节点 `TransparentBGSession+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy downloadIndexTTSAndLoadModel` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexTTSGenerateSimple` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
