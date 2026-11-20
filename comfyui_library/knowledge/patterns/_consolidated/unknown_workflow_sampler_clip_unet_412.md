---
name: unknown_workflow_sampler_clip_unet_412
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.877333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, RHBatchImages:, RHExtractImage, RHUploadZip, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/z-image批量洗图_1999447064650149889.json, 图片生成/图生图/【批量处理工具】去水印_Flux.2.0Klein9B_2031674597690576897.json, 平台全量/批量去除水印-ZIP打包上传图片-klein9b_2028756307121020930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_412

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/z-image批量洗图_1999447064650149889.json、图片生成/图生图/【批量处理工具】去水印_Flux.2.0Klein9B_2031674597690576897.json、平台全量/批量去除水印-ZIP打包上传图片-klein9b_2028756307121020930.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `HAIGC_SaveImagesToZip` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `easy batchAnything` —— 2/3 个有
- `scale` —— 2/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 2 - 10 | 3 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 2 - 10，3 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
