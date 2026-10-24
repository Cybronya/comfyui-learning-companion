---
name: unknown_workflow_sampler_clip_unet_306
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.97725
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-image局部重绘_1956259506659446786.json, 图片生成/文生图/RH-PSAPI插件用-文生图_2068260936263233538.json, 图片生成/文生图/Z-Image-base局部重绘_2016771278450991105.json, 图片生成/文生图/千问2512文生图海报、图片设计_2093310820385116161.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_306

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen-image局部重绘_1956259506659446786.json、图片生成/文生图/RH-PSAPI插件用-文生图_2068260936263233538.json、图片生成/文生图/Z-Image-base局部重绘_2016771278450991105.json、图片生成/文生图/千问2512文生图海报、图片设计_2093310820385116161.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

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
- `ConditioningZeroOut` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `InpaintModelConditioning` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `QwenImageLatentAspectRatio` —— 2/4 个有
- `DifferentialDiffusion` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `MaskBlur+` —— 1/4 个有
- `VideoLinearCFGGuidance` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 8 | 4 - 20 | 4 | 40% |
| Prompt 约束强度(CFG) | 2 | 1 - 8 | 4 | 12% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.85 - 1 | 4 | 93% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 20，4 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 8，4 个样本，取值分散，一致性仅 12%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.85 - 1，4 个样本，取值集中（一致性 93%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
