---
name: image_to_image_sampler_vae_28
type: Image To Image
frequency: 4
level: weak
coverage: 0.6695
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物一键制作角色四视图 - 高效省力 - V1_2006398311204397058.json, 图片生成/图生图/单图一键制作角色多视角（四视图）_1987716537224204290.json, 图片生成/图生图/是青慕啊_颠覆单帧创作！多视角人物生成，Qwen 让画面活起来⚡_2037200573065334786.json, 图片生成/图生图/👾怪獸-千问Edit万圣节合集👾_1983044701462888450.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_28

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/人物一键制作角色四视图 - 高效省力 - V1_2006398311204397058.json、图片生成/图生图/单图一键制作角色多视角（四视图）_1987716537224204290.json、图片生成/图生图/是青慕啊_颠覆单帧创作！多视角人物生成，Qwen 让画面活起来⚡_2037200573065334786.json、图片生成/图生图/👾怪獸-千问Edit万圣节合集👾_1983044701462888450.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `RHHiddenNodes` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `LayerUtility: CropByMask V2` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `easy imageRemBg` —— 2/4 个有
- `ImpactConditionalBranch` —— 1/4 个有
- `Int` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2.5 | 1 - 8 | 4 | 18% |
| Prompt 约束强度(CFG) | 0.5 | 0 - 1 | 4 | 0% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 2.5，观测区间 1 - 8，4 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 0.5，观测区间 0 - 1，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（17/4 个样本）：Steps较低可能导致细节不足
