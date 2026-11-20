---
name: unknown_workflow_sampler_clip_unet_460
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/朦胧唯美zimage_2005074233749372930.json, 图片生成/文生图/柔和光影日系风Soft-Light Bright- Anime Art Style -Image工作流_2070113768801128449.json, 图片生成/文生图/超自然人像生成：qwen-image-2512加Z-image双采样器文生图_2022543014375198722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_460

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/朦胧唯美zimage_2005074233749372930.json、图片生成/文生图/柔和光影日系风Soft-Light Bright- Anime Art Style -Image工作流_2070113768801128449.json、图片生成/文生图/超自然人像生成：qwen-image-2512加Z-image双采样器文生图_2022543014375198722.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
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
- `LoraLoaderModelOnly` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Latent Noise Injection` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `ZImageLoraModelOnly` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 10 | 9 - 14 | 3 | 80% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | ddim | - | 3 | 33% |
| 重绘幅度 | sgm_uniform | - | 3 | 33% |
| 宽度 | 1280 | 720 - 1280 | 3 | 76% |
| 高度 | 1280 | 720 - 1856 | 3 | 64% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 10，观测区间 9 - 14，3 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 ddim，3 个样本，一致性 33%
- 重绘幅度 最常用 sgm_uniform，3 个样本，一致性 33%
- 宽度 中位数 1280，观测区间 720 - 1280，3 个样本
- 高度 中位数 1280，观测区间 720 - 1856，3 个样本
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
