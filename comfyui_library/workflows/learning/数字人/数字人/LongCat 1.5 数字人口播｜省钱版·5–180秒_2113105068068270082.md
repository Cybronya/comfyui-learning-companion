---
key: 数字人/数字人/LongCat 1.5 数字人口播｜省钱版·5–180秒_2113105068068270082.json
name: LongCat 1.5 数字人口播｜省钱版·5–180秒_2113105068068270082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LongCat 1.5 数字人口播｜省钱版·5–180秒_2113105068068270082.json
hash: fcc361c93d96c076
coverage: 0.983333
learned_at: 2026-10-26 22:10:19
nodes: [LoadImage, SP_DynamicCombo, VHS_LoadAudioUpload, YC Extract Number, PrimitiveString, YC Extract Number, ComfyMathExpression, GetImageSize, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageResizeKJv2, RH_GetAudioDuration, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, AudioBeforeAfterSilence, WhisperModelLoader, LongCatAvatarWhisperEmbeds, WanAnimatePlus BlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, WanVideoEncode, WanVideoTextEncodeCached, WanVideoSchedulerv2, ManualSigmas, WanVideoLongCatAvatarExtendEmbeds, WanVideoSamplerv2, WanVideoDecode, VHS_VideoCombine, VHS_SelectFilename, ListCreateNode, ListAppendNode, ImageFromBatch, easy forLoopStart, ComfyMathExpression, GetImageRangeFromBatch, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoSamplerv2, ReplaceVideoLatentFrames, WanVideoDecode, ComfyMathExpression, GetImageRangeFromBatch, VHS_VideoCombine, VHS_SelectFilename, ListAppendNode, ImageFromBatch, easy forLoopEnd, SystemUUIDGenerator, AudioToPath, MultiMergeVideos, ConcatVideos, SaveVideo, SP_DynamicCombo, YC Extract Number]
patterns: []
missing: []
---

# 数字人/数字人/LongCat 1.5 数字人口播｜省钱版·5–180秒_2113105068068270082.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LongCat 1.5 数字人口播｜省钱版·5–180秒_2113105068068270082.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（60 个）：
- `LoadImage`
- `SP_DynamicCombo`
- `VHS_LoadAudioUpload`
- `YC Extract Number`
- `PrimitiveString`
- `YC Extract Number`
- `ComfyMathExpression`
- `GetImageSize`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `RH_GetAudioDuration`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `AudioBeforeAfterSilence`
- `WhisperModelLoader`
- `LongCatAvatarWhisperEmbeds`
- `WanAnimatePlus BlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `WanVideoSchedulerv2`
- `ManualSigmas`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoSamplerv2` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_SelectFilename`
- `ListCreateNode`
- `ListAppendNode`
- `ImageFromBatch`
- `easy forLoopStart`
- `ComfyMathExpression`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoSamplerv2` ★核心
- `ReplaceVideoLatentFrames`
- `WanVideoDecode`
- `ComfyMathExpression`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `VHS_SelectFilename`
- `ListAppendNode`
- `ImageFromBatch`
- `easy forLoopEnd`
- `SystemUUIDGenerator`
- `AudioToPath`
- `MultiMergeVideos`
- `ConcatVideos`
- `SaveVideo`
- `SP_DynamicCombo`
- `YC Extract Number`

## 知识

覆盖率 **98%**（59/60）

**有卡**：`LoadImage`、`SP_DynamicCombo`、`VHS_LoadAudioUpload`、`YC Extract Number`、`ComfyMathExpression`、`GetImageSize`、`ImageResizeKJv2`、`RH_GetAudioDuration`、`AudioBeforeAfterSilence`、`WhisperModelLoader`、`LongCatAvatarWhisperEmbeds`、`WanAnimatePlus BlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoSchedulerv2`、`ManualSigmas`、`WanVideoLongCatAvatarExtendEmbeds`、`WanVideoSamplerv2`、`WanVideoDecode`、`VHS_VideoCombine`、`VHS_SelectFilename`、`ListCreateNode`、`ListAppendNode`、`ImageFromBatch`、`easy forLoopStart`、`GetImageRangeFromBatch`、`ReplaceVideoLatentFrames`、`easy forLoopEnd`、`SystemUUIDGenerator`、`AudioToPath`、`MultiMergeVideos`、`ConcatVideos`、`SaveVideo`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
