---
key: 视频生成/文生视频/（自用）Wan2.2 文生视频加速版V3（进一步提升速度）_1952589120671559682.json
name: （自用）Wan2.2 文生视频加速版V3（进一步提升速度）_1952589120671559682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 文生视频加速版V3（进一步提升速度）_1952589120671559682.json
hash: e136820ab2f4b577
coverage: 0.825
learned_at: 2026-10-15 22:49:12
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, CR Prompt Text, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, Note, SaveLatent, WanVideoSampler, WanVideoVAELoader, LoadLatent, VHS_VideoCombine, WanVideoDecode, LoadImage, JWInteger, SaveImage]
patterns: []
missing: []
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

覆盖率 **82%**（33/40）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`INTConstant`、`JWInteger`、`WanVideoTorchCompileSettings`、`CR Prompt Text`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`SaveLatent`、`WanVideoVAELoader`、`LoadLatent`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadImage`、`SaveImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
