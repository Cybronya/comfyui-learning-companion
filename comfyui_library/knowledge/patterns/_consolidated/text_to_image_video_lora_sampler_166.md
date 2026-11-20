---
name: text_to_image_video_lora_sampler_166
type: Text To Image
frequency: 4
level: strong
coverage: 0.8395
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, DrawViTPose, EmptyImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, ImageConcanate, ImageResizeKJv2, Int, KSampler, LayerUtility: ImageBlend V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MaskToImage, ModelSamplingAuraFlow, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, RHHiddenNodes, SaveImage, SimpleMath+, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy indexAnything, easy int, easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/完整版【多角色替换++动作迁移+】影视恶搞++多遮罩模式控制_2029201805380423681.json, 视频生成/图生视频/影视二创整合版_2002368858285568001.json, 视频生成/图生视频/短剧二创 影视二创  完全整合版_2042237308153368578.json, 视频生成/图生视频/短剧二创 影视二创  完全整合版_2042240908560699393.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_166

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/完整版【多角色替换++动作迁移+】影视恶搞++多遮罩模式控制_2029201805380423681.json、视频生成/图生视频/影视二创整合版_2002368858285568001.json、视频生成/图生视频/短剧二创 影视二创  完全整合版_2042237308153368578.json、视频生成/图生视频/短剧二创 影视二创  完全整合版_2042240908560699393.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
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
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1536 | 1536 - 1536 | 4 | 100% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
