---
key: 平台全量/视频-动作迁移-v2-wan2.1-SCAIL2_2079575176957743105.json
name: 视频-动作迁移-v2-wan2.1-SCAIL2_2079575176957743105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-动作迁移-v2-wan2.1-SCAIL2_2079575176957743105.json
hash: 1ede887fd707c2a9
coverage: 0.530864
learned_at: 2026-11-14 02:34:06
nodes: [SetNode, WanAnimatePlus SetBlockSwap, Note, WanAnimatePlus SetLoRAs, SetNode, GetNode, SetNode, SetNode, PreviewImage, GetNode, WanAnimatePlus VAELoader, GetNode, CheckpointLoaderSimple, GetNode, CLIPVisionLoader, GetNode, PreviewImage, WanAnimatePlus Decode, VHS_VideoCombine, easy clearCacheAll, easy clearCacheAll, SAM3_VideoTrack, GetNode, easy clearCacheAll, WanAnimatePlus ModelLoader, WanAnimatePlus ClipVisionEncode V2, WanAnimatePlus LoraSelectMulti, SAM3_VideoTrack, GetNode, BatchImagesNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveFloat, MathExpression|pysssss, CM_FloatToInt, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, VHS_VideoInfoLoaded, SetNode, SCAIL2ColoredMaskV2, LoadImage, WanAnimatePlus ContextOptions, CLIPTextEncode, Int, WanVideoTorchCompileSettings, SetNode, easy showAnything, Text, MemoryCleaner, WanAnimatePlus SamplerFromSettings, SetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, GetNode, ImageConcatMulti, Note, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, WanVideoTextEncodeCached, WanAnimatePlus SamplerSettings, WanAnimatePlus SCAIL_2 TwoPhase Settings, WanAnimatePlus SCAIL_2 Embeds, easy seed, Int, PrimitiveFloat, WanAnimatePlus BlockSwap, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetImageSizeAndCount]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/视频-动作迁移-v2-wan2.1-SCAIL2_2079575176957743105.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-动作迁移-v2-wan2.1-SCAIL2_2079575176957743105.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（81 个）：
- `SetNode`
- `WanAnimatePlus SetBlockSwap`
- `Note`
- `WanAnimatePlus SetLoRAs`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `WanAnimatePlus VAELoader`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `PreviewImage`
- `WanAnimatePlus Decode`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `SAM3_VideoTrack`
- `GetNode`
- `easy clearCacheAll`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus ClipVisionEncode V2`
- `WanAnimatePlus LoraSelectMulti`
- `SAM3_VideoTrack`
- `GetNode`
- `BatchImagesNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `MathExpression|pysssss`
- `CM_FloatToInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SCAIL2ColoredMaskV2`
- `LoadImage`
- `WanAnimatePlus ContextOptions`
- `CLIPTextEncode` ★核心
- `Int`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `easy showAnything`
- `Text`
- `MemoryCleaner`
- `WanAnimatePlus SamplerFromSettings` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `GetNode`
- `ImageConcatMulti`
- `Note`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanAnimatePlus SamplerSettings` ★核心
- `WanAnimatePlus SCAIL_2 TwoPhase Settings`
- `WanAnimatePlus SCAIL_2 Embeds`
- `easy seed`
- `Int`
- `PrimitiveFloat`
- `WanAnimatePlus BlockSwap`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **53%**（43/81）

**有卡**：`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus VAELoader`、`CheckpointLoaderSimple`、`CLIPVisionLoader`、`WanAnimatePlus Decode`、`VHS_VideoCombine`、`easy clearCacheAll`、`SAM3_VideoTrack`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus ClipVisionEncode V2`、`WanAnimatePlus LoraSelectMulti`、`BatchImagesNode`、`MathExpression|pysssss`、`CM_FloatToInt`、`ImageResizeKJv2`、`VHS_VideoInfoLoaded`、`SCAIL2ColoredMaskV2`、`LoadImage`、`WanAnimatePlus ContextOptions`、`CLIPTextEncode`、`Int`、`WanVideoTorchCompileSettings`、`Text`、`MemoryCleaner`、`WanAnimatePlus SamplerFromSettings`、`VHS_LoadVideo`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncodeCached`、`WanAnimatePlus SamplerSettings`、`WanAnimatePlus SCAIL_2 TwoPhase Settings`、`WanAnimatePlus SCAIL_2 Embeds`、`easy seed`、`WanAnimatePlus BlockSwap`、`GetImageSizeAndCount`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、easy seed、WanAnimatePlus SamplerFromSettings、WanAnimatePlus SamplerSettings、WanAnimatePlus ClipVisionEncode V2
