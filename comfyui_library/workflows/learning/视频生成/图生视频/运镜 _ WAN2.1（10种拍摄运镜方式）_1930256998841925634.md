---
key: 视频生成/图生视频/运镜 _ WAN2.1（10种拍摄运镜方式）_1930256998841925634.json
name: 运镜 _ WAN2.1（10种拍摄运镜方式）_1930256998841925634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1930256998841925634.json
hash: b9fc86bb8e1a32d9
coverage: 0.8
learned_at: 2026-10-15 22:30:04
nodes: [Reroute, VAELoader, Reroute, Reroute, easy cleanGpuUsed, WanVideoTeaCacheKJ, LayerUtility: BooleanOperator, LayerUtility: BooleanOperator, easy ifElse, Int, easy ifElse, LoraLoaderModelOnly, PathchSageAttentionKJ, UpscaleModelLoader, WanImageToVideo, VAEDecode, Fast Groups Muter (rgthree), KSampler, CLIPLoader, MathExpression|pysssss, SplitStringByDelimiter, Text Find and Replace, RH_Captioner, TextBox, Reroute, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPVisionEncode, CLIPTextEncode, FluxGuidance, CLIPVisionLoader, LayerUtility: PurgeVRAM, Reroute, ImageUpscaleWithModel, VHS_VideoCombine, CR String To Combo, ModelSamplingSD3, UNETLoader, LayerUtility: PurgeVRAM, easy cleanGpuUsed, VHS_VideoCombine, LoadImage, GetRandomIntegerInRange, Int, TextBox, ImpactStringSelector, Text Find and Replace, Text Find and Replace, RH_Prompter, TextBox, RH_LLMAPI_NODE, easy showAnything, MathExpression|pysssss, easy int, MarkdownNote, PrimitiveString, PrimitiveBoolean, Model Input Switch, ImpactSwitch, MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 656146093795831, "steps": 30}
---

# 视频生成/图生视频/运镜 _ WAN2.1（10种拍摄运镜方式）_1930256998841925634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1930256998841925634.json`

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
- `LoadImage`
- `GetRandomIntegerInRange`
- `Int`
- `TextBox`
- `ImpactStringSelector`
- `Text Find and Replace`
- `Text Find and Replace`
- `RH_Prompter`
- `TextBox`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `MathExpression|pysssss`
- `easy int`
- `MarkdownNote`
- `PrimitiveString`
- `PrimitiveBoolean`
- `Model Input Switch`
- `ImpactSwitch`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `656146093795831`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（48/60）

**有卡**：`VAELoader`、`easy cleanGpuUsed`、`WanVideoTeaCacheKJ`、`LayerUtility: BooleanOperator`、`Int`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UpscaleModelLoader`、`WanImageToVideo`、`VAEDecode`、`KSampler`、`CLIPLoader`、`MathExpression|pysssss`、`SplitStringByDelimiter`、`Text Find and Replace`、`RH_Captioner`、`TextBox`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`CLIPVisionEncode`、`FluxGuidance`、`CLIPVisionLoader`、`LayerUtility: PurgeVRAM`、`ImageUpscaleWithModel`、`VHS_VideoCombine`、`CR String To Combo`、`ModelSamplingSD3`、`UNETLoader`、`LoadImage`、`GetRandomIntegerInRange`、`ImpactStringSelector`、`RH_Prompter`、`RH_LLMAPI_NODE`、`easy int`、`PrimitiveBoolean`、`Model Input Switch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
