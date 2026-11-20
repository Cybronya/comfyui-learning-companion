---
name: text_to_image_sampler_clip_unet_77
type: Text To Image
frequency: 9
level: moderate
coverage: 0.843778
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/BOOGU测试_2069366790278434817.json, 图片生成/文生图/Boogu Image 0.1 Turbo Fast Text-to-Image_2072998834151923712.json, 图片生成/文生图/Boogu turbo文生图_2067798697022418945.json, 图片生成/文生图/Boogu 文生图极速版_2069639754718728194.json, 图片生成/文生图/Boogu-Image  Turbo 文生图工作流_2078878116965081089.json, 图片生成/文生图/Krea2 Turbo + Realism Engineer  V3.1 文生图_2072595346835992577.json, 图片生成/文生图/Krea2 Turbo文生图（双采版）_2070846138026119169.json, 图片生成/文生图/Krea2-红潮_写实人像（双采版）_2070682832741163010.json, 图片生成/文生图/Krea2-风情万种_写实人像（双采版）_2071459488988749825.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/BOOGU测试_2069366790278434817.json、图片生成/文生图/Boogu Image 0.1 Turbo Fast Text-to-Image_2072998834151923712.json、图片生成/文生图/Boogu turbo文生图_2067798697022418945.json、图片生成/文生图/Boogu 文生图极速版_2069639754718728194.json、图片生成/文生图/Boogu-Image  Turbo 文生图工作流_2078878116965081089.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `ResolutionSelector` —— 4/9 个有
- `ImageConcanate` —— 2/9 个有
- `Int` —— 2/9 个有
- `LoraLoaderModelOnly` —— 2/9 个有
- `CR Seed` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `easy promptLine` —— 1/9 个有
- `easy promptList` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | lcm | - | 9 | 56% |
| 调度器 | sgm_uniform | - | 9 | 67% |
| 重绘幅度 | 1 | 0.4 - 1 | 9 | 71% |
| 宽度 | 1024 | 1024 - 1024 | 9 | 100% |
| 高度 | 1024 | 1024 - 1536 | 9 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，9 个样本，一致性 56%
- 调度器 最常用 sgm_uniform，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，9 个样本
- 宽度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，9 个样本，取值集中（一致性 81%）
- 高发问题（17/9 个样本）：Steps较低可能导致细节不足
