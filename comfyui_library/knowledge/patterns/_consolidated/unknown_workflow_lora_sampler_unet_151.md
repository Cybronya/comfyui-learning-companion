---
name: unknown_workflow_lora_sampler_unet_151
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8486
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问edit2511图像编辑批量版_2070326343346253826.json, 图片生成/图生图/千问edit2511批量图像统一编辑_2010942558175760385.json, 图片生成/图生图/千问edit2511批量图像编辑_2010723096864493569.json, 图片生成/图生图/千问edit2511批量图像编辑_2070328739568898049.json, 图片生成/图生图/少儿_迁移_换装_抠图_runninghub简化版本_2079378747140165634.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_151

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/千问edit2511图像编辑批量版_2070326343346253826.json、图片生成/图生图/千问edit2511批量图像统一编辑_2010942558175760385.json、图片生成/图生图/千问edit2511批量图像编辑_2010723096864493569.json、图片生成/图生图/千问edit2511批量图像编辑_2070328739568898049.json、图片生成/图生图/少儿_迁移_换装_抠图_runninghub简化版本_2079378747140165634.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `HAIGC_LoadImagesFromZip` —— 4/5 个有
- `HAIGC_SaveImagesToZip` —— 4/5 个有
- `ImageFromBatch+` —— 4/5 个有
- `ImageListToBatch+` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `CR Text` —— 2/5 个有
- `BackgroundEraseNetwork` —— 1/5 个有
- `ETN_LoadImageBase64` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 5 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，5 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
