---
name: unknown_workflow_lora_sampler_vae_6
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.5519
common_nodes: [CLIPLoader, ConditioningZeroOut, GetNode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王026.影视分镜回车控制批量_2034921737002950658.json, 图片生成/图生图/人物换装_多图编辑_2032426321309077505.json, 图片生成/文生图/AI代码侠土豆-Qwen-Edit-AIO+Next Scene分镜生成_1983176992105361409.json, 图片生成/文生图/分镜生成_2050910785261588482.json, 图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next Scene_1997318334771314689.json, 图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next+Scene_1998418153245958146.json, 图片生成/文生图/快速分镜生成 影视创作利器 再也不用手搓分镜了_2018317393369501697.json, 图片生成/文生图/漫剧动画分镜单镜_多镜生成_1999170734574497794.json, 图片生成/文生图/解说漫分镜工作流_2049704945468887041.json, 图片生成/文生图/超好用🔥解说漫剧分镜工作流-最新_2052760593840517122.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_6

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王026.影视分镜回车控制批量_2034921737002950658.json、图片生成/图生图/人物换装_多图编辑_2032426321309077505.json、图片生成/文生图/AI代码侠土豆-Qwen-Edit-AIO+Next Scene分镜生成_1983176992105361409.json、图片生成/文生图/分镜生成_2050910785261588482.json、图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next Scene_1997318334771314689.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 9/10 个有
- `ImageResizeKJv2` —— 9/10 个有
- `PreviewAny` —— 9/10 个有
- `ProcessString` —— 9/10 个有
- `easy promptLine` —— 9/10 个有
- `Text` —— 8/10 个有
- `PreviewImage` —— 6/10 个有
- `CR Text` —— 2/10 个有
- `FluxKontextImageScale` —— 1/10 个有
- `UNETLoader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 10 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | sa_solver | - | 10 | 90% |
| 调度器 | beta | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，10 个样本，一致性 90%
- 调度器 最常用 beta，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
