---
name: unknown_workflow_lora_sampler_clip_116
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.865
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, GetImageSize, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/加背景  产品换背景  产品展示   电商图制作_2067167781539373058.json, 图片生成/图生图/加背景  电商图制作   产品展示   产品图换背景_2067118048594718722.json, 图片生成/图生图/千问编辑模型--漫画转真人快速实现_1959596505768341506.json, 图片生成/图生图/换背景-产品白底图自动匹配背景_1977027027687612418.json, 平台全量/产品白底图自动匹配场景背景 电商产品展示 电商专用_2021153665704267777.json, 平台全量/产品白底图自动匹配背景_电商专用_2021115949344100353.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_116

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/加背景  产品换背景  产品展示   电商图制作_2067167781539373058.json、图片生成/图生图/加背景  电商图制作   产品展示   产品图换背景_2067118048594718722.json、图片生成/图生图/千问编辑模型--漫画转真人快速实现_1959596505768341506.json、图片生成/图生图/换背景-产品白底图自动匹配背景_1977027027687612418.json、平台全量/产品白底图自动匹配场景背景 电商产品展示 电商专用_2021153665704267777.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V` —— 5/6 个有
- `CR Latent Input Switch` —— 5/6 个有
- `CR Text` —— 5/6 个有
- `CR Text Concatenate` —— 5/6 个有
- `FluxKontextImageScale` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `PreviewAny` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `ShowText|pysssss` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
