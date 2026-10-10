---
key: 视频生成/文生视频/Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186.json
name: Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186.json
hash: c726204ac79efe13
coverage: 0.866667
learned_at: 2026-10-10 23:07:29
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoSetLoRAs, CreateCFGScheduleFloatList, SimpleMath+, INTConstant, INTConstant, GetImageSizeAndCount, WanVideoVAELoader, WanVideoTextEncode, INTConstant, INTConstant, INTConstant, SimpleMath+, WanVideoDecode, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, easy seed, WanVideoSampler, WanVideoLoraSelect, WanVideoEmptyEmbeds, WanVideoSampler, VHS_VideoCombine, LoadImage, easy positive]
patterns: []
missing: [SimpleMath+, SimpleMath+, easy positive, easy seed]
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **87%**（26/30）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`LoadImage`

**缺卡**（4）：`SimpleMath+`、`SimpleMath+`、`easy positive`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
