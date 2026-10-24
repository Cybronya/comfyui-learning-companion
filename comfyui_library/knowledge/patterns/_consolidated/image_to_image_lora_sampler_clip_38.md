---
name: image_to_image_lora_sampler_clip_38
type: Image To Image
frequency: 7
level: moderate
coverage: 0.862857
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux1-kontext图像转绘--换上黑色连体紧身乳胶衣_1948047861566058497.json, 图片生成/图生图/Flux1-kontext图像转绘--画面镜头拉远_1948030689980624898.json, 图片生成/图生图/Flux1-kontext图像转绘--蓝色水晶化_1948037999742332929.json, 图片生成/图生图/Flux1-kontext图像转绘-定格黏土效果_1948375118293676033.json, 图片生成/图生图/Flux1-kontext图像转绘-手绘美漫_1948401596431511554.json, 图片生成/图生图/IP图像三视图生成工作流_2046911147395256321.json, 图片生成/图生图/kontext万物迁移（产品替换+光影融合）_1948345697857863681.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux1-kontext图像转绘--换上黑色连体紧身乳胶衣_1948047861566058497.json、图片生成/图生图/Flux1-kontext图像转绘--画面镜头拉远_1948030689980624898.json、图片生成/图生图/Flux1-kontext图像转绘--蓝色水晶化_1948037999742332929.json、图片生成/图生图/Flux1-kontext图像转绘-定格黏土效果_1948375118293676033.json、图片生成/图生图/Flux1-kontext图像转绘-手绘美漫_1948401596431511554.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
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
- `EmptySD3LatentImage` —— 3/7 个有
- `FluxKontextImageScale` —— 3/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `ImageConcanate` —— 3/7 个有
- `MZ_Flux1PartialLoad_Patch` —— 3/7 个有
- `GetNode` —— 2/7 个有
- `ImpactSwitch` —— 2/7 个有
- `PIP_图像联结` —— 2/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `FastCanvas` —— 1/7 个有
- `FastCanvasTool` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `easy imageRemBg` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 57% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
