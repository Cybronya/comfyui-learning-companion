---
name: unknown_workflow_lora_sampler_clip_56
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.7045
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, GetNode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2054181247055867906.json, 图片生成/文生图/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2104525743832260609.json, 图片生成/文生图/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2104574282016837634.json, 图片生成/文生图/Z-image-base文生图12步_2058131292830650370.json, 视频生成/文生视频/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2055867642845646850.json, 视频生成/文生视频/（手动提示词基础版）Z-Image Turbo 9宫格文生图工作流_2054783450862899202.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2054181247055867906.json、图片生成/文生图/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2104525743832260609.json、图片生成/文生图/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2104574282016837634.json、图片生成/文生图/Z-image-base文生图12步_2058131292830650370.json、视频生成/文生视频/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2055867642845646850.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `GetNode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 5/6 个有
- `Anything Everywhere3` —— 5/6 个有
- `ImageGridComposite3x3` —— 5/6 个有
- `PrimitiveInt` —— 5/6 个有
- `CR Text` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 12 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_multistep | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 45/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 12，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（45/6 个样本）：Steps较低可能导致细节不足
