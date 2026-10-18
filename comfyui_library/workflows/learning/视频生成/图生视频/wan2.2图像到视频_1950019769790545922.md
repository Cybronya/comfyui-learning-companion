---
key: 视频生成/图生视频/wan2.2图像到视频_1950019769790545922.json
name: wan2.2图像到视频_1950019769790545922.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图像到视频_1950019769790545922.json
hash: 7921f13f5e489a72
coverage: 0.904762
learned_at: 2026-10-15 22:30:51
nodes: [WanVideoBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, ImageResizeKJv2, WanVideoImageToVideoEncode, Fast Groups Muter (rgthree), WanVideoDecode, WanVideoSampler, Int, Int, easy showAnything, VHS_VideoCombine, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, CreateCFGScheduleFloatList, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, TextCombinerTwo, Primitive integer [Crystools], LayerColor: Brightness & Contrast, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, GetNode, MathExpression|pysssss, easy seed, INTConstant, TextBox, LoadImage, RH_Captioner, easy anythingIndexSwitch, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoLoraSelect, RH_Prompter, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图像到视频_1950019769790545922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950019769790545922.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `Fast Groups Muter (rgthree)`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `Int`
- `Int`
- `easy showAnything`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `TextCombinerTwo`
- `Primitive integer [Crystools]`
- `LayerColor: Brightness & Contrast`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `GetNode`
- `MathExpression|pysssss`
- `easy seed`
- `INTConstant`
- `TextBox`
- `LoadImage`
- `RH_Captioner`
- `easy anythingIndexSwitch`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoLoraSelect`
- `RH_Prompter`
- `Text Multiline`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`WanVideoSampler`、`Int`、`VHS_VideoCombine`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`TextCombinerTwo`、`Primitive integer [Crystools]`、`LayerColor: Brightness & Contrast`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`MathExpression|pysssss`、`easy seed`、`INTConstant`、`TextBox`、`LoadImage`、`RH_Captioner`、`easy anythingIndexSwitch`、`RH_Prompter`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
