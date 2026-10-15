---
key: 视频生成/文生视频/Wan2.2 Smooth Mix高动态文生视频V2（KJ版）_1979020058171183105.json
name: Wan2.2 Smooth Mix高动态文生视频V2（KJ版）_1979020058171183105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth Mix高动态文生视频V2（KJ版）_1979020058171183105.json
hash: a1806e06176174e1
coverage: 0.861111
learned_at: 2026-10-15 22:47:10
nodes: [WanVideoSetBlockSwap, JWInteger, WanVideoSetBlockSwap, JWInteger, JWInteger, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, INTConstant, INTConstant, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoBlockSwap, PrimitiveNode, WanVideoEmptyEmbeds, CreateCFGScheduleFloatList, Note, Note, Note, Note, WanVideoTextEncode, CR Prompt Text, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, VHS_VideoCombine, ImageFromBatch+, WanVideoDecode, TT_img_enc, SaveImage]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 Smooth Mix高动态文生视频V2（KJ版）_1979020058171183105.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth Mix高动态文生视频V2（KJ版）_1979020058171183105.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `WanVideoSetBlockSwap`
- `JWInteger`
- `WanVideoSetBlockSwap`
- `JWInteger`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `WanVideoEmptyEmbeds`
- `CreateCFGScheduleFloatList`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `WanVideoDecode`
- `TT_img_enc`
- `SaveImage`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`WanVideoSetBlockSwap`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`INTConstant`、`WanVideoSampler`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`CR Prompt Text`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`VHS_VideoCombine`、`ImageFromBatch+`、`WanVideoDecode`、`TT_img_enc`、`SaveImage`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
