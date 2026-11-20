---
name: text_to_image_lora_sampler_clip_301
type: Text To Image
frequency: 7
level: strong
coverage: 0.859286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/拼接参考工作流，配合分镜流使用的多图参考拼接图生图工具_2103538070481096706.json, 图片生成/图生图/漫剧分镜工作流｜全能图片2角色一致四格出图｜AI漫剧分镜一步成_2099135891058024450.json, 图片生成/文生图/Image-2.5图片编辑极速版 全能图片G2.5快速处理_2098306932686802946.json, 图片生成/文生图/Qwen Image 2.1一体化文生图工作流，7B模型2K高清RGBA透明直出方案_2103624543020601346.json, 图片生成/文生图/Qwen Image 2.1写实文生图 高质量画面一键直出_2104277798167859202.json, 图片生成/文生图/Qwen Image 2.1写实文生图｜图生图双模式 文生图质感稳定在线_2104101053124931586.json, 图片生成/文生图/Qwen_Image_2.1文生图工作流｜零门槛直出创意画面_2110761065725382658.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_301

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/拼接参考工作流，配合分镜流使用的多图参考拼接图生图工具_2103538070481096706.json、图片生成/图生图/漫剧分镜工作流｜全能图片2角色一致四格出图｜AI漫剧分镜一步成_2099135891058024450.json、图片生成/文生图/Image-2.5图片编辑极速版 全能图片G2.5快速处理_2098306932686802946.json、图片生成/文生图/Qwen Image 2.1一体化文生图工作流，7B模型2K高清RGBA透明直出方案_2103624543020601346.json、图片生成/文生图/Qwen Image 2.1写实文生图 高质量画面一键直出_2104277798167859202.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 6/7 个有
- `ResolutionSelector` —— 5/7 个有
- `TextEncodeQwenImage21` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `ModelAttentionBackend` —— 3/7 个有
- `SaveImageAdvanced` —— 3/7 个有
- `ImageConcanate` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `RH_Nano_Banana2_Image2Image_Batch` —— 1/7 个有
- `RH_RhartImageG25OfficialTokenFlareEdit` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
