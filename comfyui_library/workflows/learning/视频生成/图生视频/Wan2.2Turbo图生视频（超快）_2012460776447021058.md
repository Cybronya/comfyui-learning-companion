---
key: 视频生成/图生视频/Wan2.2Turbo图生视频（超快）_2012460776447021058.json
name: Wan2.2Turbo图生视频（超快）_2012460776447021058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2Turbo图生视频（超快）_2012460776447021058.json
hash: 408d6b1a69bfa0af
coverage: 1
learned_at: 2026-10-15 22:34:27
nodes: [LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Int, CR Prompt Text, MathExpression|pysssss, RunningHub_TurboDiffusion_TurboWan_Loader, JWInteger, RunningHub_TurboDiffusion_TurboWan_Sampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2Turbo图生视频（超快）_2012460776447021058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2012460776447021058.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（9 个）：
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `CR Prompt Text`
- `MathExpression|pysssss`
- `RunningHub_TurboDiffusion_TurboWan_Loader`
- `JWInteger`
- `RunningHub_TurboDiffusion_TurboWan_Sampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`CR Prompt Text`、`MathExpression|pysssss`、`RunningHub_TurboDiffusion_TurboWan_Loader`、`JWInteger`、`RunningHub_TurboDiffusion_TurboWan_Sampler`、`VHS_VideoCombine`

**用到的条目**：LoadImage、RunningHub_TurboDiffusion_TurboWan_Sampler、CR Prompt Text、Int、VHS_VideoCombine、JWInteger、RunningHub_TurboDiffusion_TurboWan_Loader、LayerUtility: ImageScaleByAspectRatio V2
