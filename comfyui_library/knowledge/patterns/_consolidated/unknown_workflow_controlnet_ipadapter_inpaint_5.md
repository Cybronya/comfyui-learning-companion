---
name: unknown_workflow_controlnet_ipadapter_inpaint_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.534
common_nodes: [Anything Everywhere, BlendInpaint, BrushNet, BrushNetLoader, CannyEdgePreprocessor, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApplyAdvanced, ControlNetLoader, CreateShapeMask, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, ICLightApplyMaskGrey, ICLightAppply, IPAdapterNoise, IPAdapterTiled, IPAdapterUnifiedLoader, If ANY execute A else B, Image Comparer (rgthree), Image Size to Number, ImageToMask, ImpactStringSelector, InvertMask, IsMaskEmpty, JoinImageWithAlpha, KSampler, LayerUtility: ImageBlend, LoadImage, MaskToImage, PerturbedAttentionGuidance, PreviewImage, SaveImage, SetNode, ShowText|pysssss, SolidMask, String Literal, Text List, Text List to Text, UNETLoader, VAEDecode, VAEEncodeArgMax, VAELoader, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/电商产品换背景+光影优化_1902642273685811202.json, 图片生成/图生图/电商产品换背景+光影优化_1970692461653880834.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_inpaint_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/电商产品换背景+光影优化_1902642273685811202.json、图片生成/图生图/电商产品换背景+光影优化_1970692461653880834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BlendInpaint`
- `BrushNet`
- `BrushNetLoader`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CreateShapeMask`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMaskWithBlur`
- `ICLightApplyMaskGrey`
- `ICLightAppply`
- `IPAdapterNoise`
- `IPAdapterTiled`
- `IPAdapterUnifiedLoader`
- `If ANY execute A else B`
- `Image Comparer (rgthree)`
- `Image Size to Number`
- `ImageToMask`
- `ImpactStringSelector`
- `InvertMask`
- `IsMaskEmpty`
- `JoinImageWithAlpha`
- `KSampler`
- `LayerUtility: ImageBlend`
- `LoadImage`
- `MaskToImage`
- `PerturbedAttentionGuidance`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `SolidMask`
- `String Literal`
- `Text List`
- `Text List to Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncodeArgMax`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `workflow/CLIP文本编码器` —— 1/2 个有
- `workflow/模型组` —— 1/2 个有
- `workflow>CLIP文本编码器` —— 1/2 个有
- `workflow>模型组` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.9 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
