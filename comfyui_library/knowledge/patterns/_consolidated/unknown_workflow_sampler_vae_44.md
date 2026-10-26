---
name: unknown_workflow_sampler_vae_44
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.91
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku Qwen Edit  2509 1-3 Images for Reference_2037090640076480513.json, 图片生成/图生图/Nunchaku-qwen-image文生图_1965040673634308097.json, 图片生成/图生图/NunchakuQwenImageEdit2509Plus双图换背景_1971708341292625922.json, 图片生成/文生图/Nunchaku 4步加速 Qwen Image文生图_1966426602882183170.json, 图片生成/文生图/Nunchaku 8步加速 Qwen Image文生图_1966447914094637058.json, 图片生成/文生图/Nunchaku-Qwen-image-edit-plus-2509_1971430770592137218.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_44

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Nunchaku Qwen Edit  2509 1-3 Images for Reference_2037090640076480513.json、图片生成/图生图/Nunchaku-qwen-image文生图_1965040673634308097.json、图片生成/图生图/NunchakuQwenImageEdit2509Plus双图换背景_1971708341292625922.json、图片生成/文生图/Nunchaku 4步加速 Qwen Image文生图_1966426602882183170.json、图片生成/文生图/Nunchaku 8步加速 Qwen Image文生图_1966447914094637058.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `CLIPTextEncode` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `TextEncodeQwenImageEditPlus` —— 3/6 个有
- `GetImageSize` —— 2/6 个有
- `DWPreprocessor` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 6 | 0% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 4 | 6 | 38% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，6 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 4，6 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
