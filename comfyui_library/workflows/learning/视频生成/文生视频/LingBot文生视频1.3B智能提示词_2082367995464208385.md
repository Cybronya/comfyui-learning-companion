---
key: 视频生成/文生视频/LingBot文生视频1.3B智能提示词_2082367995464208385.json
name: LingBot文生视频1.3B智能提示词_2082367995464208385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LingBot文生视频1.3B智能提示词_2082367995464208385.json
hash: 24b9d9e2e94f0e34
coverage: 0.882353
learned_at: 2026-10-15 22:45:19
nodes: [SaveVideo, easy cleanGpuUsed, easy clearCacheAll, easy cleanGpuUsed, easy clearCacheAll, LingBotLoader, PrimitiveInt, FrameInterpolationModelLoader, CreateVideo, FrameInterpolate, PrimitiveInt, LingBotTextEncode, LingBotSampler, CR Prompt Text, CR Prompt Text, RH_Captioner_Pro, JWInteger]
patterns: []
missing: []
---

# 视频生成/文生视频/LingBot文生视频1.3B智能提示词_2082367995464208385.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LingBot文生视频1.3B智能提示词_2082367995464208385.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（17 个）：
- `SaveVideo`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `LingBotLoader`
- `PrimitiveInt`
- `FrameInterpolationModelLoader`
- `CreateVideo`
- `FrameInterpolate`
- `PrimitiveInt`
- `LingBotTextEncode`
- `LingBotSampler` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `RH_Captioner_Pro`
- `JWInteger`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`SaveVideo`、`easy cleanGpuUsed`、`easy clearCacheAll`、`LingBotLoader`、`FrameInterpolationModelLoader`、`CreateVideo`、`FrameInterpolate`、`LingBotTextEncode`、`LingBotSampler`、`CR Prompt Text`、`RH_Captioner_Pro`、`JWInteger`

**用到的条目**：LingBotSampler、LingBotTextEncode、CR Prompt Text、SaveVideo、CreateVideo、JWInteger、RH_Captioner_Pro、FrameInterpolate
