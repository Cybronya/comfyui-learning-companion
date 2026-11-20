---
name: text_to_image_controlnet_ipadapter_lora_3
type: Text To Image
frequency: 2
level: weak
coverage: 0.633
common_nodes: [ACN_ControlNet++LoaderSingle, AV_ControlNetPreprocessor, AV_IPAdapter, Anything Everywhere, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, EmptyLatentImage, GetImageSize+, GetNode, ImageBatch, ImageResize+, InvertMask, KSampler, Label (rgthree), LayerUtility: ColorImage, LayerUtility: ColorPicker, LayerUtility: ImageBlendAdvance V2, LoadImage, LoraLoader, PreviewImage, Prompts Everywhere, RH_Captioner, SaveImage, Seed Generator, SetNode, ShowText|pysssss, TextCombinerTwo, Textbox, VAEDecode, easy cleanGpuUsed, easy promptReplace]
problems: []
missing: []
members: [图片生成/图生图/万圣节COS妆容丨FLUX模型_1912348390825390082.json, 平台全量/万圣节主题-皮克斯风格头像_1849723620435128322.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_lora_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/万圣节COS妆容丨FLUX模型_1912348390825390082.json、平台全量/万圣节主题-皮克斯风格头像_1849723620435128322.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_ControlNet++LoaderSingle`
- `AV_ControlNetPreprocessor`
- `AV_IPAdapter`
- `Anything Everywhere`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `EmptyLatentImage`
- `GetImageSize+`
- `GetNode`
- `ImageBatch`
- `ImageResize+`
- `InvertMask`
- `KSampler`
- `Label (rgthree)`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageBlendAdvance V2`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `Prompts Everywhere`
- `RH_Captioner`
- `SaveImage`
- `Seed Generator`
- `SetNode`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `Textbox`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy promptReplace`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5.5 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| LoRA 模型强度 | 0.3 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
