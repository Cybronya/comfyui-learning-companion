---
name: unknown_workflow_lora_sampler_unet_98
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.941143
common_nodes: [CLIPLoader, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, KSampler, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeKrea2OstrisEdit, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【遇见AI】Krea2-reid锁定角色身份参考lora，锁定面部或者身体_2079506022036754434.json, 图片生成/图生图/【遇见AI】Krea2图片编辑工作流，单图Ostris版_2074791853114880002.json, 图片生成/图生图/【遇见AI】Krea2图片编辑工作流，多图Ostris版_2074792429991059458.json, 图片生成/图生图/图图KREA2参考图编辑与大面重绘工作流_2074031703919775746.json, 图片生成/图生图/服饰迁移（单图编辑）Krea2-Ostris-Edit-Outfit_2079569631408377857.json, 图片生成/图生图/服饰迁移（单图编辑）Krea2-Ostris-Edit-Outfit_2079829843113496578.json, 图片生成/文生图/Krea2 图像编辑与细节增强_2074460439945244673.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_98

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/【遇见AI】Krea2-reid锁定角色身份参考lora，锁定面部或者身体_2079506022036754434.json、图片生成/图生图/【遇见AI】Krea2图片编辑工作流，单图Ostris版_2074791853114880002.json、图片生成/图生图/【遇见AI】Krea2图片编辑工作流，多图Ostris版_2074792429991059458.json、图片生成/图生图/图图KREA2参考图编辑与大面重绘工作流_2074031703919775746.json、图片生成/图生图/服饰迁移（单图编辑）Krea2-Ostris-Edit-Outfit_2079569631408377857.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `Krea2OstrisEditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeKrea2OstrisEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 4/7 个有
- `FluxKontextImageScale` —— 3/7 个有
- `DF_Latent_Scale_to_side` —— 2/7 个有
- `JWImageResizeByLongerSide` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `TTResolutionSelector` —— 2/7 个有
- `CR Simple Image Compare` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `Int` —— 1/7 个有
- `JjkText` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 7 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 512 - 1024 | 7 | 73% |
| 高度 | 1024 | 512 - 1536 | 7 | 64% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，7 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1024，7 个样本
- 高度 中位数 1024，观测区间 512 - 1536，7 个样本
