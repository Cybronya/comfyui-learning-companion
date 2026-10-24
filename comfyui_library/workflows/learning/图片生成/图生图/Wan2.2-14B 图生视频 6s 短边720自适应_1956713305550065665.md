---
key: 图片生成/图生图/Wan2.2-14B 图生视频 6s 短边720自适应_1956713305550065665.json
name: Wan2.2-14B 图生视频 6s 短边720自适应_1956713305550065665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2-14B 图生视频 6s 短边720自适应_1956713305550065665.json
hash: a78f0625c023acf7
coverage: 0.869565
learned_at: 2026-10-23 11:28:05
nodes: [easy imageScaleDownToSize, PreviewImage, GetImageSize, PreviewImage, MathExpression|pysssss, MathExpression|pysssss, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, PrimitiveNode, WanVideoVAELoader, WanVideoTextEncode, easy showAnything, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSampler, easy showAnything, MathExpression|pysssss, MathExpression|pysssss, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, GetImageSizeAndCount, LayerUtility: BooleanOperatorV2, LayerUtility: BooleanOperatorV2, ImageScale, LayerUtility: If , LayerUtility: If , WanVideoImageToVideoEncode, WanVideoLoraSelect, LoadImage, JjkText, WanVideoBlockSwap, WanVideoLoraSelect, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoBlockSwap, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2-14B 图生视频 6s 短边720自适应_1956713305550065665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2-14B 图生视频 6s 短边720自适应_1956713305550065665.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `easy imageScaleDownToSize`
- `PreviewImage`
- `GetImageSize`
- `PreviewImage`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `easy showAnything`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: BooleanOperatorV2`
- `ImageScale`
- `LayerUtility: If `
- `LayerUtility: If `
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `LoadImage`
- `JjkText`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`easy imageScaleDownToSize`、`GetImageSize`、`MathExpression|pysssss`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`easy cleanGpuUsed`、`GetImageSizeAndCount`、`LayerUtility: BooleanOperatorV2`、`ImageScale`、`LayerUtility: If `、`WanVideoImageToVideoEncode`、`WanVideoLoraSelect`、`LoadImage`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
