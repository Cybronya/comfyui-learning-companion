---
name: image_to_image_upscale_lora_sampler_97
type: Image To Image
frequency: 2
level: weak
coverage: 0.9255
common_nodes: [CLIPTextEncode, Florence2ModelLoader, Florence2Run, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万相wan2.2洗图神器_1983816990546698242.json, 图片生成/图生图/无损2倍放大_1987797032171671554.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_97

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/万相wan2.2洗图神器_1983816990546698242.json、图片生成/图生图/无损2倍放大_1987797032171671554.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `Florence2ModelLoader`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 0.45 | - | 2 | 44% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 0.45，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
