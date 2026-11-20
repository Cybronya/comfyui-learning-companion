---
name: unknown_workflow_lora_sampler_unet_126
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.957833
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea-2-服装转移 服装试穿faster_2079840692469325825.json, 图片生成/图生图/Krea2 漫剧角色资产一键生成工作流｜图生四视图_2099734867792719874.json, 图片生成/图生图/Krea2+Edit换装(等节点更新后使用）_2078520678537588738.json, 图片生成/图生图/Krea2+Edit转黏土动画风_2077072505352839170.json, 图片生成/图生图/krea2普通pose12_2092505596032540674.json, 平台全量/001-krea2_controlnet_pose_2087013784668954625.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_126

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea-2-服装转移 服装试穿faster_2079840692469325825.json、图片生成/图生图/Krea2 漫剧角色资产一键生成工作流｜图生四视图_2099734867792719874.json、图片生成/图生图/Krea2+Edit换装(等节点更新后使用）_2078520678537588738.json、图片生成/图生图/Krea2+Edit转黏土动画风_2077072505352839170.json、图片生成/图生图/krea2普通pose12_2092505596032540674.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
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
- `FluxKontextImageScale` —— 5/6 个有
- `TextEncodeKrea2OstrisEdit` —— 5/6 个有
- `EmptyLatentImage` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `PreviewImage` —— 3/6 个有
- `DWPreprocessor` —— 2/6 个有
- `Easy_QwenEdit2509` —— 1/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `OpenposePreprocessor` —— 1/6 个有
- `ShowText|fofo` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `TextGenerate` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有
- `kkPadImageToCanvas` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 6 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，6 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
