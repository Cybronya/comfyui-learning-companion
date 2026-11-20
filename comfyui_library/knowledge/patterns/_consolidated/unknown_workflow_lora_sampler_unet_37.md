---
name: unknown_workflow_lora_sampler_unet_37
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.957
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多角度一致性工作流_1987778123494305793.json, 图片生成/图生图/多角度切换qwen2511_2036795439428673538.json, 图片生成/图生图/多角度多视角分镜图生图_2061572502698156033.json, 图片生成/图生图/多角度（短剧专用）_2046748685542891521.json, 图片生成/图生图/局部重绘 图生图 洗图 图片编辑_2046875381084463105.json, 图片生成/图生图/最新多角度分镜（人物一致性）_1985310456749432834.json, 图片生成/图生图/模特分镜 套图 Qwen_Edit_2511   IP角色多视图 多视角 三视图_2041860666541219842.json, 图片生成/图生图/模特分镜 套图 Qwen_Edit_2511   IP角色多视图 多视角 三视图_2042102718298329089.json, 图片生成/图生图/角色一致性 人物一致性 分镜 角色多视图 多视角 三视图_2046882399899885570.json, 图片生成/图生图/角色多视图_多角度_多视角_Qwen_Edit_2511_2047214356101865473.json, 图片生成/图生图/角色多视图_多角度_多视角_Qwen_Edit_2511_2047503648166514689.json, 图片生成/图生图/角色多视图_多角度_多视角_Qwen_Edit_2511_2047585223679942658.json, 图片生成/图生图/角色表演   分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2075597201874706433.json, 图片生成/文生图/Qwen_Edit_2511&分镜& 短剧分镜& 漫剧分镜_2044021959486349314.json, 图片生成/文生图/电商模特多镜头多视角生图工作流_2002650110460850177.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_37

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/多角度一致性工作流_1987778123494305793.json、图片生成/图生图/多角度切换qwen2511_2036795439428673538.json、图片生成/图生图/多角度多视角分镜图生图_2061572502698156033.json、图片生成/图生图/多角度（短剧专用）_2046748685542891521.json、图片生成/图生图/局部重绘 图生图 洗图 图片编辑_2046875381084463105.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 15 个 workflow 都包含：
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
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 14/15 个有
- `Any Switch (rgthree)` —— 3/15 个有
- `Fast Groups Bypasser (rgthree)` —— 3/15 个有
- `INTConstant` —— 3/15 个有
- `ShowText|pysssss` —— 3/15 个有
- `String Literal` —— 3/15 个有
- `Text Load Line From File` —— 3/15 个有
- `ImageConcatMulti` —— 1/15 个有
- `ImageFromBatch+` —— 1/15 个有
- `ImageListToBatch+` —— 1/15 个有
- `ImageScaleBy` —— 1/15 个有
- `SeedVR2LoadDiTModel` —— 1/15 个有
- `SeedVR2LoadVAEModel` —— 1/15 个有
- `SeedVR2VideoUpscaler` —— 1/15 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/15 个有
- `easy imageScaleToNormPixels` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 15 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 15 | 66% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（14/15 个样本）：Steps较低可能导致细节不足
