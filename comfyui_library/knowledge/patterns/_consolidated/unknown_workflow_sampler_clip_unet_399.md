---
name: unknown_workflow_sampler_clip_unet_399
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.978333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, INTConstant, JWInteger, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, TT_img_enc, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/通过单图反推提示词文生视频_1976134044670889985.json, 视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（官方版）_1975846179902722050.json, 视频生成/文生视频/（自用）Dyno+Remix文生视频（官方版）_1974785719120080898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_399

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/通过单图反推提示词文生视频_1976134044670889985.json、视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（官方版）_1975846179902722050.json、视频生成/文生视频/（自用）Dyno+Remix文生视频（官方版）_1974785719120080898.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `JWInteger`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `TT_img_enc`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/3 个有
- `Joy_caption_two_advanced` —— 1/3 个有
- `Joy_caption_two_load` —— 1/3 个有
- `Joy_extra_options` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
