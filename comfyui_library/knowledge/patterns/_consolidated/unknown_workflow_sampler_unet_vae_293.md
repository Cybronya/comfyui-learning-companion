---
name: unknown_workflow_sampler_unet_vae_293
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8345
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenPERewriteT8, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 Fix修复图像编辑_2103711535771250690.json, 图片生成/图生图/Qwen-Image 2.1图像编辑（海报）_2109584446545551362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_293

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 Fix修复图像编辑_2103711535771250690.json、图片生成/图生图/Qwen-Image 2.1图像编辑（海报）_2109584446545551362.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenPERewriteT8`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `APG` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `FreSca` —— 1/2 个有
- `JWDatetimeString` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SeedNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1112 | - | 2 | 92% |
| 高度 | 1312 | - | 2 | 78% |
| 采样步数 | 32.5 | - | 2 | 77% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | seeds_2 | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1112，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 1312，样本不足，未给区间，2 个样本
- 采样步数 中位数 32.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 seeds_2，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
