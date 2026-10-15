---
key: 视频生成/文生视频/Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186.json
name: Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186.json
hash: c726204ac79efe13
coverage: 1
learned_at: 2026-10-15 22:47:15
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoSetLoRAs, CreateCFGScheduleFloatList, SimpleMath+, INTConstant, INTConstant, GetImageSizeAndCount, WanVideoVAELoader, WanVideoTextEncode, INTConstant, INTConstant, INTConstant, SimpleMath+, WanVideoDecode, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, easy seed, WanVideoSampler, WanVideoLoraSelect, WanVideoEmptyEmbeds, WanVideoSampler, VHS_VideoCombine, LoadImage, easy positive]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `GetImageSizeAndCount`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `easy seed`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `easy positive`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`SimpleMath+`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`easy seed`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`LoadImage`、`easy positive`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
