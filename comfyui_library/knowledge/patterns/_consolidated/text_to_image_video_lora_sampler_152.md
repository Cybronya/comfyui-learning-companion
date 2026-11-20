---
name: text_to_image_video_lora_sampler_152
type: Text To Image
frequency: 5
level: strong
coverage: 0.6564
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DrawMaskOnImage, EmptyLatentImage, GetImageSizeAndCount, GetNode, GrowMask, INTConstant, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PointsEditor, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/二创首选Wan2.2 Animate视频生视频 人物精准替换高质量方案_2089318031020355585.json, 视频生成/图生视频/Wan Animate 视频换脸动作迁移｜唱歌跳舞一键复刻_2096911442065838082.json, 视频生成/图生视频/Wan Animate动作迁移工作流｜视频换脸视频生视频，动作还原到位_2104530684848201730.json, 视频生成/图生视频/Wan2.2 Animate精准人物替换｜动作迁移图生视频二创首选_2089384431193776129.json, 视频生成/图生视频/视频换脸动作迁移工作流｜WanAnimate唱歌跳舞生成_2096709392270970881.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_152

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/二创首选Wan2.2 Animate视频生视频 人物精准替换高质量方案_2089318031020355585.json、视频生成/图生视频/Wan Animate 视频换脸动作迁移｜唱歌跳舞一键复刻_2096911442065838082.json、视频生成/图生视频/Wan Animate动作迁移工作流｜视频换脸视频生视频，动作还原到位_2104530684848201730.json、视频生成/图生视频/Wan2.2 Animate精准人物替换｜动作迁移图生视频二创首选_2089384431193776129.json、视频生成/图生视频/视频换脸动作迁移工作流｜WanAnimate唱歌跳舞生成_2096709392270970881.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PointsEditor`
- `SetNode`
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
- `DWPreprocessor` —— 3/5 个有
- `DownloadAndLoadSAM2Model` —— 3/5 个有
- `FaceMaskFromPoseKeypoints` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `ImageCropByMaskAndResize` —— 3/5 个有
- `PixelPerfectResolution` —— 3/5 个有
- `Sam2Segmentation` —— 3/5 个有
- `WanVideoContextOptions` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `DrawViTPose` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `ImageFromBatch+` —— 2/5 个有
- `InvertMask` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: ImageBlend` —— 2/5 个有
- `MaskToImage` —— 2/5 个有
- `OnnxDetectionModelLoader` —— 2/5 个有
- `PoseAndFaceDetection` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SeCModelLoader` —— 2/5 个有
- `SeCVideoSegmentation` —— 2/5 个有
- `VHS_VideoInfo` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
