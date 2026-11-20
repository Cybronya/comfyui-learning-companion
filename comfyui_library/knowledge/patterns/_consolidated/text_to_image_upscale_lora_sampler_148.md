---
name: text_to_image_upscale_lora_sampler_148
type: Text To Image
frequency: 2
level: weak
coverage: 0.8475
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Crop Face, DF_Text_Box, EmptyLatentImage, ImageResize+, ImageUpscaleWithModel, KSampler, Load RetinaFace, LoadImage, LoraLoader, PrepImageForClipVision, SaveImage, ShowText|pysssss, Text Concatenate, Upscale Model Loader, VAEDecode, VAEEncode, WD14Tagger|pysssss]
problems: []
missing: []
members: [平台全量/人像新年卡通表情包_1778057031194841090.json, 平台全量/动漫写实人像_1784880582598078466.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_148

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/人像新年卡通表情包_1778057031194841090.json、平台全量/动漫写实人像_1784880582598078466.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Crop Face`
- `DF_Text_Box`
- `EmptyLatentImage`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `KSampler`
- `Load RetinaFace`
- `LoadImage`
- `LoraLoader`
- `PrepImageForClipVision`
- `SaveImage`
- `ShowText|pysssss`
- `Text Concatenate`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEEncode`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `Display Int (rgthree)` —— 1/2 个有
- `IPAdapter` —— 1/2 个有
- `IPAdapterFaceID` —— 1/2 个有
- `IPAdapterModelLoader` —— 1/2 个有
- `IPAdapterUnifiedLoader` —— 1/2 个有
- `IPAdapterUnifiedLoaderFaceID` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `ImageMaskSwitch` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RandomInt` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 640 | - | 2 | 100% |
| 高度 | 704 | - | 2 | 91% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 640，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 704，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
