---
name: unknown_workflow_sampler_clip_unet_431
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.806
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Z-image批量洗图图生图_1997513781804732418.json, 图片生成/图生图/wan2.1批量洗图_1964886774210248705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_431

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-image批量洗图图生图_1997513781804732418.json、图片生成/图生图/wan2.1批量洗图_1964886774210248705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `RH_Captioner`
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
- `Bjornulf_ShowInt` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.375 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.375，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
