---
key: 视频生成/文生视频/Wan2.2-SmoothMix-V2版 文生视频_1979793896198803458.json
name: Wan2.2-SmoothMix-V2版 文生视频_1979793896198803458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-SmoothMix-V2版 文生视频_1979793896198803458.json
hash: 07ec0fe42a58772e
coverage: 0.904762
learned_at: 2026-10-15 22:47:12
nodes: [WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, WanVideoEmptyEmbeds, WanVideoSampler, easy cleanGpuUsed, ImageFromBatch+, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, CR Text]
patterns: []
missing: []
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

覆盖率 **90%**（19/21）

**有卡**：`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`easy cleanGpuUsed`、`ImageFromBatch+`、`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`、`CR Text`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoSetLoRAs、GetImageSizeAndCount、VHS_VideoCombine
