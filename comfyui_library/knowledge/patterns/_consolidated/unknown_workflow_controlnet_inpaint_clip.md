---
name: unknown_workflow_controlnet_inpaint_clip
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.905
common_nodes: [ArgosTranslateTextNode, CLIPTextEncode, CannyEdgePreprocessor, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, GrowMask, GrowMaskWithBlur, Image Comparer (rgthree), InvertMask (segment anything), LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, SetUnionControlNetType, easy imageRemBg, 呆毛Demo_Inpainting]
problems: []
missing: []
members: [图片生成/图生图/DaiMao_Inpaint 去背景重绘_1923380436817334274.json, 图片生成/图生图/DaiMao_Inpaint 去背景重绘_2026133874945826818.json, 图片生成/图生图/DaiMao_Inpaint 背景重绘_2031202997153304578.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_clip

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/DaiMao_Inpaint 去背景重绘_1923380436817334274.json、图片生成/图生图/DaiMao_Inpaint 去背景重绘_2026133874945826818.json、图片生成/图生图/DaiMao_Inpaint 背景重绘_2031202997153304578.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `ArgosTranslateTextNode`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `GrowMask`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `InvertMask (segment anything)`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `easy imageRemBg`
- `呆毛Demo_Inpainting`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.45 - 0.45 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.45 - 0.45，3 个样本，取值集中（一致性 100%）
