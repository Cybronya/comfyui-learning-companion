---
name: unknown_workflow_sampler_clip_unet_408
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/朦胧唯美zimage_2005074233749372930.json, 图片生成/文生图/柔和光影日系风Soft-Light Bright- Anime Art Style -Image工作流_2070113768801128449.json, 图片生成/文生图/阿里Z-image，人像真实感拉满_1993853665350008834.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_408

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/朦胧唯美zimage_2005074233749372930.json、图片生成/文生图/柔和光影日系风Soft-Light Bright- Anime Art Style -Image工作流_2070113768801128449.json、图片生成/文生图/阿里Z-image，人像真实感拉满_1993853665350008834.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Latent Noise Injection` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ZImageLoraModelOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 10 | 9 - 14 | 3 | 80% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | ddim | - | 3 | 33% |
| 重绘幅度 | sgm_uniform | - | 3 | 67% |
| 宽度 | 1080 | 720 - 1280 | 3 | 77% |
| 高度 | 1856 | 1280 - 1920 | 3 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 9 - 14，3 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 ddim，3 个样本，一致性 33%
- 重绘幅度 最常用 sgm_uniform，3 个样本，一致性 67%
- 宽度 中位数 1080，观测区间 720 - 1280，3 个样本
- 高度 中位数 1856，观测区间 1280 - 1920，3 个样本，取值集中（一致性 83%）
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
