---
name: text_to_image_video_lora_sampler_173
type: Text To Image
frequency: 3
level: strong
coverage: 0.819
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, DrawViTPose, EmptyImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, ImageConcanate, ImageResizeKJv2, Int, KSampler, LayerUtility: ImageBlend V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MaskToImage, ModelSamplingAuraFlow, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, RHHiddenNodes, SaveImage, SimpleMath+, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy indexAnything, easy int, easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2002368858285568001.json, 视频生成/图生视频/2042237308153368578.json, 视频生成/图生视频/2042240908560699393.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_173

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2002368858285568001.json、视频生成/图生视频/2042237308153368578.json、视频生成/图生视频/2042240908560699393.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `DrawViTPose`
- `EmptyImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `ImageConcanate`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `LayerUtility: ImageBlend V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `PoseAndFaceDetection`
- `RHHiddenNodes`
- `SaveImage`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy indexAnything`
- `easy int`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
