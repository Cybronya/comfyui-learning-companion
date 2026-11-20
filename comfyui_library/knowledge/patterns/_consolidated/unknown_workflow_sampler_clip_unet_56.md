---
name: unknown_workflow_sampler_clip_unet_56
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.822812
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux3-klein-文生图（提示词增强）_2111099390617280514.json, 图片生成/文生图/Flux3-klein指定位置精准生成_2111266792965496834.json, 图片生成/文生图/Moss-image-base+sft 双采工作流_2115046241439674369.json, 图片生成/文生图/Moss-image-base+sft 文生图_2115583706256728065.json, 图片生成/文生图/Moss_文生图高质量版_2115646850043834370.json, 图片生成/文生图/Moss文生图（超强写真）_2114978853327298561.json, 图片生成/文生图/flux3_image_klein文生图_2111012203712311297.json, 图片生成/文生图/啊癫 Moss融合模型工作流_2115083054036381698.json, 平台全量/Moss 文生图高质量版_2118184201668358145.json, 平台全量/Moss 文生图高质量版_2121117297598361601.json, 平台全量/Moss 文生图高质量版_2121124246729609218.json, 平台全量/Moss 文生图高质量版_2121127308588306433.json, 平台全量/Moss 文生图高质量版_2121132387185815554.json, 平台全量/Moss 文生图高质量版_2121137210794799105.json, 平台全量/Moss 文生图高质量版_2121138902982549506.json, 平台全量/Moss 文生图高质量版_2121169409900376065.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_56

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/Flux3-klein-文生图（提示词增强）_2111099390617280514.json、图片生成/文生图/Flux3-klein指定位置精准生成_2111266792965496834.json、图片生成/文生图/Moss-image-base+sft 双采工作流_2115046241439674369.json、图片生成/文生图/Moss-image-base+sft 文生图_2115583706256728065.json、图片生成/文生图/Moss_文生图高质量版_2115646850043834370.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 16 个 workflow 都包含：
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
- `ResolutionSelector` —— 15/16 个有
- `MOSSMergePreset` —— 13/16 个有
- `PreviewAny` —— 12/16 个有
- `SkipLayerGuidanceDiTSimple` —— 12/16 个有
- `PreviewImage` —— 3/16 个有
- `CR Prompt Text` —— 2/16 个有
- `ConditioningZeroOut` —— 2/16 个有
- `easy showAnything` —— 2/16 个有
- `Ideogram4PromptBuilderKJ` —— 1/16 个有
- `JjkText` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 16 - 50 | 16 | 71% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 16 | 70% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 16 - 50，16 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，16 个样本
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
