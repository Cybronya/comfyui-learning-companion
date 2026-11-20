---
name: text_to_image_video_lora_sampler_21
type: Text To Image
frequency: 25
level: strong
coverage: 0.85136
common_nodes: [ApplySageAttention, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, EmptyLatentImage, EnhancedLoadDiffusionModel, GetNode, JWInteger, JjkText, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PatchModelPatcherOrder, PreviewImage, PromptRelaySmartEncode, SetNode, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/三号分镜神器｜漫剧图生视频连续镜头轻松搞定_2096523046709452802.json, 视频生成/图生视频/提示词精准控制漫剧画面｜本地开源免费图生视频_2096207799368900609.json, 视频生成/图生视频/本地开源免费真人运镜长镜头4｜图生视频实拍运镜_2089742978712686594.json, 视频生成/图生视频/本地开源免费第4版｜真人运镜长镜头图生视频流畅顺滑_2101496411501191169.json, 视频生成/图生视频/漫剧分镜视频3代升级｜图生视频分镜更连贯，漫剧成片节奏直接起飞_2100434887214977025.json, 视频生成/图生视频/漫剧分镜视频3｜图生视频角色一致性一键生成分镜出图_2092561745666727937.json, 视频生成/图生视频/漫剧分镜视频5号版本｜图生视频画面更稳，长篇漫剧分镜一次拉满_2100436582313582593.json, 视频生成/图生视频/漫剧分镜视频5｜图生视频角色一致性一键生成分镜出图_2092563202113630209.json, 视频生成/图生视频/漫剧分镜视频生成3｜参考图或视频输入总帧数图生视频_2088741080157212674.json, 视频生成/图生视频/漫剧分镜视频生成3｜角色一致图生视频直出_2092326183810715650.json, 视频生成/图生视频/漫剧分镜视频生成5｜参考图视频加帧数设置图生视频_2088742647476342786.json, 视频生成/图生视频/漫剧分镜视频生成5｜角色一致图生视频直出_2092327671568093185.json, 视频生成/图生视频/漫剧创作提速｜五号分镜视频工作流图生视频稳定出片_2096521433223622658.json, 视频生成/图生视频/漫剧提示词精准控制本地开源免费图生视频工作流_2088362781291663361.json, 视频生成/图生视频/漫剧提示词精准控制本地开源免费｜图生视频工作流_2088330265683906562.json, 视频生成/图生视频/漫剧提示词精准控制｜本地免费开源图生视频_2092570779249635329.json, 视频生成/图生视频/真人运镜长镜头4｜本地开源免费不限次随便跑_2097182147487555586.json, 视频生成/图生视频/真人运镜长镜头4｜本地开源免费图生视频一键生成_2093745920608391170.json, 视频生成/图生视频/真人运镜长镜头9｜本地开源免费图生视频一键生成_2093750131110801409.json, 视频生成/图生视频/真人运镜长镜头9｜本地开源白嫖电影感运镜_2097186782122176513.json, 视频生成/图生视频/真人运镜长镜头本地开源免费｜图生视频高质量生成_2097033306788425729.json, 视频生成/图生视频/真人运镜长镜头第九弹｜本地开源免费图生视频_2101130149273104386.json, 视频生成/图生视频/真人运镜长镜头视频｜本地开源免费一键生成_2089292246733647874.json, 视频生成/图生视频/真人运镜长镜头视频｜本地开源免费图生图直出_2093420074748178434.json, 视频生成/图生视频/真人运镜长镜头｜本地开源免费图生视频一键生成_2089449051279421442.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/三号分镜神器｜漫剧图生视频连续镜头轻松搞定_2096523046709452802.json、视频生成/图生视频/提示词精准控制漫剧画面｜本地开源免费图生视频_2096207799368900609.json、视频生成/图生视频/本地开源免费真人运镜长镜头4｜图生视频实拍运镜_2089742978712686594.json、视频生成/图生视频/本地开源免费第4版｜真人运镜长镜头图生视频流畅顺滑_2101496411501191169.json、视频生成/图生视频/漫剧分镜视频3代升级｜图生视频分镜更连贯，漫剧成片节奏直接起飞_2100434887214977025.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 25 个 workflow 都包含：
- `ApplySageAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `GetNode`
- `JWInteger`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `PreviewImage`
- `PromptRelaySmartEncode`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageBatchExtendWithOverlap` —— 21/25 个有
- `LayerUtility: PurgeVRAM V2` —— 21/25 个有
- `easy indexAnything` —— 21/25 个有
- `easy mathInt` —— 21/25 个有
- `ColorMatchV2` —— 17/25 个有
- `Switch` —— 16/25 个有
- `PreviewAny` —— 14/25 个有
- `RegexExtract` —— 14/25 个有
- `StringReplace` —— 14/25 个有
- `RHLLMChatNode` —— 10/25 个有
- `TextConcatenate_UTK` —— 10/25 个有
- `TextSplitJoinByDelimiter` —— 10/25 个有
- `easy showAnything` —— 10/25 个有
- `FlashVSR_SM_KSampler` —— 9/25 个有
- `FlashVSR_SM_Model` —— 9/25 个有
- `GetImageRangeFromBatch` —— 9/25 个有
- `GetImageSize` —— 9/25 个有
- `BatchThief` —— 4/25 个有
- `RH_Captioner` —— 4/25 个有
- `SaveImage` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高发问题（25/25 个样本）：Steps较低可能导致细节不足
