---
name: text_to_image_video_lora_sampler_60
type: Text To Image
frequency: 13
level: strong
coverage: 0.889154
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadNLFModel, EmptyLatentImage, INTConstant, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SCAIL大模型AI跳舞视频｜一键图生多人同框共舞_2105265908217376769.json, 视频生成/图生视频/SCAIL大模型一键图生AI跳舞视频 支持多人同时跳舞_2105372386395774978.json, 视频生成/图生视频/Scail一键跳舞骨骼驱动 完美动作迁移再加持动态增强_2096738198734065666.json, 视频生成/图生视频/emergency本地开源免费｜图生视频生成_2091759724470562818.json, 视频生成/图生视频/emergency紧急视频生成｜本地开源免费图生视频_2095550055485886465.json, 视频生成/图生视频/倒车请注意梗图｜本地开源免费图生视频生成_2093748735774912514.json, 视频生成/图生视频/倒车请注意梗视频｜本地开源免费图生视频创意生成_2089451915041136641.json, 视频生成/图生视频/倒车请注意魔性视频｜本地开源免费直接生成_2097185171849170946.json, 视频生成/图生视频/本地开源免费emergency流｜不花RH币也能跑，图生视频白嫖党福音_2099434348230569985.json, 视频生成/图生视频/本地开源免费emergency｜图生视频应急方案零成本_2106978438421770242.json, 视频生成/图生视频/本地开源免费倒车请注意｜图生视频趣味生成_2089745826905157633.json, 视频生成/图生视频/本地开源免费图生视频｜emergency视频生成工作流_2088169414763040769.json, 视频生成/图生视频/本地开源免费趣味款｜倒车请注意魔性图生视频整活_2101499634844790785.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_60

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/SCAIL大模型AI跳舞视频｜一键图生多人同框共舞_2105265908217376769.json、视频生成/图生视频/SCAIL大模型一键图生AI跳舞视频 支持多人同时跳舞_2105372386395774978.json、视频生成/图生视频/Scail一键跳舞骨骼驱动 完美动作迁移再加持动态增强_2096738198734065666.json、视频生成/图生视频/emergency本地开源免费｜图生视频生成_2091759724470562818.json、视频生成/图生视频/emergency紧急视频生成｜本地开源免费图生视频_2095550055485886465.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `EmptyLatentImage`
- `INTConstant`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 11/13 个有
- `PreviewImage` —— 11/13 个有
- `SimpleMath+` —— 11/13 个有
- `WanVideoTextEncode` —— 11/13 个有
- `FlashVSR_SM_KSampler` —— 10/13 个有
- `FlashVSR_SM_Model` —— 10/13 个有
- `GetImageRangeFromBatch` —— 10/13 个有
- `GetImageSize` —— 10/13 个有
- `JWInteger` —— 10/13 个有
- `LayerUtility: PurgeVRAM V2` —— 10/13 个有
- `easy indexAnything` —— 10/13 个有
- `FloatConstant` —— 3/13 个有
- `GetImageSizeAndCount` —— 3/13 个有
- `ImageConcatMulti` —— 3/13 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 2/13 个有
- `DWPreprocessor` —— 2/13 个有
- `GetNode` —— 2/13 个有
- `SetNode` —— 2/13 个有
- `SimpleCalculatorKJ` —— 2/13 个有
- `WanVideoEncode` —— 2/13 个有
- `WanVideoTextEncodeCached` —— 2/13 个有
- `WanVideoUni3C_ControlnetLoader` —— 2/13 个有
- `WanVideoUni3C_embeds` —— 2/13 个有
- `SaveImage` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
