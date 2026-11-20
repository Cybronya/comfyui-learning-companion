---
name: unknown_workflow_video_sampler_clip_248
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.436
common_nodes: [CLIPLoader, CLIPTextEncode, FloatConstant, GetImageRangeFromBatch, GetNode, INTConstant, ImageBatchMulti, ImageColorMatch+, ImageFromBatch, ImageResizeKJv2, KSampler, LayerUtility: PurgeVRAM, LoadImage, MathExpression|pysssss, ModelSamplingSD3, PreviewImage, SetNode, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_GetImageCount, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan 2.1 VACE-SVI - CN V2V - Long Video 跳舞专用_1985556166254252034.json, 视频生成/图生视频/循环重复帧图生视频无限时长_1943251826638528514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_248

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan 2.1 VACE-SVI - CN V2V - Long Video 跳舞专用_1985556166254252034.json、视频生成/图生视频/循环重复帧图生视频无限时长_1943251826638528514.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：44%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `FloatConstant`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageColorMatch+`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PreviewImage`
- `SetNode`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `Power Lora Loader (rgthree)` —— 1/2 个有
- `TorchCompileModelWanVideoV2` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
