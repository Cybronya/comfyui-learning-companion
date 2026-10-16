---
key: 视频生成/图生视频/wan2.2首尾帧生视频（附自动提示词）_2013562059773972482.json
name: wan2.2首尾帧生视频（附自动提示词）_2013562059773972482.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2013562059773972482.json
hash: fbbfa10848627df4
coverage: 0.506494
learned_at: 2026-10-15 22:34:31
nodes: [WanFirstLastFrameToVideo, UNETLoader, MarkdownNote, CLIPLoader, SetNode, VAELoader, SetNode, GetNode, GetNode, GetNode, CM_IntToFloat, GetNode, CRTFirstLastFrameSelector, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Int, Int, SetNode, SetNode, SaveImage, GetNode, RIFE VFI, GetNode, Int, MultiplyNode, VHS_VideoCombine, GetNode, easy cleanGpuUsed, SaveImage, VHS_VideoCombine, StringReplace, Qwen3_VQA, ToString, ImpactSwitch, ShellAgentPluginOutputText, easy cleanGpuUsed, LayerUtility: PurgeVRAM, JoinStrings, Reroute, LayerUtility: PurgeVRAM, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, CLIPTextEncode, GetNode, Int, easy cleanGpuUsed, EmptyImage, EmptyImage, GetNode, GetNode, GetNode, GetNode, Int, SetNode, SetNode, GetNode, DuckHideNode, SetNode, SetNode, SetNode, MarkdownNote, LoadImage, TextInput_, easy ifElse, UNETLoader, Int, Int, ImageConcatMulti, VAEDecode, KSamplerAdvanced, SetNode, GetNode, GetNode, easy ifElse, BooleanUnary, LoadImage, GetNode, ImageResizeKJv2, GetNode, easy boolean, AnyIsEmpty, easy ifElse, SetNode, INTConstant, INTConstant, easy ifElse, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImpactSwitch, SetNode, easy ifElse, INTConstant, SetNode, INTConstant, easy boolean, INTConstant, AnyIsEmpty, easy ifElse, BooleanUnary, ImpactSwitch, SetNode, KSamplerAdvanced, UNETLoader, UNETLoader, LoraLoaderModelOnly, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, SetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, SetNode, PrimitiveBoolean, ImpactSwitch, UNETLoader, MarkdownNote, GetNode, GetNode, TextInput_, MarkdownNote, TextInput_, easy showAnything, Fast Groups Bypasser (rgthree), ImpactSwitch, MarkdownNote, INTConstant, MarkdownNote, ImpactSwitch, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2首尾帧生视频（附自动提示词）_2013562059773972482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013562059773972482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（154 个）：
- `WanFirstLastFrameToVideo`
- `UNETLoader` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CM_IntToFloat`
- `GetNode`
- `CRTFirstLastFrameSelector`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `SaveImage`
- `GetNode`
- `RIFE VFI`
- `GetNode`
- `Int`
- `MultiplyNode`
- `VHS_VideoCombine`
- `GetNode`
- `easy cleanGpuUsed`
- `SaveImage`
- `VHS_VideoCombine`
- `StringReplace`
- `Qwen3_VQA`
- `ToString`
- `ImpactSwitch`
- `ShellAgentPluginOutputText`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `JoinStrings`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `Int`
- `easy cleanGpuUsed`
- `EmptyImage`
- `EmptyImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `SetNode`
- `SetNode`
- `GetNode`
- `DuckHideNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `LoadImage`
- `TextInput_`
- `easy ifElse`
- `UNETLoader` ★核心
- `Int`
- `Int`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `easy ifElse`
- `BooleanUnary`
- `LoadImage`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `easy boolean`
- `AnyIsEmpty`
- `easy ifElse`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `easy ifElse`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `SetNode`
- `easy ifElse`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `easy boolean`
- `INTConstant`
- `AnyIsEmpty`
- `easy ifElse`
- `BooleanUnary`
- `ImpactSwitch`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `SetNode`
- `PrimitiveBoolean`
- `ImpactSwitch`
- `UNETLoader` ★核心
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `TextInput_`
- `MarkdownNote`
- `TextInput_`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `ImpactSwitch`
- `MarkdownNote`
- `INTConstant`
- `MarkdownNote`
- `ImpactSwitch`
- `PrimitiveBoolean`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **51%**（78/154）

**有卡**：`WanFirstLastFrameToVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CM_IntToFloat`、`CRTFirstLastFrameSelector`、`Int`、`SaveImage`、`RIFE VFI`、`MultiplyNode`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`StringReplace`、`Qwen3_VQA`、`ToString`、`ShellAgentPluginOutputText`、`LayerUtility: PurgeVRAM`、`JoinStrings`、`CLIPTextEncode`、`EmptyImage`、`DuckHideNode`、`LoadImage`、`TextInput_`、`ImageConcatMulti`、`VAEDecode`、`KSamplerAdvanced`、`BooleanUnary`、`ImageResizeKJv2`、`easy boolean`、`AnyIsEmpty`、`INTConstant`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader
