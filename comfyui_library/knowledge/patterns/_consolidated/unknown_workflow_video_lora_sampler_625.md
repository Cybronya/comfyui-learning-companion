---
name: unknown_workflow_video_lora_sampler_625
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.394667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetNode, INTConstant, ImageConcanate, ImageFromBatch+, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, TTResolutionSelector, VAEDecodeTiled, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanContextWindowsManual, WanSCAILToVideo, easy boolean, easy imageRemBg]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Scail-2 官方千帧长视频一键生成+单图 _ 多图参考 +动作迁移+角色替换_2069089123285164033.json, 图片生成/图生图/【寄语秋歌】Scail-2-官方一键长视频+动作迁移+角色替换_2068402819106959361.json, 视频生成/图生视频/Scail2超强快速视频动作迁移_2093289454571180034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_625

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Scail-2 官方千帧长视频一键生成+单图 _ 多图参考 +动作迁移+角色替换_2069089123285164033.json、图片生成/图生图/【寄语秋歌】Scail-2-官方一键长视频+动作迁移+角色替换_2068402819106959361.json、视频生成/图生视频/Scail2超强快速视频动作迁移_2093289454571180034.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：39%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `INTConstant`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SetNode`
- `TTResolutionSelector`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanContextWindowsManual`
- `WanSCAILToVideo`
- `easy boolean`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 2/3 个有
- `ImpactConditionalBranch` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

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
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
