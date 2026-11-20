---
name: unknown_workflow_sampler_clip_unet_213
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.6015
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, KSampler, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/组件系列11-QWEN-3-VL反推节点_2054524098671325186.json, 图片生成/文生图/Krea2_turbo_fp8文生图_2083589922623156226.json, 图片生成/文生图/Krea2文生图_2083457731943555073.json, 图片生成/文生图/Qwen- 基础文生图工作流_1988231309522812930.json, 图片生成/文生图/Qwen-极致写实文生图+SD放大_1984095755768102914.json, 图片生成/文生图/Qwen千问文生图+Lora+SD放大+潜空间放大(不定时更新)_1972192446874578945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_213

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/组件系列11-QWEN-3-VL反推节点_2054524098671325186.json、图片生成/文生图/Krea2_turbo_fp8文生图_2083589922623156226.json、图片生成/文生图/Krea2文生图_2083457731943555073.json、图片生成/文生图/Qwen- 基础文生图工作流_1988231309522812930.json、图片生成/文生图/Qwen-极致写实文生图+SD放大_1984095755768102914.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `KSampler`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/6 个有
- `ModelSamplingAuraFlow` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `Lora Loader Stack (rgthree)` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `easy promptConcat` —— 3/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `LatentUpscaleBy` —— 1/6 个有
- `ShowAnything|Mie` —— 1/6 个有
- `UltimateSDUpscale` —— 1/6 个有
- `UltimateSDUpscaleNoUpscale` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 30 | 6 | 43% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 8 | 6 | 20% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 30，6 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 8，6 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
