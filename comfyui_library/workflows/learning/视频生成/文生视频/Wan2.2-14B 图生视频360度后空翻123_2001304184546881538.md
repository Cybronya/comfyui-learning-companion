---
key: 视频生成/文生视频/Wan2.2-14B 图生视频360度后空翻123_2001304184546881538.json
name: Wan2.2-14B 图生视频360度后空翻123_2001304184546881538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-14B 图生视频360度后空翻123_2001304184546881538.json
hash: ee1006bbdecf1690
coverage: 0.848485
learned_at: 2026-10-15 22:47:12
nodes: [CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, WanVideoSampler, easy cleanGpuUsed, WanVideoDecode, WanVideoTextEncode, MathExpression|pysssss, WanVideoSetLoRAs, WanVideoSampler, WanVideoImageToVideoEncode, PreviewImage, WanVideoModelLoader, LoadWanVideoT5TextEncoder, Bjornulf_ShowInt, Bjornulf_ShowInt, WanVideoSetLoRAs, VHS_VideoCombine, ImageResize+, ImageResizeKJv2, ImageFromBatch+, WanVideoLoraSelect, WanVideoLoraSelect, Fast Groups Muter (rgthree), JWInteger, LoadImage, ShowText, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, RH_Translator, JjkText, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2-14B 图生视频360度后空翻123_2001304184546881538.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-14B 图生视频360度后空翻123_2001304184546881538.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `MathExpression|pysssss`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `PreviewImage`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImageFromBatch+`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Fast Groups Muter (rgthree)`
- `JWInteger`
- `LoadImage`
- `ShowText`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `RH_Translator`
- `JjkText`
- `Note`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoTextEncode`、`MathExpression|pysssss`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`Bjornulf_ShowInt`、`VHS_VideoCombine`、`ImageResize+`、`ImageResizeKJv2`、`ImageFromBatch+`、`WanVideoLoraSelect`、`JWInteger`、`LoadImage`、`ShowText`、`RH_Translator`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
