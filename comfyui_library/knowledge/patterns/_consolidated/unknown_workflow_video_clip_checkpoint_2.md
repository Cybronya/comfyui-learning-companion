---
name: unknown_workflow_video_clip_checkpoint_2
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.4006
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, CheckpointLoaderSimple, GetNode, ImageConcatMulti, ImpactConditionalBranch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, RHHiddenNodes, SAM3_VideoTrack, SetNode, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy convertAnything, easy imageRemBg, easy int, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/转身保持一致性迁移-优化2_2084535895016951809.json, 平台全量/迄今超强scail2官流单_多图参考可多角色 转身保持一致性动作迁移_角色替换二合一更快更好 支持非人类&运镜，支持长视频-优化2_2070003999960555522.json, 平台全量/迄今超强视频卡点换装scail2角色动作迁移_替换二合一更快更好 口型同步 支持非人类&运镜，3分段+支持25秒长视频理论上无限时长优化2_1971958651256827905.json, 视频生成/图生视频/迄今超强scail2官流单_多图参考可多角色 转身保持一致性动作迁移_角色替换二合一更快更好 支持非人类&运镜，支持长视频-优化2_2001525761691533313.json, 视频生成/图生视频/迄今超强scail2角色动作迁移_替换二合一更快更好 口型同步 支持非人类&运镜，分段+支持长视频理论上无限时长_2065012111629176833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/转身保持一致性迁移-优化2_2084535895016951809.json、平台全量/迄今超强scail2官流单_多图参考可多角色 转身保持一致性动作迁移_角色替换二合一更快更好 支持非人类&运镜，支持长视频-优化2_2070003999960555522.json、平台全量/迄今超强视频卡点换装scail2角色动作迁移_替换二合一更快更好 口型同步 支持非人类&运镜，3分段+支持25秒长视频理论上无限时长优化2_1971958651256827905.json、视频生成/图生视频/迄今超强scail2官流单_多图参考可多角色 转身保持一致性动作迁移_角色替换二合一更快更好 支持非人类&运镜，支持长视频-优化2_2001525761691533313.json、视频生成/图生视频/迄今超强scail2角色动作迁移_替换二合一更快更好 口型同步 支持非人类&运镜，分段+支持长视频理论上无限时长_2065012111629176833.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：40%

## 共有节点

全部 5 个 workflow 都包含：
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
- `BatchImagesNode` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `KSampler` —— 3/5 个有
- `SCAIL2ColoredMask` —— 3/5 个有
- `VAEDecodeTiled` —— 3/5 个有
- `WanContextWindowsManual` —— 3/5 个有
- `BasicScheduler` —— 2/5 个有
- `GetImageRangeFromBatch` —— 2/5 个有
- `KSamplerSelect` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `SamplerCustom` —— 2/5 个有
- `VAEDecode` —— 2/5 个有
- `AudioCrop` —— 1/5 个有
- `AudioEvenSplitNode` —— 1/5 个有
- `AudioSelectNode` —— 1/5 个有
- `ColorTransfer` —— 1/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/5 个有
- `GIMMVFI_interpolate` —— 1/5 个有
- `Int` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有
- `SeedVR2ExtraArgs` —— 1/5 个有
- `SeedVR2GGUF` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
- 高发问题（3/5 个样本）：发现KSampler但没有VAEDecode
