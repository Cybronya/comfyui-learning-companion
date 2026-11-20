---
name: text_to_image_controlnet_ipadapter_lora
type: Text To Image
frequency: 2
level: weak
coverage: 0.9315
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, GetImageSize, IPAdapterUnifiedLoader, KSampler, LoadImage, LoraLoader, PreviewImage, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2d涂鸦线稿上色_1947480246155104257.json, 图片生成/图生图/风格参考_1976337196112322561.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_lora

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2d涂鸦线稿上色_1947480246155104257.json、图片生成/图生图/风格参考_1976337196112322561.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `GetImageSize`
- `IPAdapterUnifiedLoader`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ACN_ControlNet++LoaderSingle` —— 1/2 个有
- `CLIPSetLastLayer` —— 1/2 个有
- `DF_Image_scale_to_side` —— 1/2 个有
- `IPAdapter` —— 1/2 个有
- `IPAdapterAdvanced` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `PrepImageForClipVision` —— 1/2 个有
- `Segment` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.9 | - | 2 | 89% |
| 采样步数 | 18 | - | 2 | 33% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 67% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 524 | - | 2 | 98% |
| 高度 | 640 | - | 2 | 80% |
| LoRA 模型强度 | 0.85 | - | 2 | 82% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样步数 中位数 18，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 524，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- 高度 中位数 640，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- LoRA 模型强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
