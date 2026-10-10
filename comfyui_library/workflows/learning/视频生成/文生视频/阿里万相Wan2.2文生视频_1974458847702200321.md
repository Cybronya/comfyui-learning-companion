---
key: 视频生成/文生视频/阿里万相Wan2.2文生视频_1974458847702200321.json
name: 阿里万相Wan2.2文生视频_1974458847702200321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/阿里万相Wan2.2文生视频_1974458847702200321.json
hash: 57bdf475854aaa7f
coverage: 0.75
learned_at: 2026-10-10 23:14:16
nodes: [easy cleanGpuUsed, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy cleanGpuUsed, WanVideoDecode, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoLoraSelect, PrimitiveInt, PrimitiveInt, WanVideoBlockSwap, WanVideoTextEncode, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, GetImageSizeAndCount, WanVideoLoraSelect, WanVideoEmptyEmbeds, ImageFromBatch+, CR Text, WanVideoSampler, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: [CR Text, ImageFromBatch+, easy cleanGpuUsed, easy cleanGpuUsed]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/阿里万相Wan2.2文生视频_1974458847702200321.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/阿里万相Wan2.2文生视频_1974458847702200321.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（24 个）：
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `WanVideoEmptyEmbeds`
- `ImageFromBatch+`
- `CR Text`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **75%**（18/24）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`VHS_VideoCombine`

**缺卡**（4）：`CR Text`、`ImageFromBatch+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、GetImageSizeAndCount

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
