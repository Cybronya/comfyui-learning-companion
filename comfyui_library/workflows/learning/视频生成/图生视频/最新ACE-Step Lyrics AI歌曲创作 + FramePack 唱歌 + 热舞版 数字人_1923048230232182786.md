---
key: 视频生成/图生视频/最新ACE-Step Lyrics AI歌曲创作 + FramePack 唱歌 + 热舞版 数字人_1923048230232182786.json
name: 最新ACE-Step Lyrics AI歌曲创作 + FramePack 唱歌 + 热舞版 数字人_1923048230232182786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最新ACE-Step Lyrics AI歌曲创作 + FramePack 唱歌 + 热舞版 数字人_1923048230232182786.json
hash: ea5cb056954c231b
coverage: 0.606383
learned_at: 2026-10-15 22:29:47
nodes: [MultiLinePromptACES, CR Text, Note, Note, MultiLineLyrics, Note, SetNode, SetNode, GenerationParameters, CR Text, ACEStepGen, VHS_VideoCombine, VAEDecodeTiled, GetImageSizeAndCount, SaveAudio, Note, VHS_VideoCombine, CLIPTextEncode, GetNode, LayerUtility: PurgeVRAM, SetNode, CLIPTextEncode, VHS_VideoCombine, GetNode, SetNode, GetNode, Note, easy imageBatchToImageList, easy imageListToImageBatch, UpscaleModelLoader, SetNode, Fast Groups Muter (rgthree), Primitive float [Crystools], Note, ImageResizeKJv2, Note, Reroute, Bjornulf_ShowInt, CR Text Input Switch (4 way), DisplayText_Zho, DisplayText_Zho, CR Text, Note, Bjornulf_ShowInt, UltimateSDUpscale, PrimitiveFloat, Note, Note, Note, VHS_LoadAudioUpload, PreviewAudio, Fast Groups Muter (rgthree), Note, SetNode, SetNode, SetNode, CheckpointLoaderSimple, GetNode, easy clearCacheAll, CLIPVisionEncode, easy clearCacheAll, GetNode, RH_Translator, VAEEncode, easy clearCacheAll, LayerUtility: PurgeVRAM, Note, easy cleanGpuUsed, CLIPTextEncode, easy clearCacheAll, easy clearCacheAll, LoadFramePackModel, FramePackTorchCompileSettings, SetNode, DualCLIPLoader, easy clearCacheAll, VAELoader, ConditioningZeroOut, SetNode, CLIPVisionLoader, easy clearCacheAll, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, FramePackSampler, Note, LoadImage, Note, Note, Note, Note, LatentSyncNode, RH_Captioner, FramePackFindNearestBucket]
patterns: []
missing: []
parameters: {"checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors"}
---

# 视频生成/图生视频/最新ACE-Step Lyrics AI歌曲创作 + FramePack 唱歌 + 热舞版 数字人_1923048230232182786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1923048230232182786.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（94 个）：
- `MultiLinePromptACES`
- `CR Text`
- `Note`
- `Note`
- `MultiLineLyrics`
- `Note`
- `SetNode`
- `SetNode`
- `GenerationParameters`
- `CR Text`
- `ACEStepGen`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `SaveAudio`
- `Note`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `GetNode`
- `Note`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `UpscaleModelLoader`
- `SetNode`
- `Fast Groups Muter (rgthree)`
- `Primitive float [Crystools]`
- `Note`
- `ImageResizeKJv2`
- `Note`
- `Reroute`
- `Bjornulf_ShowInt`
- `CR Text Input Switch (4 way)`
- `DisplayText_Zho`
- `DisplayText_Zho`
- `CR Text`
- `Note`
- `Bjornulf_ShowInt`
- `UltimateSDUpscale`
- `PrimitiveFloat`
- `Note`
- `Note`
- `Note`
- `VHS_LoadAudioUpload`
- `PreviewAudio`
- `Fast Groups Muter (rgthree)`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `easy clearCacheAll`
- `CLIPVisionEncode`
- `easy clearCacheAll`
- `GetNode`
- `RH_Translator`
- `VAEEncode` ★核心
- `easy clearCacheAll`
- `LayerUtility: PurgeVRAM`
- `Note`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy clearCacheAll`
- `easy clearCacheAll`
- `LoadFramePackModel`
- `FramePackTorchCompileSettings`
- `SetNode`
- `DualCLIPLoader`
- `easy clearCacheAll`
- `VAELoader`
- `ConditioningZeroOut`
- `SetNode`
- `CLIPVisionLoader`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `FramePackSampler` ★核心
- `Note`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `LatentSyncNode`
- `RH_Captioner`
- `FramePackFindNearestBucket`

## 关键参数

- `checkpoint` = `dreamshaperXL_v21TurboDPMSDE.safetensors`

## 知识

覆盖率 **61%**（57/94）

**有卡**：`MultiLinePromptACES`、`CR Text`、`MultiLineLyrics`、`GenerationParameters`、`ACEStepGen`、`VHS_VideoCombine`、`VAEDecodeTiled`、`GetImageSizeAndCount`、`SaveAudio`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`UpscaleModelLoader`、`Primitive float [Crystools]`、`ImageResizeKJv2`、`Bjornulf_ShowInt`、`CR Text Input Switch (4 way)`、`DisplayText_Zho`、`UltimateSDUpscale`、`VHS_LoadAudioUpload`、`PreviewAudio`、`CheckpointLoaderSimple`、`easy clearCacheAll`、`CLIPVisionEncode`、`RH_Translator`、`VAEEncode`、`easy cleanGpuUsed`、`LoadFramePackModel`、`FramePackTorchCompileSettings`、`DualCLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`CLIPVisionLoader`、`FramePackSampler`、`LoadImage`、`LatentSyncNode`、`RH_Captioner`、`FramePackFindNearestBucket`

**用到的条目**：VAELoader、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、FramePackSampler、VAEDecodeTiled、VAEEncode
