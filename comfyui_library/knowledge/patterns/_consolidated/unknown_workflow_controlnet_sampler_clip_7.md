---
name: unknown_workflow_controlnet_sampler_clip_7
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.951667
common_nodes: [AIO_Preprocessor, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.1-controlnet工作流_2088611300489392130.json, 图片生成/图生图/Flux.1+ controlnet工作流_2109991263348019202.json, 图片生成/图生图/flux1controlnet工作流_2115645049852743682.json, 图片生成/文生图/F.1一键毛坯变精装工作流 Bot_LXX V3.0_1930576899993686018.json, 平台全量/FLUX.1 Controlnet工作流_2118259281589002241.json, 平台全量/图片风格重绘工作流_1984154656723107842.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FLUX.1-controlnet工作流_2088611300489392130.json、图片生成/图生图/Flux.1+ controlnet工作流_2109991263348019202.json、图片生成/图生图/flux1controlnet工作流_2115645049852743682.json、图片生成/文生图/F.1一键毛坯变精装工作流 Bot_LXX V3.0_1930576899993686018.json、平台全量/FLUX.1 Controlnet工作流_2118259281589002241.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `SetUnionControlNetType` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `PreviewImage` —— 2/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/6 个有
- `Preview from image [Crystools]` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 6 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| ControlNet 权重 | 0.6 | 0.38 - 0.65 | 6 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，观测区间 0.38 - 0.65，6 个样本，取值集中（一致性 85%）
