---
key: 视频生成/图生视频/Smooth Mix+Wan2.2 图生视频（自动提示词）_1982274042864517122.json
name: Smooth Mix+Wan2.2 图生视频（自动提示词）_1982274042864517122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1982274042864517122.json
hash: e862857e6190a51b
coverage: 0.829268
learned_at: 2026-10-15 22:32:40
nodes: [MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, LayerUtility: BooleanOperatorV2, LayerUtility: BooleanOperatorV2, LayerUtility: If , easy showAnything, LayerUtility: If , CR Text, easy int, JWInteger, MathExpression|pysssss, easy showAnything, ImageScale, PreviewImage, PreviewImage, GetImageSize, easy imageScaleDownToSize, LoadImage, easy int, LoadImage, RIFE VFI, AILab_QwenVL, ImpactSwitch, PreviewAny, RH_Translator, VHS_VideoCombine, SeedVR2ExtraArgs, SeedVR2BlockSwap, VAEDecode, VHS_VideoCombine, KSamplerAdvanced, workflow>SMOOTH MIX-WAN2.2, WanImageToVideo, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, VHS_VideoCombine, SeedVR2GGUF, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Smooth Mix+Wan2.2 图生视频（自动提示词）_1982274042864517122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982274042864517122.json`

## 结构

**生成流程**：Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: If `
- `easy showAnything`
- `LayerUtility: If `
- `CR Text`
- `easy int`
- `JWInteger`
- `MathExpression|pysssss`
- `easy showAnything`
- `ImageScale`
- `PreviewImage`
- `PreviewImage`
- `GetImageSize`
- `easy imageScaleDownToSize`
- `LoadImage`
- `easy int`
- `LoadImage`
- `RIFE VFI`
- `AILab_QwenVL`
- `ImpactSwitch`
- `PreviewAny`
- `RH_Translator`
- `VHS_VideoCombine`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `workflow>SMOOTH MIX-WAN2.2`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `SeedVR2GGUF`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`MathExpression|pysssss`、`LayerUtility: BooleanOperatorV2`、`LayerUtility: If `、`CR Text`、`easy int`、`JWInteger`、`ImageScale`、`GetImageSize`、`easy imageScaleDownToSize`、`LoadImage`、`RIFE VFI`、`AILab_QwenVL`、`RH_Translator`、`VHS_VideoCombine`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`VAEDecode`、`KSamplerAdvanced`、`workflow>SMOOTH MIX-WAN2.2`、`WanImageToVideo`、`CLIPTextEncode`、`SeedVR2GGUF`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、KSamplerAdvanced、SeedVR2BlockSwap、SeedVR2ExtraArgs、SeedVR2GGUF、GetImageSize
