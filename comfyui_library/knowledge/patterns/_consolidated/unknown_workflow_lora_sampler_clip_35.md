---
name: unknown_workflow_lora_sampler_clip_35
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7495
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-2512基础文生图 T2I_2065613919451963393.json, 图片生成/文生图/Qwen-Image-2512基础文生图 T2I_2076908888892469249.json, 图片生成/文生图/Qwen_Image_2512版4步加速出图_2006606275999703041.json, 图片生成/文生图/Qwen_Image_2512版4步加速出图_2019651247913046018.json, 图片生成/文生图/Qwen白丝长腿丝袜美腿_2019647690329559041.json, 图片生成/文生图/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2054181247055867906.json, 图片生成/文生图/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2104525743832260609.json, 图片生成/文生图/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2104574282016837634.json, 视频生成/文生视频/Z-Image Turbo 9宫格文生图工作流（手动提示词基础版）_2055867642845646850.json, 视频生成/文生视频/（手动提示词基础版）Z-Image Turbo 9宫格文生图工作流_2054783450862899202.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-2512基础文生图 T2I_2065613919451963393.json、图片生成/文生图/Qwen-Image-2512基础文生图 T2I_2076908888892469249.json、图片生成/文生图/Qwen_Image_2512版4步加速出图_2006606275999703041.json、图片生成/文生图/Qwen_Image_2512版4步加速出图_2019651247913046018.json、图片生成/文生图/Qwen白丝长腿丝袜美腿_2019647690329559041.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `Anything Everywhere` —— 5/10 个有
- `Anything Everywhere3` —— 5/10 个有
- `ImageGridComposite3x3` —— 5/10 个有
- `PrimitiveInt` —— 5/10 个有
- `PreviewImage` —— 4/10 个有
- `Int` —— 2/10 个有
- `Text` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 16 | 10 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 10 | 14% |
| 采样算法 | euler | - | 10 | 50% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 49/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 16，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，10 个样本，取值分散，一致性仅 14%
- 采样算法 最常用 euler，10 个样本，一致性 50%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（49/10 个样本）：Steps较低可能导致细节不足
