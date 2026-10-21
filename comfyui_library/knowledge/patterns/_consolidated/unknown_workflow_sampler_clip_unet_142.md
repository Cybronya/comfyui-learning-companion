---
name: unknown_workflow_sampler_clip_unet_142
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.79875
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片风格迁移转化 • 灵感造像师：实现像素级保留与灵魂级风格注入生成器_2107037189610762241.json, 图片生成/图生图/图片风格迁移转化 • 灵感造像师：实现像素级保留与灵魂级风格注入生成器_2107090731931361281.json, 图片生成/文生图/克莱因9B风格迁移 林耀2.24_2026184088469639169.json, 数字人/数字人/短剧资产_Klein_true_V3人物资产制作(角色定版三视图）V2_2086611011628519426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_142

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图片风格迁移转化 • 灵感造像师：实现像素级保留与灵魂级风格注入生成器_2107037189610762241.json、图片生成/图生图/图片风格迁移转化 • 灵感造像师：实现像素级保留与灵魂级风格注入生成器_2107090731931361281.json、图片生成/文生图/克莱因9B风格迁移 林耀2.24_2026184088469639169.json、数字人/数字人/短剧资产_Klein_true_V3人物资产制作(角色定版三视图）V2_2086611011628519426.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageColorMatch+` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `PlaySound|pysssss` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `Qwen3VL_Chat` —— 3/4 个有
- `easy imageConcat` —— 3/4 个有
- `AutoCropFaces` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
