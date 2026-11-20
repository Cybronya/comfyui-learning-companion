---
name: text_to_image_sampler_clip_unet_66
type: Text To Image
frequency: 11
level: moderate
coverage: 0.862455
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/LORA推荐第6期-MOSS IMAGE风格LORA_2114219762174746626.json, 图片生成/文生图/MJ风格工作流V2.0_2112169962583445506.json, 图片生成/文生图/MJ风格工作流V2.0_2113776644115746817.json, 图片生成/文生图/MJ风格工作流V2.0_2114196908800569346.json, 图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_1993970117180669953.json, 图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_2074311721812062209.json, 图片生成/文生图/Z-image text-to-image-文生图（完美支持中文字+超自然）​【Agent必备】_2088917231601278978.json, 图片生成/文生图/Z-image turbo D-OPSD文生图_2057063739513462785.json, 图片生成/文生图/Z-image-神级文生图-20秒超快速出图TEXT TO IMAGE_1993958594863366145.json, 图片生成/文生图/森哥AI文生图-超自然人像-20秒快速出图_2051690409042161666.json, 图片生成/文生图/（Z-image）dpmpp-2m-sde对比euler-文生图_1995128750184574977.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_66

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/LORA推荐第6期-MOSS IMAGE风格LORA_2114219762174746626.json、图片生成/文生图/MJ风格工作流V2.0_2112169962583445506.json、图片生成/文生图/MJ风格工作流V2.0_2113776644115746817.json、图片生成/文生图/MJ风格工作流V2.0_2114196908800569346.json、图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_1993970117180669953.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 10/11 个有
- `ConditioningZeroOut` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `GetNode` —— 7/11 个有
- `easy promptLine` —— 7/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `Label (rgthree)` —— 4/11 个有
- `ResolutionSelector` —— 4/11 个有
- `ConditioningKrea2Rebalance` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `EmptyImage` —— 2/11 个有
- `LoadImage` —— 2/11 个有
- `Load Lora` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1920 | 11 | 72% |
| 高度 | 1080 | 1024 - 1920 | 11 | 76% |
| 采样步数 | 10 | 8 - 50 | 11 | 11% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 11 | 51% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1920，11 个样本
- 高度 中位数 1080，观测区间 1024 - 1920，11 个样本
- 采样步数 中位数 10，观测区间 8 - 50，11 个样本，取值分散，一致性仅 11%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
