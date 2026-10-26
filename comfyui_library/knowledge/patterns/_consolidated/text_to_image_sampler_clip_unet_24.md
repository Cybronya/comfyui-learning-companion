---
name: text_to_image_sampler_clip_unet_24
type: Text To Image
frequency: 17
level: strong
coverage: 0.961471
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux.室内效果图生成_2055177379538063361.json, 图片生成/文生图/Z-image文生图（昆昆）_2044213811187556353.json, 图片生成/文生图/Z-image文生图（速度与质量兼得）_1995796523411705857.json, 图片生成/文生图/Z-image最强文生图模型_1994953430059954178.json, 图片生成/文生图/Z-image照片级超真实人物_2008470665782894594.json, 图片生成/文生图/Z-image生图_2102776816992866305.json, 图片生成/文生图/Z-image造像-文生图（最强写实人像）_1994314682653671425.json, 图片生成/文生图/Z-image高优化文生图、可生成多张_2053636873704226817.json, 图片生成/文生图/Z-image，出图 效果炸裂，效果超越Flux2_1993931824883843074.json, 图片生成/文生图/Z-image，最强文生图_1994408486224207874.json, 图片生成/文生图/ZIMAGE-杰洛特文生图_2044311451736739841.json, 图片生成/文生图/Zimage文生图_2058258679962624001.json, 图片生成/文生图/ki_krea2人物四视图_2104971759140294657.json, 图片生成/文生图/ki_krea2人物四视图_2107463809878282242.json, 图片生成/文生图/krea2基础文生图_2098922890111574018.json, 图片生成/文生图/krea2基础文生图_2098981510849327105.json, 图片生成/文生图/krea2基础文生图_2099657569232056322.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_24

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Flux.室内效果图生成_2055177379538063361.json、图片生成/文生图/Z-image文生图（昆昆）_2044213811187556353.json、图片生成/文生图/Z-image文生图（速度与质量兼得）_1995796523411705857.json、图片生成/文生图/Z-image最强文生图模型_1994953430059954178.json、图片生成/文生图/Z-image照片级超真实人物_2008470665782894594.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 16/17 个有
- `ConditioningZeroOut` —— 15/17 个有
- `LoraLoaderModelOnly` —— 9/17 个有
- `EmptyImage` —— 4/17 个有
- `PreviewImage` —— 4/17 个有
- `LayerUtility: PurgeVRAM V2` —— 2/17 个有
- `Text` —— 2/17 个有
- `BaiduTranslateNode` —— 1/17 个有
- `DualCLIPLoader` —— 1/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `ttN concat` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 20 | 17 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 76% |
| 调度器 | simple | - | 17 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 1024 | 768 - 1536 | 17 | 83% |
| 高度 | 1536 | 1024 - 2160 | 17 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 20，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 76%
- 调度器 最常用 simple，17 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1536，17 个样本，取值集中（一致性 83%）
- 高度 中位数 1536，观测区间 1024 - 2160，17 个样本
