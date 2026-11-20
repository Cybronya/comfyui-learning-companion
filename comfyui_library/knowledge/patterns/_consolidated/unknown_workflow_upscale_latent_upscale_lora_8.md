---
name: unknown_workflow_upscale_latent_upscale_lora_8
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.918167
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/LTX2.3图生视频_2042520558209863682.json, 视频生成/图生视频/LTX2.3图生视频_2043172438292303874.json, 视频生成/图生视频/LTX2.3图生视频_2043525547841556482.json, 视频生成/图生视频/LTX2.3图生视频_2045494998765936642.json, 视频生成/图生视频/LTX2.3图生视频_2046935031586758657.json, 视频生成/图生视频/LTX2.3图生视频_2047144762221797378.json, 视频生成/图生视频/LTX2.3图生视频_2047212324209041410.json, 视频生成/图生视频/LTX2.3图生视频_2048192241612623873.json, 视频生成/图生视频/LTX2.3图生视频_2060752593797869570.json, 视频生成/图生视频/LTX2.3图生视频_2062782781935149058.json, 视频生成/图生视频/LTX2.3图生视频_2070782899376451586.json, 视频生成/图生视频/LTX2.3图生视频_2072221135088996353.json, 视频生成/图生视频/LTX2.3图生视频加放大，可以选择要的清晰度_2035878269639200770.json, 视频生成/图生视频/LTX2.3图生视频支持宽高比高清视频_2029754649418403842.json, 视频生成/图生视频/LTX2.3图生视频竖屏短剧分镜11秒_2030782825120669698.json, 视频生成/图生视频/LTX2.3图生视频竖屏短剧分镜11秒_2030834724087799810.json, 视频生成/图生视频/LTX2.3图生视频竖屏短剧分镜11秒_2030844044808560641.json, 视频生成/图生视频/LTX2.3图生视频竖屏短剧分镜11秒_2040317987244220418.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_8

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/LTX2.3图生视频_2042520558209863682.json、视频生成/图生视频/LTX2.3图生视频_2043172438292303874.json、视频生成/图生视频/LTX2.3图生视频_2043525547841556482.json、视频生成/图生视频/LTX2.3图生视频_2045494998765936642.json、视频生成/图生视频/LTX2.3图生视频_2046935031586758657.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSampler`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 17/18 个有
- `GetImageSize` —— 17/18 个有
- `ImageScaleBy` —— 17/18 个有
- `PrimitiveInt` —— 17/18 个有
- `ResizeImagesByLongerEdge` —— 17/18 个有
- `VAEDecode` —— 17/18 个有
- `DualCLIPLoader` —— 16/18 个有
- `PreviewAny` —— 16/18 个有
- `TextGenerateLTX2Prompt` —— 16/18 个有
- `LoadImage` —— 15/18 个有
- `ResizeImageMaskNode` —— 14/18 个有
- `MathExpression|pysssss` —— 4/18 个有
- `ImageResizeKJv2` —— 3/18 个有
- `JWInteger` —— 3/18 个有
- `JjkText` —— 3/18 个有
- `String` —— 3/18 个有
- `LTX2_NAG` —— 2/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/18 个有
- `Load Image From Url (mtb)` —— 2/18 个有
- `PreviewImage` —— 2/18 个有
- `RH_Translator` —— 2/18 个有
- `CR Text` —— 1/18 个有
- `CR Text Concatenate` —— 1/18 个有
- `Int` —— 1/18 个有
- `IntToString` —— 1/18 个有
- `PreViewVideo` —— 1/18 个有
- `PrimitiveString` —— 1/18 个有
- `PrimitiveStringMultiline` —— 1/18 个有
- `RH_LLMAPI_NODE` —— 1/18 个有
- `RH_TopazlabsVideoUpscale` —— 1/18 个有
- `SDVN Load Image Url` —— 1/18 个有
- `StringReplace` —— 1/18 个有
- `Text` —— 1/18 个有
- `VAEDecodeTiled` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.4 | 18 | 97% |
| 宽度 | 97 | 97 - 241 | 18 | 69% |
| 高度 | 25 | 24 - 33 | 18 | 93% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/18 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.4，18 个样本，取值集中（一致性 97%）
- 宽度 中位数 97，观测区间 97 - 241，18 个样本
- 高度 中位数 25，观测区间 24 - 33，18 个样本，取值集中（一致性 93%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
