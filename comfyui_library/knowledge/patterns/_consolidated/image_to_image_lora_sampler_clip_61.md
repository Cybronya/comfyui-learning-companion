---
name: image_to_image_lora_sampler_clip_61
type: Image To Image
frequency: 5
level: strong
coverage: 0.9306
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键挂拍_平铺图转立体图-电商服饰展示 服饰提取 3D立体图_2053737452044599298.json, 图片生成/图生图/一键通道图(klein2)_2077597343460978690.json, 图片生成/图生图/一键通道图(klein2)_2081910991482343426.json, 图片生成/图生图/保持图像一致性Flux2-Klein-9B-Consis-Lora（工作流示例）_2031294897893937154.json, 图片生成/图生图/保持图像一致性提示词换场景_2031770431706894338.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_61

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键挂拍_平铺图转立体图-电商服饰展示 服饰提取 3D立体图_2053737452044599298.json、图片生成/图生图/一键通道图(klein2)_2077597343460978690.json、图片生成/图生图/一键通道图(klein2)_2081910991482343426.json、图片生成/图生图/保持图像一致性Flux2-Klein-9B-Consis-Lora（工作流示例）_2031294897893937154.json、图片生成/图生图/保持图像一致性提示词换场景_2031770431706894338.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LayerUtility: FluxKontextImageScale` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SeedVR2LoadDiTModel` —— 1/5 个有
- `SeedVR2LoadVAEModel` —— 1/5 个有
- `SeedVR2VideoUpscaler` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 5 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 5，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（9/5 个样本）：Steps较低可能导致细节不足
