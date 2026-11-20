---
name: unknown_workflow_video_upscale_sampler_11
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.629
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, DownloadAndLoadFlorence2Model, Fast Groups Bypasser (rgthree), Florence2Run, GetNode, ImageConcatMulti, ImageFromBatch+, ImageUpscaleWithModel, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, RIFE VFI, Seed_, SetNode, SkipLayerGuidanceWanVideo, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoEnhanceAVideoKJ, WanVideoTeaCacheKJ]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/通义万相WAN2.1视频转视频一致性修复-StarAI_1905197127684001794.json, 平台全量/通义万相WAN2.1视频转视频一致性修复-简化版_1924405005007114242.json, 平台全量/通义万相WAN2.1视频转视频非一致性高清修复-StarAI_1902600695588237313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/通义万相WAN2.1视频转视频一致性修复-StarAI_1905197127684001794.json、平台全量/通义万相WAN2.1视频转视频一致性修复-简化版_1924405005007114242.json、平台全量/通义万相WAN2.1视频转视频非一致性高清修复-StarAI_1902600695588237313.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `DownloadAndLoadFlorence2Model`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageUpscaleWithModel`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `RIFE VFI`
- `Seed_`
- `SetNode`
- `SkipLayerGuidanceWanVideo`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideoKJ`
- `WanVideoTeaCacheKJ`

**可变部分**（部分 workflow 才有）：
- `ImageBlur` —— 2/3 个有
- `InstructPixToPixConditioning` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `VAEEncodeTiled` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 3 | 100% |
| 采样算法 | gradient_estimation | - | 3 | 67% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 0.25 - 1 | 3 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 gradient_estimation，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，3 个样本
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
