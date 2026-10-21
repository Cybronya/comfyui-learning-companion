---
name: text_to_image_video_lora_sampler_175
type: Text To Image
frequency: 3
level: strong
coverage: 0.636667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, EmptyLatentImage, GetNode, ImageFromBatch, ImageResizeKJv2, Int, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy float, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生视频｜xunxia口哨舞一键生成，单图也能跳出舞蹈视频_2099862238462042113.json, 视频生成/图生视频/高仿动作迁移模仿生成｜风格迁移图生视频直出_2091662335898374145.json, 视频生成/图生视频/高仿动作迁移高显存｜风格迁移图生视频直出_2091645260790325249.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_175

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/图生视频｜xunxia口哨舞一键生成，单图也能跳出舞蹈视频_2099862238462042113.json、视频生成/图生视频/高仿动作迁移模仿生成｜风格迁移图生视频直出_2091662335898374145.json、视频生成/图生视频/高仿动作迁移高显存｜风格迁移图生视频直出_2091645260790325249.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `EmptyLatentImage`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy float`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 2/3 个有
- `DrawViTPose` —— 2/3 个有
- `ImageBatch` —— 2/3 个有
- `MemoryCleaner` —— 2/3 个有
- `OnnxDetectionModelLoader` —— 2/3 个有
- `PoseAndFaceDetection` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `RepeatImageBatch` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `VRAMReserver` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `easy mathInt` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Float` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
