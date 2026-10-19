---
name: text_to_image_video_lora_sampler_120
type: Text To Image
frequency: 6
level: strong
coverage: 0.8865
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DrawViTPose, EmptyLatentImage, ImageBatch, ImageFromBatch, ImageResizeKJv2, Int, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MemoryCleaner, OnnxDetectionModelLoader, PoseAndFaceDetection, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/动作迁移实测演示｜图生视频人物动作复刻测试版_2105110911513096194.json, 视频生成/图生视频/口哨舞动作迁移工作流，视频换脸动作迁移图生视频处理工具_2107540897608069122.json, 视频生成/图生视频/口哨舞动作迁移｜跟着节奏吹口哨跳舞，视频换脸动作两合一_2107349970042056706.json, 视频生成/图生视频/口哨舞手势舞换衣加动作迁移加抖X加最长30秒工作流，动作迁移图生视频_2107542399965810689.json, 视频生成/图生视频/口哨舞手势舞换衣动作迁移抖X版｜最长30秒，换装跳舞一气呵成_2107356106170392577.json, 视频生成/图生视频/换衣动作迁移抖X特效｜图生视频换装方案直出_2091274631566151682.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_120

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/动作迁移实测演示｜图生视频人物动作复刻测试版_2105110911513096194.json、视频生成/图生视频/口哨舞动作迁移工作流，视频换脸动作迁移图生视频处理工具_2107540897608069122.json、视频生成/图生视频/口哨舞动作迁移｜跟着节奏吹口哨跳舞，视频换脸动作两合一_2107349970042056706.json、视频生成/图生视频/口哨舞手势舞换衣加动作迁移加抖X加最长30秒工作流，动作迁移图生视频_2107542399965810689.json、视频生成/图生视频/口哨舞手势舞换衣动作迁移抖X版｜最长30秒，换装跳舞一气呵成_2107356106170392577.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
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
- `BatchCount+` —— 5/6 个有
- `ComfyMathExpression` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `RepeatImageBatch` —— 5/6 个有
- `VHS_VideoInfo` —— 5/6 个有
- `WanVideoContextOptions` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `easy mathInt` —— 5/6 个有
- `SaveImage` —— 4/6 个有
- `easy float` —— 4/6 个有
- `easy int` —— 4/6 个有
- `Fast Groups Muter (rgthree)` —— 3/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `CropWithPadInfo` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `QwenEditConfigPreparer` —— 2/6 个有
- `QwenEditOutputExtractor` —— 2/6 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 2/6 个有
- `easy imageRemBg` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Float` —— 1/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `GoohaiUniversalSlider` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `TextEncodeQwenImageEditPlus` —— 1/6 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/6 个有
- `WujiCleaner` —— 1/6 个有
- `WujiUpscaler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（13/6 个样本）：Steps较低可能导致细节不足
