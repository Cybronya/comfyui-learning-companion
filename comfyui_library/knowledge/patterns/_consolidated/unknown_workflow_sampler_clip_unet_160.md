---
name: unknown_workflow_sampler_clip_unet_160
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.867333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商线稿生成效果图 千问_1959246058834571266.json, 图片生成/文生图/2031595764664770561.json, 图片生成/文生图/Qwen Image 4步加速 文生图_1967372243183525890.json, 图片生成/文生图/Qwen Image 8步加速 文生图_1967367971867910145.json, 图片生成/文生图/Qwen Image封面生成-日拱一卒_1958095012225495041.json, 图片生成/文生图/Qwen Image文生图_1954799878556704770.json, 图片生成/文生图/Qwen-Image ComfyUI原生工作流_1970739735536824321.json, 图片生成/文生图/Qwen-Image的Canny&Depth&Inpaint_1958819414923751425.json, 平台全量/电商图片局部重绘 千问_1959239628047986690.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_160

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/电商线稿生成效果图 千问_1959246058834571266.json、图片生成/文生图/2031595764664770561.json、图片生成/文生图/Qwen Image 4步加速 文生图_1967372243183525890.json、图片生成/文生图/Qwen Image 8步加速 文生图_1967367971867910145.json、图片生成/文生图/Qwen Image封面生成-日拱一卒_1958095012225495041.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 7/9 个有
- `LoadImage` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `ModelSamplingAuraFlow` —— 7/9 个有
- `CFGNorm` —— 4/9 个有
- `ModelPatchLoader` —— 3/9 个有
- `QwenImageDiffsynthControlnet` —— 3/9 个有
- `easy imageSize` —— 2/9 个有
- `AIO_Preprocessor` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `String Literal` —— 1/9 个有
- `easy seed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 9 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 9 | 36% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | normal | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，9 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 normal，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
