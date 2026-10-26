---
name: unknown_workflow_sampler_clip_unet_361
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.758
common_nodes: [Anything Everywhere, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ImageCASharpening+, KSamplerSelect, ModelSamplingAuraFlow, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/【字体风格模仿】Qwen图生图-8步加速（持续加更）_1954926788238458881.json, 图片生成/文生图/【即梦平替】Qwen-image文生图（基础流）_1953815039516004354.json, 图片生成/文生图/【超全字体设计】Qwen文生图-8步加速（持续加更）_1954331468988334082.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_361

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【字体风格模仿】Qwen图生图-8步加速（持续加更）_1954926788238458881.json、图片生成/文生图/【即梦平替】Qwen-image文生图（基础流）_1953815039516004354.json、图片生成/文生图/【超全字体设计】Qwen文生图-8步加速（持续加更）_1954331468988334082.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ImageCASharpening+`
- `KSamplerSelect`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `CR Text Concatenate` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `FluxResolutionNode` —— 2/3 个有
- `Int` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `RH_Prompter` —— 2/3 个有
- `easy textSwitch` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `CR Text Replace` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 840 | - | 2 | 100% |
| 高度 | 1216 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 840，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1216，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
