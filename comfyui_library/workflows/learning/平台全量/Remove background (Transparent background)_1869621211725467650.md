---
key: 平台全量/Remove background (Transparent background)_1869621211725467650.json
name: Remove background (Transparent background)_1869621211725467650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Remove background (Transparent background)_1869621211725467650.json
hash: 7534eeb7a1c9794f
coverage: 0.902174
learned_at: 2026-11-14 00:54:54
nodes: [GroundingDinoModelLoader (segment anything), InvertMask, InvertMask, GroundingDinoSAMSegment (segment anything), SAMLoader, BboxDetectorSEGS, SAMDetectorCombined, UltralyticsDetectorProvider, SaveImage, Context (rgthree), SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, GridAnnotation, PreviewImage, MasksToMaskList, Image Padding, Reroute, SaveImage, SAMModelLoader (segment anything), Reroute, GetImageSize+, ImageScale, ImageToMask, InvertMask, Remove Image Background (abg), PreviewImage, ImageToMask, InvertMask, Context (rgthree), SaveImage, Context (rgthree), Image Overlay, Image Overlay, Context (rgthree), Image Overlay, PreviewImage, Image Overlay, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Groups Muter (rgthree), Context (rgthree), CR Color Panel, Image Rembg (Remove Background), Context (rgthree), Image Rembg (Remove Background), Context (rgthree), Image Rembg (Remove Background), Context (rgthree), Image Rembg (Remove Background), Context (rgthree), PreviewImage, Image Rembg (Remove Background), Image Rembg (Remove Background), Image Rembg (Remove Background), ImageCombine, ImageCombine, ImageCombine, ImageCombine, ImageCombine, ImageToMask, InvertMask, Image Overlay, ImageToMask, InvertMask, Image Overlay, ImageToMask, ImageToMask, InvertMask, ImageToMask, Image Overlay, ImageToMask, InvertMask, Image Overlay, InvertMask, Image Overlay, InvertMask, Image Overlay, Context (rgthree), Any Switch (rgthree), Color, Fast Muter (rgthree), Fast Muter (rgthree), Fast Muter (rgthree), LoadImage, SaveImage, SaveImage, PreviewImage, SaveImage, ImagesGridByRows]
patterns: []
missing: []
---

# 平台全量/Remove background (Transparent background)_1869621211725467650.json

> 来源文件 `comfyui_library/workflows/平台全量/Remove background (Transparent background)_1869621211725467650.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（92 个）：
- `GroundingDinoModelLoader (segment anything)`
- `InvertMask`
- `InvertMask`
- `GroundingDinoSAMSegment (segment anything)`
- `SAMLoader`
- `BboxDetectorSEGS`
- `SAMDetectorCombined`
- `UltralyticsDetectorProvider`
- `SaveImage`
- `Context (rgthree)`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `GridAnnotation`
- `PreviewImage`
- `MasksToMaskList`
- `Image Padding`
- `Reroute`
- `SaveImage`
- `SAMModelLoader (segment anything)`
- `Reroute`
- `GetImageSize+`
- `ImageScale`
- `ImageToMask`
- `InvertMask`
- `Remove Image Background (abg)`
- `PreviewImage`
- `ImageToMask`
- `InvertMask`
- `Context (rgthree)`
- `SaveImage`
- `Context (rgthree)`
- `Image Overlay`
- `Image Overlay`
- `Context (rgthree)`
- `Image Overlay`
- `PreviewImage`
- `Image Overlay`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Context (rgthree)`
- `CR Color Panel`
- `Image Rembg (Remove Background)`
- `Context (rgthree)`
- `Image Rembg (Remove Background)`
- `Context (rgthree)`
- `Image Rembg (Remove Background)`
- `Context (rgthree)`
- `Image Rembg (Remove Background)`
- `Context (rgthree)`
- `PreviewImage`
- `Image Rembg (Remove Background)`
- `Image Rembg (Remove Background)`
- `Image Rembg (Remove Background)`
- `ImageCombine`
- `ImageCombine`
- `ImageCombine`
- `ImageCombine`
- `ImageCombine`
- `ImageToMask`
- `InvertMask`
- `Image Overlay`
- `ImageToMask`
- `InvertMask`
- `Image Overlay`
- `ImageToMask`
- `ImageToMask`
- `InvertMask`
- `ImageToMask`
- `Image Overlay`
- `ImageToMask`
- `InvertMask`
- `Image Overlay`
- `InvertMask`
- `Image Overlay`
- `InvertMask`
- `Image Overlay`
- `Context (rgthree)`
- `Any Switch (rgthree)`
- `Color`
- `Fast Muter (rgthree)`
- `Fast Muter (rgthree)`
- `Fast Muter (rgthree)`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `ImagesGridByRows`

## 知识

覆盖率 **90%**（83/92）

**有卡**：`GroundingDinoModelLoader (segment anything)`、`InvertMask`、`GroundingDinoSAMSegment (segment anything)`、`SAMLoader`、`BboxDetectorSEGS`、`SAMDetectorCombined`、`UltralyticsDetectorProvider`、`SaveImage`、`Context (rgthree)`、`GridAnnotation`、`MasksToMaskList`、`Image Padding`、`SAMModelLoader (segment anything)`、`GetImageSize+`、`ImageScale`、`ImageToMask`、`Remove Image Background (abg)`、`Image Overlay`、`Mute / Bypass Repeater (rgthree)`、`CR Color Panel`、`Image Rembg (Remove Background)`、`ImageCombine`、`Color`、`Fast Muter (rgthree)`、`LoadImage`、`ImagesGridByRows`

**用到的条目**：LoadImage、GetImageSize+、SaveImage、BboxDetectorSEGS、Color、Context (rgthree)、CR Color Panel、Fast Muter (rgthree)
