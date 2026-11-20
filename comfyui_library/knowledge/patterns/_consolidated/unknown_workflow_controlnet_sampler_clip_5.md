---
name: unknown_workflow_controlnet_sampler_clip_5
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.837833
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, GetImageSize, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/25.8.23 Qwen-Image千问 线稿+深度+重绘工作流_1959069626179203074.json, 图片生成/图生图/Qwen-Image-Edit 支持CN控制 深度线稿，局部重绘_1959289171934392322.json, 图片生成/图生图/千问Qwen-controlnet-canny（线稿）_1958758858250481666.json, 图片生成/图生图/千问Qwen-controlnet-depth_1958794204036165633.json, 图片生成/图生图/🥨Qwen-Image千问 线稿+深度+重绘工作流🥨_1959058905261355009.json, 图片生成/文生图/Qwen-Image-Edit线稿_深度_局重绘工作流_1958755877442445314.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/25.8.23 Qwen-Image千问 线稿+深度+重绘工作流_1959069626179203074.json、图片生成/图生图/Qwen-Image-Edit 支持CN控制 深度线稿，局部重绘_1959289171934392322.json、图片生成/图生图/千问Qwen-controlnet-canny（线稿）_1958758858250481666.json、图片生成/图生图/千问Qwen-controlnet-depth_1958794204036165633.json、图片生成/图生图/🥨Qwen-Image千问 线稿+深度+重绘工作流🥨_1959058905261355009.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `SaveImageAndMetadata_` —— 4/6 个有
- `ImageConcanate` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `ImpactInt` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `ResizeMask` —— 2/6 个有
- `ImpactSwitch` —— 1/6 个有
- `LayerColor: ColorAdapter` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 6 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 53% |
| 采样算法 | res_2s | - | 6 | 50% |
| 调度器 | bong_tangent | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 res_2s，6 个样本，一致性 50%
- 调度器 最常用 bong_tangent，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
