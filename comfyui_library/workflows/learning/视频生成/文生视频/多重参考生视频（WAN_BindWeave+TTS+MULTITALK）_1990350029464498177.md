---
key: 视频生成/文生视频/多重参考生视频（WAN_BindWeave+TTS+MULTITALK）_1990350029464498177.json
name: 多重参考生视频（WAN_BindWeave+TTS+MULTITALK）_1990350029464498177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/多重参考生视频（WAN_BindWeave+TTS+MULTITALK）_1990350029464498177.json
hash: 10589cad4b1d7bfc
coverage: 0.87
learned_at: 2026-10-15 22:48:31
nodes: [WanVideoDecode, Int, ImageResizeKJv2, ImagePadKJ, ImageResizeKJv2, easy imageRemBg, PreviewImage, SolidMask, InvertMask, easy imageRemBg, InvertMask, PreviewImage, easy imageRemBg, TransparentBGSession+, ImageRemoveBackground+, InvertMask, InvertMask, WanVideoImageToVideoEncode, CLIPVisionLoader, WanVideoClipVisionEncode, MaskBatchMulti, ImageBatchMulti, DrawMaskOnImage, ImageBatchMulti, PreviewImage, PreviewImage, ImageBatchMulti, ImageRemoveBackground+, InvertMask, DrawMaskOnImage, InvertMask, ImageBatchMulti, WanVideoEncodeLatentBatch, TransparentBGSession+, VHS_VideoCombine, easy downloadIndexTTSAndLoadModel, easy indexTTSGenerateSimple, LayerUtility: PurgeVRAM, Reroute, CR Prompt Text, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, SetNode, PreviewAny, CLIPVisionLoader, AudioSeparation, Reroute, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, GetImageRangeFromBatch, WanVideoEncode, GetImageSizeAndCount, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoTextEncodeCached, WanVideoSampler, PrimitiveFloat, GetNode, VHS_VideoCombine, CR Prompt Text, LoadAudio, SaveAudio, LayerUtility: PurgeVRAM V2, WanVideoDecode, GetImageSizeAndCount, GetImageRangeFromBatch, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, WanVideoLoraSelect, PreviewAny, WanVideoSetBlockSwap, WanVideoBlockSwap, JWInteger, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoTextEncode, PreviewAny, WanVideoAddBindweaveEmbeds, LayerUtility: PurgeVRAM V2, GetImageSizeAndCount, VHS_VideoCombine, MathExpression|pysssss, WanVideoDecode, ImageResizeKJv2, TextImageEncodeQwenVL, PreviewImage, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, WanVideoSampler, CLIPLoader, LoadImage, LoadImage, WanVideoTorchCompileSettings, RMBG, TextInput_, LoadImage]
patterns: []
missing: []
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

覆盖率 **87%**（87/100）

**有卡**：`WanVideoDecode`、`Int`、`ImageResizeKJv2`、`ImagePadKJ`、`easy imageRemBg`、`SolidMask`、`InvertMask`、`TransparentBGSession+`、`ImageRemoveBackground+`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`MaskBatchMulti`、`ImageBatchMulti`、`DrawMaskOnImage`、`WanVideoEncodeLatentBatch`、`VHS_VideoCombine`、`easy downloadIndexTTSAndLoadModel`、`easy indexTTSGenerateSimple`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`AudioSeparation`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageRangeFromBatch`、`WanVideoEncode`、`GetImageSizeAndCount`、`WanVideoImageToVideoMultiTalk`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`LoadAudio`、`SaveAudio`、`LayerUtility: PurgeVRAM V2`、`ImageFromBatch+`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`JWInteger`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`WanVideoAddBindweaveEmbeds`、`MathExpression|pysssss`、`TextImageEncodeQwenVL`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`CLIPLoader`、`LoadImage`、`WanVideoTorchCompileSettings`、`RMBG`、`TextInput_`

**用到的条目**：CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
