---
key: 视频生成/图生视频/教学用wan2.2 video工作流_1996141035090821122.json
name: 教学用wan2.2 video工作流_1996141035090821122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1996141035090821122.json
hash: df4614d4b103dff6
coverage: 0.797753
learned_at: 2026-10-15 22:33:25
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, SimpleMath+, CLIPTextEncode, SimpleMath+, UNETLoader, UNETLoader, wanBlock_Swap, VAELoader, CLIPLoader, Int, PrimitiveStringMultiline, LoadImage, Int, CLIPVisionLoader, CLIPTextEncode, ImageResizeKJv2, CLIPVisionEncode, WanImageToVideo, WanMoeKSampler, VHS_VideoCombine, RIFE VFI, VideoCombine_Adv, VHS_VideoCombine, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPTextEncode, UNETLoader, UNETLoader, wanBlock_Swap, wanBlock_Swap, VAELoader, CLIPLoader, PrimitiveStringMultiline, Int, CLIPTextEncode, CLIPVisionEncode, WanMoeKSampler, VAEDecode, VHS_VideoCombine, RIFE VFI, VideoCombine_Adv, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, CLIPVisionLoader, Reroute, CLIPVisionEncode, Int, Fast Groups Bypasser (rgthree), ImageResizeKJv2, WanFirstLastFrameToVideo, SimpleMath+, SimpleMath+, ImageResizeKJv2, VHS_VideoCombine, RunningHub StepAudioEditX ModelLoader, RunningHub StepAudioEditX Sampler(Emotion), RunningHub StepAudioEditX ModelLoader, RunningHub StepAudioEditX Sampler(Paralinguistic), Note, CR Prompt Text, SaveAudio, CR Prompt Text, LoadAudio, RunningHub StepAudioEditX ModelLoader, RunningHub StepAudioEditX Sampler(Style), SaveAudio, LoadAudio, SaveAudio, LoadAudio, CR Prompt Text, CR Prompt Text, Fast Groups Bypasser (rgthree), easy downloadIndexTTSAndLoadModel, Note, LoadAudio, easy indexTTSGenerateSimple, SaveAudio, easy downloadIndexTTSAndLoadModel, easy indexTTSGenerateSimple, SaveAudio, SaveAudio, easy indexTTSEmotionVector, LoadAudio, Note, easy downloadIndexTTSAndLoadModel, easy indexTTSAudioMerge, easy indexTTSGenerateSimple, CR Prompt Text, LoadAudio, LoadAudio, GetNode, WanVideoClipVisionEncode, ImageConcatMulti, WanVideoClipVisionEncode, GetNode, ImageConcatMulti, INTConstant, INTConstant, INTConstant, LoadImage, GetNode, ImageResizeKJv2, SetNode, GetNode, WanVideoImageToVideoEncode, GetNode, GetNode, WanVideoTorchCompileSettings, Note, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoVAELoader, SetNode, CLIPVisionLoader, SetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, GetImageSizeAndCount, SetNode, DrawViTPose, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, WanVideoEncode, WanVideoAddSteadyDancerEmbeds, GetNode, VHS_VideoCombine, GetImageRangeFromBatch, WanVideoContextOptions, WanVideoTextEncodeCached, PrimitiveStringMultiline, VHS_VideoCombine, GetNode, WanVideoSamplerSettings, PrimitiveNode, PrimitiveNode, WanVideoScheduler, WanVideoSamplerFromSettings, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, GetNode, GetNode, INTConstant, SetNode, INTConstant, AudioSeparation, ToInt, easy showAnything, easy cleanGpuUsed, DownloadAndLoadWav2VecModel, SetNode, WanVideoDecode, Anything Everywhere, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, ImageResizeKJv2, INTConstant, easy showAnything, SimpleMath+, WanVideoImageToVideoMultiTalk, GetNode, GetNode, CLIPVisionLoader, easy cleanGpuUsed, WanVideoTextEncode, WanVideoEncode, GetNode, SimpleMath+, SetNode, intToFloat _O, WanVideoSampler, VHS_VideoInfo, easy showAnything, VHS_LoadVideo, VHS_VideoCombine, MultiTalkWav2VecEmbeds, SaveAudio, RH_GetAudioDuration, WanVideoClipVisionEncode, LoadAudio, AudioCrop, SaveAudio, GetImage, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), WanVideoTorchCompileSettings, easy int, SeCVideoSegmentation, ImageFromBatch, ClothesSegment, SeCModelLoader, easy int, GrowMask, BlockifyMask, DrawMaskOnImage, DrawViTPose, PoseAndFaceDetection, ImageBlend, PreviewImage, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, CLIPVisionLoader, Evaluate Integers, WanVideoSampler, WanVideoTextEncodeCached, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoContextOptions, PreviewImage, PreviewImage, VHS_VideoCombine, LoadImage, OnnxDetectionModelLoader, VHS_VideoCombine, WanVideoBlockSwap, LoadImage, ImageConcatMulti, PrimitiveStringMultiline, easy int, GetImageSizeAndCount, easy showAnything, VHS_VideoInfoLoaded, VHS_VideoCombine, WanVideoDecode, WanVideoVAELoader, ImageConcatMulti, PlaySound|pysssss, easy int, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoadAudio, SaveAudio, easy indexTTSEmotionVector, Note, easy downloadIndexTTSAndLoadModel, MarkdownNote, easy indexTTSGenerateSimple, Reroute, VHS_LoadVideo, Fast Groups Bypasser (rgthree), wanBlock_Swap, LoadImage, VAEDecode, SaveImage, Note]
patterns: []
missing: []
parameters: {"cfg": 7, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/教学用wan2.2 video工作流_1996141035090821122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996141035090821122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（267 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlock_Swap`
- `VAELoader`
- `CLIPLoader`
- `Int`
- `PrimitiveStringMultiline`
- `LoadImage`
- `Int`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `WanImageToVideo`
- `WanMoeKSampler` ★核心
- `VHS_VideoCombine`
- `RIFE VFI`
- `VideoCombine_Adv`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlock_Swap`
- `wanBlock_Swap`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `Int`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RIFE VFI`
- `VideoCombine_Adv`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CLIPVisionLoader`
- `Reroute`
- `CLIPVisionEncode`
- `Int`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `WanFirstLastFrameToVideo`
- `SimpleMath+`
- `SimpleMath+`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `RunningHub StepAudioEditX ModelLoader`
- `RunningHub StepAudioEditX Sampler(Emotion)` ★核心
- `RunningHub StepAudioEditX ModelLoader`
- `RunningHub StepAudioEditX Sampler(Paralinguistic)` ★核心
- `Note`
- `CR Prompt Text`
- `SaveAudio`
- `CR Prompt Text`
- `LoadAudio`
- `RunningHub StepAudioEditX ModelLoader`
- `RunningHub StepAudioEditX Sampler(Style)` ★核心
- `SaveAudio`
- `LoadAudio`
- `SaveAudio`
- `LoadAudio`
- `CR Prompt Text`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `easy downloadIndexTTSAndLoadModel`
- `Note`
- `LoadAudio`
- `easy indexTTSGenerateSimple`
- `SaveAudio`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSGenerateSimple`
- `SaveAudio`
- `SaveAudio`
- `easy indexTTSEmotionVector`
- `LoadAudio`
- `Note`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSAudioMerge`
- `easy indexTTSGenerateSimple`
- `CR Prompt Text`
- `LoadAudio`
- `LoadAudio`
- `GetNode`
- `WanVideoClipVisionEncode`
- `ImageConcatMulti`
- `WanVideoClipVisionEncode`
- `GetNode`
- `ImageConcatMulti`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `Note`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `GetImageSizeAndCount`
- `SetNode`
- `DrawViTPose`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `GetNode`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `WanVideoContextOptions`
- `WanVideoTextEncodeCached`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoSamplerSettings` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoScheduler`
- `WanVideoSamplerFromSettings` ★核心
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `AudioSeparation`
- `ToInt`
- `easy showAnything`
- `easy cleanGpuUsed`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `WanVideoDecode`
- `Anything Everywhere`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `ImageResizeKJv2`
- `INTConstant`
- `easy showAnything`
- `SimpleMath+`
- `WanVideoImageToVideoMultiTalk`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoEncode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `intToFloat _O`
- `WanVideoSampler` ★核心
- `VHS_VideoInfo`
- `easy showAnything`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `MultiTalkWav2VecEmbeds`
- `SaveAudio`
- `RH_GetAudioDuration`
- `WanVideoClipVisionEncode`
- `LoadAudio`
- `AudioCrop`
- `SaveAudio`
- `GetImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoTorchCompileSettings`
- `easy int`
- `SeCVideoSegmentation`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCModelLoader`
- `easy int`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `ImageBlend`
- `PreviewImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `Evaluate Integers`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `LoadImage`
- `ImageConcatMulti`
- `PrimitiveStringMultiline`
- `easy int`
- `GetImageSizeAndCount`
- `easy showAnything`
- `VHS_VideoInfoLoaded`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `ImageConcatMulti`
- `PlaySound|pysssss`
- `easy int`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `SaveAudio`
- `easy indexTTSEmotionVector`
- `Note`
- `easy downloadIndexTTSAndLoadModel`
- `MarkdownNote`
- `easy indexTTSGenerateSimple`
- `Reroute`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `wanBlock_Swap`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Note`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `7`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **80%**（213/267）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`SimpleMath+`、`CLIPTextEncode`、`UNETLoader`、`wanBlock_Swap`、`VAELoader`、`CLIPLoader`、`Int`、`LoadImage`、`CLIPVisionLoader`、`ImageResizeKJv2`、`CLIPVisionEncode`、`WanImageToVideo`、`WanMoeKSampler`、`VHS_VideoCombine`、`RIFE VFI`、`VideoCombine_Adv`、`VAEDecode`、`WanFirstLastFrameToVideo`、`RunningHub StepAudioEditX ModelLoader`、`RunningHub StepAudioEditX Sampler(Emotion)`、`RunningHub StepAudioEditX Sampler(Paralinguistic)`、`CR Prompt Text`、`SaveAudio`、`LoadAudio`、`RunningHub StepAudioEditX Sampler(Style)`、`easy downloadIndexTTSAndLoadModel`、`easy indexTTSGenerateSimple`、`easy indexTTSEmotionVector`、`easy indexTTSAudioMerge`、`WanVideoClipVisionEncode`、`ImageConcatMulti`、`INTConstant`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`DrawViTPose`、`WanVideoEncode`、`WanVideoAddSteadyDancerEmbeds`、`GetImageRangeFromBatch`、`WanVideoContextOptions`、`WanVideoTextEncodeCached`、`WanVideoSamplerSettings`、`WanVideoScheduler`、`WanVideoSamplerFromSettings`、`VHS_LoadVideo`、`WanVideoDecode`、`AudioSeparation`、`ToInt`、`easy cleanGpuUsed`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`MultiTalkModelLoader`、`WanVideoImageToVideoMultiTalk`、`WanVideoTextEncode`、`intToFloat _O`、`WanVideoSampler`、`VHS_VideoInfo`、`MultiTalkWav2VecEmbeds`、`RH_GetAudioDuration`、`AudioCrop`、`GetImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`SeCVideoSegmentation`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ImageBlend`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoLoraSelectMulti`、`Evaluate Integers`、`WanVideoAnimateEmbeds`、`VHS_VideoInfoLoaded`、`PlaySound|pysssss`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler
