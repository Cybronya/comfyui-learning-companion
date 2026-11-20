---
name: image_to_image_upscale_lora_sampler_58
type: Image To Image
frequency: 4
level: strong
coverage: 0.82275
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, Image Comparer (rgthree), ImageUpscaleWithModel, Joy_caption_two, Joy_caption_two_load, KSampler, LoadImage, LoraLoader|pysssss, PreviewImage, SaveImage, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, easy cleanGpuUsed]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [平台全量/IL二次采样放大2.0_1958023224401473538.json, 平台全量/IL二次采样放大2.1_1972146629300121601.json, 平台全量/IL二次采样放大2.2_1986010083274498049.json, 平台全量/IL二次采样放大_1957640905484333057.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_58

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/IL二次采样放大2.0_1958023224401473538.json、平台全量/IL二次采样放大2.1_1972146629300121601.json、平台全量/IL二次采样放大2.2_1986010083274498049.json、平台全量/IL二次采样放大_1957640905484333057.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LoadImage`
- `LoraLoader|pysssss`
- `PreviewImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningCombine` —— 3/4 个有
- `ImageScaleBy` —— 3/4 个有
- `ShowText` —— 2/4 个有
- `easy imageScaleDownToSize` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `WD14Tagger|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 28 | 20 - 50 | 4 | 60% |
| Prompt 约束强度(CFG) | 5.8 | 5.8 - 5.8 | 4 | 100% |
| 采样算法 | dpmpp_2m | - | 4 | 75% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 0.4 | 0.3 - 0.45 | 4 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 4/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 28，观测区间 20 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 5.8，观测区间 5.8 - 5.8，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 0.4，观测区间 0.3 - 0.45，4 个样本，取值集中（一致性 86%）
- 高发问题（4/4 个样本）：发现KSampler但没有VAEDecode
