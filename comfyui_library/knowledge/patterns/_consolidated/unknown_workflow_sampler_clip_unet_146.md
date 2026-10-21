---
name: unknown_workflow_sampler_clip_unet_146
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.83325
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, JjkText, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1952547805221064706.json, 图片生成/文生图/1976282578619637762.json, 图片生成/文生图/Flux文生图-基础版_1889856882952089601.json, 图片生成/文生图/Flux文生图_1819583592967110658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_146

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1952547805221064706.json、图片生成/文生图/1976282578619637762.json、图片生成/文生图/Flux文生图-基础版_1889856882952089601.json、图片生成/文生图/Flux文生图_1819583592967110658.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `JjkText`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 3/4 个有
- `FluxResolutionNode` —— 3/4 个有
- `ImpactSwitch` —— 3/4 个有
- `RH_Prompter` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `TextCombinerTwo` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 4 | 75% |
| 高度 | 1280 | 512 - 1280 | 4 | 69% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，4 个样本
- 高度 中位数 1280，观测区间 512 - 1280，4 个样本
