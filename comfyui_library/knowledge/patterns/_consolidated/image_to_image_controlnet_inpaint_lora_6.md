---
name: image_to_image_controlnet_inpaint_lora_6
type: Image To Image
frequency: 4
level: strong
coverage: 0.641
common_nodes: [AutoCropFaces, CLIPLoader, CheckpointLoaderSimple, ConditioningZeroOut, Image Comparer (rgthree), ImageStitch, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, TextEncodeQwenImageEditPlus, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/251224002.分开式-QwenEdit2509一键自动换脸-24G显存起步​_2003684393887645697.json, 图片生成/图生图/251225001.008.QwenEdit2511自动换脸-24G显存起步_2004213257336487937.json, 图片生成/图生图/LH-DMT版本-2.生图片类-047.QwenEdit2509自动换脸-24G显存起步_2016524928803151874.json, 图片生成/图生图/工作流：LH-DMT版本-49.QwenEdit2509一键自动换脸-24G显存起步​_2003670534682517505.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/251224002.分开式-QwenEdit2509一键自动换脸-24G显存起步​_2003684393887645697.json、图片生成/图生图/251225001.008.QwenEdit2511自动换脸-24G显存起步_2004213257336487937.json、图片生成/图生图/LH-DMT版本-2.生图片类-047.QwenEdit2509自动换脸-24G显存起步_2016524928803151874.json、图片生成/图生图/工作流：LH-DMT版本-49.QwenEdit2509一键自动换脸-24G显存起步​_2003670534682517505.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 4 个 workflow 都包含：
- `AutoCropFaces`
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageStitch`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
