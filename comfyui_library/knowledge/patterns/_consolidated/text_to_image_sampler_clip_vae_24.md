---
name: text_to_image_sampler_clip_vae_24
type: Text To Image
frequency: 5
level: moderate
coverage: 0.845
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, RH_Captioner, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku-Qwen-Image图生图_1982324151933386753.json, 图片生成/文生图/Z-image 反推提示词出图_2001135324149448705.json, 图片生成/文生图/boogu_image_turbo+文生图+提示词反推_2069229283981217794.json, 图片生成/文生图/boogu_image_turbo+文生图+提示词反推_2069585759648174082.json, 图片生成/文生图/最新文生图Krea2+Turbo 双采样加强版_2071101261251960834.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Nunchaku-Qwen-Image图生图_1982324151933386753.json、图片生成/文生图/Z-image 反推提示词出图_2001135324149448705.json、图片生成/文生图/boogu_image_turbo+文生图+提示词反推_2069229283981217794.json、图片生成/文生图/boogu_image_turbo+文生图+提示词反推_2069585759648174082.json、图片生成/文生图/最新文生图Krea2+Turbo 双采样加强版_2071101261251960834.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `RH_Captioner`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 2/5 个有
- `Int` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `NunchakuQwenImageDiTLoader` —— 1/5 个有
- `NunchakuQwenImageLoraStack` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `TextConcatenate` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 9 | 5 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | sgm_uniform | - | 5 | 40% |
| 重绘幅度 | 1 | 0.4 - 1 | 5 | 73% |
| 宽度 | 1024 | 512 - 1024 | 5 | 78% |
| 高度 | 1536 | 512 - 1664 | 5 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 9，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，5 个样本
- 宽度 中位数 1024，观测区间 512 - 1024，5 个样本
- 高度 中位数 1536，观测区间 512 - 1664，5 个样本
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
