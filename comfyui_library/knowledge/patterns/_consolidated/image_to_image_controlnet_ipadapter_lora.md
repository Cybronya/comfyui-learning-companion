---
name: image_to_image_controlnet_ipadapter_lora
type: Image To Image
frequency: 6
level: strong
coverage: 0.634167
common_nodes: [AIO_Preprocessor, Anything Everywhere, CLIPTextEncode, CLIPVisionLoader, CR Text Concatenate, CheckpointLoader|pysssss, ControlNetApplySD3, ControlNetLoader, GetNode, IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, Image Comparer (rgthree), KSampler, LayerColor: BrightnessContrastV2, LayerUtility: ImageBlend, LoadImage, LoraLoader|pysssss, PreviewImage, RH_Captioner, SaveImage, SetNode, ShowText|pysssss, StringConstantMultiline, VAEDecode, VAEEncode, easy imageColorMatch, easy imageScaleDownToSize]
problems: []
missing: []
members: [图片生成/图生图/【海皮】专用智能追色 V2_2010281346983272449.json, 图片生成/图生图/图像追色强化版-色彩极致还原_1920159218366611458.json, 图片生成/图生图/图片色调氛围复刻_1926615965742604290.json, 图片生成/图生图/打光参考｜图像追色强化版_1920293951952326658.json, 图片生成/图生图/色调氛围复刻_2064614362664497154.json, 平台全量/图像追色-参考调色_1939325807707791362.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_lora

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【海皮】专用智能追色 V2_2010281346983272449.json、图片生成/图生图/图像追色强化版-色彩极致还原_1920159218366611458.json、图片生成/图生图/图片色调氛围复刻_1926615965742604290.json、图片生成/图生图/打光参考｜图像追色强化版_1920293951952326658.json、图片生成/图生图/色调氛围复刻_2064614362664497154.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 6 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text Concatenate`
- `CheckpointLoader|pysssss`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `GetNode`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerColor: BrightnessContrastV2`
- `LayerUtility: ImageBlend`
- `LoadImage`
- `LoraLoader|pysssss`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `StringConstantMultiline`
- `VAEDecode`
- `VAEEncode`
- `easy imageColorMatch`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `InvertMask` —— 5/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 6 | 100% |
| LoRA 模型强度 | 0.65 | 0.5 - 0.65 | 6 | 88% |
| LoRA 文本强度 | 1 | 0.5 - 1 | 6 | 72% |
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 6 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 6 | 100% |
| 调度器 | sgm_uniform | - | 6 | 100% |
| 重绘幅度 | 1 | 0.61 - 1 | 6 | 84% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.65，观测区间 0.5 - 0.65，6 个样本，取值集中（一致性 88%）
- LoRA 文本强度 中位数 1，观测区间 0.5 - 1，6 个样本
- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，6 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.61 - 1，6 个样本，取值集中（一致性 84%）
