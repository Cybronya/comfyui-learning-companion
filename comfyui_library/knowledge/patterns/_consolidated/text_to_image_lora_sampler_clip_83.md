---
name: text_to_image_lora_sampler_clip_83
type: Text To Image
frequency: 11
level: strong
coverage: 0.850909
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, PIP_图像联结]
members: [图片生成/图生图/2102235515952132097.json, 图片生成/图生图/2102494252348563457.json, 图片生成/图生图/2102582375585763330.json, 图片生成/图生图/2102647923245932546.json, 图片生成/图生图/2106074131702829057.json, 图片生成/图生图/FireRed-Image-Edit换装｜电商服装展示小红书出图，服饰一键换_2107351449641504770.json, 图片生成/图生图/FireRed-Image-Edit服装换衣展示｜小红书电商服饰图，批量出片快_2107357535060717570.json, 图片生成/文生图/Cc-MJ影视柔光｜Krea2文生图一键生成工作流_2094792236109221890.json, 图片生成/文生图/丰盈美女写真生成｜文生图人像一键高清出图工作流_2094808157049671682.json, 图片生成/文生图/官方稳定版超强一致性｜全能图片G-2.0图生图直出_2093812472296853505.json, 图片生成/文生图/超强一致性官方稳定版｜全能图片G-2.0图生图替换_2094031047418802178.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/2102235515952132097.json、图片生成/图生图/2102494252348563457.json、图片生成/图生图/2102582375585763330.json、图片生成/图生图/2102647923245932546.json、图片生成/图生图/2106074131702829057.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/11 个有
- `PreviewImage` —— 8/11 个有
- `Fast Groups Bypasser (rgthree)` —— 6/11 个有
- `PIP_图像联结` —— 4/11 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 4/11 个有
- `RH_RhartImageG2OfficialImageToImage` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `MiniMaxH3ReferenceToVideo` —— 2/11 个有
- `ResolutionSelector` —— 2/11 个有
- `Text` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（17/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、PIP_图像联结
