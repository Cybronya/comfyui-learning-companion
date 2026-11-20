---
name: text_to_image_video_lora_sampler_177
type: Text To Image
frequency: 4
level: strong
coverage: 0.9165
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DrawViTPose, EmptyLatentImage, ImageBatch, ImageFromBatch, ImageResizeKJv2, Int, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MemoryCleaner, OnnxDetectionModelLoader, PoseAndFaceDetection, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/动作迁移实测演示｜图生视频人物动作复刻测试版_2105110911513096194.json, 视频生成/图生视频/动作迁移服装变换4段变装 灵活分段图生视频处理工具_2113318737775521794.json, 视频生成/图生视频/四段变装分段灵活版｜动作迁移服装变换一气呵成｜图生视频_2113093151845085185.json, 视频生成/图生视频/换衣动作迁移抖X特效｜图生视频换装方案直出_2091274631566151682.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_177

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/动作迁移实测演示｜图生视频人物动作复刻测试版_2105110911513096194.json、视频生成/图生视频/动作迁移服装变换4段变装 灵活分段图生视频处理工具_2113318737775521794.json、视频生成/图生视频/四段变装分段灵活版｜动作迁移服装变换一气呵成｜图生视频_2113093151845085185.json、视频生成/图生视频/换衣动作迁移抖X特效｜图生视频换装方案直出_2091274631566151682.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DrawViTPose`
- `EmptyLatentImage`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Float` —— 3/4 个有
- `GetImageSizeAndCount` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `BatchCount+` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/4 个有
- `GoohaiUniversalSlider` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RepeatImageBatch` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有
- `WanVideoContextOptions` —— 1/4 个有
- `WujiCleaner` —— 1/4 个有
- `WujiUpscaler` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy mathInt` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（9/4 个样本）：Steps较低可能导致细节不足
