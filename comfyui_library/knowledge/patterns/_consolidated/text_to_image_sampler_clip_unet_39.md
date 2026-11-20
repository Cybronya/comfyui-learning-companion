---
name: text_to_image_sampler_clip_unet_39
type: Text To Image
frequency: 14
level: moderate
coverage: 0.943643
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku双截棍4秒出图_1911939065036636162.json, 图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2047213255990448130.json, 图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2077645152755208194.json, 图片生成/文生图/Z-image基础文生图_1995758425134993409.json, 图片生成/文生图/Z-image文生图-古风插画-gu_2012675993739202562.json, 图片生成/文生图/Zimage文生图-基础_2003639567171395585.json, 图片生成/文生图/Zimage文生图工作流-国产、认识中文、认识明星_1954438175747928065.json, 图片生成/文生图/[众馨]最新王炸Z-Image超快速超细节生图_1994245198530150402.json, 图片生成/文生图/aidir-文生图-krea2_2078304053796364290.json, 图片生成/文生图/krea2_文生图_2081989846117216258.json, 图片生成/文生图/krea2文生图_2069618400707567618.json, 图片生成/文生图/krea2文生图_2069962144506011649.json, 图片生成/文生图/nunchaku_flux1对比未加速_2005576570435764226.json, 图片生成/文生图/造相 Z-image 文生图 Ultra_2073291168456200194.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_39

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Nunchaku双截棍4秒出图_1911939065036636162.json、图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2047213255990448130.json、图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2077645152755208194.json、图片生成/文生图/Z-image基础文生图_1995758425134993409.json、图片生成/文生图/Z-image文生图-古风插画-gu_2012675993739202562.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 12/14 个有
- `ConditioningZeroOut` —— 12/14 个有
- `Image Comparer (rgthree)` —— 5/14 个有
- `DualCLIPLoader` —— 2/14 个有
- `LoraLoaderModelOnly` —— 2/14 个有
- `NunchakuFluxDiTLoader` —— 2/14 个有
- `ImageSharpen` —— 1/14 个有
- `LatentUpscaleBy` —— 1/14 个有
- `LayerUtility: PurgeVRAM` —— 1/14 个有
- `LoraLoaderModelOnly_Any` —— 1/14 个有
- `NunchakuFluxLoraLoader` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 544 - 1536 | 14 | 80% |
| 高度 | 1176 | 720 - 1536 | 14 | 77% |
| 采样步数 | 9 | 8 - 25 | 14 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.2 | 14 | 95% |
| 采样算法 | euler | - | 14 | 86% |
| 调度器 | simple | - | 14 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 544 - 1536，14 个样本
- 高度 中位数 1176，观测区间 720 - 1536，14 个样本
- 采样步数 中位数 9，观测区间 8 - 25，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.2，14 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，14 个样本，一致性 86%
- 调度器 最常用 simple，14 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（11/14 个样本）：Steps较低可能导致细节不足
