---
name: image_to_image_upscale_lora_sampler_90
type: Image To Image
frequency: 2
level: weak
coverage: 0.7465
common_nodes: [Anything Everywhere, CLIPTextEncode, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), ImageUpscaleWithModel, KSampler, LoadImage, LoraLoader, PreviewImage, RTXVideoSuperResolution, SaveImage, UltimateSDUpscale, UpscaleModelLoader_Optimized, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/latent 放大+rtx 4倍放大+面部修复_2028775960002174978.json, 图片生成/图生图/细节放大工作流对比_2032017003145334786.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_90

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/latent 放大+rtx 4倍放大+面部修复_2028775960002174978.json、图片生成/图生图/细节放大工作流对比_2032017003145334786.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Fast Groups Bypasser (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RTXVideoSuperResolution`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader_Optimized`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `FaceDetailer` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `SAMLoader` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `iToolsCompareImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.65 | - | 2 | 46% |
| LoRA 文本强度 | 0.65 | - | 2 | 46% |
| 采样步数 | 35 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.375 | - | 2 | 53% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- LoRA 文本强度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.375，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
