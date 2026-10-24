---
name: text_to_image_sampler_clip_unet_165
type: Text To Image
frequency: 3
level: moderate
coverage: 0.765667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/3渲2_1985050728211369986.json, 图片生成/图生图/FLUX-Kontext 史诗级改图工作流_2049464217354375170.json, 图片生成/图生图/提取印花图案_1952199218133979137.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_165

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/3渲2_1985050728211369986.json、图片生成/图生图/FLUX-Kontext 史诗级改图工作流_2049464217354375170.json、图片生成/图生图/提取印花图案_1952199218133979137.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `BNK_CLIPTextEncodeAdvanced` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageFlip+` —— 1/3 个有
- `LineArtPreprocessor` —— 1/3 个有
- `UltralyticsDetectorProvider` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 512 - 1472 | 3 | 61% |
| 高度 | 768 | 512 - 1024 | 3 | 73% |
| ControlNet 权重 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1472，3 个样本
- 高度 中位数 768，观测区间 512 - 1024，3 个样本
