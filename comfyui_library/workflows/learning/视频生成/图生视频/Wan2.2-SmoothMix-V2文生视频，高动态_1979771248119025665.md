---
key: 视频生成/图生视频/Wan2.2-SmoothMix-V2文生视频，高动态_1979771248119025665.json
name: Wan2.2-SmoothMix-V2文生视频，高动态_1979771248119025665.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979771248119025665.json
hash: c574cf71162978aa
coverage: 0.875
learned_at: 2026-10-15 22:32:26
nodes: [WanVideoDecode, WanVideoSetBlockSwap, GetImageSizeAndCount, VHS_VideoCombine, LoadImage, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, PrimitiveInt, PrimitiveInt, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoTextEncode, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, CR Text, WanVideoEmptyEmbeds, ImageFromBatch+, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-SmoothMix-V2文生视频，高动态_1979771248119025665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979771248119025665.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（24 个）：
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `LoadImage`
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `WanVideoEmptyEmbeds`
- `ImageFromBatch+`
- `MarkdownNote`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`WanVideoDecode`、`WanVideoSetBlockSwap`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`LoadImage`、`easy cleanGpuUsed`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoSampler`、`CR Text`、`WanVideoEmptyEmbeds`、`ImageFromBatch+`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoSetLoRAs、GetImageSizeAndCount
