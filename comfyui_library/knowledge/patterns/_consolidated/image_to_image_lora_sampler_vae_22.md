---
name: image_to_image_lora_sampler_vae_22
type: Image To Image
frequency: 2
level: weak
coverage: 0.941
common_nodes: [EmptyLatentImage, ImageScale, KSampler, LayerColor: BrightnessContrastV2, LayerFilter: AddGrain, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, Seed (rgthree), TTResolutionSelector, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2_动漫转真人🌸低显存版🌸INT8 A卡专用6G版_2110215134198198273.json, 图片生成/图生图/Krea2🌸动漫转真人🌸免提示词版_2110225472079618050.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Krea2_动漫转真人🌸低显存版🌸INT8 A卡专用6G版_2110215134198198273.json、图片生成/图生图/Krea2🌸动漫转真人🌸免提示词版_2110225472079618050.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `EmptyLatentImage`
- `ImageScale`
- `KSampler`
- `LayerColor: BrightnessContrastV2`
- `LayerFilter: AddGrain`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `TTResolutionSelector`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1088 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.575 | - | 2 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1088，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.575，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
