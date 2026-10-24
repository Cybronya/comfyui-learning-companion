---
name: unknown_workflow_lora_unet_vae_11
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7465
common_nodes: [CLIPLoader, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), Image Overlay, ImageScale, ImageToMask, Int, JjkText, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PreviewImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/细节恢复 qwen_image_2.1_2107159669243473921.json, 图片生成/图生图/表情迁移 qwen_image_2.1_2105577290787807234.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/细节恢复 qwen_image_2.1_2107159669243473921.json、图片生成/图生图/表情迁移 qwen_image_2.1_2105577290787807234.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `Image Overlay`
- `ImageScale`
- `ImageToMask`
- `Int`
- `JjkText`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PreviewImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `FaceAnalysisModels` —— 1/2 个有
- `FaceBoundingBox` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `KuwaharaBlur` —— 1/2 个有
- `LayerFilter: GaussianBlur` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `MaskPreview` —— 1/2 个有
- `MaxNode` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有
- `SamplerCustom` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
