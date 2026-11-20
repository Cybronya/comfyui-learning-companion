---
name: image_to_image_sampler_clip_unet_163
type: Image To Image
frequency: 4
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/一键洗图小红书男女生通用_1923690959681277953.json, 平台全量/去水印（完美无痕）flux2_2015350812653916161.json, 平台全量/情侣Q版转绘淘宝转绘_2060860918644436994.json, 平台全量/最强flux kontext去水印_1941123812471816194.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_163

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/一键洗图小红书男女生通用_1923690959681277953.json、平台全量/去水印（完美无痕）flux2_2015350812653916161.json、平台全量/情侣Q版转绘淘宝转绘_2060860918644436994.json、平台全量/最强flux kontext去水印_1941123812471816194.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `LoraLoader` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `ClipInterrogator` —— 1/4 个有
- `DifferentialDiffusion` —— 1/4 个有
- `JoinStringMulti` —— 1/4 个有
- `RMBG` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.925 | - | 2 | 92% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 20 | 20 - 38 | 4 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 0.35 - 1 | 4 | 66% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.925，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 38，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，4 个样本
