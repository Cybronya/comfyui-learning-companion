---
name: text_to_image_lora_sampler_clip_92
type: Text To Image
frequency: 9
level: strong
coverage: 0.859889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, PIP_图像联结]
members: [图片生成/图生图/2102235515952132097.json, 图片生成/图生图/2102494252348563457.json, 图片生成/图生图/2102582375585763330.json, 图片生成/图生图/2102647923245932546.json, 图片生成/图生图/2106074131702829057.json, 图片生成/图生图/FireRed-Image-Edit换装｜电商服装展示小红书出图，服饰一键换_2107351449641504770.json, 图片生成/图生图/FireRed-Image-Edit服装换衣展示｜小红书电商服饰图，批量出片快_2107357535060717570.json, 图片生成/文生图/krea2-turbo极简极速文生图｜小说配图专用 文生图秒出插画_2104056464099864578.json, 图片生成/文生图/小说配图极速直出 krea2 turbo极简文生图工作流_2104314139870060545.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/2102235515952132097.json、图片生成/图生图/2102494252348563457.json、图片生成/图生图/2102582375585763330.json、图片生成/图生图/2102647923245932546.json、图片生成/图生图/2106074131702829057.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `LoadImage` —— 7/9 个有
- `PreviewImage` —— 6/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `PIP_图像联结` —— 4/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `MiniMaxH3ReferenceToVideo` —— 2/9 个有
- `Seed (rgthree)` —— 2/9 个有
- `Text` —— 2/9 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（15/9 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、PIP_图像联结
