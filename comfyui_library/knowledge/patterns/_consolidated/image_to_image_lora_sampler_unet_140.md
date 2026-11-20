---
name: image_to_image_lora_sampler_unet_140
type: Image To Image
frequency: 6
level: moderate
coverage: 0.854333
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Qwen-Image-Edit 溶图+透视纠正+精修-SD-PPP版本（2025-10-20）_2009308784446935041.json, 平台全量/Qwen2509超强光影迁移光影重绘重打光灯光_2031904512788664321.json, 平台全量/Y-image_qwen_image_edit_2509_1970861122448461825.json, 平台全量/qwen_image_edit-升级版_1970765333353164801.json, 平台全量/千问edit2509_1981565767470727170.json, 平台全量/让电商人没有难P的商品图！Qwen-Image-Edit-2509 强势来袭！_1971026680708009986.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_140

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Qwen-Image-Edit 溶图+透视纠正+精修-SD-PPP版本（2025-10-20）_2009308784446935041.json、平台全量/Qwen2509超强光影迁移光影重绘重打光灯光_2031904512788664321.json、平台全量/Y-image_qwen_image_edit_2509_1970861122448461825.json、平台全量/qwen_image_edit-升级版_1970765333353164801.json、平台全量/千问edit2509_1981565767470727170.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 5/6 个有
- `EmptySD3LatentImage` —— 4/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `GetImageSize+` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `RepeatLatentBatch` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 6 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 55% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，6 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
