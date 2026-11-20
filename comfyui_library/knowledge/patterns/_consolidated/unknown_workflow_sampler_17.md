---
name: unknown_workflow_sampler_17
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.732286
common_nodes: [Bjornulf_ShowInt, CR Overlay Text, CR Text, Float, GetImageSize, ImageCropMerge, ImageScale, ImageScaleBy, Int, LayerColor: Brightness & Contrast, LayerMask: MaskBoxDetect, LayerUtility: ColorImage V2, LoadImage, MaskToImage, PreviewImage, SaveImage, SimpleMath+, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Flux TExt 文字修改 支持中文、英文_1945386726137450498.json, 图片生成/图生图/FluxText改字（支持中文）_1942630895235084289.json, 图片生成/图生图/海报修改文字｜Flux Text_1948239404558102530.json, 平台全量/FluxText修改中英文字_1944391856266596354.json, 平台全量/FluxText改字（支持中文）_2072887133530050562.json, 平台全量/FluxText改字（支持中文）_2072888217279488001.json, 平台全量/FluxText改字（支持中文）_2072890209276088321.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_17

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux TExt 文字修改 支持中文、英文_1945386726137450498.json、图片生成/图生图/FluxText改字（支持中文）_1942630895235084289.json、图片生成/图生图/海报修改文字｜Flux Text_1948239404558102530.json、平台全量/FluxText修改中英文字_1944391856266596354.json、平台全量/FluxText改字（支持中文）_2072887133530050562.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 7 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CR Overlay Text`
- `CR Text`
- `Float`
- `GetImageSize`
- `ImageCropMerge`
- `ImageScale`
- `ImageScaleBy`
- `Int`
- `LayerColor: Brightness & Contrast`
- `LayerMask: MaskBoxDetect`
- `LayerUtility: ColorImage V2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `SimpleMath+`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `FLUXTextGenerate` —— 6/7 个有
- `FLUXTextLoad` —— 6/7 个有
- `FluxTextPipeLine` —— 1/7 个有
- `FluxTextSampler` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
