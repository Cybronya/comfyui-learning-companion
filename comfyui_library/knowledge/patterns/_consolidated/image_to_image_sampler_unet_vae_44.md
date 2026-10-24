---
name: image_to_image_sampler_unet_vae_44
type: Image To Image
frequency: 5
level: strong
coverage: 0.821
common_nodes: [CLIPLoader, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 - Klein _  九宫格分镜_2015362104047443970.json, 图片生成/图生图/Flux2 Klein 图像重构-线色分离组合_2017242186005356545.json, 图片生成/图生图/Klein完美一致性分镜图制作_2021413605844979714.json, 图片生成/图生图/切换镜头klein9b_2037790414211653633.json, 图片生成/图生图/应用级：写真写意+多角度，千问编辑模型，和风整理。_2008029412943466498.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_44

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2 - Klein _  九宫格分镜_2015362104047443970.json、图片生成/图生图/Flux2 Klein 图像重构-线色分离组合_2017242186005356545.json、图片生成/图生图/Klein完美一致性分镜图制作_2021413605844979714.json、图片生成/图生图/切换镜头klein9b_2037790414211653633.json、图片生成/图生图/应用级：写真写意+多角度，千问编辑模型，和风整理。_2008029412943466498.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `Qwen3_VQA` —— 4/5 个有
- `easy promptLine` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `EmptyFlux2LatentImage` —— 3/5 个有
- `JWStringConcat` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `Anything Everywhere` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `ProcessString` —— 1/5 个有
- `ResizeImagesByLongerEdge` —— 1/5 个有
- `TextEncodeQwenImageEdit` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 5 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
