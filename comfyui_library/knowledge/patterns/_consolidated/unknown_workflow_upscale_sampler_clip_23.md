---
name: unknown_workflow_upscale_sampler_clip_23
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9445
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, Image Levels Adjustment, ImageInvert, ImageResizeKJ, ImageUpscaleWithModel, KSamplerSelect, LineArtPreprocessor, LoadImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/WF10_转线稿工作流_1926609891962593282.json, 图片生成/图生图/seedance2.5真人过审，转线稿，站位图，适用于即梦_2086720325940760578.json, 图片生成/图生图/seedance2.5真人过审，转线稿，站位图，适用于即梦_2088403416916774913.json, 图片生成/图生图/人物线稿快速提取_2044971488368926721.json, 图片生成/图生图/人物线稿快速提取_2062088784119943169.json, 图片生成/文生图/人物线稿快速提取_2062709947036688385.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/WF10_转线稿工作流_1926609891962593282.json、图片生成/图生图/seedance2.5真人过审，转线稿，站位图，适用于即梦_2086720325940760578.json、图片生成/图生图/seedance2.5真人过审，转线稿，站位图，适用于即梦_2088403416916774913.json、图片生成/图生图/人物线稿快速提取_2044971488368926721.json、图片生成/图生图/人物线稿快速提取_2062088784119943169.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Image Levels Adjustment`
- `ImageInvert`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LineArtPreprocessor`
- `LoadImage`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Checkpoint Loader (Simple)` —— 5/6 个有
- `Any Switch (rgthree)` —— 1/6 个有
- `ApplyFBCacheOnModel` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `String Literal` —— 1/6 个有
- `UNETLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
