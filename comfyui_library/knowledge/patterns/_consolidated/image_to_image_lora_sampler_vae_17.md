---
name: image_to_image_lora_sampler_vae_17
type: Image To Image
frequency: 6
level: strong
coverage: 0.935
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen换装_1972259814439055362.json, 图片生成/图生图/qwen真人转网红手办_3D_盲盒手办_效果堪比Naon 全能图片V1_1989295548085751810.json, 图片生成/图生图/qwen编辑 人物转手办_1959056979866103809.json, 图片生成/图生图/图片转桌面手办（Qwen+编辑）_1962479307606110209.json, 图片生成/图生图/服装消失qwen_1960328722777894913.json, 图片生成/文生图/qwen编辑 提示词合集_1959223893091364865.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_17

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/qwen换装_1972259814439055362.json、图片生成/图生图/qwen真人转网红手办_3D_盲盒手办_效果堪比Naon 全能图片V1_1989295548085751810.json、图片生成/图生图/qwen编辑 人物转手办_1959056979866103809.json、图片生成/图生图/图片转桌面手办（Qwen+编辑）_1962479307606110209.json、图片生成/图生图/服装消失qwen_1960328722777894913.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `JjkText` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `easy imageConcat` —— 2/6 个有
- `CLIPTextEncode` —— 1/6 个有
- `CR Prompt List` —— 1/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `Image Remove Background Rembg (mtb)` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `JWImageResizeByLongerSide` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 6 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 928 | - | 1 | 100% |
| 高度 | 1664 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
