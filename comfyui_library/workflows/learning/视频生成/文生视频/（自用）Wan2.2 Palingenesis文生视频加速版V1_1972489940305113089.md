---
key: 视频生成/文生视频/（自用）Wan2.2 Palingenesis文生视频加速版V1_1972489940305113089.json
name: （自用）Wan2.2 Palingenesis文生视频加速版V1_1972489940305113089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 Palingenesis文生视频加速版V1_1972489940305113089.json
hash: 80616140733a54b6
coverage: 0.840909
learned_at: 2026-10-10 23:14:41
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, WanVideoVAELoader, Float, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, SaveImage, WanVideoModelLoader, WanVideoModelLoader, JWInteger, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoTextEncode, PrimitiveNode, WanVideoSampler, GetImageSizeAndCount, WanVideoDecode, TT_img_enc, WanVideoSigmaToStep, INTConstant, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, SaveImage, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（自用）Wan2.2 Palingenesis文生视频加速版V1_1972489940305113089.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 Palingenesis文生视频加速版V1_1972489940305113089.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoVAELoader`
- `Float`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `SaveImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `JWInteger`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `WanVideoTextEncode`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `TT_img_enc`
- `WanVideoSigmaToStep`
- `INTConstant`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `SaveImage`
- `CR Prompt Text`

## 知识

覆盖率 **84%**（37/44）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoScheduler`、`WanVideoVAELoader`、`Float`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`SaveImage`、`WanVideoModelLoader`、`JWInteger`、`WanVideoEmptyEmbeds`、`WanVideoTextEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`TT_img_enc`、`WanVideoSigmaToStep`、`INTConstant`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`LoadImage`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
