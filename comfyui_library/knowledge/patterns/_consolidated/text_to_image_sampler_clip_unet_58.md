---
name: text_to_image_sampler_clip_unet_58
type: Text To Image
frequency: 8
level: moderate
coverage: 0.868625
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX2-双图融合_1993897229222084609.json, 图片生成/文生图/Krea2_2070039943791071234.json, 图片生成/文生图/Krea2双相成片术｜RAW起稿×Turbo收束_2072657822646624257.json, 图片生成/文生图/Krea2合并模型实现_2072942696737632257.json, 图片生成/文生图/Krea2质感解锁核心流｜条件控制增强版_2072681347575017474.json, 图片生成/文生图/Z-IMAGE：文生图，一段话生出好看的美图！_1993890310312968194.json, 图片生成/文生图/Z-Image：文生图，极速光影，将文字转化为超现实影像！_1993869296981966849.json, 图片生成/文生图/最强模型Z-Image：超写实生图_1993922948425777153.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_58

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/FLUX2-双图融合_1993897229222084609.json、图片生成/文生图/Krea2_2070039943791071234.json、图片生成/文生图/Krea2双相成片术｜RAW起稿×Turbo收束_2072657822646624257.json、图片生成/文生图/Krea2合并模型实现_2072942696737632257.json、图片生成/文生图/Krea2质感解锁核心流｜条件控制增强版_2072681347575017474.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
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
- `PreviewImage` —— 7/8 个有
- `JWInteger` —— 4/8 个有
- `JjkText` —— 4/8 个有
- `RH_LLMAPI_NODE` —— 4/8 个有
- `FluxResolutionNode` —— 3/8 个有
- `ComfyUI-Krea2T-Enhancer` —— 2/8 个有
- `ConditioningKrea2Rebalance` —— 2/8 个有
- `Power Lora Loader (rgthree)` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 30 | 8 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 28% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1080 | 1024 - 1280 | 8 | 93% |
| 高度 | 1920 | 720 - 1920 | 8 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 30，8 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1024 - 1280，8 个样本，取值集中（一致性 93%）
- 高度 中位数 1920，观测区间 720 - 1920，8 个样本
