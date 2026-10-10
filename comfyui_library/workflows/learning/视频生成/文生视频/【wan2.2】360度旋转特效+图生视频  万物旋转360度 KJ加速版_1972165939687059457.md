---
key: 视频生成/文生视频/【wan2.2】360度旋转特效+图生视频  万物旋转360度 KJ加速版_1972165939687059457.json
name: 【wan2.2】360度旋转特效+图生视频  万物旋转360度 KJ加速版_1972165939687059457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【wan2.2】360度旋转特效+图生视频  万物旋转360度 KJ加速版_1972165939687059457.json
hash: 30f9880808a98b56
coverage: 0.820513
learned_at: 2026-10-10 23:10:08
nodes: [easy textSwitch, WanVideoTextEncode, CombinationText, WanVideoVAELoader, MathExpression|pysssss, WanVideoSampler, WanVideoSampler, INTConstant, INTConstant, WanVideoExperimentalArgs, WanVideoSLG, Note, CogVideoEnhanceAVideo, WanVideoDecode, WanVideoImageToVideoEncode, JWInteger, Int, CreateCFGScheduleFloatList, easy showAnything, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, Int, WanVideoTorchCompileSettings, WanVideoLoraSelect, easy string, CR Text, VHS_VideoCombine, GetImageSizeAndCount, PreviewImage, RH_LLMAPI_NODE, ImageResizeKJv2, LoadImage]
patterns: []
missing: [CR Text, MathExpression|pysssss, easy string, easy textSwitch]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy string` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/【wan2.2】360度旋转特效+图生视频  万物旋转360度 KJ加速版_1972165939687059457.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【wan2.2】360度旋转特效+图生视频  万物旋转360度 KJ加速版_1972165939687059457.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `easy textSwitch`
- `WanVideoTextEncode`
- `CombinationText`
- `WanVideoVAELoader`
- `MathExpression|pysssss`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `Note`
- `CogVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `JWInteger`
- `Int`
- `CreateCFGScheduleFloatList`
- `easy showAnything`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `Int`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `easy string`
- `CR Text`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `ImageResizeKJv2`
- `LoadImage`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`WanVideoTextEncode`、`CombinationText`、`WanVideoVAELoader`、`WanVideoSampler`、`INTConstant`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`CogVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`JWInteger`、`Int`、`CreateCFGScheduleFloatList`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`RH_LLMAPI_NODE`、`ImageResizeKJv2`、`LoadImage`

**缺卡**（4）：`CR Text`、`MathExpression|pysssss`、`easy string`、`easy textSwitch`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy string` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
