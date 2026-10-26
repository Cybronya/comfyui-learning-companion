---
key: 数字人/数字人/LongCat 1.5 数字人口播｜5–180秒·三档分辨率_2112843247210033153.json
name: LongCat 1.5 数字人口播｜5–180秒·三档分辨率_2112843247210033153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LongCat 1.5 数字人口播｜5–180秒·三档分辨率_2112843247210033153.json
hash: 87eb9cd321c9704a
coverage: 0.982759
learned_at: 2026-10-26 22:10:19
nodes: [LoadImage, SP_DynamicCombo, LoadAudio, YC Extract Number, PrimitiveString, YC Extract Number, ComfyMathExpression, GetImageSize, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageResizeKJv2, RH_GetAudioDuration, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, AudioBeforeAfterSilence, WhisperModelLoader, LongCatAvatarWhisperEmbeds, WanAnimatePlus BlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, WanVideoEncode, WanVideoTextEncodeCached, WanVideoSchedulerv2, ManualSigmas, WanVideoLongCatAvatarExtendEmbeds, WanVideoSamplerv2, WanVideoDecode, VHS_VideoCombine, VHS_SelectFilename, ListCreateNode, ListAppendNode, ImageFromBatch, easy forLoopStart, ComfyMathExpression, GetImageRangeFromBatch, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoSamplerv2, ReplaceVideoLatentFrames, WanVideoDecode, ComfyMathExpression, GetImageRangeFromBatch, VHS_VideoCombine, VHS_SelectFilename, ListAppendNode, ImageFromBatch, easy forLoopEnd, SystemUUIDGenerator, AudioToPath, MultiMergeVideos, ConcatVideos, SaveVideo]
patterns: []
missing: []
---

# 数字人/数字人/LongCat 1.5 数字人口播｜5–180秒·三档分辨率_2112843247210033153.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LongCat 1.5 数字人口播｜5–180秒·三档分辨率_2112843247210033153.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（58 个）：
- `LoadImage`
- `SP_DynamicCombo`
- `LoadAudio`
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

## 知识

覆盖率 **98%**（57/58）

**有卡**：`LoadImage`、`SP_DynamicCombo`、`LoadAudio`、`YC Extract Number`、`ComfyMathExpression`、`GetImageSize`、`ImageResizeKJv2`、`RH_GetAudioDuration`、`AudioBeforeAfterSilence`、`WhisperModelLoader`、`LongCatAvatarWhisperEmbeds`、`WanAnimatePlus BlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoSchedulerv2`、`ManualSigmas`、`WanVideoLongCatAvatarExtendEmbeds`、`WanVideoSamplerv2`、`WanVideoDecode`、`VHS_VideoCombine`、`VHS_SelectFilename`、`ListCreateNode`、`ListAppendNode`、`ImageFromBatch`、`easy forLoopStart`、`GetImageRangeFromBatch`、`ReplaceVideoLatentFrames`、`easy forLoopEnd`、`SystemUUIDGenerator`、`AudioToPath`、`MultiMergeVideos`、`ConcatVideos`、`SaveVideo`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
