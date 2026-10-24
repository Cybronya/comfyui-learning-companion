---
name: unknown_workflow_sampler_35
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.698
common_nodes: [LoadImage, LoadQwenImageDiffSynthiPipe, PreviewImage, PrimitiveStringMultiline, QwenImageDiffSynthSampler, SaveImage, SetControlArgs]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image控制 Canny_1956688249889460225.json, 图片生成/图生图/Qwen-Image控制 Depth_1956649792756486146.json, 图片生成/图生图/洗图神器！Qwen-Image图生图之Canny_1955746699391090689.json, 图片生成/图生图/洗图神器！Qwen-Image图生图之Depth_1955880534075428865.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_35

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Image控制 Canny_1956688249889460225.json、图片生成/图生图/Qwen-Image控制 Depth_1956649792756486146.json、图片生成/图生图/洗图神器！Qwen-Image图生图之Canny_1955746699391090689.json、图片生成/图生图/洗图神器！Qwen-Image图生图之Depth_1955880534075428865.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `LoadQwenImageDiffSynthiPipe`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImageDiffSynthSampler`
- `SaveImage`
- `SetControlArgs`

**可变部分**（部分 workflow 才有）：
- `Canny` —— 2/4 个有
- `DepthAnythingV2Preprocessor` —— 2/4 个有
- `LayerUtility: ImageScaleRestore V2` —— 2/4 个有
- `QwenImageRatio2Size` —— 2/4 个有
- `ImageResizeKJv2` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
