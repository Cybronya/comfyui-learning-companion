---
name: unknown_workflow_lora_sampler_unet_139
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9684
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea-2-服装转移 服装试穿faster_2079840692469325825.json, 图片生成/图生图/Krea2 漫剧角色资产一键生成工作流｜图生四视图_2099734867792719874.json, 图片生成/图生图/Krea2+Edit换装(等节点更新后使用）_2078520678537588738.json, 图片生成/图生图/Krea2+Edit转黏土动画风_2077072505352839170.json, 图片生成/图生图/krea2普通pose12_2092505596032540674.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_139

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Krea-2-服装转移 服装试穿faster_2079840692469325825.json、图片生成/图生图/Krea2 漫剧角色资产一键生成工作流｜图生四视图_2099734867792719874.json、图片生成/图生图/Krea2+Edit换装(等节点更新后使用）_2078520678537588738.json、图片生成/图生图/Krea2+Edit转黏土动画风_2077072505352839170.json、图片生成/图生图/krea2普通pose12_2092505596032540674.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `Krea2OstrisEditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 4/5 个有
- `TextEncodeKrea2OstrisEdit` —— 4/5 个有
- `EmptyLatentImage` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `DWPreprocessor` —— 1/5 个有
- `Easy_QwenEdit2509` —— 1/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `ShowText|fofo` —— 1/5 个有
- `TextGenerate` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有
- `kkPadImageToCanvas` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
