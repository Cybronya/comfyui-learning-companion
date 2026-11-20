---
name: unknown_workflow_sampler_26
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6862
common_nodes: [ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadQwenImageDiffSynthiPipe, PreviewImage, PrimitiveStringMultiline, QwenImageDiffSynthSampler, RH_Captioner, SaveImage, SetControlArgs]
problems: []
missing: []
members: [图片生成/图生图/Qwen image Canny深度控制洗图_1956309859379675137.json, 图片生成/图生图/Qwen image Canny深度控制洗图工作流V1_1956163824573448193.json, 图片生成/图生图/Qwen image Canny线稿控制洗图_1956268870371823617.json, 图片生成/图生图/Qwen image Canny线稿控制洗图工作流V1_1956163852192894977.json, 图片生成/文生图/Qwen (千问) canny+depth 洗图_1956246979544272898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_26

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen image Canny深度控制洗图_1956309859379675137.json、图片生成/图生图/Qwen image Canny深度控制洗图工作流V1_1956163824573448193.json、图片生成/图生图/Qwen image Canny线稿控制洗图_1956268870371823617.json、图片生成/图生图/Qwen image Canny线稿控制洗图工作流V1_1956163852192894977.json、图片生成/文生图/Qwen (千问) canny+depth 洗图_1956246979544272898.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadQwenImageDiffSynthiPipe`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImageDiffSynthSampler`
- `RH_Captioner`
- `SaveImage`
- `SetControlArgs`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 4/5 个有
- `JWInteger` —— 4/5 个有
- `PDIMAGE_LongerSize` —— 4/5 个有
- `DepthAnythingV2Preprocessor` —— 3/5 个有
- `Canny` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `Int` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `CannyEdgePreprocessor` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
