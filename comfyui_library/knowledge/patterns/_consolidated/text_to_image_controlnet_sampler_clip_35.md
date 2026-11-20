---
name: text_to_image_controlnet_sampler_clip_35
type: Text To Image
frequency: 2
level: weak
coverage: 0.812
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, ImageGenResolutionFromImage, ImageInvert, KSampler, LineartStandardPreprocessor, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/还不错的线稿_1896445718376873986.json, 平台全量/一键线稿提取，操作简单_1910261787839688706.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/还不错的线稿_1896445718376873986.json、平台全量/一键线稿提取，操作简单_1910261787839688706.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `ImageGenResolutionFromImage`
- `ImageInvert`
- `KSampler`
- `LineartStandardPreprocessor`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LineArtPreprocessor` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.85 | - | 2 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
