---
name: unknown_workflow_lora_sampler_clip_80
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.78075
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, PreviewAny, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, CR Text Concatenate, easy textSwitch]
members: [图片生成/文生图/1981298041351208962.json, 图片生成/文生图/1982648292121165825.json, 图片生成/文生图/Qwen Rebalance 写实洗图工作流_1991492700780371970.json, 图片生成/文生图/rebalancev1+Qwen3VL(Gemini3)-如歌（更新）_1992884906248261634.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1981298041351208962.json、图片生成/文生图/1982648292121165825.json、图片生成/文生图/Qwen Rebalance 写实洗图工作流_1991492700780371970.json、图片生成/文生图/rebalancev1+Qwen3VL(Gemini3)-如歌（更新）_1992884906248261634.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `easy textSwitch` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 26 | 4 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 4 | 42% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 26，4 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，4 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、easy textSwitch
