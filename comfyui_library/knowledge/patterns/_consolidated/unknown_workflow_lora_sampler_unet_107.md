---
name: unknown_workflow_lora_sampler_unet_107
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.916714
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多角度一致性工作流_1987778123494305793.json, 图片生成/图生图/最新多角度分镜（人物一致性）_1985310456749432834.json, 图片生成/文生图/多角度-生图_2077359821246001153.json, 图片生成/文生图/多角度（短剧专用）-邻家AI大女孩_2042370680309686273.json, 图片生成/文生图/多角度（短剧专用）-邻家AI大女孩_2056917392671985665.json, 图片生成/文生图/模特分镜 套图 Qwen_Edit_2511   IP角色多视图 多视角 三视图_2042929279717085186.json, 图片生成/文生图/电商模特多镜头多视角生图工作流_2002650110460850177.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_107

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/多角度一致性工作流_1987778123494305793.json、图片生成/图生图/最新多角度分镜（人物一致性）_1985310456749432834.json、图片生成/文生图/多角度-生图_2077359821246001153.json、图片生成/文生图/多角度（短剧专用）-邻家AI大女孩_2042370680309686273.json、图片生成/文生图/多角度（短剧专用）-邻家AI大女孩_2056917392671985665.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 6/7 个有
- `Any Switch (rgthree)` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `INTConstant` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `String Literal` —— 3/7 个有
- `Text Load Line From File` —— 3/7 个有
- `ImageScaleBy` —— 1/7 个有
- `SeedVR2LoadDiTModel` —— 1/7 个有
- `SeedVR2LoadVAEModel` —— 1/7 个有
- `SeedVR2VideoUpscaler` —— 1/7 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/7 个有
- `easy imageScaleToNormPixels` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 7 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 57% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
