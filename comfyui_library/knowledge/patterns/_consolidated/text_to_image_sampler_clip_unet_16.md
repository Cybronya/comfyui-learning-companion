---
name: text_to_image_sampler_clip_unet_16
type: Text To Image
frequency: 20
level: moderate
coverage: 0.81665
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen3超强图片反推_2043616761685221378.json, 图片生成/文生图/Red-Z image Base-10步出图极速版_2018674863816318977.json, 图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json, 图片生成/文生图/Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602.json, 图片生成/文生图/Super Z-image 3.0文生图_2018000830837825538.json, 图片生成/文生图/Z Image BF16&FP8对比 + 4K超清放大_2005803927591415810.json, 图片生成/文生图/Z Image BF16&FP8对比 + 4K超清放大【AI小王子】_1995339494473785345.json, 图片生成/文生图/Z Image出图 + 4K超清放大_2005868847062286337.json, 图片生成/文生图/Z image文生图_2048404891235786754.json, 图片生成/文生图/Z-IMAGE：4K超清放大工作流+BF16-FP8效果对比_1996194432674414594.json, 图片生成/文生图/Z-IMAGE：小而美图像模型：文生图_1993913992611643394.json, 图片生成/文生图/Z-IMAGE：小而美图像模型：文生图_2035264157662060546.json, 图片生成/文生图/Z-IMAGE：文生图【无ai感】_1994210417830461442.json, 图片生成/文生图/Z-IMAGE：新王登基  文生图_1995696465139863553.json, 图片生成/文生图/Z-IMAGE：新王登基  文生图_2009258918182129665.json, 图片生成/文生图/Z-Image+lora测试工作流_2027762368310157313.json, 图片生成/文生图/Z-Image-跑场景图-v3.0_2044237946076794881.json, 图片生成/文生图/Z-Image-跑场景图-v4.0_2044957910106640386.json, 图片生成/文生图/Z-Image-跑场景图_2037100091957317634.json, 图片生成/文生图/Z-image绝世美女人物一致性lora和工作流，高清美女图适合抖音、快手等自媒体平台_1995357519012880385.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_16

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Qwen3超强图片反推_2043616761685221378.json、图片生成/文生图/Red-Z image Base-10步出图极速版_2018674863816318977.json、图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json、图片生成/文生图/Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602.json、图片生成/文生图/Super Z-image 3.0文生图_2018000830837825538.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 16/20 个有
- `Image Comparer (rgthree)` —— 16/20 个有
- `ImageScaleBy` —— 16/20 个有
- `SeedVR2LoadDiTModel` —— 16/20 个有
- `SeedVR2LoadVAEModel` —— 16/20 个有
- `SeedVR2VideoUpscaler` —— 16/20 个有
- `Fast Groups Bypasser (rgthree)` —— 15/20 个有
- `ImpactInt` —— 9/20 个有
- `PrimitiveInt` —— 4/20 个有
- `CR Prompt Text` —— 3/20 个有
- `LayerUtility: PurgeVRAM` —— 3/20 个有
- `easy promptList` —— 3/20 个有
- `LoraLoader` —— 2/20 个有
- `LoraLoaderModelOnly` —— 2/20 个有
- `Text` —— 2/20 个有
- `Int` —— 1/20 个有
- `JoinStringMulti` —— 1/20 个有
- `KepStringLiteral` —— 1/20 个有
- `PrimitiveStringMultiline` —— 1/20 个有
- `TextInputNode` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 15 | 20 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 1080 | 720 - 1920 | 20 | 66% |
| 高度 | 1280 | 1080 - 1920 | 20 | 73% |
| LoRA 模型强度 | 1.55 | - | 2 | 65% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 15，20 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1920，20 个样本
- 高度 中位数 1280，观测区间 1080 - 1920，20 个样本
- LoRA 模型强度 中位数 1.55，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
