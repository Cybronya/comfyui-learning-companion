---
name: unknown_workflow_sampler_clip_unet_205
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.680429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux3 t2v 蒸馏版本_2111318527201341441.json, 图片生成/文生图/flux3-image-klein（文生图）_2110956174114910210.json, 图片生成/文生图/flux3_image_klein文生图_2111012203712311297.json, 图片生成/文生图/flux3_klein 文生图 base版本_2110956211372904449.json, 图片生成/文生图/moss_image图像生成_2112202038108049409.json, 图片生成/文生图/moss文生图_2113583535255805954.json, 图片生成/文生图/（自用-贞贞版）Moss-image Sft Fixed文生图_2112438870972387329.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_205

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/flux3 t2v 蒸馏版本_2111318527201341441.json、图片生成/文生图/flux3-image-klein（文生图）_2110956174114910210.json、图片生成/文生图/flux3_image_klein文生图_2111012203712311297.json、图片生成/文生图/flux3_klein 文生图 base版本_2110956211372904449.json、图片生成/文生图/moss_image图像生成_2112202038108049409.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 6/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `PrimitiveBoolean` —— 2/7 个有
- `SkipLayerGuidanceDiTSimple` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `CreateBoundingBoxes` —— 1/7 个有
- `Ideogram4PromptBuilderKJ` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 15 - 50 | 7 | 56% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 3.5 | 7 | 52% |
| 采样算法 | er_sde | - | 7 | 71% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 15 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 3.5，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
