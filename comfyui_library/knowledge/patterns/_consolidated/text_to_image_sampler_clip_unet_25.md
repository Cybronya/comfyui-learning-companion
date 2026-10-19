---
name: text_to_image_sampler_clip_unet_25
type: Text To Image
frequency: 2
level: weak
coverage: 0.7435
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM, easy imageConcat]
members: [图片生成/文生图/1955802388865191937.json, 图片生成/文生图/1975922379924877314.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1955802388865191937.json、图片生成/文生图/1975922379924877314.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy imageConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 35 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、easy imageConcat
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
