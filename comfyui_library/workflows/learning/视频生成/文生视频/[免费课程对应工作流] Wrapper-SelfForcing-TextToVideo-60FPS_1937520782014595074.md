---
key: 视频生成/文生视频/[免费课程对应工作流] Wrapper-SelfForcing-TextToVideo-60FPS_1937520782014595074.json
name: [免费课程对应工作流] Wrapper-SelfForcing-TextToVideo-60FPS_1937520782014595074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/[免费课程对应工作流] Wrapper-SelfForcing-TextToVideo-60FPS_1937520782014595074.json
hash: 0e91b09fd3a12f77
coverage: 0.384615
learned_at: 2026-10-10 23:08:25
nodes: [SetNode, Anything Everywhere, Reroute, Reroute, Note, Note, Note, Reroute, Reroute, VHS_VideoCombine, WanVideoEnhanceAVideo, Reroute, WanVideoDecode, easy cleanGpuUsed, Reroute, RIFE VFI, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, Reroute, easy clearCacheAll, Int, Text Prompt (JPS), Text Prompt (JPS), WanVideoSampler, easy cleanGpuUsed, WanVideoTextEncode, easy clearCacheAll, Note, WanVideoLoraSelect, easy cleanGpuUsed, Reroute, easy cleanGpuUsed, UpscaleModelLoader, Reroute, VHS_VideoCombine, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder]
patterns: []
missing: [RIFE VFI, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, easy clearCacheAll, Text Prompt (JPS), Text Prompt (JPS)]
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `Text Prompt (JPS)` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Text Prompt (JPS)` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/[免费课程对应工作流] Wrapper-SelfForcing-TextToVideo-60FPS_1937520782014595074.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/[免费课程对应工作流] Wrapper-SelfForcing-TextToVideo-60FPS_1937520782014595074.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（39 个）：
- `SetNode`
- `Anything Everywhere`
- `Reroute`
- `Reroute`
- `Note`
- `Note`
- `Note`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `Reroute`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `Reroute`
- `RIFE VFI`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `Reroute`
- `easy clearCacheAll`
- `Int`
- `Text Prompt (JPS)`
- `Text Prompt (JPS)`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `easy clearCacheAll`
- `Note`
- `WanVideoLoraSelect`
- `easy cleanGpuUsed`
- `Reroute`
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `Reroute`
- `VHS_VideoCombine`
- `WanVideoEmptyEmbeds`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **38%**（15/39）

**有卡**：`VHS_VideoCombine`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`Int`、`WanVideoSampler`、`WanVideoTextEncode`、`UpscaleModelLoader`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`

**缺卡**（9）：`RIFE VFI`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy clearCacheAll`、`easy clearCacheAll`、`Text Prompt (JPS)`、`Text Prompt (JPS)`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、UpscaleModelLoader、UpscaleModelLoader

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Prompt (JPS)` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Text Prompt (JPS)` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
