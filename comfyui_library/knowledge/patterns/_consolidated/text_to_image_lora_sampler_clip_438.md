---
name: text_to_image_lora_sampler_clip_438
type: Text To Image
frequency: 4
level: strong
coverage: 0.887
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2.1心宝溶图打光｜18种光效11种光照方向｜产品图光影自由调_2112107722241044481.json, 图片生成/图生图/Qwen image 2.1角色四视图极速版｜4或8步加速秒出设定图_2103680364186259458.json, 图片生成/图生图/Qwen-Image-2.1一键抠图｜电商产品照透明背景自动生成_2105114072894238722.json, 图片生成/图生图/心宝全能打光18种光效11向｜溶图打光一板搞定_2111300395590053890.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_438

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1心宝溶图打光｜18种光效11种光照方向｜产品图光影自由调_2112107722241044481.json、图片生成/图生图/Qwen image 2.1角色四视图极速版｜4或8步加速秒出设定图_2103680364186259458.json、图片生成/图生图/Qwen-Image-2.1一键抠图｜电商产品照透明背景自动生成_2105114072894238722.json、图片生成/图生图/心宝全能打光18种光效11向｜溶图打光一板搞定_2111300395590053890.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `XinbaoImageStandardizer` —— 2/4 个有
- `XinbaoLightingCompanion` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `DapaoImagePadDirectionNode` —— 1/4 个有
- `Float` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
