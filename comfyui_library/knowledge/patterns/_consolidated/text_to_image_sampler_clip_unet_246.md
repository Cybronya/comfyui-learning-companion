---
name: text_to_image_sampler_clip_unet_246
type: Text To Image
frequency: 2
level: weak
coverage: 0.9335
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/基础文生图+把主图抠出来+透明背景_2012053498615042049.json, 数字人/数字人/绘本测试3_2042521074520297474.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_246

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/基础文生图+把主图抠出来+透明背景_2012053498615042049.json、数字人/数字人/绘本测试3_2042521074520297474.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 640 | - | 2 | 80% |
| 高度 | 640 | - | 2 | 80% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3.4 | - | 2 | 82% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 0.96 | - | 2 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 640，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高度 中位数 640，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.4，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 0.96，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
