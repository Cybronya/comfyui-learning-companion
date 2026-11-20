---
name: unknown_workflow_lora_sampler_clip_119
type: Unknown Workflow
frequency: 5
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, SaveImage, Simple String, String Literal, Text Concatenate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image 胶片感_2035669521972858882.json, 图片生成/文生图/Z-image 胶片感_2071411620244447234.json, 图片生成/文生图/Zimage 基础流_2064620356811448321.json, 图片生成/文生图/Zimage 水印工作流_2038956956236386305.json, 图片生成/文生图/Zimage 胶片工作流_2060357293669179394.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_119

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image 胶片感_2035669521972858882.json、图片生成/文生图/Z-image 胶片感_2071411620244447234.json、图片生成/文生图/Zimage 基础流_2064620356811448321.json、图片生成/文生图/Zimage 水印工作流_2038956956236386305.json、图片生成/文生图/Zimage 胶片工作流_2060357293669179394.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Simple String`
- `String Literal`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BetterFilmGrain` —— 4/5 个有
- `ImageSharpen` —— 4/5 个有
- `LayerColor: ColorBalance` —— 4/5 个有
- `LayerUtility: ImageBlendAdvance` —— 4/5 个有
- `LoadImage` —— 4/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
