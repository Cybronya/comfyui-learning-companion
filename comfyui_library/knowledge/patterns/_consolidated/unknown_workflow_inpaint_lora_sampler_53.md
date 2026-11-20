---
name: unknown_workflow_inpaint_lora_sampler_53
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.963
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GetImageSizeAndCount, ImageCrop, InpaintModelConditioning, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, SaveImage, SolidMask, VAEDecode, VAELoader, easy makeImageForICLora, easy seed]
problems: []
missing: []
members: [图片生成/图生图/ICEdit图像编辑_1918955197224124417.json, 图片生成/图生图/【15 秒极速版】Flux-ICEdit-MoE Lora-人物一致性图像编辑-StarAI_1918335426757591041.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_53

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ICEdit图像编辑_1918955197224124417.json、图片生成/图生图/【15 秒极速版】Flux-ICEdit-MoE Lora-人物一致性图像编辑-StarAI_1918335426757591041.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `ImageCrop`
- `InpaintModelConditioning`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SolidMask`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CR Upscale Image` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | beta | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 beta，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
