---
key: 视频生成/图生视频/⓫ SCAIL2循环迁移 单-多图-背景-人物替换-动作迁移-去字幕（KJ流）6.21_2066818960833728513.json
name: ⓫ SCAIL2循环迁移 单-多图-背景-人物替换-动作迁移-去字幕（KJ流）6.21_2066818960833728513.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/⓫ SCAIL2循环迁移 单-多图-背景-人物替换-动作迁移-去字幕（KJ流）6.21_2066818960833728513.json
hash: 47b049a970938458
coverage: 0.315789
learned_at: 2026-10-15 22:39:53
nodes: [WanAnimatePlus VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SCAIL2ColoredMask, SCAIL2ColoredMask, SCAIL2ColoredMask, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, LoadImage, LoadImage, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, WanAnimatePlus SetLoRAs, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SAM3_VideoTrack, SAM3_VideoTrack, SAM3_VideoTrack, SetNode, SetNode, GetNode, SetNode, LoadImage, GetNode, GetNode, SetNode, PrimitiveBoolean, PrimitiveBoolean, PrimitiveBoolean, GetNode, INTConstant, GetNode, GetNode, MarkdownNote, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, GetNode, SetNode, SetNode, SetNode, MarkdownNote, ImageBatchMulti, GetNode, GetNode, SetNode, SetNode, CheckpointLoaderSimple, SetNode, ImageResizeKJv2, GetNode, SAM3_VideoTrack, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, INTConstant, INTConstant, CLIPVisionLoader, GetNode, WanAnimatePlus ClipVisionEncode, SetNode, VHS_LoadVideo, WanAnimatePlus ModelLoader, DownloadAndLoadGIMMVFIModel, ImageConcatMulti, FL_VideoTrim, FL_FILM, easy cleanGpuUsed, FL_RIFE, GIMMVFI_interpolate, FL_RIFE, VHS_VideoCombine, PlaySound|pysssss, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanAnimatePlus TextEncodeCached, WanAnimatePlus SamplerSettings, WanAnimatePlus Decode, GetNode, GetNode, GetNode, SetNode, INTConstant, SAM3_VideoTrack, CLIPTextEncode, SetNode, GetNode, ComfySwitchNode, GetNode, Any Switch (rgthree), Convert Masks to Images, ImageCompositeMasked, SAM3_TrackToMask, InvertMask, LayerUtility: ImageScaleByAspectRatio V2, WanAnimatePlus BlockSwap, MarkdownNote, SetNode, ImageResizeKJv2, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ContextOptions, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), SetNode, GetNode, GetNode, WanAnimatePlus SamplerFromSettings, Fast Groups Bypasser (rgthree), SetNode, SetNode, TextInput_, SetNode, TextInput_, Fast Groups Bypasser (rgthree), WanAnimatePlus SCAIL_2 Embeds, MarkdownNote, PreviewImage, GetNode, MarkdownNote, SAM3_TrackPreview, VHS_VideoCombine, MarkdownNote, ImageConcatMulti, GetNode, MarkdownNote, TextInput_, INTConstant, MarkdownNote, GetNode, GetNode, GetNode, SetNode, ImageBatchMulti, SetNode, GetNode, GetNode, PreviewImage, PreviewImage, MarkdownNote, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), MarkdownNote]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/图生视频/⓫ SCAIL2循环迁移 单-多图-背景-人物替换-动作迁移-去字幕（KJ流）6.21_2066818960833728513.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066818960833728513.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（209 个）：
- `WanAnimatePlus VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SCAIL2ColoredMask`
- `SCAIL2ColoredMask`
- `SCAIL2ColoredMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanAnimatePlus SetLoRAs`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `GetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `SAM3_VideoTrack`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `CLIPVisionLoader`
- `GetNode`
- `WanAnimatePlus ClipVisionEncode`
- `SetNode`
- `VHS_LoadVideo`
- `WanAnimatePlus ModelLoader`
- `DownloadAndLoadGIMMVFIModel`
- `ImageConcatMulti`
- `FL_VideoTrim`
- `FL_FILM`
- `easy cleanGpuUsed`
- `FL_RIFE`
- `GIMMVFI_interpolate`
- `FL_RIFE`
- `VHS_VideoCombine`
- `PlaySound|pysssss`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus SamplerSettings` ★核心
- `WanAnimatePlus Decode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `SAM3_VideoTrack`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `Any Switch (rgthree)`
- `Convert Masks to Images`
- `ImageCompositeMasked`
- `SAM3_TrackToMask`
- `InvertMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanAnimatePlus BlockSwap`
- `MarkdownNote`
- `SetNode`
- `ImageResizeKJv2`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ContextOptions`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanAnimatePlus SamplerFromSettings` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `SetNode`
- `TextInput_`
- `SetNode`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `WanAnimatePlus SCAIL_2 Embeds`
- `MarkdownNote`
- `PreviewImage`
- `GetNode`
- `MarkdownNote`
- `SAM3_TrackPreview`
- `VHS_VideoCombine`
- `MarkdownNote`
- `ImageConcatMulti`
- `GetNode`
- `MarkdownNote`
- `TextInput_`
- `INTConstant`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageBatchMulti`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **32%**（66/209）

**有卡**：`WanAnimatePlus VAELoader`、`SCAIL2ColoredMask`、`LoadImage`、`ImageResizeKJv2`、`WanAnimatePlus SetLoRAs`、`SAM3_VideoTrack`、`PrimitiveBoolean`、`INTConstant`、`CLIPTextEncode`、`ImageBatchMulti`、`CheckpointLoaderSimple`、`CLIPVisionLoader`、`WanAnimatePlus ClipVisionEncode`、`VHS_LoadVideo`、`WanAnimatePlus ModelLoader`、`DownloadAndLoadGIMMVFIModel`、`ImageConcatMulti`、`FL_VideoTrim`、`FL_FILM`、`easy cleanGpuUsed`、`FL_RIFE`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`PlaySound|pysssss`、`WanAnimatePlus TextEncodeCached`、`WanAnimatePlus SamplerSettings`、`WanAnimatePlus Decode`、`Convert Masks to Images`、`ImageCompositeMasked`、`SAM3_TrackToMask`、`InvertMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus SamplerFromSettings`、`TextInput_`、`WanAnimatePlus SCAIL_2 Embeds`、`SAM3_TrackPreview`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanAnimatePlus SamplerFromSettings、WanAnimatePlus SamplerSettings、WanAnimatePlus ClipVisionEncode、WanAnimatePlus Decode
