---
name: text_to_image_sampler_clip_unet_107
type: Text To Image
frequency: 7
level: moderate
coverage: 0.933429
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku双截棍4秒出图_1911939065036636162.json, 图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2047213255990448130.json, 图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2077645152755208194.json, 图片生成/文生图/Z-image基础文生图_1995758425134993409.json, 图片生成/文生图/Z-image文生图   自然风格首选_1993896427099193345.json, 图片生成/文生图/nunchaku_flux1对比未加速_2005576570435764226.json, 图片生成/文生图/【批量提示词】LORA模型测试_2067411590521122818.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_107

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Nunchaku双截棍4秒出图_1911939065036636162.json、图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2047213255990448130.json、图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2077645152755208194.json、图片生成/文生图/Z-image基础文生图_1995758425134993409.json、图片生成/文生图/Z-image文生图   自然风格首选_1993896427099193345.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/7 个有
- `CLIPLoader` —— 4/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `DualCLIPLoader` —— 3/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `NunchakuFluxDiTLoader` —— 2/7 个有
- `easy promptLine` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `MultiLinePrompt` —— 1/7 个有
- `NunchakuFluxLoraLoader` —— 1/7 个有
- `RebatchLatents` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 544 - 1536 | 7 | 74% |
| 高度 | 1024 | 960 - 1920 | 7 | 73% |
| 采样步数 | 10 | 9 - 25 | 7 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 544 - 1536，7 个样本
- 高度 中位数 1024，观测区间 960 - 1920，7 个样本
- 采样步数 中位数 10，观测区间 9 - 25，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
