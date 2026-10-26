---
name: unknown_workflow_lora_8
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [DeepTranslatorTextNode, EasyControlGenerate, EasyControlLoadFlux, EasyControlLoadLora, GetImageSize, LayerUtility: PurgeVRAM, LoadImage, PreviewImage, RH_Captioner, SaveImage, ShowText|pysssss, Text Concatenate (JPS), easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/EasyControlnet - pose_1909582155595378690.json, 图片生成/文生图/EasyControl吉卜力风格转绘_1911711182053670913.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/EasyControlnet - pose_1909582155595378690.json、图片生成/文生图/EasyControl吉卜力风格转绘_1911711182053670913.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `DeepTranslatorTextNode`
- `EasyControlGenerate`
- `EasyControlLoadFlux`
- `EasyControlLoadLora`
- `GetImageSize`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `ShowText|pysssss`
- `Text Concatenate (JPS)`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `EasyControlLoadMultiLora` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `InpaintPreprocessor` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
