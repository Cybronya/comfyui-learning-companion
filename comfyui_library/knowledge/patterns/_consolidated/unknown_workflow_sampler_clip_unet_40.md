---
name: unknown_workflow_sampler_clip_unet_40
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.962
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, INTConstant, JWInteger, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, TT_img_enc, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [ImageFromBatch+, LayerUtility: PurgeVRAM, Text Concatenate, CR Prompt Text]
members: [视频生成/文生视频/1974785719120080898.json, 视频生成/文生视频/1974792612945244161.json, 视频生成/文生视频/1975846179902722050.json, 视频生成/文生视频/1975847969142517762.json, 视频生成/文生视频/1976134044670889985.json, 视频生成/文生视频/1978740895153541121.json, 视频生成/文生视频/Wan2.2 lightx2v 1217文生视频V1_2001672195485122562.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/1974785719120080898.json、视频生成/文生视频/1974792612945244161.json、视频生成/文生视频/1975846179902722050.json、视频生成/文生视频/1975847969142517762.json、视频生成/文生视频/1976134044670889985.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `JWInteger`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `TT_img_enc`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 5/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `ImageFromBatch+` —— 3/7 个有
- `LoadImage` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `Joy_caption_two_advanced` —— 1/7 个有
- `Joy_caption_two_load` —— 1/7 个有
- `Joy_extra_options` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `Text Concatenate` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 57% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 86% |
| 重绘幅度 | simple | - | 7 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 86%
- 重绘幅度 最常用 simple，7 个样本，一致性 86%
- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、LayerUtility: PurgeVRAM、Text Concatenate、CR Prompt Text
