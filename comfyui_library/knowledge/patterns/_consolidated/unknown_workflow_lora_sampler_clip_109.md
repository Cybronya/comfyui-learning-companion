---
name: unknown_workflow_lora_sampler_clip_109
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6654
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/01 Qwen image 批量文生图 亚马逊平台外国儿童模特_2009990778717741058.json, 图片生成/文生图/Anima8步极速工作流_2055609870266707970.json, 图片生成/文生图/Krea2_turbo_fp8文生图_2083589922623156226.json, 图片生成/文生图/Krea2文生图_2083457731943555073.json, 图片生成/文生图/qwen + z-image + qwen2512 三合一批量文生图 亚马逊外国模特场景生成_2018887241812152322.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_109

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/01 Qwen image 批量文生图 亚马逊平台外国儿童模特_2009990778717741058.json、图片生成/文生图/Anima8步极速工作流_2055609870266707970.json、图片生成/文生图/Krea2_turbo_fp8文生图_2083589922623156226.json、图片生成/文生图/Krea2文生图_2083457731943555073.json、图片生成/文生图/qwen + z-image + qwen2512 三合一批量文生图 亚马逊外国模特场景生成_2018887241812152322.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `CR Prompt List` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `LatentColorMatch` —— 1/5 个有
- `LayerColor: Brightness & Contrast` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `ResolutionMaster` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_2s | - | 5 | 40% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
