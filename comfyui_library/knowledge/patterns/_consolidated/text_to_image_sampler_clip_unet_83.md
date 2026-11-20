---
name: text_to_image_sampler_clip_unet_83
type: Text To Image
frequency: 9
level: strong
coverage: 0.894444
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/榨干Zimage！最强画质Dype原生4K生图，海量细节！_1999459942526484482.json, 图片生成/文生图/欧式美女Z-image文生图真实人像质感御姐美女_2041498182881910785.json, 图片生成/文生图/漏脐短裤Z-image文生图真实人像质感御姐美女_2041453018750652418.json, 图片生成/文生图/睡衣系列Z-image真实人像质感御姐美女_2041442705942777858.json, 图片生成/文生图/立体立绘Z-image文生图真实人像质感御姐美女_2042587073584046082.json, 图片生成/文生图/粉色头发Z-image文生图真实人像质感御姐美女_2042599230799351810.json, 图片生成/文生图/美女写真图Z-image文生图真实人像质感御姐美女_2041492850801643522.json, 图片生成/文生图/蕾丝内衣Z-image文生图真实人像质感御姐美女_2041472513884033025.json, 图片生成/文生图/阳台东方美女Z-image文生图真实人像质感御姐美女_2041499720912216066.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_83

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/榨干Zimage！最强画质Dype原生4K生图，海量细节！_1999459942526484482.json、图片生成/文生图/欧式美女Z-image文生图真实人像质感御姐美女_2041498182881910785.json、图片生成/文生图/漏脐短裤Z-image文生图真实人像质感御姐美女_2041453018750652418.json、图片生成/文生图/睡衣系列Z-image真实人像质感御姐美女_2041442705942777858.json、图片生成/文生图/立体立绘Z-image文生图真实人像质感御姐美女_2042587073584046082.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

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
- `ZImageLoraModelOnly` —— 8/9 个有
- `DyPE_FLUX` —— 1/9 个有
- `Seed Generator` —— 1/9 个有
- `Text` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 9 | 9 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1080 | 1024 - 1080 | 9 | 98% |
| 高度 | 1920 | 1536 - 1920 | 9 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 9，9 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1024 - 1080，9 个样本，取值集中（一致性 98%）
- 高度 中位数 1920，观测区间 1536 - 1920，9 个样本，取值集中（一致性 94%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
