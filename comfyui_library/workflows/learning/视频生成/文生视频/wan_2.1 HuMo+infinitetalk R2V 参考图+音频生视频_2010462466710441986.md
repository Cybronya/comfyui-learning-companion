---
key: 视频生成/文生视频/wan_2.1 HuMo+infinitetalk R2V 参考图+音频生视频_2010462466710441986.json
name: wan_2.1 HuMo+infinitetalk R2V 参考图+音频生视频_2010462466710441986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan_2.1 HuMo+infinitetalk R2V 参考图+音频生视频_2010462466710441986.json
hash: 0831ff26c6b163cb
coverage: 0.338028
learned_at: 2026-10-11 03:07:14
nodes: [SetNode, Note, PreviewImage, LynxEncodeFaceIP, WanVideoTextEncodeCached, SetNode, MultiTalkSilentEmbeds, CLIPVisionLoader, easy showAnything, easy showAnything, SetNode, SetNode, WanVideoAddLynxEmbeds, WanVideoExtraModelSelect, WanVideoExtraModelSelect, AudioSeparation, SetNode, WanVideoClipVisionEncode, GetNode, SetNode, GetNode, GetNode, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, 孤海图像组合批次, SetNode, GetNode, ImageResizeKJ, SetNode, GetImageSize, GetImageRangeFromBatch, GetNode, Any Switch (rgthree), GetNode, Bjornulf_ShowInt, Fast Groups Bypasser (rgthree), SaveAudio, ImpactSwitch, GetNode, SetNode, Bjornulf_ShowFloat, SimpleMath+, SetNode, SetNode, ImageSmartSharpen+, easy showAnything, easy showAnything, easy showAnything, PreviewAny, AudioSeparation, easy showAnything, ImageSmartSharpen+, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, Int, Int, SetNode, ImageResizeKJ, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, MultiTalkWav2VecEmbeds, SetNode, GetNode, WanVideoVAELoader, SetNode, GetNode, GetNode, WanVideoDecode, SetNode, GetNode, GetNode, GetNode, GetImageSize, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, 孤海图像组合批次, ImageResizeKJ, LoadLynxResampler, LynxInsightFaceCrop, easy imageRemBg, GetNode, GetImageRangeFromBatch, PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetNode, Fast Groups Bypasser (rgthree), GetNode, WanVideoBlockSwap, MultiTalkModelLoader, WanVideoCombineEmbeds, WanVideoImageToVideoMultiTalk, GetNode, WanVideoLoraSelect, WanVideoTextEncodeCached, GetNode, SetNode, MultiTalkModelLoader, HuMoEmbeds, WanVideoSampler, easy cleanGpuUsed, WhisperModelLoader, DownloadAndLoadWav2VecModel, WanVideoModelLoader, WanVideoTorchCompileSettings, VHS_VideoCombine, SetNode, Note, VHS_LoadAudioUpload, VHS_LoadVideo, easy seed, Text, LoadImage, LoadImage, ImpactSwitch, Fast Groups Bypasser (rgthree), Note]
patterns: []
missing: [ImageSmartSharpen+, ImageSmartSharpen+, SimpleMath+, easy cleanGpuUsed, easy imageRemBg, 孤海图像组合批次, 孤海图像组合批次, easy seed]
discoveries: [次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识, 次要节点 `孤海图像组合批次` 知识库中没有该节点类型的任何知识, 次要节点 `孤海图像组合批次` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan_2.1 HuMo+infinitetalk R2V 参考图+音频生视频_2010462466710441986.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan_2.1 HuMo+infinitetalk R2V 参考图+音频生视频_2010462466710441986.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（142 个）：
- `SetNode`
- `Note`
- `PreviewImage`
- `LynxEncodeFaceIP`
- `WanVideoTextEncodeCached`
- `SetNode`
- `MultiTalkSilentEmbeds`
- `CLIPVisionLoader`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `WanVideoAddLynxEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `AudioSeparation`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `孤海图像组合批次`
- `SetNode`
- `GetNode`
- `ImageResizeKJ`
- `SetNode`
- `GetImageSize`
- `GetImageRangeFromBatch`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `Bjornulf_ShowInt`
- `Fast Groups Bypasser (rgthree)`
- `SaveAudio`
- `ImpactSwitch`
- `GetNode`
- `SetNode`
- `Bjornulf_ShowFloat`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `ImageSmartSharpen+`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `PreviewAny`
- `AudioSeparation`
- `easy showAnything`
- `ImageSmartSharpen+`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `SetNode`
- `ImageResizeKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `孤海图像组合批次`
- `ImageResizeKJ`
- `LoadLynxResampler` ★核心
- `LynxInsightFaceCrop`
- `easy imageRemBg`
- `GetNode`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `WanVideoBlockSwap`
- `MultiTalkModelLoader`
- `WanVideoCombineEmbeds`
- `WanVideoImageToVideoMultiTalk`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `GetNode`
- `SetNode`
- `MultiTalkModelLoader`
- `HuMoEmbeds`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WhisperModelLoader`
- `DownloadAndLoadWav2VecModel`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `SetNode`
- `Note`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `easy seed`
- `Text`
- `LoadImage`
- `LoadImage`
- `ImpactSwitch`
- `Fast Groups Bypasser (rgthree)`
- `Note`

## 知识

覆盖率 **34%**（48/142）

**有卡**：`LynxEncodeFaceIP`、`WanVideoTextEncodeCached`、`MultiTalkSilentEmbeds`、`CLIPVisionLoader`、`WanVideoAddLynxEmbeds`、`WanVideoExtraModelSelect`、`AudioSeparation`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`ImageResizeKJ`、`GetImageSize`、`GetImageRangeFromBatch`、`Bjornulf_ShowInt`、`SaveAudio`、`Bjornulf_ShowFloat`、`Int`、`MultiTalkWav2VecEmbeds`、`WanVideoVAELoader`、`WanVideoDecode`、`LoadLynxResampler`、`LynxInsightFaceCrop`、`WanVideoBlockSwap`、`MultiTalkModelLoader`、`WanVideoCombineEmbeds`、`WanVideoImageToVideoMultiTalk`、`HuMoEmbeds`、`WanVideoSampler`、`WhisperModelLoader`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`VHS_LoadAudioUpload`、`VHS_LoadVideo`、`Text`、`LoadImage`

**缺卡**（8）：`ImageSmartSharpen+`、`ImageSmartSharpen+`、`SimpleMath+`、`easy cleanGpuUsed`、`easy imageRemBg`、`孤海图像组合批次`、`孤海图像组合批次`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、LynxEncodeFaceIP

## 学习发现

- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识
- 次要节点 `孤海图像组合批次` 知识库中没有该节点类型的任何知识
- 次要节点 `孤海图像组合批次` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
