---
name: unknown_workflow_sampler_clip_unet_257
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9134
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2029798924080390146.json, 图片生成/文生图/2031356956467798017.json, 图片生成/文生图/8G 显卡专属｜Flux2 Klein4B 文生图加洗图 43 秒极速生成_2054786195737071617.json, 图片生成/文生图/Flux2-Klein文生图+图生图_2012291526050717697.json, 图片生成/文生图/klein建筑，室内工作流+Klein放大工作流_2087711918889984002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_257

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/2029798924080390146.json、图片生成/文生图/2031356956467798017.json、图片生成/文生图/8G 显卡专属｜Flux2 Klein4B 文生图加洗图 43 秒极速生成_2054786195737071617.json、图片生成/文生图/Flux2-Klein文生图+图生图_2012291526050717697.json、图片生成/文生图/klein建筑，室内工作流+Klein放大工作流_2087711918889984002.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `VAEEncode` —— 4/5 个有
- `GetImageSize` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `ReferenceLatent` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `PlaySound|pysssss` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `AddLabel` —— 1/5 个有
- `ColorMatch` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `ImageSharpen` —— 1/5 个有
- `Int` —— 1/5 个有
- `KSampler` —— 1/5 个有
- `LoraLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.4 | - | 1 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
