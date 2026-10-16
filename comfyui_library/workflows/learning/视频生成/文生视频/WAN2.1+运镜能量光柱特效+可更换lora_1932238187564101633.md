---
key: 视频生成/文生视频/WAN2.1+运镜能量光柱特效+可更换lora_1932238187564101633.json
name: WAN2.1+运镜能量光柱特效+可更换lora_1932238187564101633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1932238187564101633.json
hash: 5bab8fd420a029f4
coverage: 1
learned_at: 2026-10-15 22:43:26
nodes: [LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, MathExpression|pysssss, Int, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, WanVideoVAELoader, ImageSizeAndBatchSize, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, WanVideoImageClipEncode, VHS_VideoCombine, Int, LoadImage, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.1+运镜能量光柱特效+可更换lora_1932238187564101633.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1932238187564101633.json`

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
- `VHS_VideoCombine`
- `Int`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`LoadWanVideoClipTextEncoder`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`Int`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoVAELoader`、`ImageSizeAndBatchSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`WanVideoImageClipEncode`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTextEncode`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
