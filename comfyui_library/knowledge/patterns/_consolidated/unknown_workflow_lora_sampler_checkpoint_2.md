---
name: unknown_workflow_lora_sampler_checkpoint_2
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.519571
common_nodes: [CLIPLoader, CheckpointLoaderSimple, ConditioningZeroOut, GetNode, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, PreviewAny, ProcessString, SaveImage, SetNode, Text, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: [easy promptLine]
members: [图片生成/文生图/1983176992105361409.json, 图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next Scene_1997318334771314689.json, 图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next+Scene_1998418153245958146.json, 图片生成/文生图/快速分镜生成 影视创作利器 再也不用手搓分镜了_2018317393369501697.json, 图片生成/文生图/漫剧动画分镜单镜_多镜生成_1999170734574497794.json, 图片生成/文生图/解说漫分镜工作流_2049704945468887041.json, 视频生成/图生视频/1983176992105361409.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1983176992105361409.json、图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next Scene_1997318334771314689.json、图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next+Scene_1998418153245958146.json、图片生成/文生图/快速分镜生成 影视创作利器 再也不用手搓分镜了_2018317393369501697.json、图片生成/文生图/漫剧动画分镜单镜_多镜生成_1999170734574497794.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `GetNode`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `ProcessString`
- `SaveImage`
- `SetNode`
- `Text`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | sa_solver | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy promptLine
