---
name: text_to_image_sampler_clip_unet_152
type: Text To Image
frequency: 4
level: strong
coverage: 0.81425
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-双图风格融合-T8版_2070051493448867842.json, 图片生成/文生图/Krea2-红潮_写实人像（双采版）_2070682832741163010.json, 图片生成/文生图/Krea2-风格扩展_无限创意_2090018651477987330.json, 图片生成/文生图/krea2-场景图_2094627383453241346.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_152

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2-双图风格融合-T8版_2070051493448867842.json、图片生成/文生图/Krea2-红潮_写实人像（双采版）_2070682832741163010.json、图片生成/文生图/Krea2-风格扩展_无限创意_2090018651477987330.json、图片生成/文生图/krea2-场景图_2094627383453241346.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `easy stylesSelector` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 4 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 896 | 720 - 1024 | 4 | 84% |
| 高度 | 1152 | 1024 - 1280 | 4 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 720 - 1024，4 个样本，取值集中（一致性 84%）
- 高度 中位数 1152，观测区间 1024 - 1280，4 个样本，取值集中（一致性 89%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
