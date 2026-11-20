---
name: text_to_image_sampler_clip_unet_157
type: Text To Image
frequency: 4
level: moderate
coverage: 0.882
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Krea + LoRA 写实 _ 动漫_1951094193005506562.json, 图片生成/图生图/商业级CAD一键彩平_1896564248325890049.json, 图片生成/文生图/Flux 文生图 两种方法对比  (1Girl 为例)_1824358791352881153.json, 平台全量/Flux lora 写实VS动漫_1825377726868926466.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux Krea + LoRA 写实 _ 动漫_1951094193005506562.json、图片生成/图生图/商业级CAD一键彩平_1896564248325890049.json、图片生成/文生图/Flux 文生图 两种方法对比  (1Girl 为例)_1824358791352881153.json、平台全量/Flux lora 写实VS动漫_1825377726868926466.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LoraLoader` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `SDXLEmptyLatentSizePicker+` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `Lora Loader Stack (rgthree)` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `ControlNetApplyAdvanced` —— 1/4 个有
- `ControlNetLoader` —— 1/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896x1152 (0.78) | - | 4 | 75% |
| 高度 | 1 | 1 - 896 | 4 | 0% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 4 | 0% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.88 | 0.88 - 1 | 3 | 94% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 896x1152 (0.78)，4 个样本，一致性 75%
- 高度 中位数 1，观测区间 1 - 896，4 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.88，观测区间 0.88 - 1，3 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
