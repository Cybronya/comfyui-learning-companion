---
name: unknown_workflow_sampler_unet_vae_191
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8916
common_nodes: [CLIPLoader, ConditioningZeroOut, INTConstant, KSampler, LoadImage, QwenEditTextEncode_EditUtils, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed-一键服装提取_2039137376810835970.json, 图片生成/图生图/FireRed-人物换装_2039149983168991234.json, 图片生成/图生图/FireRed-人物换装_2083805030485938177.json, 图片生成/图生图/人物换装（极速版）_2083245105582006273.json, 图片生成/图生图/豹豹喵呜：FIRERED换装&服装提取二合一工作流。_2031352097077207041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_191

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FireRed-一键服装提取_2039137376810835970.json、图片生成/图生图/FireRed-人物换装_2039149983168991234.json、图片生成/图生图/FireRed-人物换装_2083805030485938177.json、图片生成/图生图/人物换装（极速版）_2083245105582006273.json、图片生成/图生图/豹豹喵呜：FIRERED换装&服装提取二合一工作流。_2031352097077207041.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `INTConstant`
- `KSampler`
- `LoadImage`
- `QwenEditTextEncode_EditUtils`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Lora Loader Stack (rgthree)` —— 4/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LazySwitch2way` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `Switch string [Crystools]` —— 1/5 个有
- `easy boolean` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
