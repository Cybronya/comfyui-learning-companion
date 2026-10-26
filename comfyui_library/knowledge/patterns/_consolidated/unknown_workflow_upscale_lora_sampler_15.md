---
name: unknown_workflow_upscale_lora_sampler_15
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.721154
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Moss 洗图 图片反推_2113119843267469314.json, 图片生成/反推提示词/【WorkFisher】全能生图王 _ 适配所有类型_2112563481311535106.json, 图片生成/图生图/moss-prompt-文生图+图生图_2113432801054904322.json, 图片生成/图生图/【WorkFisher】全能生图王_适配所有类型_2113453468659834882.json, 图片生成/文生图/Moss image 官方文生图_2112078306463019010.json, 图片生成/文生图/Moss image 文生图角色资产生成+真实美感【提示词增强】_2112449151177940994.json, 图片生成/文生图/moss-prompt-RH版本角色定妆照_2114038844743049217.json, 图片生成/文生图/moss-prompt-短剧角色定妆照_2114013825287680002.json, 图片生成/文生图/moss全能生图_2113226191116267522.json, 图片生成/文生图/【Moss-image】文生图_2113267040969646081.json, 图片生成/文生图/文生图海报8K特写_2114022887387656193.json, 视频生成/图生视频/【WorkFisher】全能生图王_适配所有类型_2113792326656151554.json, 视频生成/图生视频/【WorkFisher】全能生图王_适配所有类型_2113803846358228994.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/Moss 洗图 图片反推_2113119843267469314.json、图片生成/反推提示词/【WorkFisher】全能生图王 _ 适配所有类型_2112563481311535106.json、图片生成/图生图/moss-prompt-文生图+图生图_2113432801054904322.json、图片生成/图生图/【WorkFisher】全能生图王_适配所有类型_2113453468659834882.json、图片生成/文生图/Moss image 官方文生图_2112078306463019010.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 12/13 个有
- `PreviewAny` —— 12/13 个有
- `INTConstant` —— 11/13 个有
- `PreviewImage` —— 11/13 个有
- `SkipLayerGuidanceDiTSimple` —— 11/13 个有
- `Fast Groups Bypasser (rgthree)` —— 9/13 个有
- `LoadImage` —— 9/13 个有
- `RH_LLMAPI_Pro_Node` —— 9/13 个有
- `EmptyImage` —— 3/13 个有
- `easy saveText` —— 3/13 个有
- `ComfySwitchNode` —— 2/13 个有
- `TextGenerate` —— 2/13 个有
- `忽略多组孤海` —— 2/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `llama_cpp_instruct_adv` —— 1/13 个有
- `llama_cpp_model_loader` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 13 | 63% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 13 | 81% |
| 采样算法 | er_sde | - | 13 | 85% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，13 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，13 个样本，取值集中（一致性 81%）
- 采样算法 最常用 er_sde，13 个样本，一致性 85%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
