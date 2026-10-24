---
name: text_to_image_video_lora_sampler_79
type: Text To Image
frequency: 9
level: strong
coverage: 0.636222
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, ControlNextGetPoses, EmptyLatentImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageFromBatch, ImageResizeKJ, ImageResizeKJv2, ImpactSwitch, Int, JjkText, KSampler, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, PreviewImage, Primitive float [Crystools], Primitive integer [Crystools], RHHiddenNodes, RH_Captioner, SetNode, ShowText|pysssss, SimpleMath+, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoSLG, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/30秒整条视频一键复刻｜Wan2.2动作迁移真实度拉满图生视频_2092135573669629954.json, 视频生成/图生视频/Wan2.2动作迁移30s复刻｜整条视频一键操作真实度拉满_2089492438435065857.json, 视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2089707963748540418.json, 视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2092133210959466497.json, 视频生成/图生视频/Wan2.2动作迁移单次复刻30s｜整条视频一键真实度拉满_2095127512291565569.json, 视频生成/图生视频/Wan2.2单次复刻30秒时长｜动作迁移整条视频一键真实度拉满_2092005020848971778.json, 视频生成/图生视频/wan2.2动作迁移打造真实感视频 真人级动作复刻效果_2094816106904113154.json, 视频生成/图生视频/真实度拉满动作迁移：整条视频一键操作时长！Wan2.230s单次复刻_2087304945753214978.json, 视频生成/图生视频/真实感动作迁移｜wan2.2图生视频一键生成_2092165775426674689.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/30秒整条视频一键复刻｜Wan2.2动作迁移真实度拉满图生视频_2092135573669629954.json、视频生成/图生视频/Wan2.2动作迁移30s复刻｜整条视频一键操作真实度拉满_2089492438435065857.json、视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2089707963748540418.json、视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2092133210959466497.json、视频生成/图生视频/Wan2.2动作迁移单次复刻30s｜整条视频一键真实度拉满_2095127512291565569.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ControlNextGetPoses`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `Int`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Primitive float [Crystools]`
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
- `VHS_VideoInfoLoaded`
- `WanVideoBlockSwap`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 7/9 个有
- `ImageBatchMulti` —— 7/9 个有
- `RepeatImageBatch` —— 7/9 个有
- `easy forLoopEnd` —— 7/9 个有
- `easy forLoopStart` —— 7/9 个有
- `easy showAnything` —— 7/9 个有
- `WanVideoSetBlockSwap` —— 2/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
