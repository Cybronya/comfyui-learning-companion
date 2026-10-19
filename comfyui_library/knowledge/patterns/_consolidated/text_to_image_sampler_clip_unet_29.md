---
name: text_to_image_sampler_clip_unet_29
type: Text To Image
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSampler, NunchakuFluxDiTLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1968880877902155777.json, 视频生成/图生视频/1910971389912805378.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_29

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1968880877902155777.json、视频生成/图生视频/1910971389912805378.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 30 | - | 2 | 83% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
