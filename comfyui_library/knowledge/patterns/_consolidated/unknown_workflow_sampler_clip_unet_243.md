---
name: unknown_workflow_sampler_clip_unet_243
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8664
common_nodes: [BasicScheduler, CLIPTextEncode, Image Comparer (rgthree), KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Kontext中文版提示词单图模式（开源版）_1938426067969314817.json, 图片生成/图生图/Kontext遮罩指哪打哪中文版提示词（开源版）_1939937892967817218.json, 图片生成/图生图/WAN2.2图像洗图放大（纯种WAN2.2）_1952371299358322690.json, 图片生成/图生图/即梦单图模式（1K放大版）_1968538127075815425.json, 图片生成/文生图/Kontext中文版提示词漫画转绘_1968667688585318402.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_243

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext中文版提示词单图模式（开源版）_1938426067969314817.json、图片生成/图生图/Kontext遮罩指哪打哪中文版提示词（开源版）_1939937892967817218.json、图片生成/图生图/WAN2.2图像洗图放大（纯种WAN2.2）_1952371299358322690.json、图片生成/图生图/即梦单图模式（1K放大版）_1968538127075815425.json、图片生成/文生图/Kontext中文版提示词漫画转绘_1968667688585318402.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 4/5 个有
- `CLIPLoader` —— 4/5 个有
- `DisableNoise` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `ModelSamplingSD3` —— 4/5 个有
- `RH_Captioner` —— 4/5 个有
- `SeedVR2` —— 4/5 个有
- `SplitSigmas` —— 4/5 个有
- `WanVideoNAG` —— 4/5 个有
- `BasicGuider` —— 3/5 个有
- `DualCLIPLoader` —— 3/5 个有
- `FluxGuidance` —— 3/5 个有
- `FluxKontextImageScale` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `ReferenceLatent` —— 3/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `MaskToImage` —— 1/5 个有
- `Mix Color By Mask` —— 1/5 个有
- `RH_Jimeng4_Image2Image` —— 1/5 个有
- `SDXLPromptStyler` —— 1/5 个有
- `UltimateSDUpscale` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
