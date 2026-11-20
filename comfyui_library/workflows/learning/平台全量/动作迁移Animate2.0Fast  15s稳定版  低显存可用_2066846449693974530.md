---
key: 平台全量/动作迁移Animate2.0Fast  15s稳定版  低显存可用_2066846449693974530.json
name: 动作迁移Animate2.0Fast  15s稳定版  低显存可用_2066846449693974530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作迁移Animate2.0Fast  15s稳定版  低显存可用_2066846449693974530.json
hash: d43796f8421fcc07
coverage: 0.55
learned_at: 2026-11-14 01:45:15
nodes: [GetNode, GetNode, CLIPVisionLoader, GetNode, DrawViTPose, SetNode, SetNode, WanVideoSetBlockSwap, OnnxDetectionModelLoader, WanVideoTextEncodeCached, WanVideoVAELoader, SetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, PoseAndFaceDetection, GetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, WanVideoSetLoRAs, SetNode, easy cleanGpuUsed, WanVideoDecode, SetNode, GetNode, easy cleanGpuUsed, WanVideoSampler, WanVideoClipVisionEncode, GetNode, WanVideoLoraSelect, LoadImage, ComfyMathExpression, Int, GetNode, GetNode, SetNode, SetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoContextOptions, DownloadAndLoadGIMMVFIModel, SetNode, GetNode, WanVideoAnimateEmbeds, GIMMVFI_interpolate, easy showAnything, GetNode, GetNode, Fast Groups Bypasser (rgthree), easy anythingIndexSwitch, Int, Int, ComfyMathExpression, SetNode, 图像缩放V2_孤海, ImpactSwitch, Int, Int, Int, Int, PrimitiveBoolean, Int, Int, InversionDemoLazySwitch, SetNode, SetNode, GetNode, VHS_VideoCombine, MinNode, WanVideoBlockSwap, SetNode, SetNode, VHS_VideoInfo, ComfyMathExpression, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/动作迁移Animate2.0Fast  15s稳定版  低显存可用_2066846449693974530.json

> 来源文件 `comfyui_library/workflows/平台全量/动作迁移Animate2.0Fast  15s稳定版  低显存可用_2066846449693974530.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（80 个）：
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `DrawViTPose`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `OnnxDetectionModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoLoraSelect`
- `LoadImage`
- `ComfyMathExpression`
- `Int`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoContextOptions`
- `DownloadAndLoadGIMMVFIModel`
- `SetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GIMMVFI_interpolate`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `easy anythingIndexSwitch`
- `Int`
- `Int`
- `ComfyMathExpression`
- `SetNode`
- `图像缩放V2_孤海`
- `ImpactSwitch`
- `Int`
- `Int`
- `Int`
- `Int`
- `PrimitiveBoolean`
- `Int`
- `Int`
- `InversionDemoLazySwitch`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `MinNode`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `ComfyMathExpression`
- `VHS_LoadVideo`

## 知识

覆盖率 **55%**（44/80）

**有卡**：`CLIPVisionLoader`、`DrawViTPose`、`WanVideoSetBlockSwap`、`OnnxDetectionModelLoader`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`ImageResizeKJv2`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`LoadImage`、`ComfyMathExpression`、`Int`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoContextOptions`、`DownloadAndLoadGIMMVFIModel`、`WanVideoAnimateEmbeds`、`GIMMVFI_interpolate`、`easy anythingIndexSwitch`、`图像缩放V2_孤海`、`PrimitiveBoolean`、`InversionDemoLazySwitch`、`VHS_VideoCombine`、`MinNode`、`WanVideoBlockSwap`、`VHS_VideoInfo`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect、WanVideoLoraSelectMulti
