---
name: image_to_image_upscale_lora_sampler_86
type: Image To Image
frequency: 3
level: strong
coverage: 0.946333
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/姿势模仿-直出4K-Qwen-edit-2509_2009202730081980417.json, 平台全量/电商精准溶图打光 Qwen 2511_2044660323596115969.json, 平台全量/电商精准溶图打光 Qwen 2511_2046387663330091009.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_86

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/姿势模仿-直出4K-Qwen-edit-2509_2009202730081980417.json、平台全量/电商精准溶图打光 Qwen 2511_2044660323596115969.json、平台全量/电商精准溶图打光 Qwen 2511_2046387663330091009.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
