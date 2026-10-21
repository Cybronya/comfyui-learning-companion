---
name: unknown_workflow_sampler_unet_vae_58
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7601
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json, 图片生成/文生图/Qwen Image 2.1-文生图_2101855895343951873.json, 图片生成/文生图/Qwen Image 2.1文生图_2101560854905970690.json, 图片生成/文生图/Qwen Image 2.1文生图_2101902260690313218.json, 图片生成/文生图/Qwen Image 2.1透明图层+文生图！_2101836586576072706.json, 图片生成/文生图/Qwen Image 2.1：文生图_2104089249137119233.json, 图片生成/文生图/Qwen image 2.1 文生图-V1_2101852626458599426.json, 图片生成/文生图/Qwen image 2.1 文生图-角色四视图-V1_2101850121867718657.json, 图片生成/文生图/Qwen2.1_BF16_文生图官方工作流_2101860361765998594.json, 图片生成/文生图/Qwenimage2.1 文生图工作流_2101837000008622081.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_58

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json、图片生成/文生图/Qwen Image 2.1-文生图_2101855895343951873.json、图片生成/文生图/Qwen Image 2.1文生图_2101560854905970690.json、图片生成/文生图/Qwen Image 2.1文生图_2101902260690313218.json、图片生成/文生图/Qwen Image 2.1透明图层+文生图！_2101836586576072706.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 9/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `SaveImageAdvanced` —— 5/10 个有
- `TextGenerateLTX2Prompt` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `JjkText` —— 2/10 个有
- `StringConcatenate` —— 2/10 个有
- `孤海注释` —— 2/10 个有
- `ComfySwitchNode` —— 1/10 个有
- `ModelAttentionBackend` —— 1/10 个有
- `PrimitiveBoolean` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 25 - 50 | 10 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1024 | 1024 - 1600 | 10 | 84% |
| 高度 | 1024 | 1024 - 2000 | 10 | 74% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 25 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1600，10 个样本，取值集中（一致性 84%）
- 高度 中位数 1024，观测区间 1024 - 2000，10 个样本
