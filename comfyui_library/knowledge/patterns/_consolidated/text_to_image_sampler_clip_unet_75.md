---
name: text_to_image_sampler_clip_unet_75
type: Text To Image
frequency: 9
level: moderate
coverage: 0.942222
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 漫剧角色资产一键生成工作流｜文生四视图_2099740461484302337.json, 图片生成/文生图/Krea2-trubo-文生图_2069750701965791233.json, 图片生成/文生图/Krea2-turbo文生图3D国漫CG场景_2085325906326937602.json, 图片生成/文生图/Krea2-turbo文生图3D国漫CG风格_2089394677895221249.json, 图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫场景_2085270687903731714.json, 图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫风格_2084650330515660801.json, 图片生成/文生图/Krea2-turbo文生图超写实真人摄影风格_2089316645973086210.json, 图片生成/文生图/Krea2-风情万种_写实人像（双采版）_2071459488988749825.json, 图片生成/文生图/▶▷Krea2文生图_2107457543818801153.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Krea2 漫剧角色资产一键生成工作流｜文生四视图_2099740461484302337.json、图片生成/文生图/Krea2-trubo-文生图_2069750701965791233.json、图片生成/文生图/Krea2-turbo文生图3D国漫CG场景_2085325906326937602.json、图片生成/文生图/Krea2-turbo文生图3D国漫CG风格_2089394677895221249.json、图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫场景_2085270687903731714.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `PreviewImage` —— 3/9 个有
- `PrimitiveStringMultiline` —— 3/9 个有
- `ConditioningKrea2Rebalance` —— 2/9 个有
- `ConditioningZeroOut` —— 2/9 个有
- `ResolutionSelector` —— 2/9 个有
- `LatentSwitch` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `StringFunction|pysssss` —— 1/9 个有
- `easy anythingIndexSwitch` —— 1/9 个有
- `easy promptLine` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 9 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 0.4 - 1 | 9 | 80% |
| 宽度 | 1080 | 768 - 2000 | 9 | 66% |
| 高度 | 1280 | 1024 - 1920 | 9 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，9 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，9 个样本
- 宽度 中位数 1080，观测区间 768 - 2000，9 个样本
- 高度 中位数 1280，观测区间 1024 - 1920，9 个样本
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
