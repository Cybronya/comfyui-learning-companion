---
name: unknown_workflow_controlnet_clip_unet_2
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8294
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image controlnet2.0反推洗图_2073292094273318914.json, 图片生成/文生图/z-image controlnet反推洗图_2073286416464957442.json, 图片生成/文生图/z-image-深度图_1996814449833123841.json, 平台全量/z-image-turbo_fun_controlnet_1996823785732984833.json, 平台全量/自用CN控制洗图工作流_带抠图_2041759141802287106.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/z-image controlnet2.0反推洗图_2073292094273318914.json、图片生成/文生图/z-image controlnet反推洗图_2073286416464957442.json、图片生成/文生图/z-image-深度图_1996814449833123841.json、平台全量/z-image-turbo_fun_controlnet_1996823785732984833.json、平台全量/自用CN控制洗图工作流_带抠图_2041759141802287106.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetImageSize`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DJZImageScaleToTotalPixels` —— 3/5 个有
- `KSamplerAdvanced` —— 3/5 个有
- `AILab_QwenVL` —— 2/5 个有
- `KSampler` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `ImageScaleToMaxDimension` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2ExtraArgs` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 5 | 40% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 5 | 34% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 8，5 个样本，一致性 40%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，5 个样本，取值分散，一致性仅 34%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
