---
name: text_to_image_video_upscale_latent_upscale_24
type: Text To Image
frequency: 3
level: weak
coverage: 0.738
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX2.3 Edit Anything编辑万物｜视频任意元素替换修改，还能动作迁移_2099539066382540802.json, 视频生成/图生视频/LTX2.3-MSR-V2多图生视频_2083001091343601666.json, 视频生成/图生视频/2070813435004284929.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 Edit Anything编辑万物｜视频任意元素替换修改，还能动作迁移_2099539066382540802.json、视频生成/图生视频/LTX2.3-MSR-V2多图生视频_2083001091343601666.json、视频生成/图生视频/2070813435004284929.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `FrameInterpolate` —— 2/3 个有
- `FrameInterpolationModelLoader` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LTX2_NAG` —— 2/3 个有
- `LTXAddVideoICLoRAGuide` —— 2/3 个有
- `LTXICLoRALoaderModelOnly` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `LiconMSR` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `RTXVideoSuperResolution` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GPTImage2PromptPreview` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LTXVImgToVideoInplace` —— 1/3 个有
- `Preview from image [Crystools]` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RHLLMChatNode` —— 1/3 个有
- `RH_RhartImageG2ImageToImage` —— 1/3 个有
- `ResizeImagesByLongerEdge` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `easy imageSave` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1920 | 3 | 0% |
| 高度 | 80 | 80 - 1080 | 3 | 0% |
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1920，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1080，3 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
