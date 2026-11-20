---
key: 平台全量/运镜 _ WAN2.1-10种拍摄运镜方式_1970672070436790273.json
name: 运镜 _ WAN2.1-10种拍摄运镜方式_1970672070436790273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/运镜 _ WAN2.1-10种拍摄运镜方式_1970672070436790273.json
hash: 38b49f8e4bc063c1
coverage: 0.8
learned_at: 2026-11-14 02:48:14
nodes: [Reroute, VAELoader, Reroute, Reroute, easy cleanGpuUsed, WanVideoTeaCacheKJ, LayerUtility: BooleanOperator, LayerUtility: BooleanOperator, easy ifElse, Int, easy ifElse, LoraLoaderModelOnly, PathchSageAttentionKJ, UpscaleModelLoader, WanImageToVideo, VAEDecode, Fast Groups Muter (rgthree), KSampler, CLIPLoader, MathExpression|pysssss, SplitStringByDelimiter, Text Find and Replace, RH_Captioner, TextBox, Reroute, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPVisionEncode, CLIPTextEncode, FluxGuidance, CLIPVisionLoader, LayerUtility: PurgeVRAM, Reroute, ImageUpscaleWithModel, VHS_VideoCombine, CR String To Combo, ModelSamplingSD3, UNETLoader, LayerUtility: PurgeVRAM, easy cleanGpuUsed, VHS_VideoCombine, GetRandomIntegerInRange, Int, ImpactStringSelector, Text Find and Replace, Text Find and Replace, RH_Prompter, TextBox, RH_LLMAPI_NODE, easy showAnything, MathExpression|pysssss, easy int, PrimitiveString, PrimitiveBoolean, Model Input Switch, MathExpression|pysssss, LoadImage, MarkdownNote, TextBox, ImpactSwitch]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 558997555894137, "steps": 30}
---

# 平台全量/运镜 _ WAN2.1-10种拍摄运镜方式_1970672070436790273.json

> 来源文件 `comfyui_library/workflows/平台全量/运镜 _ WAN2.1-10种拍摄运镜方式_1970672070436790273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（60 个）：
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `WanVideoTeaCacheKJ`
- `LayerUtility: BooleanOperator`
- `LayerUtility: BooleanOperator`
- `easy ifElse`
- `Int`
- `easy ifElse`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UpscaleModelLoader`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `Fast Groups Muter (rgthree)`
- `KSampler` ★核心
- `CLIPLoader`
- `MathExpression|pysssss`
- `SplitStringByDelimiter`
- `Text Find and Replace`
- `RH_Captioner`
- `TextBox`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPVisionLoader`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `CR String To Combo`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `GetRandomIntegerInRange`
- `Int`
- `ImpactStringSelector`
- `Text Find and Replace`
- `Text Find and Replace`
- `RH_Prompter`
- `TextBox`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `MathExpression|pysssss`
- `easy int`
- `PrimitiveString`
- `PrimitiveBoolean`
- `Model Input Switch`
- `MathExpression|pysssss`
- `LoadImage`
- `MarkdownNote`
- `TextBox`
- `ImpactSwitch`

## 关键参数

- `seed` = `558997555894137`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（48/60）

**有卡**：`VAELoader`、`easy cleanGpuUsed`、`WanVideoTeaCacheKJ`、`LayerUtility: BooleanOperator`、`Int`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UpscaleModelLoader`、`WanImageToVideo`、`VAEDecode`、`KSampler`、`CLIPLoader`、`MathExpression|pysssss`、`SplitStringByDelimiter`、`Text Find and Replace`、`RH_Captioner`、`TextBox`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`CLIPVisionEncode`、`FluxGuidance`、`CLIPVisionLoader`、`LayerUtility: PurgeVRAM`、`ImageUpscaleWithModel`、`VHS_VideoCombine`、`CR String To Combo`、`ModelSamplingSD3`、`UNETLoader`、`GetRandomIntegerInRange`、`ImpactStringSelector`、`RH_Prompter`、`RH_LLMAPI_NODE`、`easy int`、`PrimitiveBoolean`、`Model Input Switch`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage
