---
name: image_to_image_lora_sampler_unet_121
type: Image To Image
frequency: 7
level: moderate
coverage: 0.94
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Qwen-Edit 2511溶图_合成_透视角度纠正_2004892145121193986.json, 平台全量/主体抠图与黑白蒙版生成_2058261827443847170.json, 平台全量/常规沙发_无茶几_北欧_v1_2025079910972268546.json, 平台全量/常规沙发_茶几不遮挡_北欧_v1_2023299558998024193.json, 平台全量/懒人沙发_北欧_v1_2024833579053752321.json, 平台全量/移除主体 _ 千问-edit-2511_1868334844831760385.json, 平台全量/移除主体 无痕局部重绘 消除指定物体 qwen-edit-2511_2067063406582128641.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_121

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Qwen-Edit 2511溶图_合成_透视角度纠正_2004892145121193986.json、平台全量/主体抠图与黑白蒙版生成_2058261827443847170.json、平台全量/常规沙发_无茶几_北欧_v1_2025079910972268546.json、平台全量/常规沙发_茶几不遮挡_北欧_v1_2023299558998024193.json、平台全量/懒人沙发_北欧_v1_2024833579053752321.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
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
- `ConditioningZeroOut` —— 4/7 个有
- `FluxKontextImageScale` —— 3/7 个有
- `ReferenceLatent` —— 2/7 个有
- `BiRefNet_Hugo` —— 1/7 个有
- `FastCanvas` —— 1/7 个有
- `FastCanvasTool` —— 1/7 个有
- `ImageCropper` —— 1/7 个有
- `ImageResize+` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 7 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，7 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
