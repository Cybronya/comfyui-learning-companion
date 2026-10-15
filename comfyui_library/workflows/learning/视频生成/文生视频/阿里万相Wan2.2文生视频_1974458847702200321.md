---
key: 视频生成/文生视频/阿里万相Wan2.2文生视频_1974458847702200321.json
name: 阿里万相Wan2.2文生视频_1974458847702200321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/阿里万相Wan2.2文生视频_1974458847702200321.json
hash: 57bdf475854aaa7f
coverage: 0.916667
learned_at: 2026-10-15 22:49:05
nodes: [easy cleanGpuUsed, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy cleanGpuUsed, WanVideoDecode, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoLoraSelect, PrimitiveInt, PrimitiveInt, WanVideoBlockSwap, WanVideoTextEncode, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, GetImageSizeAndCount, WanVideoLoraSelect, WanVideoEmptyEmbeds, ImageFromBatch+, CR Text, WanVideoSampler, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
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

覆盖率 **92%**（22/24）

**有卡**：`easy cleanGpuUsed`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`WanVideoEmptyEmbeds`、`ImageFromBatch+`、`CR Text`、`WanVideoSampler`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、GetImageSizeAndCount
