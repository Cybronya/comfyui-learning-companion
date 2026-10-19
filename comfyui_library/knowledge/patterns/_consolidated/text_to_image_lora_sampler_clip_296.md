---
name: text_to_image_lora_sampler_clip_296
type: Text To Image
frequency: 2
level: weak
coverage: 0.886
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/游戏场景01文生图打底｜场景概念图批量生成，游戏美术素材库起步首选_2100481657882107905.json, 视频生成/文生视频/Anima-2.9B智能图生图Qwen3VL反推｜文生视频视频生视频图生视频_2090074818287849473.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_296

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/游戏场景01文生图打底｜场景概念图批量生成，游戏美术素材库起步首选_2100481657882107905.json、视频生成/文生视频/Anima-2.9B智能图生图Qwen3VL反推｜文生视频视频生视频图生视频_2090074818287849473.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageScale` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `Power Lora Loader (rgthree)` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `Qwen3VLProcessor` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `VAELoaderKJ` —— 1/2 个有
- `image_scale_pixel_v2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
