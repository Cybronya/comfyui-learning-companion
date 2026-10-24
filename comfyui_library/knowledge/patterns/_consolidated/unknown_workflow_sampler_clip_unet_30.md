---
name: unknown_workflow_sampler_clip_unet_30
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.742864
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MOSS Image布局控制图像设计Sft+base_2112216902151008257.json, 图片生成/图生图/MOSS sft Comfyui官方工作流_2112732679153209345.json, 图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2044590595057917954.json, 图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2046103550576562177.json, 图片生成/文生图/FLUX 3 Image Klein 文生图_2111461052599857153.json, 图片生成/文生图/HS-image_ernie_image_2044628228756742146.json, 图片生成/文生图/MOSS SFT 提示增强标准文生图_2112193931260813313.json, 图片生成/文生图/Moss 文生图_2111394608352681986.json, 图片生成/文生图/Moss-image Base Fixed文生图_2112185356295688193.json, 图片生成/文生图/Moss-image Base文生图_2112066738195091457.json, 图片生成/文生图/Moss-image Base文生图_2112122177809108994.json, 图片生成/文生图/Moss-image Base文生图_2112140955116728321.json, 图片生成/文生图/Moss-image Sft Fixed文生图_2112185347613487105.json, 图片生成/文生图/Moss-image Sft文生图_2112060921463001089.json, 图片生成/文生图/Moss-image(文生图）_2111701557262766082.json, 图片生成/文生图/Moss-image+Base+Fixed文生图_2112225720482226178.json, 图片生成/文生图/Moss-image+Base文生图_2112079816290816001.json, 图片生成/文生图/Moss-image+Sft+Fixed文生图_2112225707626680321.json, 图片生成/文生图/Moss-image+Sft文生图_2112079796443369473.json, 图片生成/文生图/Moss_Image_sft图像生产工作流_2112494670994567169.json, 图片生成/文生图/Qwen3.5反推提示词+ernie_image_turbo_2046120898310180865.json, 图片生成/文生图/moss_image图像生成_2112202038108049409.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/MOSS Image布局控制图像设计Sft+base_2112216902151008257.json、图片生成/图生图/MOSS sft Comfyui官方工作流_2112732679153209345.json、图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2044590595057917954.json、图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2046103550576562177.json、图片生成/文生图/FLUX 3 Image Klein 文生图_2111461052599857153.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 21/22 个有
- `TextGenerate` —— 21/22 个有
- `ComfySwitchNode` —— 20/22 个有
- `PrimitiveBoolean` —— 19/22 个有
- `ResolutionSelector` —— 18/22 个有
- `SkipLayerGuidanceDiTSimple` —— 7/22 个有
- `StringReplace` —— 4/22 个有
- `CreateBoundingBoxes` —— 2/22 个有
- `LoadImage` —— 2/22 个有
- `MOSSImageLayoutPrompt` —— 2/22 个有
- `INTConstant` —— 1/22 个有
- `llama_cpp_instruct_adv` —— 1/22 个有
- `llama_cpp_model_loader` —— 1/22 个有
- `llama_cpp_parameters` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 22 | 61% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 22 | 74% |
| 采样算法 | er_sde | - | 22 | 73% |
| 调度器 | simple | - | 22 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，22 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，22 个样本
- 采样算法 最常用 er_sde，22 个样本，一致性 73%
- 调度器 最常用 simple，22 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
