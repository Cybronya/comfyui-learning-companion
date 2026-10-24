---
name: unknown_workflow_sampler_unet_vae_321
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8845
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/透明素材生成丨Qwen Image 2.1丨文生图·透明PNG_2112093151107305474.json, 数字人/数字人/【尺素】Qwen_image_2.1文生图_2101923741793079298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_321

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/透明素材生成丨Qwen Image 2.1丨文生图·透明PNG_2112093151107305474.json、数字人/数字人/【尺素】Qwen_image_2.1文生图_2101923741793079298.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `SplitImageWithAlpha` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1056 | - | 2 | 97% |
| 高度 | 1472 | - | 2 | 70% |
| 采样步数 | 37.5 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1056，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1472，样本不足，未给区间，2 个样本
- 采样步数 中位数 37.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
