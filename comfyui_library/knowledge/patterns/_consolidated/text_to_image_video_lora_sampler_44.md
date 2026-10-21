---
name: text_to_image_video_lora_sampler_44
type: Text To Image
frequency: 14
level: strong
coverage: 0.838286
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DrawViTPose, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, PreviewAny, PreviewImage, PromptRelayEncode, RH_Captioner, RegexExtract, SamplerCustom, SetNode, StringReplace, Text, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy mathInt, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX+Animate画质提升版图生视频处理工作流_2101352132011188225.json, 视频生成/图生视频/LTX+animate 画质增强版｜图生视频清晰度直线提升_2096820591998365697.json, 视频生成/图生视频/LTX+animate画质提升｜图生视频高清处理_2093237772462149633.json, 视频生成/图生视频/LTX+animate视频增强画质提升｜图生视频高清化_2089741659234988033.json, 视频生成/图生视频/LTX与animate画质提升｜图生视频清晰度增强处理_2096646919664783361.json, 视频生成/图生视频/带货视频制作｜电商服装展示图生视频一键搞定_2101123800619372545.json, 视频生成/图生视频/服装模特图生视频工作流｜商品展示动态视频生成_2097760030060793857.json, 视频生成/图生视频/电商服装带货专用｜图生视频一键批量生成制作_2093236473716895745.json, 视频生成/图生视频/电商服装带货展示视频图生视频处理生成工具包_2101354114839040002.json, 视频生成/图生视频/电商服装带货视频制作利器｜图生视频轻松出片_2096819064780967937.json, 视频生成/图生视频/电商服装带货视频制作｜图生视频商品展示生成_2096645546810372098.json, 视频生成/图生视频/电商服装带货视频生成｜图生视频一键直出成片_2089287871336370177.json, 视频生成/图生视频/画质提升实战｜LTX+animate动画增强图生视频一号_2101122305043812354.json, 视频生成/图生视频/画质提升｜LTX+animate 视频增强_2089289390064488449.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_44

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/LTX+Animate画质提升版图生视频处理工作流_2101352132011188225.json、视频生成/图生视频/LTX+animate 画质增强版｜图生视频清晰度直线提升_2096820591998365697.json、视频生成/图生视频/LTX+animate画质提升｜图生视频高清处理_2093237772462149633.json、视频生成/图生视频/LTX+animate视频增强画质提升｜图生视频高清化_2089741659234988033.json、视频生成/图生视频/LTX与animate画质提升｜图生视频清晰度增强处理_2096646919664783361.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DrawViTPose`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `PreviewAny`
- `PreviewImage`
- `PromptRelayEncode`
- `RH_Captioner`
- `RegexExtract`
- `SamplerCustom`
- `SetNode`
- `StringReplace`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy mathInt`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 3/14 个有
- `Int` —— 1/14 个有
- `LoadAudio` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（15/14 个样本）：Steps较低可能导致细节不足
