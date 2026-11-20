---
name: image_to_image_sampler_clip_unet_186
type: Image To Image
frequency: 3
level: strong
coverage: 0.771667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, GetImageSize+, KSampler, LoadImage, ModelSamplingFlux, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/热门玩法 灵魂画手（测试版1.0）_ Kontext 开源版本_1965806023804104706.json, 平台全量/Kontext实用技巧 _ 一键去文字_1955243833391923202.json, 平台全量/一键kontext图像转版画_1955547613467590657.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_186

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/热门玩法 灵魂画手（测试版1.0）_ Kontext 开源版本_1965806023804104706.json、平台全量/Kontext实用技巧 _ 一键去文字_1955243833391923202.json、平台全量/一键kontext图像转版画_1955547613467590657.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `KSampler`
- `LoadImage`
- `ModelSamplingFlux`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
