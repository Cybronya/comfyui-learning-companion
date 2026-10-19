---
name: unknown_workflow_video_lora_sampler_162
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.620545
common_nodes: [CLIPVisionLoader, DrawViTPose, GetImageRangeFromBatch, ImageResizeKJv2, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2064169491482894338.json, 视频生成/图生视频/1996396266479296514.json, 视频生成/图生视频/1995679581803778050.json, 视频生成/图生视频/2073284965781032961.json, 视频生成/图生视频/1997949647484256258.json, 视频生成/图生视频/1996237432284651521.json, 视频生成/图生视频/2068694345024360450.json, 视频生成/图生视频/1996110517959868418.json, 视频生成/图生视频/2037499475232559105.json, 视频生成/图生视频/2049292828706086913.json, 视频生成/图生视频/1996562415049383938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_162

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2064169491482894338.json、视频生成/图生视频/1996396266479296514.json、视频生成/图生视频/1995679581803778050.json、视频生成/图生视频/2073284965781032961.json、视频生成/图生视频/1997949647484256258.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 10/11 个有
- `GetNode` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `WanVideoTorchCompileSettings` —— 9/11 个有
- `ImageConcatMulti` —— 8/11 个有
- `JWInteger` —— 8/11 个有
- `CheckpointLoaderSimple` —— 7/11 个有
- `EmptyLatentImage` —— 7/11 个有
- `KSampler` —— 7/11 个有
- `LayerUtility: PurgeVRAM` —— 7/11 个有
- `PrimitiveInt` —— 7/11 个有
- `SimpleMath+` —— 7/11 个有
- `TextEncodeQwenImageEditPlus` —— 7/11 个有
- `VAEDecode` —— 7/11 个有
- `ttN float` —— 7/11 个有
- `ImageFromBatch+` —— 6/11 个有
- `JjkText` —— 6/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `SaveImage` —— 6/11 个有
- `LoadImage` —— 5/11 个有
- `Text` —— 4/11 个有
- `Text Concatenate` —— 4/11 个有
- `Text Multiline` —— 4/11 个有
- `easy anythingIndexSwitch` —— 4/11 个有
- `DF_Int_to_Float` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `TT_img_enc` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 720 | 720 - 768 | 7 | 98% |
| 高度 | 1280 | 768 - 1280 | 7 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 720 - 768，7 个样本，取值集中（一致性 98%）
- 高度 中位数 1280，观测区间 768 - 1280，7 个样本，取值集中（一致性 85%）
- 高发问题（7/11 个样本）：Steps较低可能导致细节不足
