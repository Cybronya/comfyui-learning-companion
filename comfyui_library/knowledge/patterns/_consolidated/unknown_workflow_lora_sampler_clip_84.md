---
name: unknown_workflow_lora_sampler_clip_84
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.866333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商线稿生成效果图 千问_1959246058834571266.json, 图片生成/文生图/2031595764664770561.json, 图片生成/文生图/Qwen Image 4步加速 文生图_1967372243183525890.json, 图片生成/文生图/Qwen Image 8步加速 文生图_1967367971867910145.json, 图片生成/文生图/Qwen-Image ComfyUI原生工作流_1970739735536824321.json, 图片生成/文生图/Qwen-Image的Canny&Depth&Inpaint_1958819414923751425.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/电商线稿生成效果图 千问_1959246058834571266.json、图片生成/文生图/2031595764664770561.json、图片生成/文生图/Qwen Image 4步加速 文生图_1967372243183525890.json、图片生成/文生图/Qwen Image 8步加速 文生图_1967367971867910145.json、图片生成/文生图/Qwen-Image ComfyUI原生工作流_1970739735536824321.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/6 个有
- `JjkText` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `CFGNorm` —— 3/6 个有
- `ModelPatchLoader` —— 2/6 个有
- `QwenImageDiffsynthControlnet` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `String Literal` —— 1/6 个有
- `easy imageSize` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 6 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 6 | 34% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，6 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（9/6 个样本）：Steps较低可能导致细节不足
