---
name: unknown_workflow_inpaint_lora_sampler_63
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8465
common_nodes: [AutoCropFaces, CLIPLoader, ConditioningZeroOut, DrawMaskOnImage, InpaintModelConditioning, KSampler, LayerMask: HumanPartsUltra, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图形图像高级换脸_2008430786852167682.json, 图片生成/图生图/脸部一致性修复 Qwen Image Edit F2P_1998401058412068865.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图形图像高级换脸_2008430786852167682.json、图片生成/图生图/脸部一致性修复 Qwen Image Edit F2P_1998401058412068865.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AutoCropFaces`
- `CLIPLoader`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: HumanPartsUltra`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ACE_TextConcatenate` —— 1/2 个有
- `AILab_QwenVL` —— 1/2 个有
- `BooleanBasic` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `GGUFLoaderKJ` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `MaskPreview` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.65 | - | 2 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.65，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
