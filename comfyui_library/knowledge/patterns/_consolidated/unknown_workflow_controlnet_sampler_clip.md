---
name: unknown_workflow_controlnet_sampler_clip
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8765
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z Image Turbo Fun Controlnet Union_2063526631158935554.json, 图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json, 图片生成/文生图/Z-Image_turbo控制ControlNet-2601_2020760393320243201.json, 图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json, 图片生成/文生图/z-image controlnet2.0反推洗图_2073292094273318914.json, 图片生成/文生图/z-image controlnet反推洗图_2073286416464957442.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z Image Turbo Fun Controlnet Union_2063526631158935554.json、图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json、图片生成/文生图/Z-Image_turbo控制ControlNet-2601_2020760393320243201.json、图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json、图片生成/文生图/z-image controlnet2.0反推洗图_2073292094273318914.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `RH_Captioner` —— 2/6 个有
- `CannyEdgePreprocessor` —— 1/6 个有
- `DWPreprocessor` —— 1/6 个有
- `DepthAnythingV2Preprocessor` —— 1/6 个有
- `ImageScaleToMaxDimension` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `SeedVR2` —— 1/6 个有
- `SeedVR2ExtraArgs` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 8 - 15 | 6 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_multistep | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 8 - 15，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
