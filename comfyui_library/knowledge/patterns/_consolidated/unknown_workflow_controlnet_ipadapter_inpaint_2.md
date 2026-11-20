---
name: unknown_workflow_controlnet_ipadapter_inpaint_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.536333
common_nodes: [Anything Everywhere, BlendInpaint, BrushNet, BrushNetLoader, CannyEdgePreprocessor, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApplyAdvanced, ControlNetLoader, CreateShapeMask, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, ICLightApplyMaskGrey, ICLightAppply, IPAdapterNoise, IPAdapterTiled, IPAdapterUnifiedLoader, If ANY execute A else B, Image Comparer (rgthree), Image Size to Number, ImageToMask, ImpactStringSelector, InvertMask, IsMaskEmpty, JoinImageWithAlpha, KSampler, LayerUtility: ImageBlend, LoadImage, MaskToImage, PerturbedAttentionGuidance, PreviewImage, SaveImage, SetNode, ShowText|pysssss, SolidMask, String Literal, Text List, Text List to Text, UNETLoader, VAEDecode, VAEEncodeArgMax, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/电商产品换背景+光影优化_1902642273685811202.json, 图片生成/图生图/电商产品换背景+光影优化_1970692461653880834.json, 平台全量/Easy Product Relight_1863434480945135618.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_inpaint_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/电商产品换背景+光影优化_1902642273685811202.json、图片生成/图生图/电商产品换背景+光影优化_1970692461653880834.json、平台全量/Easy Product Relight_1863434480945135618.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 3 个 workflow 都包含：
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
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 2/3 个有
- `BiRefNet_Hugo` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `ICLightConditioning` —— 1/3 个有
- `ImageBlend` —— 1/3 个有
- `InpaintPreprocessor` —— 1/3 个有
- `KSampler (Efficient)` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `LoadAndApplyICLightUnet` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `workflow/CLIP文本编码器` —— 1/3 个有
- `workflow/模型组` —— 1/3 个有
- `workflow>CLIP文本编码器` —— 1/3 个有
- `workflow>模型组` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 2 | 2 - 3 | 3 | 80% |
| 采样算法 | dpmpp_sde | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.9 | 0.9 - 1 | 3 | 95% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 3，3 个样本
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.9，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
