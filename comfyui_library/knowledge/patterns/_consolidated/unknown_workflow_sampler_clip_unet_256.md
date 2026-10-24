---
name: unknown_workflow_sampler_clip_unet_256
type: Unknown Workflow
frequency: 5
level: strong
coverage: 1
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/重绘流V1_2087151061260922882.json, 图片生成/图生图/重绘流V2_2087151258632286210.json, 图片生成/文生图/Krea2文生图标准工作流_2091191129374019586.json, 图片生成/文生图/SPARK.Chroma_preview 反推文生图_1984856656842473473.json, 图片生成/文生图/文生图V1_2087151380954963970.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_256

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/重绘流V1_2087151061260922882.json、图片生成/图生图/重绘流V2_2087151258632286210.json、图片生成/文生图/Krea2文生图标准工作流_2091191129374019586.json、图片生成/文生图/SPARK.Chroma_preview 反推文生图_1984856656842473473.json、图片生成/文生图/文生图V1_2087151380954963970.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `LoraLoader` —— 3/5 个有
- `EmptyLatentImage` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有
- `T5TokenizerOptions` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0 | 0 - 0 | 3 | 100% |
| LoRA 文本强度 | 0 | 0 - 0 | 3 | 100% |
| 宽度 | 1052 | - | 2 | 97% |
| 高度 | 1472 | - | 2 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0，观测区间 0 - 0，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0，观测区间 0 - 0，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1472，样本不足，未给区间，2 个样本
