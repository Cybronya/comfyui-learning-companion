---
name: text_to_image_ipadapter_upscale_lora_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.815
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DualCLIPLoader, EmptyLatentImage, Fast Groups Muter (rgthree), FluxGuidance, GetImageSize+, IPAdapterAdvanced, IPAdapterModelLoader, Image Comparer (rgthree), ImageResize, Joy_caption, Joy_caption_load, KSampler, KSamplerSelect, LoadImage, LoraLoader, MirroredImage, ModelSamplingFlux, PrepImageForClipVision, PreviewImage, RH_Captioner, RandomNoise, SDXLPromptStyler, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/场景风格复制（XL+FLUX+Krea）_2029029158524821506.json, 平台全量/场景风格复制（XL+FLUX Krea）_1867252676089069569.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/场景风格复制（XL+FLUX+Krea）_2029029158524821506.json、平台全量/场景风格复制（XL+FLUX Krea）_1867252676089069569.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `GetImageSize+`
- `IPAdapterAdvanced`
- `IPAdapterModelLoader`
- `Image Comparer (rgthree)`
- `ImageResize`
- `Joy_caption`
- `Joy_caption_load`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `MirroredImage`
- `ModelSamplingFlux`
- `PrepImageForClipVision`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SDXLPromptStyler`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.2 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
