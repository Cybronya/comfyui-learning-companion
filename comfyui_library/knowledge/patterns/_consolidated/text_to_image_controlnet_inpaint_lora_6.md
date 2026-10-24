---
name: text_to_image_controlnet_inpaint_lora_6
type: Text To Image
frequency: 2
level: weak
coverage: 0.645
common_nodes: [CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, ImagePadForOutpaint, InpaintPreprocessor, KSampler, LayerMask: LoadFlorence2Model, LayerMask: MaskPreview, LayerUtility: Florence2Image2Prompt, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, PreviewImage, PrimitiveInt, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux_alimama顶级扩图_1887812358683648002.json, 图片生成/图生图/扩图神器！Flux_alimama超自然_2029118211471446017.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux_alimama顶级扩图_1887812358683648002.json、图片生成/图生图/扩图神器！Flux_alimama超自然_2029118211471446017.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ImagePadForOutpaint`
- `InpaintPreprocessor`
- `KSampler`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: MaskPreview`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 22 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 22，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
