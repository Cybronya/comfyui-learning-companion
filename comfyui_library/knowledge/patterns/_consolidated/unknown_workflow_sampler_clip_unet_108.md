---
name: unknown_workflow_sampler_clip_unet_108
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.8574
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商线稿生成效果图 千问_1959246058834571266.json, 图片生成/文生图/2031595764664770561.json, 图片生成/文生图/QWEN FP8文生图8步快速工作流_1966317820562878466.json, 图片生成/文生图/Qwen Image 4步加速 文生图_1967372243183525890.json, 图片生成/文生图/Qwen Image 8步加速 文生图_1967367971867910145.json, 图片生成/文生图/Qwen Image封面生成-日拱一卒_1958095012225495041.json, 图片生成/文生图/Qwen Image文生图_1954799878556704770.json, 图片生成/文生图/【老金驿站】4步Qwen2512极速lighiting出图工作流_2006643426929938433.json, 图片生成/文生图/【老金驿站】Z-imageBase真实系列Lora工作流_2037516112421720066.json, 图片生成/文生图/【老金驿站】Z-imageBase高质量稳定直出工作流_2016671045016625154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_108

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/电商线稿生成效果图 千问_1959246058834571266.json、图片生成/文生图/2031595764664770561.json、图片生成/文生图/QWEN FP8文生图8步快速工作流_1966317820562878466.json、图片生成/文生图/Qwen Image 4步加速 文生图_1967372243183525890.json、图片生成/文生图/Qwen Image 8步加速 文生图_1967367971867910145.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 9/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `CFGNorm` —— 6/10 个有
- `JjkText` —— 6/10 个有
- `LoadImage` —— 5/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `PreviewImage` —— 2/10 个有
- `ModelPatchLoader` —— 1/10 个有
- `QwenImageDiffsynthControlnet` —— 1/10 个有
- `easy imageSize` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 10 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 37% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | normal | - | 10 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，10 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 normal，10 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（6/10 个样本）：Steps较低可能导致细节不足
