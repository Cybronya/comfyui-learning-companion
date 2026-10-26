---
name: unknown_workflow_upscale_sampler_clip_56
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ImageScaleBy, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/GGUF／BF16阿里开源 Z-IMAGE TURBO _ Z-Image＋SeedVR2高清放大_1994292255422955521.json, 图片生成/文生图/Moody-v10文生图_2027415650590789634.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/GGUF／BF16阿里开源 Z-IMAGE TURBO _ Z-Image＋SeedVR2高清放大_1994292255422955521.json、图片生成/文生图/Moody-v10文生图_2027415650590789634.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ImageScaleBy`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Model Input Switch` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Power Lora Loader (rgthree)` —— 1/2 个有
- `TT_img_enc` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `ZImageLoraModelOnly` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.975 | - | 2 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.975，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
