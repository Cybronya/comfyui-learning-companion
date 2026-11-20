---
name: unknown_workflow_controlnet_inpaint_lora_2
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.728917
common_nodes: [BasicScheduler, BiRefNet_Hugo, CFGGuider, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingFlux, PreviewImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, ShowText|pysssss, TextCombinerSix, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/logo迁移到物品上之flux_1909564150056714242.json, 图片生成/图生图/珠宝首饰AI模特展示_2020751487340650498.json, 图片生成/图生图/饰品项链到AI模特展示_2016329762465128449.json, 图片生成/图生图/首饰生成模特海报 一键生图系列_1909074737446662146.json, 图片生成/文生图/饰品项链到AI模特展示_1939508745355575297.json, 平台全量/图案印花Logo迁移到产品_1859066956040286209.json, 平台全量/图案印花Logo迁移到服装_1858768575564582914.json, 平台全量/模特穿戴 产品展示_1879423314983641090.json, 平台全量/虚拟换装_1858801790417342465.json, 平台全量/饰品手表到男女模特展示_1860931626497871873.json, 平台全量/饰品眼镜到AI模特展示_1861001108763361281.json, 平台全量/饰品项链到AI模特展示_1860896559767621634.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/logo迁移到物品上之flux_1909564150056714242.json、图片生成/图生图/珠宝首饰AI模特展示_2020751487340650498.json、图片生成/图生图/饰品项链到AI模特展示_2016329762465128449.json、图片生成/图生图/首饰生成模特海报 一键生图系列_1909074737446662146.json、图片生成/文生图/饰品项链到AI模特展示_1939508745355575297.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `BiRefNet_Hugo`
- `CFGGuider`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
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
- `CLIPTextEncodeFlux` —— 11/12 个有
- `ImageCrop+` —— 11/12 个有
- `ImageResize+` —— 11/12 个有
- `JjkText` —— 11/12 个有
- `Label (rgthree)` —— 11/12 个有
- `CR Simple Image Compare` —— 10/12 个有
- `TTP_Expand_And_Mask` —— 10/12 个有
- `Seed (rgthree)` —— 9/12 个有
- `RH_Prompter` —— 6/12 个有
- `TextCombinerTwo` —— 5/12 个有
- `SeedGenerator` —— 3/12 个有
- `Image To Mask` —— 2/12 个有
- `ImageResizeKJ` —— 2/12 个有
- `LayerMask: MaskPreview` —— 2/12 个有
- `LayerUtility: ColorImage` —— 2/12 个有
- `LayerUtility: ColorPicker` —— 2/12 个有
- `easy imageConcat` —— 2/12 个有
- `ArgosTranslateTextNode` —— 1/12 个有
- `ImagePadForOutpaint` —— 1/12 个有
- `ImageScale` —— 1/12 个有
- `SeargePromptText` —— 1/12 个有
- `easy imageSplitGrid` —— 1/12 个有
- `easy imagesSplitImage` —— 1/12 个有
- `easy prompt` —— 1/12 个有
- `easy promptReplace` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
