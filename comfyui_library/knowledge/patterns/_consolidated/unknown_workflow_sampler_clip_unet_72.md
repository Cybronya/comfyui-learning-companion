---
name: unknown_workflow_sampler_clip_unet_72
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.86175
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [SDXL Resolutions (JPS)]
members: [图片生成/文生图/1971904444222926850.json, 图片生成/文生图/Z_image文生图标准版_2064278139861299201.json, 数字人/数字人/万圣节萌系插画-文生图_2093977653907902466.json, 数字人/数字人/中秋萌系插画-文生图_2093973513794318337.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1971904444222926850.json、图片生成/文生图/Z_image文生图标准版_2064278139861299201.json、数字人/数字人/万圣节萌系插画-文生图_2093977653907902466.json、数字人/数字人/中秋萌系插画-文生图_2093973513794318337.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `LoraLoader` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `EmptyChromaRadianceLatentImage` —— 1/4 个有
- `SDXL Resolutions (JPS)` —— 1/4 个有
- `T5TokenizerOptions` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26 | 25 - 30 | 4 | 93% |
| Prompt 约束强度(CFG) | 4.25 | 4 - 4.5 | 4 | 94% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 26，观测区间 25 - 30，4 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 4.25，观测区间 4 - 4.5，4 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：SDXL Resolutions (JPS)
