---
name: text_to_image_sampler_clip_unet_150
type: Text To Image
frequency: 5
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/zimage_z-image文生图_1999490922389831681.json, 图片生成/文生图/（贞贞Lora）Z-image文生图5600步V2（Dop测试）_1997311938298331137.json, 图片生成/文生图/（贞贞lora）z-image-turbo D-OPSD版文生图V1_2056616951438471170.json, 图片生成/文生图/（贞贞lora）z-image-turbo D-OPSD版文生图V1（27W步-Final版）_2056686307514077186.json, 图片生成/文生图/（贞贞lora）z-image-turbo flow dpo版文生图V1_2026975683213266946.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_150

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/zimage_z-image文生图_1999490922389831681.json、图片生成/文生图/（贞贞Lora）Z-image文生图5600步V2（Dop测试）_1997311938298331137.json、图片生成/文生图/（贞贞lora）z-image-turbo D-OPSD版文生图V1_2056616951438471170.json、图片生成/文生图/（贞贞lora）z-image-turbo D-OPSD版文生图V1（27W步-Final版）_2056686307514077186.json、图片生成/文生图/（贞贞lora）z-image-turbo flow dpo版文生图V1_2026975683213266946.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `easy seed` —— 3/5 个有
- `ImpactInt` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `easy getNode` —— 1/5 个有
- `easy setNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1080 - 1920 | 5 | 74% |
| 高度 | 1080 | 1080 - 1920 | 5 | 71% |
| 采样步数 | 10 | 9 - 10 | 5 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 1080 - 1920，5 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，5 个样本
- 采样步数 中位数 10，观测区间 9 - 10，5 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
