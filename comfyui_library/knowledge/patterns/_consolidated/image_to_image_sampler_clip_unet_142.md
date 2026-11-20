---
name: image_to_image_sampler_clip_unet_142
type: Image To Image
frequency: 3
level: weak
coverage: 0.928333
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSampler, LoadImage, ModelSamplingSD3, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2——图生图_1951276154261024770.json, 图片生成/图生图/Wan2.2图生图_1989916164019154946.json, 图片生成/图生图/Wan2.2图生图最优实现_1950904111136972802.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_142

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Wan2.2——图生图_1951276154261024770.json、图片生成/图生图/Wan2.2图生图_1989916164019154946.json、图片生成/图生图/Wan2.2图生图最优实现_1950904111136972802.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `QZ_ResolutionPreset` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `String Literal` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy seed` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 3 | 56% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.4 | 0.35 - 1 | 3 | 49% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.35 - 1，3 个样本，取值分散，一致性仅 49%
