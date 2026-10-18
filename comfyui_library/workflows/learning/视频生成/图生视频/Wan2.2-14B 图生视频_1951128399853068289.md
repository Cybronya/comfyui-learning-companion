---
key: 视频生成/图生视频/Wan2.2-14B 图生视频_1951128399853068289.json
name: Wan2.2-14B 图生视频_1951128399853068289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-14B 图生视频_1951128399853068289.json
hash: c2cc5885fe0cec99
coverage: 0.824561
learned_at: 2026-10-15 22:30:57
nodes: [easy showAnything, easy showAnything, UpscaleModelLoader, ImageUpscaleWithModel, RIFE VFI, ImageScale, SimpleMath+, SimpleMath+, PlaySound|pysssss, WanVideoDecode, easy cleanGpuUsed, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoLoraSelect, PlaySound|pysssss, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoModelLoader, ImageResizeKJv2, VHS_VideoCombine, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoSampler, INTConstant, INTConstant, PrimitiveNode, RH_Prompter, CR Text Concatenate, LoadImage, RH_Captioner, JjkText, easy showAnything, easy anythingIndexSwitch, RH_Captioner, easy showAnything, easy showAnything, easy showAnything, CR Text Concatenate, ttN concat, RH_Prompter, easy showAnything, JjkText, VHS_VideoCombine, MathExpression|pysssss, JWInteger, CR Text, JWInteger, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-14B 图生视频_1951128399853068289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951128399853068289.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（57 个）：
- `easy showAnything`
- `easy showAnything`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `RIFE VFI`
- `ImageScale`
- `SimpleMath+`
- `SimpleMath+`
- `PlaySound|pysssss`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `PlaySound|pysssss`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `PrimitiveNode`
- `RH_Prompter`
- `CR Text Concatenate`
- `LoadImage`
- `RH_Captioner`
- `JjkText`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `RH_Captioner`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `CR Text Concatenate`
- `ttN concat`
- `RH_Prompter`
- `easy showAnything`
- `JjkText`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `JWInteger`
- `CR Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **82%**（47/57）

**有卡**：`UpscaleModelLoader`、`ImageUpscaleWithModel`、`RIFE VFI`、`ImageScale`、`SimpleMath+`、`PlaySound|pysssss`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`INTConstant`、`RH_Prompter`、`CR Text Concatenate`、`LoadImage`、`RH_Captioner`、`easy anythingIndexSwitch`、`ttN concat`、`MathExpression|pysssss`、`JWInteger`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
