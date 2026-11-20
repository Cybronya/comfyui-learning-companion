---
name: text_to_image_sampler_clip_unet_76
type: Text To Image
frequency: 9
level: weak
coverage: 0.883889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/LORA推荐第6期-MOSS IMAGE风格LORA_2114219762174746626.json, 图片生成/文生图/MJ风格工作流V2.0_2112169962583445506.json, 图片生成/文生图/MJ风格工作流V2.0_2113776644115746817.json, 图片生成/文生图/MJ风格工作流V2.0_2114196908800569346.json, 图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_1993970117180669953.json, 图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_2074311721812062209.json, 图片生成/文生图/Z-image text-to-image-文生图（完美支持中文字+超自然）​【Agent必备】_2088917231601278978.json, 图片生成/文生图/Z-image turbo D-OPSD文生图_2057063739513462785.json, 图片生成/文生图/电影级质感（图像） 一键生成_2113423908694224898.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_76

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/LORA推荐第6期-MOSS IMAGE风格LORA_2114219762174746626.json、图片生成/文生图/MJ风格工作流V2.0_2112169962583445506.json、图片生成/文生图/MJ风格工作流V2.0_2113776644115746817.json、图片生成/文生图/MJ风格工作流V2.0_2114196908800569346.json、图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_1993970117180669953.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

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
- `CR Prompt Text` —— 8/9 个有
- `ConditioningZeroOut` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `ResolutionSelector` —— 5/9 个有
- `ConditioningKrea2Rebalance` —— 4/9 个有
- `GetNode` —— 4/9 个有
- `Label (rgthree)` —— 4/9 个有
- `easy promptLine` —— 4/9 个有
- `PreviewImage` —— 3/9 个有
- `EmptyImage` —— 2/9 个有
- `Load Lora` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1920 | 9 | 70% |
| 高度 | 1024 | 1024 - 1920 | 9 | 73% |
| 采样步数 | 10 | 8 - 50 | 9 | 5% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 9 | 49% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1920，9 个样本
- 高度 中位数 1024，观测区间 1024 - 1920，9 个样本
- 采样步数 中位数 10，观测区间 8 - 50，9 个样本，取值分散，一致性仅 5%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，9 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
