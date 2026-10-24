---
name: unknown_workflow_sampler_unet_vae_208
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7844
common_nodes: [CLIPLoader, CR Text, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1 文生图_2110328458579632130.json, 图片生成/文生图/qwen-image-2.1_2101675550237614082.json, 图片生成/文生图/qwen-image-2.1多图编辑_2101799458202804226.json, 图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json, 数字人/数字人/【尺素】Qwen_image_2.1文生图（自带PE）_2101922141309595650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_208

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1 文生图_2110328458579632130.json、图片生成/文生图/qwen-image-2.1_2101675550237614082.json、图片生成/文生图/qwen-image-2.1多图编辑_2101799458202804226.json、图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json、数字人/数字人/【尺素】Qwen_image_2.1文生图（自带PE）_2101922141309595650.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 3/5 个有
- `TextGenerateLTX2Prompt` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `EmptyLatentImage` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `ResolutionSelector` —— 2/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
