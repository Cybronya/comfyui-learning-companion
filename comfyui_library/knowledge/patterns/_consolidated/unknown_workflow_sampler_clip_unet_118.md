---
name: unknown_workflow_sampler_clip_unet_118
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.862111
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, KSamplerSelect, LoadImage, MaskToSEGS, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SEGSPreview, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/CK-卡通3D盲盒手办玩具摆件_1919664617679949825.json, 图片生成/图生图/全能图片G-4o风格丨全网爆火人物转拍立得_1915015916936200193.json, 图片生成/图生图/卡通3D手办玩具摆件_1921883212824395777.json, 图片生成/图生图/卡通3D收藏娃娃_1937704786118774785.json, 图片生成/图生图/卡通可爱四格漫画生成工作流｜一键生图系列_1909904998782959617.json, 图片生成/图生图/参考图生成卡通可爱四宫格漫画_1918124542395617281.json, 图片生成/图生图/拍立得照片卡通形象_1912392096207306754.json, 图片生成/图生图/拍立得照片卡通形象_1913231363498278913.json, 图片生成/图生图/真人转剪纸艺术工作流_1895381354098065410.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_118

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/CK-卡通3D盲盒手办玩具摆件_1919664617679949825.json、图片生成/图生图/全能图片G-4o风格丨全网爆火人物转拍立得_1915015916936200193.json、图片生成/图生图/卡通3D手办玩具摆件_1921883212824395777.json、图片生成/图生图/卡通3D收藏娃娃_1937704786118774785.json、图片生成/图生图/卡通可爱四格漫画生成工作流｜一键生图系列_1909904998782959617.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `MaskToSEGS`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SEGSPreview`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 8/9 个有
- `ShowText|pysssss` —— 8/9 个有
- `easy cleanGpuUsed` —— 8/9 个有
- `FluxResolutionNode` —— 7/9 个有
- `JjkText` —— 7/9 个有
- `LoraLoader` —— 7/9 个有
- `TextCombinerTwo` —— 7/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `ApplyFBCacheOnModel` —— 2/9 个有
- `ImageResizeKJ` —— 2/9 个有
- `ApplyFluxControlNet` —— 1/9 个有
- `BaiduTranslateNode` —— 1/9 个有
- `CR Text Concatenate` —— 1/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `ETN_Translate` —— 1/9 个有
- `HEDPreprocessor` —— 1/9 个有
- `HfImageToRGB` —— 1/9 个有
- `Image Levels Adjustment` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `LoadFluxControlNet` —— 1/9 个有
- `MaskPreview+` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `PMRF` —— 1/9 个有
- `VAEEncode` —— 1/9 个有
- `XlabsSampler` —— 1/9 个有
- `easy imageRemBg` —— 1/9 个有
- `easy positive` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 9 | 87% |
| 高度 | 1024 | 1024 - 1024 | 9 | 100% |
| LoRA 模型强度 | 0.85 | 0.7 - 1 | 7 | 86% |
| LoRA 文本强度 | 0.8 | 0.7 - 1 | 7 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，9 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.85，观测区间 0.7 - 1，7 个样本，取值集中（一致性 86%）
- LoRA 文本强度 中位数 0.8，观测区间 0.7 - 1，7 个样本，取值集中（一致性 85%）
