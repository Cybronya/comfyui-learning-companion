---
name: unknown_workflow_sampler_47
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8885
common_nodes: [CR Prompt Text, CreateVideo, FrameInterpolate, FrameInterpolationModelLoader, JWInteger, LingBotSampler, LingBotTextEncode, PrimitiveInt, RH_Captioner_Pro, SaveVideo, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/文生视频/LingBot文生视频1.3B智能提示词_2082367995464208385.json, 视频生成/文生视频/LingBot文生视频30B智能提示词_2082368008017764354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_47

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/LingBot文生视频1.3B智能提示词_2082367995464208385.json、视频生成/文生视频/LingBot文生视频30B智能提示词_2082368008017764354.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `CreateVideo`
- `FrameInterpolate`
- `FrameInterpolationModelLoader`
- `JWInteger`
- `LingBotSampler`
- `LingBotTextEncode`
- `PrimitiveInt`
- `RH_Captioner_Pro`
- `SaveVideo`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 1/2 个有
- `LingBotLoader` —— 1/2 个有
- `LingBotMoELoaderGGUF` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
