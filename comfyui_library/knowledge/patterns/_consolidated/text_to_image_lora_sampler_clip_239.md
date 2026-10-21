---
name: text_to_image_lora_sampler_clip_239
type: Text To Image
frequency: 5
level: strong
coverage: 0.9804
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/（贞贞Lora）Z-image同丹不同配方Lora对比测试_1996261458461736961.json, 图片生成/文生图/（贞贞Lora）Z-image文生图5600步V2（Dop测试）_1997311938298331137.json, 图片生成/文生图/（贞贞Lora）Z-image文生图V2（11000步）_1996234333444775938.json, 图片生成/文生图/（贞贞Lora）Z-image文生图V2（24000步）_1996258756096835586.json, 图片生成/文生图/（贞贞Lora）Z-image文生图V2（4500步）_1994676967016439809.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_239

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/（贞贞Lora）Z-image同丹不同配方Lora对比测试_1996261458461736961.json、图片生成/文生图/（贞贞Lora）Z-image文生图5600步V2（Dop测试）_1997311938298331137.json、图片生成/文生图/（贞贞Lora）Z-image文生图V2（11000步）_1996234333444775938.json、图片生成/文生图/（贞贞Lora）Z-image文生图V2（24000步）_1996258756096835586.json、图片生成/文生图/（贞贞Lora）Z-image文生图V2（4500步）_1994676967016439809.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy promptLine` —— 4/5 个有
- `AddLabel` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `PDIMAGE_LongerSize` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1080 - 1920 | 5 | 74% |
| 高度 | 1080 | 1080 - 1920 | 5 | 71% |
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1920，观测区间 1080 - 1920，5 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，5 个样本
- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
