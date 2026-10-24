---
name: unknown_workflow_sampler_clip_unet_152
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.94675
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux文生图_1988616802869624833.json, 图片生成/文生图/Pornmaster_krea2_t2i_Raw+Turbo_2098728229115879426.json, 图片生成/文生图/Z-Image+Base&Turbo双重采样工作流_2058016487142674434.json, 图片生成/文生图/Z-Image-Turbo文生图双重采样_2018553894216929282.json, 图片生成/文生图/Z-image-Turbo文生图 双重采样_2020839379777884161.json, 图片生成/文生图/一键生成美女Z-Image双重采样_2039874902513160193.json, 图片生成/文生图/文生图 双采 行为艺术 黑兽9优化版_2065363132853612544.json, 图片生成/文生图/电商生成真实感模特 ZImage 双采样_2046138498574454786.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_152

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/flux文生图_1988616802869624833.json、图片生成/文生图/Pornmaster_krea2_t2i_Raw+Turbo_2098728229115879426.json、图片生成/文生图/Z-Image+Base&Turbo双重采样工作流_2058016487142674434.json、图片生成/文生图/Z-Image-Turbo文生图双重采样_2018553894216929282.json、图片生成/文生图/Z-image-Turbo文生图 双重采样_2020839379777884161.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/8 个有
- `Int` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 6/8 个有
- `SaveImage` —— 6/8 个有
- `Seed (rgthree)` —— 6/8 个有
- `CompressImages` —— 4/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `DualCLIPLoader` —— 1/8 个有
- `FluxGuidance` —— 1/8 个有
- `JjkText` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 20 | 8 | 9% |
| 采样算法 | 1 | 1 - 1.5 | 8 | 84% |
| 调度器 | euler | - | 8 | 88% |
| 重绘幅度 | sgm_uniform | - | 8 | 75% |
| 宽度 | 1080 | 832 - 1920 | 8 | 74% |
| 高度 | 1728 | 1080 - 1920 | 8 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 20，8 个样本，取值分散，一致性仅 9%
- 采样算法 中位数 1，观测区间 1 - 1.5，8 个样本，取值集中（一致性 84%）
- 调度器 最常用 euler，8 个样本，一致性 88%
- 重绘幅度 最常用 sgm_uniform，8 个样本，一致性 75%
- 宽度 中位数 1080，观测区间 832 - 1920，8 个样本
- 高度 中位数 1728，观测区间 1080 - 1920，8 个样本
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
