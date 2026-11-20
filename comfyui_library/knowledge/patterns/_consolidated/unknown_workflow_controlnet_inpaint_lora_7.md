---
name: unknown_workflow_controlnet_inpaint_lora_7
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8005
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CLIPTextEncodeFlux, CR Simple Image Compare, ControlNetInpaintingAliMamaApply, ControlNetLoader, DualCLIPLoader, FluxGuidance, ImageCrop+, KSamplerSelect, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetLatentNoiseMask, TTP_Expand_And_Mask, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/无模特穿衣_1907288358165307394.json, 平台全量/Cute Anime Character Converter_1864926084088164353.json, 平台全量/一致性参考图像服装迁移_1857807038956122114.json, 平台全量/服装迁移 Clothing Migration Kit_1857379679656194049.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/无模特穿衣_1907288358165307394.json、平台全量/Cute Anime Character Converter_1864926084088164353.json、平台全量/一致性参考图像服装迁移_1857807038956122114.json、平台全量/服装迁移 Clothing Migration Kit_1857379679656194049.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Simple Image Compare`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageCrop+`
- `KSamplerSelect`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `TTP_Expand_And_Mask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ExtraOptionsNode` —— 3/4 个有
- `INPAINT_MaskedFill` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `InvertMask` —— 3/4 个有
- `JoyCaption2_simple` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `TTP_text_mix` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy textSwitch` —— 3/4 个有
- `ImageResize+` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `easy prompt` —— 2/4 个有
- `HfImageToRGB` —— 1/4 个有
- `Images to RGB` —— 1/4 个有
- `Note _O` —— 1/4 个有
- `PreviewMask_` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
