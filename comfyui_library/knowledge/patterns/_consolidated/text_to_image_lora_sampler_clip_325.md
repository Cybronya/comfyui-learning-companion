---
name: text_to_image_lora_sampler_clip_325
type: Text To Image
frequency: 6
level: strong
coverage: 0.898
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux-高清放大_精修_图生图_2080931216911589378.json, 图片生成/图生图/Flux3 Klein图像编辑 局部重绘图生图处理生成工具_2112991480737521665.json, 图片生成/图生图/G IMAGE 2.5全能15图连出｜单张0.04平价出图_2098752661825875969.json, 图片生成/图生图/flux3 klein image edit图像编辑｜局部重绘改图不掉质感_2112861866576924674.json, 图片生成/图生图/flux3_klein_image_edit九图批量图像编辑｜图生图党福音_2111266093682745346.json, 图片生成/图生图/flux3_klein_image_edit图像编辑，角色一致性换装_2111568626292707329.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_325

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux-高清放大_精修_图生图_2080931216911589378.json、图片生成/图生图/Flux3 Klein图像编辑 局部重绘图生图处理生成工具_2112991480737521665.json、图片生成/图生图/G IMAGE 2.5全能15图连出｜单张0.04平价出图_2098752661825875969.json、图片生成/图生图/flux3 klein image edit图像编辑｜局部重绘改图不掉质感_2112861866576924674.json、图片生成/图生图/flux3_klein_image_edit九图批量图像编辑｜图生图党福音_2111266093682745346.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 5/6 个有
- `JjkText` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `ReferenceMultiLatent` —— 4/6 个有
- `TextGenerate` —— 4/6 个有
- `CR Prompt Text` —— 2/6 个有
- `DualCLIPLoader` —— 1/6 个有
- `Seedance_Config` —— 1/6 个有
- `UltimateSDUpscale` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有
- `Zhenzhen_Image_G25_Lowprice` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
