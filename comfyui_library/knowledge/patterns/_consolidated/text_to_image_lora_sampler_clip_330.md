---
name: text_to_image_lora_sampler_clip_330
type: Text To Image
frequency: 6
level: strong
coverage: 0.8655
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2二次元转真人 动漫角色写实化工作流_2098816280273965057.json, 图片生成/图生图/Krea2图生四视图图生图处理生成工作流工具_2101759217957949442.json, 图片生成/图生图/VOSR2图像高清放大工作流 图片超分辨率增强_2099949349093597185.json, 图片生成/图生图/VOSR2图像高清放大工作流 图片超分辨率增强_2100311895210287105.json, 图片生成/图生图/无提示词极速图生图 Krea2加MJ美学风格 照片级质感_2108980279997198337.json, 图片生成/图生图/最强动漫转真实Krea2双采加高清放大 动漫风格转写实_2108671339107278849.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_330

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea2二次元转真人 动漫角色写实化工作流_2098816280273965057.json、图片生成/图生图/Krea2图生四视图图生图处理生成工作流工具_2101759217957949442.json、图片生成/图生图/VOSR2图像高清放大工作流 图片超分辨率增强_2099949349093597185.json、图片生成/图生图/VOSR2图像高清放大工作流 图片超分辨率增强_2100311895210287105.json、图片生成/图生图/无提示词极速图生图 Krea2加MJ美学风格 照片级质感_2108980279997198337.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `VOSR2ModelLoader` —— 5/6 个有
- `VOSR2Upscale` —— 5/6 个有
- `Krea2OstrisEditModelPatch` —— 4/6 个有
- `VAEEncode` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `PrimitiveInt` —— 3/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `PDIMAGE_LongerSize` —— 2/6 个有
- `TextEncodeKrea2OstrisEdit` —— 2/6 个有
- `easy imageSave` —— 2/6 个有
- `CR Apply LoRA Stack` —— 1/6 个有
- `CR LoRA Stack` —— 1/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `TextEncodeQwenImageEditPlus` —— 1/6 个有
- `workflow>Krea 2 Ostris Edit` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（11/6 个样本）：Steps较低可能导致细节不足
