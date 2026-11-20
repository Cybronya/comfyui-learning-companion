---
name: unknown_workflow_sampler_clip_unet_30
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.73325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/MOSS image 提示增强_反推_风格参考 全能流_2113532439992823810.json, 图片生成/反推提示词/MOSS image 日系摄影风格_2114718978487709698.json, 图片生成/反推提示词/MOSS 高分辨率适配器_2114926721924419585.json, 图片生成/反推提示词/MOSS_Kromoss_8Step_8步 全能生图王 _ 适配所有类型_2115061221979410434.json, 图片生成/反推提示词/MoSS-sft 全能生图王 _ 适配所有类型_2114718090054430722.json, 图片生成/反推提示词/Moss 洗图 图片反推_2113119843267469314.json, 图片生成/反推提示词/【WorkFisher】全能生图王 _ 适配所有类型_2112563481311535106.json, 图片生成/图生图/moss-prompt-文生图+图生图_2113432801054904322.json, 图片生成/图生图/【WorkFisher】全能生图王_适配所有类型_2113453468659834882.json, 图片生成/文生图/MOSS_Beauty_人像美感创作_2115056903393992706.json, 图片生成/文生图/MOSS_SFT_风格实验_2115047167877537794.json, 图片生成/文生图/Moss image 官方文生图_2112078306463019010.json, 图片生成/文生图/Moss image 文生图角色资产生成+真实美感【提示词增强】_2112449151177940994.json, 图片生成/文生图/moss-prompt-RH版本角色定妆照_2114038844743049217.json, 图片生成/文生图/moss全能生图_2113226191116267522.json, 平台全量/MOSS_Beauty_人像美感创作_2117903904150216705.json, 平台全量/MOSS_Kromoss_8Step_8步 全能生图王_2119692635848925186.json, 平台全量/【Moss-image】角色设定卡_2119588333532835842.json, 视频生成/图生视频/【WorkFisher】全能生图王_适配所有类型_2113792326656151554.json, 视频生成/图生视频/【WorkFisher】全能生图王_适配所有类型_2113803846358228994.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/反推提示词/MOSS image 提示增强_反推_风格参考 全能流_2113532439992823810.json、图片生成/反推提示词/MOSS image 日系摄影风格_2114718978487709698.json、图片生成/反推提示词/MOSS 高分辨率适配器_2114926721924419585.json、图片生成/反推提示词/MOSS_Kromoss_8Step_8步 全能生图王 _ 适配所有类型_2115061221979410434.json、图片生成/反推提示词/MoSS-sft 全能生图王 _ 适配所有类型_2114718090054430722.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 19/20 个有
- `ImageScaleToTotalPixels` —— 17/20 个有
- `SeedVR2LoadDiTModel` —— 17/20 个有
- `SeedVR2LoadVAEModel` —— 17/20 个有
- `SeedVR2VideoUpscaler` —— 17/20 个有
- `SkipLayerGuidanceDiTSimple` —— 17/20 个有
- `RH_LLMAPI_Pro_Node` —— 16/20 个有
- `Fast Groups Bypasser (rgthree)` —— 15/20 个有
- `INTConstant` —— 15/20 个有
- `LoadImage` —— 15/20 个有
- `PreviewImage` —— 15/20 个有
- `Image Comparer (rgthree)` —— 14/20 个有
- `Anything Everywhere3` —— 7/20 个有
- `ComfySwitchNode` —— 4/20 个有
- `TextEncodeMOSSImageOstrisEdit` —— 4/20 个有
- `TextGenerate` —— 4/20 个有
- `EmptyImage` —— 3/20 个有
- `easy saveText` —— 3/20 个有
- `忽略多组孤海` —— 3/20 个有
- `PrimitiveBoolean` —— 2/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 20 | 60% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 20 | 73% |
| 采样算法 | er_sde | - | 20 | 70% |
| 调度器 | simple | - | 20 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，20 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，20 个样本
- 采样算法 最常用 er_sde，20 个样本，一致性 70%
- 调度器 最常用 simple，20 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
