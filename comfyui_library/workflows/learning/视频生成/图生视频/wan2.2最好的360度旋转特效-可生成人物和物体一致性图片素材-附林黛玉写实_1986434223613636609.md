---
key: 视频生成/图生视频/wan2.2最好的360度旋转特效-可生成人物和物体一致性图片素材-附林黛玉写实_1986434223613636609.json
name: wan2.2最好的360度旋转特效-可生成人物和物体一致性图片素材-附林黛玉写实_1986434223613636609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2最好的360度旋转特效-可生成人物和物体一致性图片素材-附林黛玉写实_1986434223613636609.json
hash: 81b49c86d2569016
coverage: 0.76087
learned_at: 2026-10-15 22:32:55
nodes: [CLIPTextEncode, CLIPLoader, Note, CLIPTextEncode, WanVideoTextEmbedBridge, WanVideoDecode, CreateCFGScheduleFloatList, WanVideoSampler, INTConstant, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, INTConstant, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoImageToVideoEncode, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoSampler, GetImageSizeAndCount, SetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, Note, LoadWanVideoT5TextEncoder, WanVideoTextEncode, GetNode, SetNode, Note, WanVideoLoraSelect, WanVideoLoraSelect, Primitive integer [Crystools], WanVideoBlockSwap, SetNode, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, JWStringMultiline, LoadImage, SaveImage, GetNode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2最好的360度旋转特效-可生成人物和物体一致性图片素材-附林黛玉写实_1986434223613636609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986434223613636609.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（46 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Note`
- `CLIPTextEncode` ★核心
- `WanVideoTextEmbedBridge`
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `INTConstant`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Primitive integer [Crystools]`
- `WanVideoBlockSwap`
- `SetNode`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWStringMultiline`
- `LoadImage`
- `SaveImage`
- `GetNode`
- `VHS_VideoCombine`

## 知识

覆盖率 **76%**（35/46）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`WanVideoTextEmbedBridge`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`INTConstant`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`Primitive integer [Crystools]`、`WanVideoBlockSwap`、`JWStringMultiline`、`LoadImage`、`SaveImage`、`VHS_VideoCombine`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
