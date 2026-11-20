---
name: image_to_image_controlnet_ipadapter_upscale_2
type: Image To Image
frequency: 2
level: weak
coverage: 0.7375
common_nodes: [CLIPTextEncode, CLIPVisionLoader, Canny, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, DeepTranslatorTextNode, Fast Bypasser (rgthree), IPAdapterAdvanced, IPAdapterModelLoader, KSampler, LatentUpscaleBy, LineArtPreprocessor, LoadImage, LoraLoader, M-LSDPreprocessor, Mute / Bypass Repeater (rgthree), PreviewImage, SaveImage, StringFunction|pysssss, Text Concatenate (JPS), VAEDecode, VAEEncode, Zoe-DepthMapPreprocessor, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/SD1.5 图生图_1868267213772718082.json, 图片生成/图生图/SDXL 图生图_1868284691441926146.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_upscale_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SD1.5 图生图_1868267213772718082.json、图片生成/图生图/SDXL 图生图_1868284691441926146.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `Canny`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `DeepTranslatorTextNode`
- `Fast Bypasser (rgthree)`
- `IPAdapterAdvanced`
- `IPAdapterModelLoader`
- `KSampler`
- `LatentUpscaleBy`
- `LineArtPreprocessor`
- `LoadImage`
- `LoraLoader`
- `M-LSDPreprocessor`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `SaveImage`
- `StringFunction|pysssss`
- `Text Concatenate (JPS)`
- `VAEDecode`
- `VAEEncode`
- `Zoe-DepthMapPreprocessor`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
