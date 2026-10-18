---
key: 视频生成/文生视频/一致性数字人Stand-In VACE MultiTalk 跳舞唱歌_1956601667196211201.json
name: 一致性数字人Stand-In VACE MultiTalk 跳舞唱歌_1956601667196211201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/一致性数字人Stand-In VACE MultiTalk 跳舞唱歌_1956601667196211201.json
hash: f01dba3d55ab85df
coverage: 0.666667
learned_at: 2026-10-15 22:43:41
nodes: [WanVideoTorchCompileSettings, WanVideoSetLoRAs, easy cleanGpuUsed, easy clearCacheAll, SetNode, JWStringMultiline, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, FaceProcessorLoader, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, MathExpression|pysssss, GetNode, GetNode, GetNode, ImageResizeKJv2, DownloadAndLoadDepthAnythingV2Model, WanVideoDecode, easy cleanGpuUsed, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, easy cleanGpuUsed, easy clearCacheAll, GetNode, MultiTalkWav2VecEmbeds, GetNode, GetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, GetNode, easy cleanGpuUsed, easy clearCacheAll, VHS_VideoCombine, AudioSeparation, DownloadAndLoadWav2VecModel, GetNode, SaveAudio, GetNode, WanVideoEncode, WanVideoAddStandInLatent, AudioCrop, SetNode, easy showAnything, VHS_VideoInfoLoaded, PreviewImage, WanVideoApplyNAG, WanVideoContextOptions, ImageResizeKJv2, GetNode, WanVideoBlockSwap, GetImageRangeFromBatch, GetImageSizeAndCount, DepthAnything_V2, ApplyFaceProcessor, JWStringMultiline, WanVideoSampler, WanVideoLoraSelect, WanVideoVACEEncode, INTConstant, INTConstant, VHS_VideoCombine, WanVideoModelLoader, INTConstant, MultiTalkModelLoader, WanVideoLoraSelect, VHS_LoadVideo, LG_LoadImage, UnloadAllModels, easy cleanGpuUsed, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, easy cleanGpuUsed, GetNode, easy clearCacheAll, VHS_VideoCombine, VHS_VideoCombine, Video_Upscale_With_Model, Free_Video_Memory, GetNode, VHS_LoadVideoPath, easy clearCacheAll]
patterns: []
missing: []
---

# 视频生成/文生视频/一致性数字人Stand-In VACE MultiTalk 跳舞唱歌_1956601667196211201.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1956601667196211201.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（96 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `JWStringMultiline`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceProcessorLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `DownloadAndLoadDepthAnythingV2Model`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `GetNode`
- `MultiTalkWav2VecEmbeds`
- `GetNode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `VHS_VideoCombine`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `SaveAudio`
- `GetNode`
- `WanVideoEncode`
- `WanVideoAddStandInLatent`
- `AudioCrop`
- `SetNode`
- `easy showAnything`
- `VHS_VideoInfoLoaded`
- `PreviewImage`
- `WanVideoApplyNAG`
- `WanVideoContextOptions`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoBlockSwap`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `DepthAnything_V2`
- `ApplyFaceProcessor`
- `JWStringMultiline`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoVACEEncode`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `INTConstant`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `VHS_LoadVideo`
- `LG_LoadImage`
- `UnloadAllModels`
- `easy cleanGpuUsed`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `easy cleanGpuUsed`
- `GetNode`
- `easy clearCacheAll`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Video_Upscale_With_Model`
- `Free_Video_Memory`
- `GetNode`
- `VHS_LoadVideoPath`
- `easy clearCacheAll`

## 知识

覆盖率 **67%**（64/96）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`easy cleanGpuUsed`、`easy clearCacheAll`、`JWStringMultiline`、`WanVideoTextEncodeSingle`、`FaceProcessorLoader`、`MathExpression|pysssss`、`ImageResizeKJv2`、`DownloadAndLoadDepthAnythingV2Model`、`WanVideoDecode`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`MultiTalkWav2VecEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`VHS_VideoCombine`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`SaveAudio`、`WanVideoEncode`、`WanVideoAddStandInLatent`、`AudioCrop`、`VHS_VideoInfoLoaded`、`WanVideoApplyNAG`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`DepthAnything_V2`、`ApplyFaceProcessor`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoVACEEncode`、`INTConstant`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`VHS_LoadVideo`、`LG_LoadImage`、`UnloadAllModels`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`Video_Upscale_With_Model`、`Free_Video_Memory`、`VHS_LoadVideoPath`

**用到的条目**：DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode
