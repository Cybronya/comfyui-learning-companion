---
name: text_to_image_sampler_clip_checkpoint_37
type: Text To Image
frequency: 2
level: weak
coverage: 0.95
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [平台全量/动漫道具生成器（生成透明背景素材工作流）_1828237128303300609.json, 数字人/数字人/酒吧美男_2089335688880807938.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_37

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/动漫道具生成器（生成透明背景素材工作流）_1828237128303300609.json、数字人/数字人/酒吧美男_2089335688880807938.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LayeredDiffusionApply` —— 1/2 个有
- `LayeredDiffusionDecodeRGBA` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 752 | - | 2 | 64% |
| 高度 | 832 | - | 2 | 77% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6.5 | - | 2 | 77% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.95 | - | 2 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 752，样本不足，未给区间，2 个样本
- 高度 中位数 832，样本不足，未给区间，2 个样本
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6.5，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
