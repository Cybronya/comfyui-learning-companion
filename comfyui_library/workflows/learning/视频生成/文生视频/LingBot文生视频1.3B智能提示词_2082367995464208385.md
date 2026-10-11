---
key: 视频生成/文生视频/LingBot文生视频1.3B智能提示词_2082367995464208385.json
name: LingBot文生视频1.3B智能提示词_2082367995464208385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LingBot文生视频1.3B智能提示词_2082367995464208385.json
hash: 24b9d9e2e94f0e34
coverage: 0.529412
learned_at: 2026-10-11 20:38:35
nodes: [SaveVideo, easy cleanGpuUsed, easy clearCacheAll, easy cleanGpuUsed, easy clearCacheAll, LingBotLoader, PrimitiveInt, FrameInterpolationModelLoader, CreateVideo, FrameInterpolate, PrimitiveInt, LingBotTextEncode, LingBotSampler, CR Prompt Text, CR Prompt Text, RH_Captioner_Pro, JWInteger]
patterns: []
missing: [easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, easy clearCacheAll, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **53%**（9/17）

**有卡**：`SaveVideo`、`LingBotLoader`、`FrameInterpolationModelLoader`、`CreateVideo`、`FrameInterpolate`、`LingBotTextEncode`、`LingBotSampler`、`RH_Captioner_Pro`、`JWInteger`

**缺卡**（6）：`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy clearCacheAll`、`easy clearCacheAll`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LingBotSampler、LingBotTextEncode、SaveVideo、CreateVideo、JWInteger、RH_Captioner_Pro、FrameInterpolate、FrameInterpolationModelLoader

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
