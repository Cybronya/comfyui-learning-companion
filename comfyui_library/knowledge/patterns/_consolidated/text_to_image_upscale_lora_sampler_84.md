---
name: text_to_image_upscale_lora_sampler_84
type: Text To Image
frequency: 3
level: strong
coverage: 0.803
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, Get Image Size, GetImageSize, GetImageSize+, GetNode, INTConstant, ImageResize+, ImageScale, ImageScaleBy, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewAny, QwenImage21Cache, RH_LLMAPI_NODE, SaveImage, SaveImageAdvanced, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy getNode, easy imageScaleToNormPixels, easy int, easy promptConcat, easy setNode, easy showAnything, easy textIndexSwitch, 孤海-浮点滑条, 数学运算_孤海]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen 2.1人像精修工作流 质感磨皮 去除痘痘 自动肤色 高清放大_2113914158981931009.json, 图片生成/图生图/Qwen_2.1人像精修工作流_质感磨皮_去除痘痘_自动肤色_高清放大_2115616877639716866.json, 图片生成/图生图/Qwen_2.1人像精修工作流_质感磨皮_去除痘痘_自动肤色_高清放大_2115664863556104193.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/Qwen 2.1人像精修工作流 质感磨皮 去除痘痘 自动肤色 高清放大_2113914158981931009.json、图片生成/图生图/Qwen_2.1人像精修工作流_质感磨皮_去除痘痘_自动肤色_高清放大_2115616877639716866.json、图片生成/图生图/Qwen_2.1人像精修工作流_质感磨皮_去除痘痘_自动肤色_高清放大_2115664863556104193.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Get Image Size`
- `GetImageSize`
- `GetImageSize+`
- `GetNode`
- `INTConstant`
- `ImageResize+`
- `ImageScale`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `QwenImage21Cache`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SaveImageAdvanced`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy getNode`
- `easy imageScaleToNormPixels`
- `easy int`
- `easy promptConcat`
- `easy setNode`
- `easy showAnything`
- `easy textIndexSwitch`
- `孤海-浮点滑条`
- `数学运算_孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | beta57 | - | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 beta57，3 个样本，一致性 100%
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
