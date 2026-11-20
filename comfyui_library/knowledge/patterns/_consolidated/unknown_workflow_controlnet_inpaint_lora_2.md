---
name: unknown_workflow_controlnet_inpaint_lora_2
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7172
common_nodes: [BasicScheduler, BiRefNet_Hugo, CFGGuider, CLIPTextEncode, CLIPTextEncodeFlux, ControlNetInpaintingAliMamaApply, ControlNetLoader, DualCLIPLoader, FluxGuidance, ImageCrop+, ImageResize+, JjkText, KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingFlux, PreviewImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, ShowText|pysssss, TextCombinerSix, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/logo迁移到物品上之flux_1909564150056714242.json, 图片生成/图生图/珠宝首饰AI模特展示_2020751487340650498.json, 图片生成/图生图/饰品项链到AI模特展示_2016329762465128449.json, 图片生成/图生图/首饰生成模特海报 一键生图系列_1909074737446662146.json, 图片生成/文生图/饰品项链到AI模特展示_1939508745355575297.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/logo迁移到物品上之flux_1909564150056714242.json、图片生成/图生图/珠宝首饰AI模特展示_2020751487340650498.json、图片生成/图生图/饰品项链到AI模特展示_2016329762465128449.json、图片生成/图生图/首饰生成模特海报 一键生图系列_1909074737446662146.json、图片生成/文生图/饰品项链到AI模特展示_1939508745355575297.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `BiRefNet_Hugo`
- `CFGGuider`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageCrop+`
- `ImageResize+`
- `JjkText`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingFlux`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `TextCombinerSix`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 4/5 个有
- `RH_Prompter` —— 4/5 个有
- `Seed (rgthree)` —— 4/5 个有
- `TTP_Expand_And_Mask` —— 4/5 个有
- `TextCombinerTwo` —— 4/5 个有
- `Image To Mask` —— 1/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `LayerMask: MaskPreview` —— 1/5 个有
- `LayerUtility: ColorImage` —— 1/5 个有
- `LayerUtility: ColorPicker` —— 1/5 个有
- `SeedGenerator` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
