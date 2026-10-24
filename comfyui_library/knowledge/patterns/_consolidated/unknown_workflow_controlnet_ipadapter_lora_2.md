---
name: unknown_workflow_controlnet_ipadapter_lora_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.690667
common_nodes: [AIO_Preprocessor, Any Switch (rgthree), Anything Everywhere3, BNK_CLIPTextEncodeAdvanced, BiRefNet_Hugo, CR SDXL Aspect Ratio, CR Text Concatenate, CheckpointLoaderSimple, ColorMatch, ControlNetApplyAdvanced, ControlNetLoader, DF_Text_Box, GrowMaskWithBlur, IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, ImageAndMaskPreview, ImageCompositeMasked, ImpactDilateMask, InspyrenetRembg, KSampler //Inspire, LayerMask: LoadSegmentAnythingModels, LayerMask: MaskEdgeUltraDetail V2, LayerMask: MaskGrow, LayerMask: SegmentAnythingUltra V3, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LoadImage, LoraLoader, MaskPreview+, PerturbedAttentionGuidance, PrepImageForClipVision, PreviewImage, Prompts Everywhere, RH_Captioner, RepeatLatentBatch, SaveImage, ShowText|pysssss, Simple String, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/宠物肖像一键风格转绘_1946022145187082241.json, 图片生成/图生图/宠物肖像一键风格转绘_2005829887875313665.json, 图片生成/图生图/宠物肖像一键风格转绘单次版_1947111781057212418.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_lora_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/宠物肖像一键风格转绘_1946022145187082241.json、图片生成/图生图/宠物肖像一键风格转绘_2005829887875313665.json、图片生成/图生图/宠物肖像一键风格转绘单次版_1947111781057212418.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Any Switch (rgthree)`
- `Anything Everywhere3`
- `BNK_CLIPTextEncodeAdvanced`
- `BiRefNet_Hugo`
- `CR SDXL Aspect Ratio`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DF_Text_Box`
- `GrowMaskWithBlur`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `ImageAndMaskPreview`
- `ImageCompositeMasked`
- `ImpactDilateMask`
- `InspyrenetRembg`
- `KSampler //Inspire`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: MaskEdgeUltraDetail V2`
- `LayerMask: MaskGrow`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `LoraLoader`
- `MaskPreview+`
- `PerturbedAttentionGuidance`
- `PrepImageForClipVision`
- `PreviewImage`
- `Prompts Everywhere`
- `RH_Captioner`
- `RepeatLatentBatch`
- `SaveImage`
- `ShowText|pysssss`
- `Simple String`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ColorPicker` —— 2/3 个有
- `ColorPickerMW` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `RandomPrompt` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1.2 | 1.2 - 1.2 | 3 | 100% |
| 采样算法 | dpmpp_sde | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.88 | 0.88 - 0.88 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.2，观测区间 1.2 - 1.2，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.88，观测区间 0.88 - 0.88，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
