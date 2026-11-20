---
name: text_to_image_video_lora_sampler_112
type: Text To Image
frequency: 7
level: strong
coverage: 0.750857
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, EmptyLatentImage, ImageFromBatch, ImageResizeKJv2, Int, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/四段变装分段灵活版｜动作迁移服装变换一气呵成｜图生视频_2113093151845085185.json, 视频生成/图生视频/图生视频｜xunxia口哨舞一键生成，单图也能跳出舞蹈视频_2099862238462042113.json, 视频生成/图生视频/换衣动作迁移抖X特效｜图生视频换装方案直出_2091274631566151682.json, 视频生成/图生视频/服装变换动作迁移4段变装 灵活分段视频生成处理工具_2113501434972033025.json, 视频生成/图生视频/高仿动作迁移图生视频 高显存动作复刻处理生成工具_2112996489915101186.json, 视频生成/图生视频/高仿动作迁移模仿生成｜风格迁移图生视频直出_2091662335898374145.json, 视频生成/图生视频/高仿动作迁移高显存｜风格迁移图生视频直出_2091645260790325249.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/四段变装分段灵活版｜动作迁移服装变换一气呵成｜图生视频_2113093151845085185.json、视频生成/图生视频/图生视频｜xunxia口哨舞一键生成，单图也能跳出舞蹈视频_2099862238462042113.json、视频生成/图生视频/换衣动作迁移抖X特效｜图生视频换装方案直出_2091274631566151682.json、视频生成/图生视频/服装变换动作迁移4段变装 灵活分段视频生成处理工具_2113501434972033025.json、视频生成/图生视频/高仿动作迁移图生视频 高显存动作复刻处理生成工具_2112996489915101186.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `EmptyLatentImage`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
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
- `DrawViTPose` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `ImageBatch` —— 6/7 个有
- `MemoryCleaner` —— 6/7 个有
- `OnnxDetectionModelLoader` —— 6/7 个有
- `PoseAndFaceDetection` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `WanVideoLoraSelect` —— 6/7 个有
- `WanVideoContextOptions` —— 5/7 个有
- `easy cleanGpuUsed` —— 5/7 个有
- `BatchCount+` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `RepeatImageBatch` —— 4/7 个有
- `VHS_VideoInfo` —— 4/7 个有
- `easy float` —— 4/7 个有
- `easy mathInt` —— 4/7 个有
- `Float` —— 3/7 个有
- `RHHiddenNodes` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `VRAMReserver` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `GetImageSizeAndCount` —— 2/7 个有
- `ComfyMathExpression` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `GoohaiUniversalSlider` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
