---
key: 视频生成/图生视频/Wan2.1_2.2 low VACE姿势+u3c运镜+对口型multi_infinitetalk_1977065847162314754.json
name: Wan2.1_2.2 low VACE姿势+u3c运镜+对口型multi_infinitetalk_1977065847162314754.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1977065847162314754.json
hash: ec752ea9b81f4820
coverage: 0.433121
learned_at: 2026-10-15 22:32:13
nodes: [PreviewAny, AudioSeparation, GetNode, MultiTalkSilentEmbeds, DownloadAndLoadWav2VecModel, GetNode, SetNode, SetNode, SetNode, PreviewImage, PreviewImage, LoadLynxResampler, SetNode, GetNode, GetNode, GetNode, easy showAnything, GetNode, GetNode, GetNode, GetNode, WanVideoExtraModelSelect, WanVideoVAELoader, ImageResizeKJ, WanVideoDecode, GetNode, VHS_VideoCombine, easy showAnything, GetNode, Audio Cut (mtb), ImageFromBatch+, GetNode, GetNode, SimpleMath+, LynxEncodeFaceIP, easy imageRemBg, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoContextOptions, SetNode, LoadImage, WanVideoUni3C_ControlnetLoader, WanVideoEncode, WanVideoTextEncodeCached, GetNode, SetNode, VHS_VideoCombine, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, Int, easy showAnything, easy showAnything, SetNode, SetNode, DWPreprocessor, GetNode, SetNode, SetNode, WanVideoAddLynxEmbeds, WanVideoExtraModelSelect, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, GetNode, GetNode, GetNode, PreviewImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, GetNode, VHS_LoadVideo, GetNode, GetNode, VHS_LoadVideo, Reroute, Reroute, WanVideoUni3C_embeds, SetNode, GetNode, GetNode, VHS_LoadAudioUpload, SimpleMath+, Reroute, GetNode, GetNode, GetNode, GetNode, ImageResizeKJ, GetNode, WanVideoTextEncodeCached, SetNode, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, SetNode, ImageResizeKJ, FaceProcessorLoader, WanVideoAddStandInLatent, WanVideoEncode, ApplyFaceProcessor, LynxInsightFaceCrop, SetNode, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, ImpactControlBridge, SetNode, easy cleanGpuUsed, GetNode, AIO_Preprocessor, Reroute, GetNode, easy seed, Int, SetNode, SetNode, Int, GetNode, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ImageResizeKJ, SetNode, GetNode, Any Switch (rgthree), PreviewImage, GetNode, GetNode, LayerMask: PersonMaskUltra V2, easy imageRemBg, GetNode, WanVideoVACEEncode, InpaintCropImproved, GetNode, WanVideoSampler, MultiTalkModelLoader, MultiTalkModelLoader, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, CR Text, VHS_VideoCombine, VHS_LoadVideo, MultiTalkWav2VecEmbeds]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1_2.2 low VACE姿势+u3c运镜+对口型multi_infinitetalk_1977065847162314754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1977065847162314754.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（157 个）：
- `PreviewAny`
- `AudioSeparation`
- `GetNode`
- `MultiTalkSilentEmbeds`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `LoadLynxResampler` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoExtraModelSelect`
- `WanVideoVAELoader`
- `ImageResizeKJ`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `easy showAnything`
- `GetNode`
- `Audio Cut (mtb)`
- `ImageFromBatch+`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `LynxEncodeFaceIP`
- `easy imageRemBg`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoContextOptions`
- `SetNode`
- `LoadImage`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Int`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `DWPreprocessor`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoAddLynxEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `Reroute`
- `Reroute`
- `WanVideoUni3C_embeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadAudioUpload`
- `SimpleMath+`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `WanVideoTextEncodeCached`
- `SetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJ`
- `FaceProcessorLoader`
- `WanVideoAddStandInLatent`
- `WanVideoEncode`
- `ApplyFaceProcessor`
- `LynxInsightFaceCrop`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `ImpactControlBridge`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `AIO_Preprocessor`
- `Reroute`
- `GetNode`
- `easy seed`
- `Int`
- `SetNode`
- `SetNode`
- `Int`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJ`
- `SetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `LayerMask: PersonMaskUltra V2`
- `easy imageRemBg`
- `GetNode`
- `WanVideoVACEEncode`
- `InpaintCropImproved`
- `GetNode`
- `WanVideoSampler` ★核心
- `MultiTalkModelLoader`
- `MultiTalkModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `CR Text`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `MultiTalkWav2VecEmbeds`

## 知识

覆盖率 **43%**（68/157）

**有卡**：`AudioSeparation`、`MultiTalkSilentEmbeds`、`DownloadAndLoadWav2VecModel`、`LoadLynxResampler`、`WanVideoExtraModelSelect`、`WanVideoVAELoader`、`ImageResizeKJ`、`WanVideoDecode`、`VHS_VideoCombine`、`Audio Cut (mtb)`、`ImageFromBatch+`、`SimpleMath+`、`LynxEncodeFaceIP`、`easy imageRemBg`、`easy cleanGpuUsed`、`WanVideoContextOptions`、`LoadImage`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`Int`、`DWPreprocessor`、`WanVideoAddLynxEmbeds`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`VHS_LoadVideo`、`WanVideoUni3C_embeds`、`VHS_LoadAudioUpload`、`GetImageSizeAndCount`、`FaceProcessorLoader`、`WanVideoAddStandInLatent`、`ApplyFaceProcessor`、`LynxInsightFaceCrop`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`ImpactControlBridge`、`AIO_Preprocessor`、`easy seed`、`LayerMask: PersonMaskUltra V2`、`WanVideoVACEEncode`、`InpaintCropImproved`、`WanVideoSampler`、`MultiTalkModelLoader`、`CR Text`、`MultiTalkWav2VecEmbeds`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、LoadLynxResampler、easy seed、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode
