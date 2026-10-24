---
name: text_to_image_sampler_clip_unet_52
type: Text To Image
frequency: 12
level: strong
coverage: 0.93225
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image 超清快速文生图_2038470583129743361.json, 图片生成/文生图/Z-image-MJ风格图像生成_2041506818840596482.json, 图片生成/文生图/Z-image-turbo 超清极速文生图_2039249261858136065.json, 图片生成/文生图/Z-image-turbo+D-opsd-文生图_2056751759552503810.json, 图片生成/文生图/Z-image照片级超真实人物_2008470665782894594.json, 图片生成/文生图/Zimage_Turbo尺寸控制器版_2073283589403402242.json, 图片生成/文生图/Zimage_Turbo经典版_2047589392318992385.json, 图片生成/文生图/ki_krea2人物四视图_2107463809878282242.json, 图片生成/文生图/krea2基础文生图_2098922890111574018.json, 图片生成/文生图/krea2基础文生图_2098981510849327105.json, 图片生成/文生图/krea2基础文生图_2099657569232056322.json, 图片生成/文生图/z-image文生图工作流_2099060664231874562.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_52

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Z-image 超清快速文生图_2038470583129743361.json、图片生成/文生图/Z-image-MJ风格图像生成_2041506818840596482.json、图片生成/文生图/Z-image-turbo 超清极速文生图_2039249261858136065.json、图片生成/文生图/Z-image-turbo+D-opsd-文生图_2056751759552503810.json、图片生成/文生图/Z-image照片级超真实人物_2008470665782894594.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/12 个有
- `ConditioningZeroOut` —— 7/12 个有
- `PreviewImage` —— 7/12 个有
- `EmptyImage` —— 5/12 个有
- `Int` —— 3/12 个有
- `DuckHideNode` —— 1/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `LamSwitcherCase` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 960 - 1536 | 12 | 87% |
| 高度 | 1536 | 1280 - 2048 | 12 | 87% |
| 采样步数 | 10 | 8 - 10 | 12 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 58% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 960 - 1536，12 个样本，取值集中（一致性 87%）
- 高度 中位数 1536，观测区间 1280 - 2048，12 个样本，取值集中（一致性 87%）
- 采样步数 中位数 10，观测区间 8 - 10，12 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 58%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（6/12 个样本）：Steps较低可能导致细节不足
