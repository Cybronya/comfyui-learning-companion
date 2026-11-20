---
name: unknown_workflow_lora_sampler_unet_13
type: Unknown Workflow
frequency: 25
level: strong
coverage: 0.9934
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Nextscene自动分镜_1993161031792918530.json, 图片生成/图生图/图片多视角 角色多视图 多角度  Qwen_Edit_2511_2050776686031056897.json, 图片生成/图生图/图生图  分镜多视图  多角度  多视角  Qwen_Edit_2511_2076960940599369729.json, 图片生成/图生图/图生图--多视角 角色多视图 多角度  Qwen_Edit_2511_2049002518016958465.json, 图片生成/图生图/图生图--多视角 角色多视图 多角度  Qwen_Edit_2511_2049008140716351489.json, 图片生成/图生图/多视图  多角度  多视角  分镜图生图  Qwen_Edit_2511_2075598024025403394.json, 图片生成/图生图/多视图  多角度  多视角  分镜图生图  Qwen_Edit_2511_2084517613262163970.json, 图片生成/图生图/多视图  多角度  多视角  分镜表演 图生图  Qwen_Edit_2511_2063269110716387329.json, 图片生成/图生图/多视图  多角度  多视角  分镜表演 图生图  Qwen_Edit_2511_2069026835308040194.json, 图片生成/图生图/多视图  多角度  多视角 角色表演  分镜图生图   Qwen_Edit_2511_2074733214786211841.json, 图片生成/图生图/多视角 分镜头 角色多视图 多角度  Qwen_Edit_2511_2057745501512093697.json, 图片生成/图生图/多视角 分镜头 角色多视图 多角度  Qwen_Edit_2511_2066030705288765441.json, 图片生成/图生图/多视角 角色多视图 多角度  Qwen_Edit_2511_2045858528677597185.json, 图片生成/图生图/多视角 角色多视图 多角度  Qwen_Edit_2511_2046787815349952514.json, 图片生成/图生图/多视角 角色多视图 多角度  Qwen_Edit_2511_2047901643370401793.json, 图片生成/图生图/多视角 角色多视图 多角度  Qwen_Edit_2511_2048406727007150081.json, 图片生成/图生图/多视角 角色多视图 多角度  Qwen_Edit_2511_2053522805450387457.json, 图片生成/图生图/多视角 角色多视图 多角度  Qwen_Edit_2511_2058594092136878082.json, 图片生成/图生图/多视角 角色多视图 多角度  Qwen_Edit_2511_2058598881121882114.json, 图片生成/图生图/多角度  多视图  分镜   多视角_2046781273150066690.json, 图片生成/文生图/多角度-生图_2077359821246001153.json, 图片生成/文生图/多角度（短剧专用）-邻家AI大女孩_2042370680309686273.json, 图片生成/文生图/多角度（短剧专用）-邻家AI大女孩_2056917392671985665.json, 图片生成/文生图/模特分镜 套图 Qwen_Edit_2511   IP角色多视图 多视角 三视图_2042929279717085186.json, 平台全量/Qwen Edit2509产品一致性+多角度分镜_1987420854432804866.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/Qwen_Nextscene自动分镜_1993161031792918530.json、图片生成/图生图/图片多视角 角色多视图 多角度  Qwen_Edit_2511_2050776686031056897.json、图片生成/图生图/图生图  分镜多视图  多角度  多视角  Qwen_Edit_2511_2076960940599369729.json、图片生成/图生图/图生图--多视角 角色多视图 多角度  Qwen_Edit_2511_2049002518016958465.json、图片生成/图生图/图生图--多视角 角色多视图 多角度  Qwen_Edit_2511_2049008140716351489.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 25 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 2/25 个有
- `CR Prompt Text` —— 1/25 个有
- `EmptyLatentImage` —— 1/25 个有
- `Fast Groups Muter (rgthree)` —— 1/25 个有
- `JWStringConcat` —— 1/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/25 个有
- `ProcessString` —— 1/25 个有
- `Qwen3_VQA` —— 1/25 个有
- `easy imageConcat` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 25 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 25 | 100% |
| 采样算法 | euler | - | 25 | 100% |
| 调度器 | simple | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 1280 | - | 1 | 100% |
| 高度 | 720 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，25 个样本，一致性 100%
- 调度器 最常用 simple，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 高发问题（26/25 个样本）：Steps较低可能导致细节不足
