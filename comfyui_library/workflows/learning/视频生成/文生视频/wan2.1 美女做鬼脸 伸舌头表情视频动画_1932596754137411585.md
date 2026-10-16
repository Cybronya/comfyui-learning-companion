---
key: 视频生成/文生视频/wan2.1 美女做鬼脸 伸舌头表情视频动画_1932596754137411585.json
name: wan2.1 美女做鬼脸 伸舌头表情视频动画_1932596754137411585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1932596754137411585.json
hash: af774745c5fc5b01
coverage: 1
learned_at: 2026-10-15 22:43:26
nodes: [LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, MathExpression|pysssss, Int, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, WanVideoVAELoader, ImageSizeAndBatchSize, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, WanVideoImageClipEncode, Int, WanVideoLoraSelect, VHS_VideoCombine, WanVideoTextEncode, WanVideoLoraSelect, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1 美女做鬼脸 伸舌头表情视频动画_1932596754137411585.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1932596754137411585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（19 个）：
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `MathExpression|pysssss`
- `Int`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoVAELoader`
- `ImageSizeAndBatchSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `WanVideoImageClipEncode`
- `Int`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `LoadImage`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`LoadWanVideoClipTextEncoder`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`Int`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoVAELoader`、`ImageSizeAndBatchSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`WanVideoImageClipEncode`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
