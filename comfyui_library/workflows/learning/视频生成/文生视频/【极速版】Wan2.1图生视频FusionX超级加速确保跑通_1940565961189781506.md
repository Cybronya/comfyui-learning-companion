---
key: 视频生成/文生视频/【极速版】Wan2.1图生视频FusionX超级加速确保跑通_1940565961189781506.json
name: 【极速版】Wan2.1图生视频FusionX超级加速确保跑通_1940565961189781506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【极速版】Wan2.1图生视频FusionX超级加速确保跑通_1940565961189781506.json
hash: 376317070a8f0a85
coverage: 0.779661
learned_at: 2026-10-15 22:43:30
nodes: [TextCombinerTwo, JjkText, easy showAnything, TextCombinerTwo, RH_Captioner, FluxResolutionNode, MMAudioFeatureUtilsLoader, easy showAnything, MMAudioModelLoader, RH_Captioner, RH_Translator, WanVideoDecode, JjkText, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, ColorMatch, Int, easy showAnything, ImageResize+, Evaluate Integers, JWInteger, MathExpression|pysssss, MMAudioSampler, Int, easy showAnything, RH_Translator, Reroute, easy showAnything, Reroute, SDVN Any Show, RH_Prompter, PreviewAudio, InversionDemoLazyIndexSwitch, Int, WanVideoApplyNAG, WanVideoSampler, WanVideoSLG, WanVideoEnhanceAVideo, JjkText, ImageResize+, Int, InversionDemoLazyIndexSwitch, ImageResize+, LoadImage, ImpactSwitch, ImpactSwitch, easy showAnything, WanVideoBlockSwap, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/【极速版】Wan2.1图生视频FusionX超级加速确保跑通_1940565961189781506.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1940565961189781506.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（59 个）：
- `TextCombinerTwo`
- `JjkText`
- `easy showAnything`
- `TextCombinerTwo`
- `RH_Captioner`
- `FluxResolutionNode`
- `MMAudioFeatureUtilsLoader`
- `easy showAnything`
- `MMAudioModelLoader`
- `RH_Captioner`
- `RH_Translator`
- `WanVideoDecode`
- `JjkText`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `ColorMatch`
- `Int`
- `easy showAnything`
- `ImageResize+`
- `Evaluate Integers`
- `JWInteger`
- `MathExpression|pysssss`
- `MMAudioSampler` ★核心
- `Int`
- `easy showAnything`
- `RH_Translator`
- `Reroute`
- `easy showAnything`
- `Reroute`
- `SDVN Any Show`
- `RH_Prompter`
- `PreviewAudio`
- `InversionDemoLazyIndexSwitch`
- `Int`
- `WanVideoApplyNAG`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `JjkText`
- `ImageResize+`
- `Int`
- `InversionDemoLazyIndexSwitch`
- `ImageResize+`
- `LoadImage`
- `ImpactSwitch`
- `ImpactSwitch`
- `easy showAnything`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **78%**（46/59）

**有卡**：`TextCombinerTwo`、`RH_Captioner`、`FluxResolutionNode`、`MMAudioFeatureUtilsLoader`、`MMAudioModelLoader`、`RH_Translator`、`WanVideoDecode`、`MathExpression|pysssss`、`WanVideoTextEncodeSingle`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoExperimentalArgs`、`WanVideoImageToVideoEncode`、`ColorMatch`、`Int`、`ImageResize+`、`Evaluate Integers`、`JWInteger`、`MMAudioSampler`、`SDVN Any Show`、`RH_Prompter`、`PreviewAudio`、`InversionDemoLazyIndexSwitch`、`WanVideoApplyNAG`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、MMAudioSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
