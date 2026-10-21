---
name: text_to_image_upscale_latent_upscale_sampler_5
type: Text To Image
frequency: 2
level: weak
coverage: 0.7735
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LatentUpscaleBy, LoadImage, PreviewImage, PrimitiveStringMultiline, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/二次元动漫插画柔和画风_2078488117400657921.json, 图片生成/文生图/游戏场景01_2100180693333659649.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/二次元动漫插画柔和画风_2078488117400657921.json、图片生成/文生图/游戏场景01_2100180693333659649.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `LatentUpscaleBy`
- `LoadImage`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AnimaLayerReplayPatcher` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `FaceDetailer` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `Power Lora Loader (rgthree)` —— 1/2 个有
- `SAMLoader` —— 1/2 个有
- `TextConcatenate` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有
- `VAEDecodeTiled` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 13 | - | 2 | 62% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.33 | - | 2 | 91% |
| 宽度 | 1128 | - | 2 | 64% |
| 高度 | 1024 | - | 2 | 75% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 13，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.33，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 宽度 中位数 1128，样本不足，未给区间，2 个样本
- 高度 中位数 1024，样本不足，未给区间，2 个样本
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
