---
key: 平台全量/Wan2.2动作迁移animate背景锁定+背部？？？_2056022446129598465.json
name: Wan2.2动作迁移animate背景锁定+背部？？？_2056022446129598465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2动作迁移animate背景锁定+背部？？？_2056022446129598465.json
hash: dcfc9b51257165ca
coverage: 0.407692
learned_at: 2026-11-14 01:06:19
nodes: [GetNode, SetNode, SetNode, PreviewImage, GetNode, GetNode, GetNode, WanVideoDecode, easy sam3ModelLoader, ImageFromBatch, GetNode, SeCModelLoader, DrawMaskOnImage, SetNode, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Int, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, GetNode, ImageFromBatch, SetNode, SetNode, SetNode, OnnxDetectionModelLoader, SetNode, SetNode, WanVideoUni3C_embeds, WanVideoEncode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoBlockSwap, GetNode, GetNode, Int, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, WanVideoUni3C_ControlnetLoader, GetNode, WanVideoModelLoader, SetNode, GetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, easy sam3ImageSegmentation, GetNode, GrowMask, BlockifyMask, LazySwitch1way, GetNode, Int, Int, WanVideoContextOptions, CLIPVisionLoader, SetNode, Note, SeCVideoSegmentation, GetNode, GetNode, easy cleanGpuUsed, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, PreviewImage, ImageResizeKJv2, LoadImage, SetNode, GetNode, WanVideoTextEncodeCached, RepeatImageBatch, VHS_LoadVideo, ImageResizeKJv2, GetNode, GetNode, ImageFromBatch, GetNode, LoadImage, GetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, Note, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, easy boolean, GetNode, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, PoseAndFaceDetection, DrawViTPose, Fast Groups Bypasser (rgthree), Note, Note, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 平台全量/Wan2.2动作迁移animate背景锁定+背部？？？_2056022446129598465.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2动作迁移animate背景锁定+背部？？？_2056022446129598465.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（130 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `easy sam3ModelLoader`
- `ImageFromBatch`
- `GetNode`
- `SeCModelLoader`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Int`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `ImageFromBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `WanVideoUni3C_embeds`
- `WanVideoEncode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `Int`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `WanVideoModelLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `easy sam3ImageSegmentation`
- `GetNode`
- `GrowMask`
- `BlockifyMask`
- `LazySwitch1way`
- `GetNode`
- `Int`
- `Int`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `SetNode`
- `Note`
- `SeCVideoSegmentation`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `PreviewImage`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `easy boolean`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **41%**（53/130）

**有卡**：`WanVideoDecode`、`easy sam3ModelLoader`、`ImageFromBatch`、`SeCModelLoader`、`DrawMaskOnImage`、`VHS_VideoCombine`、`Int`、`ImageResizeKJv2`、`OnnxDetectionModelLoader`、`WanVideoUni3C_embeds`、`WanVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoUni3C_ControlnetLoader`、`WanVideoModelLoader`、`VHS_VideoInfo`、`easy sam3ImageSegmentation`、`GrowMask`、`BlockifyMask`、`LazySwitch1way`、`WanVideoContextOptions`、`CLIPVisionLoader`、`SeCVideoSegmentation`、`easy cleanGpuUsed`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTextEncodeCached`、`RepeatImageBatch`、`easy boolean`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`PoseAndFaceDetection`、`DrawViTPose`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
