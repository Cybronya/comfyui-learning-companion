---
name: image_to_image_sampler_clip_unet_11
type: Image To Image
frequency: 19
level: moderate
coverage: 0.914316
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/东方阳台美女Flux2-Klein真实人像质感御姐美女_2040723148257107969.json, 图片生成/图生图/丝绸珠宝陈列LoRA图生图-穿戴甲产品图工作流_2094783879763808258.json, 图片生成/图生图/人物换装   Klein_2029535177847869442.json, 图片生成/图生图/俯视户外Flux2-Klein真实人像质感御姐美女_2040703603123425281.json, 图片生成/图生图/古风美女Flux2-Klein真实人像质感御姐美女_2040758027002847234.json, 图片生成/图生图/吊带睡衣Flux2-Klein真实人像质感御姐美女_2040696643078590466.json, 图片生成/图生图/图像去噪_2078426606925864962.json, 图片生成/图生图/城市夜景Flux2-Klein真实人像质感御姐美女_2040749920210128898.json, 图片生成/图生图/婚纱美女Flux2-Klein真实人像质感御姐美女_2040752758709555201.json, 图片生成/图生图/学生妹Flux2-Klein真实人像质感御姐美女_2040755363972128770.json, 图片生成/图生图/居家美女Flux2-Klein真实人像质感御姐美女_2040768972542447617.json, 图片生成/图生图/巷子印花少女Flux2-Klein真实人像质感御姐美女_2040771105161482241.json, 图片生成/图生图/异域风情雪山Flux2-Klein真实人像质感御姐美女_2040747316449124353.json, 图片生成/图生图/电商产品全能化妆品场景美妆白底图精修_2042856879147196418.json, 图片生成/图生图/电商产品全能场景人物手臂手势白底图精修_2048960893014249473.json, 图片生成/图生图/电商产品全能珠宝首饰场景戒指项链手镯白底图精修_2043516708916301826.json, 图片生成/图生图/电商人物修图全能场景模特人像白底图精修_2050541837659713538.json, 图片生成/图生图/视角转换-Klein_2093164478102859778.json, 图片生成/文生图/电商产品全能珠宝首饰场景戒指项链手镯白底图精修_2112371719381016577.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/东方阳台美女Flux2-Klein真实人像质感御姐美女_2040723148257107969.json、图片生成/图生图/丝绸珠宝陈列LoRA图生图-穿戴甲产品图工作流_2094783879763808258.json、图片生成/图生图/人物换装   Klein_2029535177847869442.json、图片生成/图生图/俯视户外Flux2-Klein真实人像质感御姐美女_2040703603123425281.json、图片生成/图生图/古风美女Flux2-Klein真实人像质感御姐美女_2040758027002847234.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 17/19 个有
- `ConditioningZeroOut` —— 13/19 个有
- `scale` —— 10/19 个有
- `ReferenceLatent` —— 8/19 个有
- `Image Comparer (rgthree)` —— 7/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/19 个有
- `ConditioningCombine` —— 5/19 个有
- `ttN concat` —— 2/19 个有
- `ttN text` —— 2/19 个有
- `ImageConcanate` —— 1/19 个有
- `ImageScaleToTotalPixels` —— 1/19 个有
- `QwenMultiangleCameraNode` —— 1/19 个有
- `easy imageRemBg` —— 1/19 个有
- `easy promptReplace` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 18 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | beta | - | 18 | 56% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 18 | 43% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 17 | 89% |
| LoRA 文本强度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 56%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，18 个样本，取值分散，一致性仅 43%
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，17 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/19 个样本）：Steps较低可能导致细节不足
