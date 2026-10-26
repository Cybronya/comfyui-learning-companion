---
name: unknown_workflow_sampler_clip_unet_231
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.779667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, JjkText, KSamplerSelect, RH_Prompter, RandomNoise, SamplerCustomAdvanced, SaveImage, TextCombinerTwo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux文生图(超级简化_带备注)V1.0_1920028263266324482.json, 图片生成/文生图/Flux文生图-1_1_1940662965035233282.json, 图片生成/文生图/Flux文生图_1819583592967110658.json, 图片生成/文生图/Flux文生图_1938488997612027905.json, 图片生成/文生图/Flux文生图_1976282578619637762.json, 图片生成/文生图/Flux文生图（JC自用）_1952547805221064706.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_231

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Flux文生图(超级简化_带备注)V1.0_1920028263266324482.json、图片生成/文生图/Flux文生图-1_1_1940662965035233282.json、图片生成/文生图/Flux文生图_1819583592967110658.json、图片生成/文生图/Flux文生图_1938488997612027905.json、图片生成/文生图/Flux文生图_1976282578619637762.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `JjkText`
- `KSamplerSelect`
- `RH_Prompter`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextCombinerTwo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `Bjornulf_ShowStringText` —— 3/6 个有
- `CR Text Input Switch (4 way)` —— 3/6 个有
- `ImpactSwitch` —— 3/6 个有
- `RH_Translator` —— 3/6 个有
- `PreviewImage` —— 2/6 个有
- `ArgosTranslateTextNode` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `ShowText` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1280 | 1280 - 1280 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，6 个样本，取值集中（一致性 100%）
