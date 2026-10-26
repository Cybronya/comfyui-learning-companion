---
name: unknown_workflow_lora_sampler_unet_101
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.911571
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptySD3LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511 人物三视图一键生成工作流_2062516959513767937.json, 图片生成/图生图/Qwen-Edit-2511-图像编辑-一致性加强版本_2003677586276401154.json, 图片生成/图生图/三视图-三视图一键生成-Qwen-Edit-2511_2007681800415481857.json, 图片生成/图生图/人物三视图、影视短剧角色资产图一键生成_Qwen-Edit-2511_2087508775061254145.json, 图片生成/图生图/人物三视图一键生成_Qwen-Edit-2511_2024773960365248513.json, 图片生成/图生图/人物三视图一键生成_Qwen-Edit-2511_2037433892415737858.json, 数字人/数字人/真人参考生成基础演员资产_2094427436439134210.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_101

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511 人物三视图一键生成工作流_2062516959513767937.json、图片生成/图生图/Qwen-Edit-2511-图像编辑-一致性加强版本_2003677586276401154.json、图片生成/图生图/三视图-三视图一键生成-Qwen-Edit-2511_2007681800415481857.json、图片生成/图生图/人物三视图、影视短剧角色资产图一键生成_Qwen-Edit-2511_2087508775061254145.json、图片生成/图生图/人物三视图一键生成_Qwen-Edit-2511_2024773960365248513.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `Int` —— 6/7 个有
- `easy boolean` —— 6/7 个有
- `easy ifElse` —— 6/7 个有
- `GODMT_BatchToList` —— 5/7 个有
- `GODMT_SplitString` —— 5/7 个有
- `JjkConcat` —— 2/7 个有
- `SizeSelector` —— 2/7 个有
- `Text` —— 2/7 个有
- `easy setNode` —— 2/7 个有
- `GetNode` —— 1/7 个有
- `ImageMergeNode` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `ShowAnything|Mie` —— 1/7 个有
- `easy getNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | sa_solver | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
