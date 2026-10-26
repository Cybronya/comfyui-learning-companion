---
name: text_to_image_lora_sampler_clip_114
type: Text To Image
frequency: 13
level: weak
coverage: 0.779538
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS image 最强开源文生图｜开源生图的黑马_2112029308096176130.json, 图片生成/文生图/MOSS image 最强开源文生图｜电商海报文字清晰_2112488209677635586.json, 图片生成/文生图/MOSS image文生图基础版 提示词直出图像生成工具_2113349395633754113.json, 图片生成/文生图/MOSS image文生图极速版 提示词优化写实写真工具_2113720461162008577.json, 图片生成/文生图/MOSS image文生图极速版｜自带提示词优化人像写真出图_2113565898840821761.json, 图片生成/文生图/MOSS sft Comfyui官方流｜原汁原味官方文生图_2112425060618297345.json, 图片生成/文生图/MOSS 文生图新秀｜数字人全能助手一键出图_2112373662857908225.json, 图片生成/文生图/MOSS-Image 文生图_2108772466398158849.json, 图片生成/文生图/MOSS-Image文生图工作流｜一句话直出高质量AI图片_2114621205297848321.json, 图片生成/文生图/MOSS_BBOX边界框精准布局文生图工作流｜海报排版随心控_2114234330708013057.json, 图片生成/文生图/MOSS文生图基础工作流，简洁易上手快速生成高质量图片素材_2114468798932799490.json, 图片生成/文生图/Moss Image布局控制工作流 元素位置精准海报工具_2114136772199403521.json, 图片生成/文生图/Moss Image布局控制工作流｜文生图海报制作元素位置精准可控_2113884746953609218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_114

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/MOSS image 最强开源文生图｜开源生图的黑马_2112029308096176130.json、图片生成/文生图/MOSS image 最强开源文生图｜电商海报文字清晰_2112488209677635586.json、图片生成/文生图/MOSS image文生图基础版 提示词直出图像生成工具_2113349395633754113.json、图片生成/文生图/MOSS image文生图极速版 提示词优化写实写真工具_2113720461162008577.json、图片生成/文生图/MOSS image文生图极速版｜自带提示词优化人像写真出图_2113565898840821761.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 10/13 个有
- `PreviewAny` —— 10/13 个有
- `PrimitiveStringMultiline` —— 10/13 个有
- `SkipLayerGuidanceDiTSimple` —— 10/13 个有
- `TextGenerate` —— 10/13 个有
- `solarL_SaveImagesToZip` —— 10/13 个有
- `孤海注释` —— 10/13 个有
- `EmptyFlux2LatentImage` —— 9/13 个有
- `PreviewImage` —— 9/13 个有
- `ComfySwitchNode` —— 8/13 个有
- `ResolutionSelector` —— 8/13 个有
- `CreateBoundingBoxes` —— 3/13 个有
- `MOSSImageLayoutPrompt` —— 3/13 个有
- `GetNode` —— 2/13 个有
- `LoadImage` —— 2/13 个有
- `MuyeTextEditOutput` —— 2/13 个有
- `PrimitiveBoolean` —— 2/13 个有
- `SetNode` —— 2/13 个有
- `SpectrumMOSSImageAdaptive` —— 2/13 个有
- `ConditioningZeroOut` —— 1/13 个有
- `FastGroupsBypassSwitch` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 13 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 13 | 77% |
| 采样算法 | er_sde | - | 13 | 85% |
| 调度器 | beta | - | 13 | 77% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 1200 | 13 | 0% |
| 高度 | 80 | 80 - 1600 | 13 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，13 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，13 个样本
- 采样算法 最常用 er_sde，13 个样本，一致性 85%
- 调度器 最常用 beta，13 个样本，一致性 77%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1200，13 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1600，13 个样本，取值分散，一致性仅 0%
- 高发问题（15/13 个样本）：Steps较低可能导致细节不足
