---
name: text_to_image_lora_sampler_clip_336
type: Text To Image
frequency: 5
level: strong
coverage: 0.864
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/DLSS5人脸洗图工作流，图生图高清质感还原_2111276746967437314.json, 图片生成/图生图/FLUX 场景图无限裂变_角色一致性_图生图_2080932254032945153.json, 图片生成/图生图/Flux-高清放大_精修_图生图_2080931216911589378.json, 图片生成/图生图/G IMAGE 2.5全能15图连出｜单张0.04平价出图_2098752661825875969.json, 图片生成/图生图/千府AI DLSS5洗图图生图处理生成工作流_2102177419565297665.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_336

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/DLSS5人脸洗图工作流，图生图高清质感还原_2111276746967437314.json、图片生成/图生图/FLUX 场景图无限裂变_角色一致性_图生图_2080932254032945153.json、图片生成/图生图/Flux-高清放大_精修_图生图_2080931216911589378.json、图片生成/图生图/G IMAGE 2.5全能15图连出｜单张0.04平价出图_2098752661825875969.json、图片生成/图生图/千府AI DLSS5洗图图生图处理生成工作流_2102177419565297665.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
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
- `CR Prompt Text` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `RH_DLSS5Enhance` —— 2/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `ImageCASharpening+` —— 1/5 个有
- `Seedance_Config` —— 1/5 个有
- `ShunjingAIShade` —— 1/5 个有
- `UltimateSDUpscale` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有
- `Zhenzhen_Image_G25_Lowprice` —— 1/5 个有
- `workflow>场景图裂变` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
