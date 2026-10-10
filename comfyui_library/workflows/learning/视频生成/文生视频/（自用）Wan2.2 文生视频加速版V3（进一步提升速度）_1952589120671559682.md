---
key: 视频生成/文生视频/（自用）Wan2.2 文生视频加速版V3（进一步提升速度）_1952589120671559682.json
name: （自用）Wan2.2 文生视频加速版V3（进一步提升速度）_1952589120671559682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 文生视频加速版V3（进一步提升速度）_1952589120671559682.json
hash: e136820ab2f4b577
coverage: 0.8
learned_at: 2026-10-10 23:14:44
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, CR Prompt Text, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, Note, SaveLatent, WanVideoSampler, WanVideoVAELoader, LoadLatent, VHS_VideoCombine, WanVideoDecode, LoadImage, JWInteger, SaveImage]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（自用）Wan2.2 文生视频加速版V3（进一步提升速度）_1952589120671559682.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 文生视频加速版V3（进一步提升速度）_1952589120671559682.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（40 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `CR Prompt Text`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Note`
- `SaveLatent`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `LoadLatent`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LoadImage`
- `JWInteger`
- `SaveImage`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`INTConstant`、`JWInteger`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`SaveLatent`、`WanVideoVAELoader`、`LoadLatent`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadImage`、`SaveImage`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
