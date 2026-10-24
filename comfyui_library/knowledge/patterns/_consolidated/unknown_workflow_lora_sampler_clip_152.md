---
name: unknown_workflow_lora_sampler_clip_152
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.5615
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, KSampler, Lora Loader Stack (rgthree), ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen- 基础文生图工作流_1988231309522812930.json, 图片生成/文生图/Qwen-千问多字体直出-字体设计 中文字体设计_1993312885105426433.json, 图片生成/文生图/Qwen-极致写实文生图+SD放大_1984095755768102914.json, 图片生成/文生图/Qwen千问文生图+Lora+SD放大+潜空间放大(不定时更新)_1972192446874578945.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_152

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen- 基础文生图工作流_1988231309522812930.json、图片生成/文生图/Qwen-千问多字体直出-字体设计 中文字体设计_1993312885105426433.json、图片生成/文生图/Qwen-极致写实文生图+SD放大_1984095755768102914.json、图片生成/文生图/Qwen千问文生图+Lora+SD放大+潜空间放大(不定时更新)_1972192446874578945.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `KSampler`
- `Lora Loader Stack (rgthree)`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `Seed (rgthree)` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `easy promptConcat` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `LatentUpscaleBy` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `UltimateSDUpscale` —— 1/4 个有
- `UltimateSDUpscaleNoUpscale` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 4 | 80% |
| Prompt 约束强度(CFG) | 4 | 3 - 8 | 4 | 60% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 3 - 8，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
