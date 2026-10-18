---
key: 视频生成/图生视频/YJ_APP_WanAnimate_动作迁移v2.5_2034884568989310978.json
name: YJ_APP_WanAnimate_动作迁移v2.5_2034884568989310978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/YJ_APP_WanAnimate_动作迁移v2.5_2034884568989310978.json
hash: 4748e6e1725e3be1
coverage: 0.387755
learned_at: 2026-10-15 22:35:46
nodes: [Reroute, WanVideoVAELoader, Reroute, Reroute, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, easy compare, GetNode, GetNode, easy ifElse, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, WanVideoTextEncodeCached, GetNode, GetNode, DF_Int_to_Float, SetNode, SetNode, WanVideoDecode, GetNode, Reroute, GetNode, SetNode, DrawViTPose, GetNode, WanVideoClipVisionEncode, ImageFromBatch, SetNode, easy showAnything, easy showAnything, GetNode, SetNode, Reroute, ImageFromBatch, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, LoadImage, GetNode, GetNode, CR Text, SetNode, SetNode, easy int, SimpleMath+, GetNode, Reroute, SetNode, GetNode, PoseAndFaceDetection, OnnxDetectionModelLoader, PrimitiveInt, easy cleanGpuUsed, RIFE VFI, GetNode, GetNode, SimpleMath+, VHS_VideoCombine, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, PrimitiveInt, CLIPVisionLoader, VHS_VideoCombine, SetNode, VHS_VideoCombine, WanVideoBlockSwap, easy float, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoSetBlockSwap, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/YJ_APP_WanAnimate_动作迁移v2.5_2034884568989310978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034884568989310978.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（98 个）：
- `Reroute`
- `WanVideoVAELoader`
- `Reroute`
- `Reroute`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy compare`
- `GetNode`
- `GetNode`
- `easy ifElse`
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
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `DF_Int_to_Float`
- `SetNode`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `Reroute`
- `GetNode`
- `SetNode`
- `DrawViTPose`
- `GetNode`
- `WanVideoClipVisionEncode`
- `ImageFromBatch`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `Reroute`
- `ImageFromBatch`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `GetNode`
- `GetNode`
- `CR Text`
- `SetNode`
- `SetNode`
- `easy int`
- `SimpleMath+`
- `GetNode`
- `Reroute`
- `SetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `easy float`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `VHS_LoadVideo`

## 知识

覆盖率 **39%**（38/98）

**有卡**：`WanVideoVAELoader`、`easy compare`、`WanVideoTextEncodeCached`、`DF_Int_to_Float`、`WanVideoDecode`、`DrawViTPose`、`WanVideoClipVisionEncode`、`ImageFromBatch`、`INTConstant`、`VHS_VideoCombine`、`LoadImage`、`CR Text`、`easy int`、`SimpleMath+`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`easy cleanGpuUsed`、`RIFE VFI`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`easy float`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
