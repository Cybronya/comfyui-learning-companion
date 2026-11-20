---
name: text_to_image_controlnet_lora_sampler_15
type: Text To Image
frequency: 3
level: moderate
coverage: 0.808333
common_nodes: [AIO_Preprocessor, Anything Everywhere, Anything Everywhere3, CLIPTextEncode, CLIPVisionLoader, ConditioningCombine, ConditioningSetAreaStrength, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SetUnionControlNetType, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, YC_LG_Redux, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/redux多图融合-仿图_1900787845584273409.json, 图片生成/图生图/图片融合_Flux_1956666150820175873.json, 图片生成/文生图/redux多图元素融合（效果优化版）_1912822659770478594.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/redux多图融合-仿图_1900787845584273409.json、图片生成/图生图/图片融合_Flux_1956666150820175873.json、图片生成/文生图/redux多图元素融合（效果优化版）_1912822659770478594.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningCombine`
- `ConditioningSetAreaStrength`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YC_LG_Redux`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 2/3 个有
- `FloatSlider` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `TextCombinerTwo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1080 | 3 | 97% |
| 高度 | 1536 | 1536 - 1920 | 3 | 89% |
| ControlNet 权重 | 0 | 0 - 0.3 | 3 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1080，3 个样本，取值集中（一致性 97%）
- 高度 中位数 1536，观测区间 1536 - 1920，3 个样本，取值集中（一致性 89%）
- ControlNet 权重 中位数 0，观测区间 0 - 0.3，3 个样本，取值分散，一致性仅 0%
