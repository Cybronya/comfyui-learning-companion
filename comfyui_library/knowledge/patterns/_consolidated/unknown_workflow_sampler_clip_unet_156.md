---
name: unknown_workflow_sampler_clip_unet_156
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.99125
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/服装替换_2083162795322994690.json, 图片生成/图生图/泳装专用对镜自拍跨境带货涨粉买家秀_2039984637874806786.json, 图片生成/图生图/真实换脸 - Flux2Klein4B加速版_2078661674969681922.json, 图片生成/图生图/赫本公主风换脸换装 _ 写实保留服饰细节 Flux2_2109120696780673025.json, 图片生成/图生图/超级换脸Flux2Klein多图编辑4B加速版_2093340946711793665.json, 图片生成/图生图/超级换脸Flux2Klein多图编辑4B加速版_2093623432524156930.json, 图片生成/图生图/超级换脸Flux2Klein多图编辑4B加速版_2093892857491976194.json, 图片生成/文生图/换装Flux2Klein多图编辑4B加速版Flux2Klein多图编辑4B加速版_2035315458378833922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_156

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/服装替换_2083162795322994690.json、图片生成/图生图/泳装专用对镜自拍跨境带货涨粉买家秀_2039984637874806786.json、图片生成/图生图/真实换脸 - Flux2Klein4B加速版_2078661674969681922.json、图片生成/图生图/赫本公主风换脸换装 _ 写实保留服饰细节 Flux2_2109120696780673025.json、图片生成/图生图/超级换脸Flux2Klein多图编辑4B加速版_2093340946711793665.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 7/8 个有
- `JWFloat` —— 7/8 个有
- `ImageConcanate` —— 6/8 个有
- `easy imageSize` —— 3/8 个有
- `EmptyFlux2LatentImage` —— 1/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/8 个有
- `Text` —— 1/8 个有
- `TextConcat` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
