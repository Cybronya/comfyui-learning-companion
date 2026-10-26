---
name: text_to_image_sampler_clip_unet_82
type: Text To Image
frequency: 8
level: moderate
coverage: 0.899
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2031033876067393537.json, 图片生成/文生图/2031306114851147777.json, 图片生成/文生图/251225001.013. Z image_v3升级版更强提示词理解_2004252074999246849.json, 图片生成/文生图/87time 造相-Z-Image-Turbo_1992926870398238721.json, 图片生成/文生图/9 个 Krea 2 LoRA 测试_2069657247956946945.json, 图片生成/文生图/Krea2双相成片术｜RAW起稿×Turbo收束_2072657822646624257.json, 图片生成/文生图/Krea2合并模型实现_2072942696737632257.json, 图片生成/文生图/Krea2质感解锁核心流｜条件控制增强版_2072681347575017474.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_82

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/2031033876067393537.json、图片生成/文生图/2031306114851147777.json、图片生成/文生图/251225001.013. Z image_v3升级版更强提示词理解_2004252074999246849.json、图片生成/文生图/87time 造相-Z-Image-Turbo_1992926870398238721.json、图片生成/文生图/9 个 Krea 2 LoRA 测试_2069657247956946945.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/8 个有
- `FluxResolutionNode` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `ComfyUI-Krea2T-Enhancer` —— 2/8 个有
- `ConditioningKrea2Rebalance` —— 2/8 个有
- `AnyAspectRatio` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `LoraLoader` —— 1/8 个有
- `Power Lora Loader (rgthree)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 832 - 1920 | 8 | 73% |
| 高度 | 1452 | 720 - 1920 | 8 | 73% |
| 采样步数 | 9 | 7 - 30 | 8 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 32% |
| 采样算法 | euler | - | 8 | 62% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，观测区间 832 - 1920，8 个样本
- 高度 中位数 1452，观测区间 720 - 1920，8 个样本
- 采样步数 中位数 9，观测区间 7 - 30，8 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（12/8 个样本）：Steps较低可能导致细节不足
