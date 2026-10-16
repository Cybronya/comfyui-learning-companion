---
key: 视频生成/图生视频/Wan2.2图生视频，支持首尾帧_1979152204013670402.json
name: Wan2.2图生视频，支持首尾帧_1979152204013670402.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979152204013670402.json
hash: b2ce9f39eb1c5200
coverage: 0.965517
learned_at: 2026-10-15 22:32:22
nodes: [WanVideoSampler, WanVideoSampler, easy cleanGpuUsed, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadImage, ImageResize+, DF_Integer, WanVideoDecode, ImageFromBatch+, CreateCFGScheduleFloatList, ImageResize+, DF_Integer, JWInteger, DF_Integer, DF_Int_to_Float, WanVideoTextEncode, DF_Text_Box, VHS_VideoCombine, LoadImage, LoadWanVideoT5TextEncoder, WanVideoVAELoader, PrimitiveNode, MathExpression|pysssss, WanVideoImageToVideoEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频，支持首尾帧_1979152204013670402.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979152204013670402.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadImage`
- `ImageResize+`
- `DF_Integer`
- `WanVideoDecode`
- `ImageFromBatch+`
- `CreateCFGScheduleFloatList`
- `ImageResize+`
- `DF_Integer`
- `JWInteger`
- `DF_Integer`
- `DF_Int_to_Float`
- `WanVideoTextEncode`
- `DF_Text_Box`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `PrimitiveNode`
- `MathExpression|pysssss`
- `WanVideoImageToVideoEncode`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`LoadImage`、`ImageResize+`、`DF_Integer`、`WanVideoDecode`、`ImageFromBatch+`、`CreateCFGScheduleFloatList`、`JWInteger`、`DF_Int_to_Float`、`WanVideoTextEncode`、`DF_Text_Box`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
