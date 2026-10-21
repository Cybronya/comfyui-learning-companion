---
name: unknown_workflow_sampler_clip_unet_207
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/素简动漫_2018965018250846209.json, 数字人/数字人/万圣节萌系插画-文生图_2093977653907902466.json, 数字人/数字人/中秋萌系插画-文生图_2093973513794318337.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_207

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/素简动漫_2018965018250846209.json、数字人/数字人/万圣节萌系插画-文生图_2093977653907902466.json、数字人/数字人/中秋萌系插画-文生图_2093973513794318337.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `EmptyZImageLatentImage //ZImagePowerNodes` —— 1/3 个有
- `FlexLoraLoaderModelOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26 | 20 - 26 | 3 | 88% |
| Prompt 约束强度(CFG) | 4.5 | 1.5 - 4.5 | 3 | 60% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 26，观测区间 20 - 26，3 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1.5 - 4.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
