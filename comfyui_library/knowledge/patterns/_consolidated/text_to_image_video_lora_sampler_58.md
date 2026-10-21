---
name: text_to_image_video_lora_sampler_58
type: Text To Image
frequency: 12
level: strong
coverage: 0.946583
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, Compare, DWPreprocessor, EmptyLatentImage, FaceMaskFromPoseKeypoints, INTConstant, If ANY execute A else B, ImageFromBatch, ImageResizeKJv2, JjkText, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PixelPerfectResolution, PoseAndFaceDetection, Primitive integer [Crystools], RHHiddenNodes, RH_Captioner, ShowText|pysssss, SimpleMath+, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoVAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/不限时长动作迁移PLUS｜面部表情身材优化图生视频_2095505487574953985.json, 视频生成/图生视频/动作迁移PLUS不限时长｜动作面部表情身材优化_2095235508216619010.json, 视频生成/图生视频/爆款复刻三合一｜角色替换+动作迁移+面部表情图生视频_2092558999911755778.json, 视频生成/图生视频/爆款复刻面部表情动作迁移角色替换 视频生视频动作迁移排版优化_2094020897270231042.json, 视频生成/图生视频/爆款复刻面部表情动作迁移角色替换 视频生视频动作迁移排版优化_2097100031206707202.json, 视频生成/图生视频/爆款视频复刻公式 面部表情自然的角色替换加动作迁移（排版优化）_2095068461927059458.json, 视频生成/图生视频/爆款视频复刻公式 面部表情自然的角色替换加动作迁移（排版优化）_2106524735935967234.json, 视频生成/图生视频/角色替换加动作迁移加面部表情 爆款视频复刻工具_2099210651427237889.json, 视频生成/图生视频/角色替换加动作迁移加面部表情 爆款视频复刻工具_2099589829465042946.json, 视频生成/图生视频/角色替换动作迁移面部表情三件套｜爆款视频一键复刻，节点全解密_2099484578393190402.json, 视频生成/图生视频/角色替换动作迁移面部表情｜爆款复刻排版优化可解密_2092324804513845250.json, 视频生成/图生视频/面部表情动作迁移角色替换｜爆款复刻视频生视频方案_2093761798544642049.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_58

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/不限时长动作迁移PLUS｜面部表情身材优化图生视频_2095505487574953985.json、视频生成/图生视频/动作迁移PLUS不限时长｜动作面部表情身材优化_2095235508216619010.json、视频生成/图生视频/爆款复刻三合一｜角色替换+动作迁移+面部表情图生视频_2092558999911755778.json、视频生成/图生视频/爆款复刻面部表情动作迁移角色替换 视频生视频动作迁移排版优化_2094020897270231042.json、视频生成/图生视频/爆款复刻面部表情动作迁移角色替换 视频生视频动作迁移排版优化_2097100031206707202.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `Compare`
- `DWPreprocessor`
- `EmptyLatentImage`
- `FaceMaskFromPoseKeypoints`
- `INTConstant`
- `If ANY execute A else B`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PixelPerfectResolution`
- `PoseAndFaceDetection`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_Captioner`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
