---
name: image_to_image_lora_sampler_unet_234
type: Image To Image
frequency: 3
level: strong
coverage: 0.913
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Kontext QwenEdit三种换脸方案对比_1968857171360456705.json, 平台全量/flux_kontext图像编辑_移除物体+teache加速，1分钟出图_1962867038823878657.json, 平台全量/角度编辑器-两种方式，自由选择_1970768227989155841.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_234

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Kontext QwenEdit三种换脸方案对比_1968857171360456705.json、平台全量/flux_kontext图像编辑_移除物体+teache加速，1分钟出图_1962867038823878657.json、平台全量/角度编辑器-两种方式，自由选择_1970768227989155841.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `CLIPTextEncode` —— 2/3 个有
- `DF_Text_Box` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `TeaCache` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `CFGNorm` —— 1/3 个有
- `CLIPTextEncodeFlux` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `NunchakuFluxLoraLoader` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有
- `TextEncodeQwenImageEditEnhanced` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 8 - 20 | 3 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
