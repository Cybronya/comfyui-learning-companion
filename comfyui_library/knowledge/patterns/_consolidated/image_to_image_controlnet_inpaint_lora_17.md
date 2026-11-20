---
name: image_to_image_controlnet_inpaint_lora_17
type: Image To Image
frequency: 2
level: weak
coverage: 0.8635
common_nodes: [Anything Everywhere, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetInpaintingAliMamaApply, ControlNetLoader, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImagePadForOutpaint, InpaintModelConditioning, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskBlur+, PreviewImage, SDPoseOODLoader, SDPoseOODProcessor, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEditAIO工作流合集，换装_扩图_姿势参考_局部重绘_2002630215639678978.json, 平台全量/QwenEditAIO工作流合集，换装_扩图_姿势参考_局部重绘全部搞定_1997888664980062209.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/QwenEditAIO工作流合集，换装_扩图_姿势参考_局部重绘_2002630215639678978.json、平台全量/QwenEditAIO工作流合集，换装_扩图_姿势参考_局部重绘全部搞定_1997888664980062209.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskBlur+`
- `PreviewImage`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAEEncode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（10/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
