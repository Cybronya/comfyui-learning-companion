---
name: text_to_image_upscale_sampler_clip_51
type: Text To Image
frequency: 2
level: weak
coverage: 0.9525
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, ImageUpscaleWithModel, KSampler, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/文生图/【自用】4k3D图生成_1976841710645002242.json, 平台全量/高清摄影水下食物特写拍摄_1782607070206406657.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【自用】4k3D图生成_1976841710645002242.json、平台全量/高清摄影水下食物特写拍摄_1782607070206406657.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `DuckHideNode` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Lora Loader Stack (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 40% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.26 | - | 2 | 96% |
| 宽度 | 832 | - | 2 | 77% |
| 高度 | 992 | - | 2 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.26，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 宽度 中位数 832，样本不足，未给区间，2 个样本
- 高度 中位数 992，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
