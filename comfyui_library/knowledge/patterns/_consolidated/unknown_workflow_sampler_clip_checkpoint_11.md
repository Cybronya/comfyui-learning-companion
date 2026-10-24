---
name: unknown_workflow_sampler_clip_checkpoint_11
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.966429
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/emoji 表情包穿搭出图神器_1948991782609199106.json, 图片生成/图生图/人物胸肌变大工作流｜Kontext_1948252483918397442.json, 图片生成/图生图/我的世界风格｜Kontext_1953632390562414593.json, 图片生成/图生图/服装模特试穿｜单图_1947220004598128642.json, 图片生成/图生图/服装模特试穿｜双图模式_1947216262428577793.json, 图片生成/图生图/真人转动漫｜Kontext_1959130581290397698.json, 图片生成/图生图/耳环产品展示｜单图生成_1947212156586643457.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_11

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/emoji 表情包穿搭出图神器_1948991782609199106.json、图片生成/图生图/人物胸肌变大工作流｜Kontext_1948252483918397442.json、图片生成/图生图/我的世界风格｜Kontext_1953632390562414593.json、图片生成/图生图/服装模特试穿｜单图_1947220004598128642.json、图片生成/图生图/服装模特试穿｜双图模式_1947216262428577793.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `ModelSamplingFlux` —— 4/7 个有
- `ImageSizeInfo` —— 2/7 个有
- `Evaluate Integers` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `Image Overlay` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `InvertMask` —— 1/7 个有
- `PIP_图像联结` —— 1/7 个有
- `RMBG` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
