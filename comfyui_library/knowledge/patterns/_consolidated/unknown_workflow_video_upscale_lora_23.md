---
name: unknown_workflow_video_upscale_lora_23
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.582
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, Float, GetImageRangeFromBatch, GetNode, ImageBatchMulti, ImageConcatMulti, ImageSmartSharpen+, ImpactSwitch, Int, KSampler, LatentPixelScale, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, ReverseImageBatch, SetNode, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncodeTiled, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanContextWindowsManual]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/视频重绘+基础视频到视频重绘_2033421118345846785.json, 平台全量/🈚️wan2.1_2.2 low native v2v 视频重绘 基础视频到视频重绘_1936618028199219202.json, 视频生成/图生视频/重绘_2041483351273508865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_23

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频重绘+基础视频到视频重绘_2033421118345846785.json、平台全量/🈚️wan2.1_2.2 low native v2v 视频重绘 基础视频到视频重绘_1936618028199219202.json、视频生成/图生视频/重绘_2041483351273508865.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `Float`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `ImageSmartSharpen+`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LatentPixelScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ReverseImageBatch`
- `SetNode`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncodeTiled`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanContextWindowsManual`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
