---
name: unknown_workflow_lora_sampler_unet_300
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.763
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1海报设计强化LORA｜细节修复｜文字排版优化_2111603744281550850.json, 图片生成/文生图/Qwen-2.1-海报设计_2111467394572046338.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_300

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1海报设计强化LORA｜细节修复｜文字排版优化_2111603744281550850.json、图片生成/文生图/Qwen-2.1-海报设计_2111467394572046338.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Seed` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1560 | - | 2 | 77% |
| 高度 | 1340 | - | 2 | 81% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1560，样本不足，未给区间，2 个样本
- 高度 中位数 1340，样本不足，未给区间，2 个样本，取值集中（一致性 81%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
