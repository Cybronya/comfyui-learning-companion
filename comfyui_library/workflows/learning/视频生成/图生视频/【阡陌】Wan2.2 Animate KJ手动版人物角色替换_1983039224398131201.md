---
key: 视频生成/图生视频/【阡陌】Wan2.2 Animate KJ手动版人物角色替换_1983039224398131201.json
name: 【阡陌】Wan2.2 Animate KJ手动版人物角色替换_1983039224398131201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1983039224398131201.json
hash: 818413a87ab42cc4
coverage: 0.47191
learned_at: 2026-10-15 22:32:43
nodes: [WanVideoModelLoader, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, PreviewImage, GetNode, easy showAnything, SetNode, GetNode, SetNode, SetNode, SetNode, OnnxDetectionModelLoader, SetNode, GetNode, SetNode, WanVideoVAELoader, SetNode, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, SetNode, WanVideoClipVisionEncode, CLIPVisionLoader, GetNode, GetNode, WanVideoLoraSelectMulti, GetNode, WanVideoAnimateEmbeds, GetNode, Note, WanVideoDecode, ImageFromBatch, VHS_VideoCombine, ImageConcanate, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, PoseAndFaceDetection, LayerMask: MaskGrow, DrawMaskOnImage, BlockifyMask, SetNode, SetNode, LayerMask: MaskPreview, WanVideoTextEncodeCached, GetNode, DrawMaskOnImage, SetNode, LayerMask: MaskPreview, SetNode, VHS_VideoCombine, SeCVideoSegmentation, LayerMask: MaskGrow, GetNode, GetNode, GetNode, GetNode, BlockifyMask, SeCModelLoader, GetNode, SeCVideoSegmentation, SeCModelLoader, VHS_VideoCombine, LayerMask: MaskPreview, Note, VHS_VideoCombine, DrawViTPose, LoadImage, VHS_LoadVideo, PointsEditor, LayerMask: MaskPreview]
patterns: []
missing: []
---

# 视频生成/图生视频/【阡陌】Wan2.2 Animate KJ手动版人物角色替换_1983039224398131201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983039224398131201.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（89 个）：
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `Note`
- `WanVideoDecode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `ImageConcanate`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `LayerMask: MaskGrow`
- `DrawMaskOnImage`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `WanVideoTextEncodeCached`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `LayerMask: MaskPreview`
- `SetNode`
- `VHS_VideoCombine`
- `SeCVideoSegmentation`
- `LayerMask: MaskGrow`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `SeCModelLoader`
- `GetNode`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `VHS_VideoCombine`
- `LayerMask: MaskPreview`
- `Note`
- `VHS_VideoCombine`
- `DrawViTPose`
- `LoadImage`
- `VHS_LoadVideo`
- `PointsEditor`
- `LayerMask: MaskPreview`

## 知识

覆盖率 **47%**（42/89）

**有卡**：`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`WanVideoSampler`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`ImageFromBatch`、`ImageConcanate`、`PoseAndFaceDetection`、`LayerMask: MaskGrow`、`DrawMaskOnImage`、`BlockifyMask`、`LayerMask: MaskPreview`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`SeCModelLoader`、`DrawViTPose`、`LoadImage`、`VHS_LoadVideo`、`PointsEditor`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
