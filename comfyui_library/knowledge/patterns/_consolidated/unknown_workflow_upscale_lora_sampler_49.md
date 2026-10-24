---
name: unknown_workflow_upscale_lora_sampler_49
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7165
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, ComfyUI_Image_Round__ImageRound, Context (rgthree), DisableNoise, DualCLIPLoader, FluxGuidance, GetNode, Image Comparer (rgthree), ImageColorMatch+, ImageListToBatch+, ImageScaleBy, ImageSmartSharpen+, ImageUpscaleWithModel, ImitationHueNode, InjectLatentNoise+, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, ShowText|pysssss, SplitSigmasDenoise, StaticNumberFloat, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/一键洗图_1898892984958537729.json, 图片生成/图生图/一键洗图_1930496325371203585.json, 图片生成/图生图/一键洗图_去水印版_1923753318063984641.json, 图片生成/图生图/一键洗图_去水印版_1925677447029673986.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_49

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键洗图_1898892984958537729.json、图片生成/图生图/一键洗图_1930496325371203585.json、图片生成/图生图/一键洗图_去水印版_1923753318063984641.json、图片生成/图生图/一键洗图_去水印版_1925677447029673986.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `ComfyUI_Image_Round__ImageRound`
- `Context (rgthree)`
- `DisableNoise`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `ImageListToBatch+`
- `ImageScaleBy`
- `ImageSmartSharpen+`
- `ImageUpscaleWithModel`
- `ImitationHueNode`
- `InjectLatentNoise+`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `ShowText|pysssss`
- `SplitSigmasDenoise`
- `StaticNumberFloat`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Convert Masks to Images` —— 2/4 个有
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `ICEFConditioning` —— 2/4 个有
- `Image To Mask` —— 2/4 个有
- `ImageCrop` —— 2/4 个有
- `InContextEditInstruction` —— 2/4 个有
- `JWMaskResize` —— 2/4 个有
- `JoinImages` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `LayerUtility: ImageAutoCrop V3` —— 2/4 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/4 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 2/4 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `Mask Invert` —— 2/4 个有
- `PreviewImage` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.51 | 0.51 - 0.51 | 4 | 100% |
| LoRA 文本强度 | 0.51 | 0.51 - 0.51 | 4 | 100% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 28 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.51，观测区间 0.51 - 0.51，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.51，观测区间 0.51 - 0.51，4 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 28，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
