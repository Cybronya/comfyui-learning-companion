---
name: text_to_image_sampler_clip_vae_20
type: Text To Image
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, NunchakuFluxDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1947462711925952514.json, 图片生成/文生图/1951451403174752257.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_20

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1947462711925952514.json、图片生成/文生图/1951451403174752257.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 1/2 个有
- `GoogleTranslateCLIPTextEncodeNode` —— 1/2 个有
- `LongCLIPTextEncodeFlux` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 896 | - | 2 | 86% |
| 采样步数 | 15 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样步数 中位数 15，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
