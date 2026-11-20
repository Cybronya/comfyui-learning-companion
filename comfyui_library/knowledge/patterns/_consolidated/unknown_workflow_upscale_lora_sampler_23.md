---
name: unknown_workflow_upscale_lora_sampler_23
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.739909
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, INTConstant, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS 认清 19 种拍摄角度_2116594503158157313.json, 图片生成/文生图/Moss 模型融合工作流_2115114419226238978.json, 图片生成/文生图/moss-prompt-短剧角色定妆照_2114013825287680002.json, 图片生成/文生图/【Moss-image】【二次元角色设计】_2114889859943976962.json, 图片生成/文生图/【Moss-image】文生图_2113267040969646081.json, 图片生成/文生图/文生图 可调MOSS_2115033252464521218.json, 图片生成/文生图/文生图海报8K特写_2114022887387656193.json, 平台全量/MOSS 真实世界_2118012614012915713.json, 平台全量/MOSS 真实世界宝丽来拍立得风格 LoRA_2118030150209196034.json, 平台全量/MOSS-堪比全能图片G2[文生图]_2118662997282480130.json, 平台全量/【WorkFisher】全能生图王 _ 适配所有类型_2120386694309572610.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/MOSS 认清 19 种拍摄角度_2116594503158157313.json、图片生成/文生图/Moss 模型融合工作流_2115114419226238978.json、图片生成/文生图/moss-prompt-短剧角色定妆照_2114013825287680002.json、图片生成/文生图/【Moss-image】【二次元角色设计】_2114889859943976962.json、图片生成/文生图/【Moss-image】文生图_2113267040969646081.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 10/11 个有
- `RH_LLMAPI_Pro_Node` —— 8/11 个有
- `Image Comparer (rgthree)` —— 7/11 个有
- `Fast Groups Bypasser (rgthree)` —— 5/11 个有
- `MOSSMergePreset` —— 5/11 个有
- `TextGenerate` —— 5/11 个有
- `llama_cpp_instruct_adv` —— 5/11 个有
- `llama_cpp_model_loader` —— 5/11 个有
- `CR Text Input Switch (4 way)` —— 4/11 个有
- `LoadImage` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `FastGroupsBypassSwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 11 | 65% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 11 | 80% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，11 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
