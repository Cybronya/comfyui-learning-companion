---
name: unknown_workflow_video_lora_sampler_573
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.583667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyMathExpression, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, Fast Groups Muter (rgthree), GIMMVFI_interpolate, GetNode, ImageFromBatch, ImageResizeKJv2, ImpactConditionalBranch, ImpactSwitch, Int, KSampler, LoadImage, LoraLoaderModelOnly, MinNode, ModelSamplingSD3, PreviewImage, PrimitiveBoolean, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanContextWindowsManual, WanSCAILToVideo, easy cleanGpuUsed, easy imageRemBg, easy int, easy showAnything, 图像缩放V2_孤海]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [数字人/数字人/动作迁移人物替换最新Scail2(多参考图版)V3_2078363419417333761.json, 视频生成/图生视频/2076246273501515777.json, 视频生成/图生视频/2076969142116245505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_573

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/动作迁移人物替换最新Scail2(多参考图版)V3_2078363419417333761.json、视频生成/图生视频/2076246273501515777.json、视频生成/图生视频/2076969142116245505.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `DownloadAndLoadGIMMVFIModel`
- `Fast Groups Muter (rgthree)`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MinNode`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveBoolean`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SetNode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanContextWindowsManual`
- `WanSCAILToVideo`
- `easy cleanGpuUsed`
- `easy imageRemBg`
- `easy int`
- `easy showAnything`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `AFL:ImageSwitch` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageBatchMulti` —— 2/3 个有
- `ImpactIfNone` —— 2/3 个有
- `InversionDemoLazySwitch` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `Text` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `VAEDecodeTiled` —— 2/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `easy getNode` —— 1/3 个有
- `easy setNode` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

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
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
