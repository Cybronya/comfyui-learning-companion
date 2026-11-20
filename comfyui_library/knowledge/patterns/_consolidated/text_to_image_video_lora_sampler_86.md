---
name: text_to_image_video_lora_sampler_86
type: Text To Image
frequency: 10
level: strong
coverage: 0.6555
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, EmptyLatentImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageFromBatch, ImageResizeKJ, ImpactSwitch, JjkText, KSampler, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, PreviewImage, Primitive integer [Crystools], RHHiddenNodes, RH_Captioner, SetNode, ShowText|pysssss, SimpleMath+, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/30秒整条视频一键复刻｜Wan2.2动作迁移真实度拉满图生视频_2092135573669629954.json, 视频生成/图生视频/Wan2.2动作迁移30s复刻｜整条视频一键操作真实度拉满_2089492438435065857.json, 视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2089707963748540418.json, 视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2092133210959466497.json, 视频生成/图生视频/Wan2.2动作迁移单次复刻30s｜整条视频一键真实度拉满_2095127512291565569.json, 视频生成/图生视频/Wan2.2单次复刻30秒时长｜动作迁移整条视频一键真实度拉满_2092005020848971778.json, 视频生成/图生视频/wan2.2动作迁移打造真实感视频 真人级动作复刻效果_2094816106904113154.json, 视频生成/图生视频/真实度拉满动作迁移：整条视频一键操作时长！Wan2.230s单次复刻_2087304945753214978.json, 视频生成/图生视频/真实感动作迁移｜wan2.2图生视频一键生成_2092165775426674689.json, 视频生成/文生视频/V2视频换背景｜文生视频视频生视频替换生成_2092171934913097729.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_86

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/30秒整条视频一键复刻｜Wan2.2动作迁移真实度拉满图生视频_2092135573669629954.json、视频生成/图生视频/Wan2.2动作迁移30s复刻｜整条视频一键操作真实度拉满_2089492438435065857.json、视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2089707963748540418.json、视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2092133210959466497.json、视频生成/图生视频/Wan2.2动作迁移单次复刻30s｜整条视频一键真实度拉满_2095127512291565569.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJ`
- `ImpactSwitch`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_Captioner`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ControlNextGetPoses` —— 9/10 个有
- `ImageResizeKJv2` —— 9/10 个有
- `Int` —— 9/10 个有
- `Primitive float [Crystools]` —— 9/10 个有
- `VHS_VideoInfoLoaded` —— 9/10 个有
- `WanVideoBlockSwap` —— 9/10 个有
- `WanVideoControlEmbeds` —— 9/10 个有
- `WanVideoEncode` —— 9/10 个有
- `WanVideoImageToVideoEncode` —— 9/10 个有
- `WanVideoSetLoRAs` —— 9/10 个有
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `GetImageRangeFromBatch` —— 7/10 个有
- `ImageBatchMulti` —— 7/10 个有
- `RepeatImageBatch` —— 7/10 个有
- `easy forLoopEnd` —— 7/10 个有
- `easy forLoopStart` —— 7/10 个有
- `easy showAnything` —— 7/10 个有
- `WanVideoSetBlockSwap` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `LayerUtility: ImageBlend` —— 1/10 个有
- `WanVideoEnhanceAVideo` —— 1/10 个有
- `WanVideoExperimentalArgs` —— 1/10 个有
- `WanVideoVACEEncode` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
