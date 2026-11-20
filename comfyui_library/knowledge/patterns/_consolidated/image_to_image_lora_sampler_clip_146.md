---
name: image_to_image_lora_sampler_clip_146
type: Image To Image
frequency: 3
level: strong
coverage: 0.861667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImageResize+, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy getNode, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/棕暗瓶身精修-工作流_2055228697560526850.json, 图片生成/图生图/高光亮面瓶身精修_2059191486960463873.json, 平台全量/人像修复 2.0_2082403021249671169.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_146

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/棕暗瓶身精修-工作流_2055228697560526850.json、图片生成/图生图/高光亮面瓶身精修_2059191486960463873.json、平台全量/人像修复 2.0_2082403021249671169.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `easy float` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Value` —— 1/3 个有
- `ColorMatch` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `SDVN Image Color Match` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.95 | 0.8 - 1 | 3 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.95，观测区间 0.8 - 1，3 个样本，取值集中（一致性 91%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
