---
name: text_to_image_upscale_latent_upscale_lora_9
type: Text To Image
frequency: 6
level: strong
coverage: 0.889333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyLatentImage, KSampler, LatentUpscaleBy, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 Realism Engineer v2文生图4K版双采样_2074349507999002625.json, 图片生成/文生图/Krea2 Realism Engineer v2文生图4K版双采样_2074791174111588353.json, 图片生成/文生图/Krea2 Realism Engineer 文生图4K版双采样_2074477575698739201.json, 图片生成/文生图/Krea2 Realism Engineer 文生图4K版双采样_2075218432907370497.json, 图片生成/文生图/Krea2双采样4K高清_2074396375680372738.json, 图片生成/文生图/Krea2文生图-双采样-高清直出_2074498674947878913.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Krea2 Realism Engineer v2文生图4K版双采样_2074349507999002625.json、图片生成/文生图/Krea2 Realism Engineer v2文生图4K版双采样_2074791174111588353.json、图片生成/文生图/Krea2 Realism Engineer 文生图4K版双采样_2074477575698739201.json、图片生成/文生图/Krea2 Realism Engineer 文生图4K版双采样_2075218432907370497.json、图片生成/文生图/Krea2双采样4K高清_2074396375680372738.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Note _O` —— 5/6 个有
- `Seed Generator` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `String Literal` —— 5/6 个有
- `DuckHideNode` —— 4/6 个有
- `ImageStitch` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `easy positive` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1024 - 1280 | 6 | 92% |
| 高度 | 1536 | 1536 - 1536 | 6 | 100% |
| 采样步数 | 6 | 6 - 8 | 6 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 0.6 | 0.6 - 1 | 6 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 1024 - 1280，6 个样本，取值集中（一致性 92%）
- 高度 中位数 1536，观测区间 1536 - 1536，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，观测区间 6 - 8，6 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 1，6 个样本
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足
