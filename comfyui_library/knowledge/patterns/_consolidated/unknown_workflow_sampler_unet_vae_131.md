---
name: unknown_workflow_sampler_unet_vae_131
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9358
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Get resolution [Crystools]]
members: [图片生成/图生图/2104392510440304641.json, 图片生成/图生图/2106021474862723074.json, 图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json, 图片生成/文生图/Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722.json, 图片生成/文生图/Qwen-Image 2.1 重磅升级：一键抠图直出 PNG，无缝重塑图像工作流！_2106021474862723074.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_131

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2104392510440304641.json、图片生成/图生图/2106021474862723074.json、图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json、图片生成/文生图/Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722.json、图片生成/文生图/Qwen-Image 2.1 重磅升级：一键抠图直出 PNG，无缝重塑图像工作流！_2106021474862723074.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 4/5 个有
- `SaveImageAdvanced` —— 3/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `Get resolution [Crystools]` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 24 - 25 | 5 | 98% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 5 | 43% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1536 | - | 1 | 100% |
| 高度 | 2048 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 24 - 25，5 个样本，取值集中（一致性 98%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，5 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Get resolution [Crystools]
