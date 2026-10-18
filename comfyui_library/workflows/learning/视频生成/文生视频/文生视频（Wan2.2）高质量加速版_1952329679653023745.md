---
key: 视频生成/文生视频/文生视频（Wan2.2）高质量加速版_1952329679653023745.json
name: 文生视频（Wan2.2）高质量加速版_1952329679653023745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频（Wan2.2）高质量加速版_1952329679653023745.json
hash: 1d5118ce7bbb5779
coverage: 1
learned_at: 2026-10-15 22:43:38
nodes: [WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetLoRAs, CreateCFGScheduleFloatList, INTConstant, JWInteger, WanVideoEmptyEmbeds, VHS_VideoCombine, WanVideoSampler, INTConstant, CR Prompt Text, WanVideoSampler, WanVideoDecode, WanVideoVAELoader, easy seed, WanVideoModelLoader, WanVideoModelLoader, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/文生视频/文生视频（Wan2.2）高质量加速版_1952329679653023745.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1952329679653023745.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（28 个）：
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `INTConstant`
- `CR Prompt Text`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoVAELoader`
- `easy seed`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`INTConstant`、`JWInteger`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`WanVideoSampler`、`CR Prompt Text`、`WanVideoDecode`、`WanVideoVAELoader`、`easy seed`、`WanVideoModelLoader`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
