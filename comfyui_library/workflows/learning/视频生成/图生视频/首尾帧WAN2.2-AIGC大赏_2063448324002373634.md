---
key: 视频生成/图生视频/首尾帧WAN2.2-AIGC大赏_2063448324002373634.json
name: 首尾帧WAN2.2-AIGC大赏_2063448324002373634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063448324002373634.json
hash: 3fc0f7ee65a4c442
coverage: 0.974359
learned_at: 2026-10-15 22:39:13
nodes: [PrimitiveNode, JWInteger, WanVideoTextEncode, INTConstant, SimpleMath+, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, LayerUtility: PurgeVRAM, WanVideoDecode, ImageResize+, ImageResize+, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, LayerUtility: PurgeVRAM, CreateCFGScheduleFloatList, WanVideoLoraSelect, LoadImage, JWInteger, JWInteger, JWInteger, JWInteger, CR Prompt Text, easy cleanGpuUsed, VHS_VideoCombine, DF_Int_to_Float, SaveImage, TT_img_enc_v2, WanVideoClipVisionEncode, WanVideoModelLoader, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧WAN2.2-AIGC大赏_2063448324002373634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063448324002373634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（39 个）：
- `PrimitiveNode`
- `JWInteger`
- `WanVideoTextEncode`
- `INTConstant`
- `SimpleMath+`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `ImageResize+`
- `ImageResize+`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `DF_Int_to_Float`
- `SaveImage`
- `TT_img_enc_v2`
- `WanVideoClipVisionEncode`
- `WanVideoModelLoader`
- `LoadImage`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`JWInteger`、`WanVideoTextEncode`、`INTConstant`、`SimpleMath+`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`ImageResize+`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`LoadImage`、`CR Prompt Text`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`DF_Int_to_Float`、`SaveImage`、`TT_img_enc_v2`、`WanVideoClipVisionEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
