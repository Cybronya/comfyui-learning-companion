---
name: unknown_workflow_sampler_53
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.924
common_nodes: [ImageAndMaskPreview, ImageStitch, InvertMask, LoadImage, MaskPreview, PreviewImage, RunningHub OneReward Loader, RunningHub OneReward Sampler, SaveImage, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/换背景 _ OneReward-Fill_1966173106291249153.json, 图片生成/图生图/换背景-字节OneReward-Fill_1966394196582150145.json, 图片生成/图生图/重绘换背景-字节OneReward-Fill重绘_1965807959672557570.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_53

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/换背景 _ OneReward-Fill_1966173106291249153.json、图片生成/图生图/换背景-字节OneReward-Fill_1966394196582150145.json、图片生成/图生图/重绘换背景-字节OneReward-Fill重绘_1965807959672557570.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageAndMaskPreview`
- `ImageStitch`
- `InvertMask`
- `LoadImage`
- `MaskPreview`
- `PreviewImage`
- `RunningHub OneReward Loader`
- `RunningHub OneReward Sampler`
- `SaveImage`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 2/3 个有
- `InspyrenetRembgLoader` —— 1/3 个有
- `InspyrenetRembgProcess` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
