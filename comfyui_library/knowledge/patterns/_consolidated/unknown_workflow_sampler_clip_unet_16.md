---
name: unknown_workflow_sampler_clip_unet_16
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.698
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, DualCLIPLoader, KSampler, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Primitive integer [Crystools], Text Multiline, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1950931756763521026.json, 图片生成/文生图/1950961660334899201.json, 图片生成/文生图/1951062054163652610.json, 图片生成/文生图/1951086073063612417.json, 图片生成/文生图/1951117515063762945.json, 图片生成/文生图/1951132729087864833.json, 图片生成/文生图/1951205710673719298.json, 图片生成/文生图/1951508454584340482.json, 图片生成/文生图/1951846909747122177.json, 图片生成/文生图/1956944111003688962.json, 图片生成/文生图/1986360219359969282.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_16

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1950931756763521026.json、图片生成/文生图/1950961660334899201.json、图片生成/文生图/1951062054163652610.json、图片生成/文生图/1951086073063612417.json、图片生成/文生图/1951117515063762945.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 10/11 个有
- `easy showAnything` —— 8/11 个有
- `Primitive integer [Crystools]` —— 3/11 个有
- `NunchakuFluxDiTLoader` —— 2/11 个有
- `ShowText|pysssss` —— 2/11 个有
- `RH_LLMAPI_NODE` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Primitive integer [Crystools]、Text Multiline、CR SDXL Aspect Ratio
