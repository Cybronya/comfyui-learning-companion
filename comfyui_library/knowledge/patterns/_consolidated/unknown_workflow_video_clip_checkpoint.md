---
name: unknown_workflow_video_clip_checkpoint
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4045
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, CheckpointLoaderSimple, GetNode, ImageConcatMulti, ImpactConditionalBranch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, RHHiddenNodes, SAM3_VideoTrack, SetNode, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy convertAnything, easy imageRemBg, easy int, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2001525761691533313.json, 视频生成/图生视频/2065012111629176833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2001525761691533313.json、视频生成/图生视频/2065012111629176833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：40%

## 共有节点

全部 2 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CheckpointLoaderSimple`
- `GetNode`
- `ImageConcatMulti`
- `ImpactConditionalBranch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `RHHiddenNodes`
- `SAM3_VideoTrack`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `easy convertAnything`
- `easy imageRemBg`
- `easy int`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `ColorTransfer` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `Int` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SCAIL2ColoredMask` —— 1/2 个有
- `SamplerCustom` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEDecodeTiled` —— 1/2 个有
- `WanContextWindowsManual` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 高发问题（1/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
