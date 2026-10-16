---
key: 视频生成/图生视频/Wan2.2 Animate姿势参考图生视频_1980564316481044481.json
name: Wan2.2 Animate姿势参考图生视频_1980564316481044481.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980564316481044481.json
hash: 5bfea8cbe5f6ae7a
coverage: 0.864865
learned_at: 2026-10-15 22:32:31
nodes: [VHS_VideoCombine, WanVideoTextEncodeCached, WanVideoSampler, CR Text, PrimitiveInt, LoadImage, MarkdownNote, PrimitiveInt, VHS_VideoCombine, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, WanVideoBlockSwap, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM V2, CLIPVisionLoader, WanVideoVAELoader, GetImageSizeAndCount, ImageFromBatch+, WanVideoClipVisionEncode, ImageResizeKJv2, WanVideoAnimateEmbeds, WanVideoDecode, LayerUtility: PurgeVRAM V2, PrimitiveInt, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, LoadImage, VHS_LoadVideo, VHS_VideoInfo, SimpleMath+, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate姿势参考图生视频_1980564316481044481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980564316481044481.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `CR Text`
- `PrimitiveInt`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM V2`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `PrimitiveInt`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `SimpleMath+`
- `PrimitiveInt`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`CR Text`、`LoadImage`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`LayerUtility: PurgeVRAM V2`、`CLIPVisionLoader`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`ImageFromBatch+`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`VHS_LoadVideo`、`VHS_VideoInfo`、`SimpleMath+`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
