---
name: unknown_workflow_unet_vae_16
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6825
common_nodes: [CR Text, DualCLIPLoader, FaceParse(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParsingResultsParser(FaceParsing), FaceRestoreCFWithModel, FaceRestoreModelLoader, GetNode, LayerUtility: ImageCombineAlpha, LoadImage, ModelSamplingFlux, PreviewImage, RH_Captioner, RH_Jimeng4_Image2Image, ReActorFaceSwap, SaveImage, SetNode, UNETLoader, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/子易数字人形象创作工坊【一致性图生图即梦4.0版本】_1976839121555668993.json, 图片生成/文生图/子易数字人形象创作工坊【文生图即梦4.0版本】_1976796575240540161.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/子易数字人形象创作工坊【一致性图生图即梦4.0版本】_1976839121555668993.json、图片生成/文生图/子易数字人形象创作工坊【文生图即梦4.0版本】_1976796575240540161.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `DualCLIPLoader`
- `FaceParse(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `FaceRestoreCFWithModel`
- `FaceRestoreModelLoader`
- `GetNode`
- `LayerUtility: ImageCombineAlpha`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RH_Captioner`
- `RH_Jimeng4_Image2Image`
- `ReActorFaceSwap`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `BasicScheduler` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `Int` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
