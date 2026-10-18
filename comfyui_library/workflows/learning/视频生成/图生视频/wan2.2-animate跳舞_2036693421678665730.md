---
key: 视频生成/图生视频/wan2.2-animate跳舞_2036693421678665730.json
name: wan2.2-animate跳舞_2036693421678665730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-animate跳舞_2036693421678665730.json
hash: 127c7df1dfe8ad6a
coverage: 0.489796
learned_at: 2026-10-15 22:35:53
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, ImageResizeKJv2, VHS_VideoInfo, WanVideoContextOptions, Display Any (rgthree), LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, MathExpression|pysssss, Note, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, Display Any (rgthree), SetNode, GetNode, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSamplerExtraArgs, SetNode, SetNode, GetNode, Amage FPS Converter, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, Note, CR Text, INTConstant, INTConstant, JWIntegerToFloat, GetNode, WanVideoBlockSwap, WanVideoTextEncodeCached, CLIPVisionLoader, GetNode, GetNode, CM_FloatToInt, VHS_LoadVideo, INTConstant, SetNode, ImageResizeKJv2, INTConstant, INTConstant, INTConstant, LoadImage, OnnxDetectionModelLoader, DrawViTPose, PoseAndFaceDetection, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, WanVideoDecode, VHS_SelectImages, SetNode, SetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, DuckHideNode, SaveImage, GetNode, ImpactSwitch, ImpactSwitch, LoadImage, easy int]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-animate跳舞_2036693421678665730.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036693421678665730.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（98 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `VHS_VideoInfo`
- `WanVideoContextOptions`
- `Display Any (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `MathExpression|pysssss`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Display Any (rgthree)`
- `SetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoSchedulerv2`
- `WanVideoSamplerExtraArgs` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `Amage FPS Converter`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `CR Text`
- `INTConstant`
- `INTConstant`
- `JWIntegerToFloat`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `CM_FloatToInt`
- `VHS_LoadVideo`
- `INTConstant`
- `SetNode`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `VHS_SelectImages`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DuckHideNode`
- `SaveImage`
- `GetNode`
- `ImpactSwitch`
- `ImpactSwitch`
- `LoadImage`
- `easy int`

## 知识

覆盖率 **49%**（48/98）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`VHS_VideoInfo`、`WanVideoContextOptions`、`Display Any (rgthree)`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`MathExpression|pysssss`、`WanVideoSamplerv2`、`WanVideoSchedulerv2`、`WanVideoSamplerExtraArgs`、`Amage FPS Converter`、`CR Text`、`INTConstant`、`JWIntegerToFloat`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`CM_FloatToInt`、`VHS_LoadVideo`、`LoadImage`、`OnnxDetectionModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`VHS_SelectImages`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`DuckHideNode`、`SaveImage`、`easy int`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoSamplerExtraArgs、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
