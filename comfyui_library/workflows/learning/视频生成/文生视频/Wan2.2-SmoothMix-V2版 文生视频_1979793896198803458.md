---
key: 视频生成/文生视频/Wan2.2-SmoothMix-V2版 文生视频_1979793896198803458.json
name: Wan2.2-SmoothMix-V2版 文生视频_1979793896198803458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-SmoothMix-V2版 文生视频_1979793896198803458.json
hash: 07ec0fe42a58772e
coverage: 0.761905
learned_at: 2026-10-11 02:45:02
nodes: [WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, WanVideoEmptyEmbeds, WanVideoSampler, easy cleanGpuUsed, ImageFromBatch+, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, CR Text]
patterns: []
missing: [CR Text, ImageFromBatch+, easy cleanGpuUsed]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2-SmoothMix-V2版 文生视频_1979793896198803458.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-SmoothMix-V2版 文生视频_1979793896198803458.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `ImageFromBatch+`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `CR Text`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`

**缺卡**（3）：`CR Text`、`ImageFromBatch+`、`easy cleanGpuUsed`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoSetLoRAs、GetImageSizeAndCount、VHS_VideoCombine

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
