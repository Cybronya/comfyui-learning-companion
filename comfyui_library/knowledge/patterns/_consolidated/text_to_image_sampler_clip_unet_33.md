---
name: text_to_image_sampler_clip_unet_33
type: Text To Image
frequency: 15
level: moderate
coverage: 0.935533
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image 超清快速文生图_2038470583129743361.json, 图片生成/文生图/Z-image-MJ风格图像生成_2041506818840596482.json, 图片生成/文生图/Z-image-turbo 超清极速文生图_2039249261858136065.json, 图片生成/文生图/Z-image-turbo+D-opsd-文生图_2056751759552503810.json, 图片生成/文生图/Zimage_Turbo尺寸控制器版_2073283589403402242.json, 图片生成/文生图/Zimage_Turbo经典版_2047589392318992385.json, 图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2048945759399186433.json, 图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2096423431855230977.json, 图片生成/文生图/Z‑Image‑Turbo+蜂腰身材_2101265974426161154.json, 图片生成/文生图/krea2+Lora文生图_2082750366432718849.json, 图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json, 图片生成/文生图/千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json, 图片生成/文生图/失败作图工作流_2077959412047765506.json, 图片生成/文生图/超智能提示词反推照片V2_2004362690019684353.json, 图片生成/文生图/🦄Z-IMAGE-4&8STEPN🎯天下无腰_2022940063344103425.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_33

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Z-image 超清快速文生图_2038470583129743361.json、图片生成/文生图/Z-image-MJ风格图像生成_2041506818840596482.json、图片生成/文生图/Z-image-turbo 超清极速文生图_2039249261858136065.json、图片生成/文生图/Z-image-turbo+D-opsd-文生图_2056751759552503810.json、图片生成/文生图/Zimage_Turbo尺寸控制器版_2073283589403402242.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 13/15 个有
- `ConditioningZeroOut` —— 11/15 个有
- `Int` —— 7/15 个有
- `PreviewImage` —— 7/15 个有
- `ModelSamplingAuraFlow` —— 5/15 个有
- `Fast Groups Muter (rgthree)` —— 2/15 个有
- `AspectRatio` —— 1/15 个有
- `DuckHideNode` —— 1/15 个有
- `LamSwitcherCase` —— 1/15 个有
- `easy globalSeed` —— 1/15 个有
- `easy promptList` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 56 - 1920 | 15 | 41% |
| 高度 | 1920 | 512 - 2048 | 15 | 73% |
| 采样步数 | 8 | 4 - 30 | 15 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 87% |
| 调度器 | simple | - | 15 | 87% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 56 - 1920，15 个样本，取值分散，一致性仅 41%
- 高度 中位数 1920，观测区间 512 - 2048，15 个样本
- 采样步数 中位数 8，观测区间 4 - 30，15 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 87%
- 调度器 最常用 simple，15 个样本，一致性 87%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（13/15 个样本）：Steps较低可能导致细节不足
