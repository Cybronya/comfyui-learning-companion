---
key: 平台全量/LongCat 1.5 数字人口播｜384P直出·Plus·5–180秒_2118977321343475713.json
name: LongCat 1.5 数字人口播｜384P直出·Plus·5–180秒_2118977321343475713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LongCat 1.5 数字人口播｜384P直出·Plus·5–180秒_2118977321343475713.json
hash: 83db5b4f29b58767
coverage: 1
learned_at: 2026-11-14 00:39:26
nodes: [LoadImage, LoadAudio, GetImageSize, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageResizeKJv2, RH_GetAudioDuration, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, AudioBeforeAfterSilence, WhisperModelLoader, LongCatAvatarWhisperEmbeds, WanAnimatePlus BlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, WanVideoEncode, WanVideoTextEncodeCached, WanVideoSchedulerv2, ManualSigmas, WanVideoLongCatAvatarExtendEmbeds, WanVideoSamplerv2, WanVideoDecode, VHS_VideoCombine, VHS_SelectFilename, ListCreateNode, ListAppendNode, ImageFromBatch, easy forLoopStart, ComfyMathExpression, GetImageRangeFromBatch, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoSamplerv2, ReplaceVideoLatentFrames, WanVideoDecode, ComfyMathExpression, GetImageRangeFromBatch, VHS_VideoCombine, VHS_SelectFilename, ListAppendNode, ImageFromBatch, easy forLoopEnd, SystemUUIDGenerator, AudioToPath, MultiMergeVideos, ConcatVideos, SaveVideo, SP_DynamicCombo, YC Extract Number]
patterns: []
missing: []
---

# 平台全量/LongCat 1.5 数字人口播｜384P直出·Plus·5–180秒_2118977321343475713.json

> 来源文件 `comfyui_library/workflows/平台全量/LongCat 1.5 数字人口播｜384P直出·Plus·5–180秒_2118977321343475713.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（53 个）：
- `LoadImage`
- `LoadAudio`
- `GetImageSize`
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

覆盖率 **100%**（53/53）

**有卡**：`LoadImage`、`LoadAudio`、`GetImageSize`、`ComfyMathExpression`、`ImageResizeKJv2`、`RH_GetAudioDuration`、`AudioBeforeAfterSilence`、`WhisperModelLoader`、`LongCatAvatarWhisperEmbeds`、`WanAnimatePlus BlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoSchedulerv2`、`ManualSigmas`、`WanVideoLongCatAvatarExtendEmbeds`、`WanVideoSamplerv2`、`WanVideoDecode`、`VHS_VideoCombine`、`VHS_SelectFilename`、`ListCreateNode`、`ListAppendNode`、`ImageFromBatch`、`easy forLoopStart`、`GetImageRangeFromBatch`、`ReplaceVideoLatentFrames`、`easy forLoopEnd`、`SystemUUIDGenerator`、`AudioToPath`、`MultiMergeVideos`、`ConcatVideos`、`SaveVideo`、`SP_DynamicCombo`、`YC Extract Number`

**用到的条目**：LoadImage、WanVideoSamplerv2、ReplaceVideoLatentFrames、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect
