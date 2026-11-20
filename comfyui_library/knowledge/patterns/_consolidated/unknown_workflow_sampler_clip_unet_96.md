---
name: unknown_workflow_sampler_clip_unet_96
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.898455
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/任意图片转“手持自拍”_2052670657846099969.json, 图片生成/图生图/任意画风转写实_2053048956061536257.json, 图片生成/图生图/优化场景去除图像AI感 增加细节_2041708135127191554.json, 图片生成/图生图/动漫少女现实化_2056400490073780225.json, 图片生成/图生图/去AI塑料感与真实肤质_2051201941220405249.json, 图片生成/图生图/去除图像AI感 增加细节_2032271913573158914.json, 图片生成/图生图/去除图像AI感 增加细节_2036273754577313794.json, 图片生成/图生图/场景去除图像AI感 增加细节_2032342155766796289.json, 图片生成/图生图/场景去除图像AI感+增加细节_2046436726729613313.json, 图片生成/文生图/klein建筑，室内工作流+Klein放大工作流_2087711918889984002.json, 图片生成/文生图/去除图像AI感 去油腻质感，增加细节纹理，防止僵尸脸_2093538755654275073.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_96

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/任意图片转“手持自拍”_2052670657846099969.json、图片生成/图生图/任意画风转写实_2053048956061536257.json、图片生成/图生图/优化场景去除图像AI感 增加细节_2041708135127191554.json、图片生成/图生图/动漫少女现实化_2056400490073780225.json、图片生成/图生图/去AI塑料感与真实肤质_2051201941220405249.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
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
- `Image Comparer (rgthree)` —— 10/11 个有
- `ColorMatch` —— 7/11 个有
- `ImageScaleToTotalPixels` —— 7/11 个有
- `ImageSharpen` —— 7/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `DetailDaemonSamplerNode` —— 6/11 个有
- `ImageResize+` —— 6/11 个有
- `ImpactInt` —— 6/11 个有
- `easy float` —— 6/11 个有
- `FluxKontextImageScale` —— 4/11 个有
- `PrimitiveInt` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `ImageConcatenate_UTK` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `LoraLoader` —— 1/11 个有
- `PlaySound|pysssss` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
