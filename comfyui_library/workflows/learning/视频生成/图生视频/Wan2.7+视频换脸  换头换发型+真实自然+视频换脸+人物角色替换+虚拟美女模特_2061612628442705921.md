---
key: 视频生成/图生视频/Wan2.7+视频换脸  换头换发型+真实自然+视频换脸+人物角色替换+虚拟美女模特_2061612628442705921.json
name: Wan2.7+视频换脸  换头换发型+真实自然+视频换脸+人物角色替换+虚拟美女模特_2061612628442705921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.7+视频换脸  换头换发型+真实自然+视频换脸+人物角色替换+虚拟美女模特_2061612628442705921.json
hash: 832078f18555c451
coverage: 0.626667
learned_at: 2026-10-15 22:38:55
nodes: [GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoAnimateEmbeds, CLIPVisionLoader, GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, ImageCropByMaskAndResize, DWPreprocessor, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, JWInteger, JWInteger, FaceMaskFromPoseKeypoints, PixelPerfectResolution, Reroute, WanVideoBlockSwap, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, ImageResizeKJv2, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, MathExpression|pysssss, MathExpression|pysssss, SetNode, GetNode, DrawMaskOnImage, SetNode, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageConcatMulti, ImageConcatMulti, VHS_VideoInfo, Int, SetNode, SetNode, GetNode, GetNode, GetNode, GrowMask, BlockifyMask, SetNode, SetNode, SetNode, GetNode, Int, LayerMask: SegformerB2ClothesUltra, GetNode, SetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, Int, CR Text, SaveVideo, RH_AlibabaWan27VideoEdit, MarkdownNote, LoadImage, LoadVideo, Fast Groups Bypasser (rgthree), LoadImage, VHS_LoadVideo, Fast Groups Bypasser (rgthree), Int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.7+视频换脸  换头换发型+真实自然+视频换脸+人物角色替换+虚拟美女模特_2061612628442705921.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061612628442705921.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（75 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCropByMaskAndResize`
- `DWPreprocessor`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `JWInteger`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `Reroute`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoInfo`
- `Int`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `Int`
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `CR Text`
- `SaveVideo`
- `RH_AlibabaWan27VideoEdit`
- `MarkdownNote`
- `LoadImage`
- `LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `Int`

## 知识

覆盖率 **63%**（47/75）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`MathExpression|pysssss`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`VHS_VideoInfo`、`Int`、`GrowMask`、`BlockifyMask`、`LayerMask: SegformerB2ClothesUltra`、`VHS_VideoCombine`、`CR Text`、`SaveVideo`、`RH_AlibabaWan27VideoEdit`、`LoadImage`、`LoadVideo`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
