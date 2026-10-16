---
key: 视频生成/文生视频/wan2.2文_图生视频反推图像_1951334192300937218.json
name: wan2.2文_图生视频反推图像_1951334192300937218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1951334192300937218.json
hash: 0a8f3f61f12c5bcf
coverage: 0.777778
learned_at: 2026-10-15 22:43:37
nodes: [PreviewImage, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoDecode, JjkText, WanVideoVAELoader, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, FluxResolutionNode, easy showAnything, Note, RH_Prompter, TextCombinerTwo, JjkText, JjkText, TextCombinerTwo, JjkText, easy showAnything, RH_Prompter, easy showAnything, LoadWanVideoT5TextEncoder, easy anythingIndexSwitch, Reroute, Display Any (rgthree), VHS_VideoCombine, INTConstant, WanVideoSampler, WanVideoTextEncode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoLoraSelect, JjkText, MMAudioFeatureUtilsLoader, MMAudioModelLoader, easy showAnything, RH_Captioner, RH_Translator, MMAudioSampler, Int, Evaluate Integers, Int, MathExpression|pysssss, WanVideoImageToVideoEncode, JWInteger, WanVideoModelLoader, WanVideoModelLoader, easy anythingIndexSwitch, easy anythingIndexSwitch, Int, LoadImage, ImageResizeKJv2, easy showAnything, WanVideoTextEncode, CreateCFGScheduleFloatList, INTConstant, PrimitiveNode, LayerUtility: PurgeVRAM, RH_LLMAPI_NODE, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2文_图生视频反推图像_1951334192300937218.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1951334192300937218.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（63 个）：
- `PreviewImage`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `JjkText`
- `WanVideoVAELoader`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `FluxResolutionNode`
- `easy showAnything`
- `Note`
- `RH_Prompter`
- `TextCombinerTwo`
- `JjkText`
- `JjkText`
- `TextCombinerTwo`
- `JjkText`
- `easy showAnything`
- `RH_Prompter`
- `easy showAnything`
- `LoadWanVideoT5TextEncoder`
- `easy anythingIndexSwitch`
- `Reroute`
- `Display Any (rgthree)`
- `VHS_VideoCombine`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JjkText`
- `MMAudioFeatureUtilsLoader`
- `MMAudioModelLoader`
- `easy showAnything`
- `RH_Captioner`
- `RH_Translator`
- `MMAudioSampler` ★核心
- `Int`
- `Evaluate Integers`
- `Int`
- `MathExpression|pysssss`
- `WanVideoImageToVideoEncode`
- `JWInteger`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `Int`
- `LoadImage`
- `ImageResizeKJv2`
- `easy showAnything`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `PrimitiveNode`
- `LayerUtility: PurgeVRAM`
- `RH_LLMAPI_NODE`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **78%**（49/63）

**有卡**：`LoadWanVideoT5TextEncoder`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoVAELoader`、`MathExpression|pysssss`、`FluxResolutionNode`、`RH_Prompter`、`TextCombinerTwo`、`easy anythingIndexSwitch`、`Display Any (rgthree)`、`VHS_VideoCombine`、`INTConstant`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoLoraSelect`、`MMAudioFeatureUtilsLoader`、`MMAudioModelLoader`、`RH_Captioner`、`RH_Translator`、`MMAudioSampler`、`Int`、`Evaluate Integers`、`WanVideoImageToVideoEncode`、`JWInteger`、`WanVideoModelLoader`、`LoadImage`、`ImageResizeKJv2`、`CreateCFGScheduleFloatList`、`RH_LLMAPI_NODE`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、MMAudioSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
