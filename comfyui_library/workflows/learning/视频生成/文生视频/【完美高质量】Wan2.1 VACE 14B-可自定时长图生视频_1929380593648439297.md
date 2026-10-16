---
key: 视频生成/文生视频/【完美高质量】Wan2.1 VACE 14B-可自定时长图生视频_1929380593648439297.json
name: 【完美高质量】Wan2.1 VACE 14B-可自定时长图生视频_1929380593648439297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1929380593648439297.json
hash: 77f5b7b732388224
coverage: 0.965517
learned_at: 2026-10-15 22:43:25
nodes: [WanVideoTeaCache, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoVAELoader, WanVideoVACEEncode, WanVideoBlockSwap, WanVideoVACEModelSelect, FluxResolutionNode, LoadImage, WanVideoTextEncode, JjkText, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoExperimentalArgs, WanVideoDecode, ColorMatch, WanVideoSampler, WanVideoModelLoader, Int, JWInteger, InversionDemoLazyIndexSwitch, MathExpression|pysssss, MathExpression|pysssss, ImageResize+, InversionDemoLazyIndexSwitch, MathExpression|pysssss, MathExpression|pysssss, ImageResize+, MathExpression|pysssss]
patterns: []
missing: []
---

# 视频生成/文生视频/【完美高质量】Wan2.1 VACE 14B-可自定时长图生视频_1929380593648439297.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1929380593648439297.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `FluxResolutionNode`
- `LoadImage`
- `WanVideoTextEncode`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `ColorMatch`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `Int`
- `JWInteger`
- `InversionDemoLazyIndexSwitch`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageResize+`
- `InversionDemoLazyIndexSwitch`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageResize+`
- `MathExpression|pysssss`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`FluxResolutionNode`、`LoadImage`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`ColorMatch`、`WanVideoSampler`、`WanVideoModelLoader`、`Int`、`JWInteger`、`InversionDemoLazyIndexSwitch`、`MathExpression|pysssss`、`ImageResize+`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、FluxResolutionNode
