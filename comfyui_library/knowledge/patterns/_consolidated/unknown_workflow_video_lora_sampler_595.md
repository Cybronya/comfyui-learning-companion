---
name: unknown_workflow_video_lora_sampler_595
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9175
common_nodes: [CLIPLoader, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageSizeAndCount, ImageBatchMulti, ImageResizeKJ, Int, JWImageExtractFromBatch, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, String Literal, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, WanVideoEnhanceAVideoKJ, WanVideoVACEStartToEndFrame, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/六图丝滑循环变身_1982724016962183169.json, 视频生成/图生视频/六图丝滑循环变身wan2.2+vace+FlashVSR+变身LORA_1962779273469771778.json, 视频生成/图生视频/六图丝滑循环变身wan2.2+vace+FlashVSR+变身LORA_1997299541873475585.json, 视频生成/图生视频/极速无限循环变身VACE串联首尾帧_1927192575344594946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_595

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/六图丝滑循环变身_1982724016962183169.json、视频生成/图生视频/六图丝滑循环变身wan2.2+vace+FlashVSR+变身LORA_1962779273469771778.json、视频生成/图生视频/六图丝滑循环变身wan2.2+vace+FlashVSR+变身LORA_1997299541873475585.json、视频生成/图生视频/极速无限循环变身VACE串联首尾帧_1927192575344594946.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `ImageBatchMulti`
- `ImageResizeKJ`
- `Int`
- `JWImageExtractFromBatch`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `String Literal`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoEnhanceAVideoKJ`
- `WanVideoVACEStartToEndFrame`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `FlashVSRNode` —— 3/4 个有
- `Lora Loader Stack (rgthree)` —— 3/4 个有
- `RHHiddenNodes` —— 3/4 个有
- `CFGZeroStarAndInit` —— 1/4 个有
- `CR Upscale Image` —— 1/4 个有
- `PatchModelPatcherOrder` —— 1/4 个有
- `SkipLayerGuidanceWanVideo` —— 1/4 个有
- `TorchCompileModelWanVideo` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `WanVideoTeaCacheKJ` —— 1/4 个有
- `wanBlockSwap` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 3 - 4 | 4 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 3 - 4，4 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
