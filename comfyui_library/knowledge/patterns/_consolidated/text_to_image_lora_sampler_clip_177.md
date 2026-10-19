---
name: text_to_image_lora_sampler_clip_177
type: Text To Image
frequency: 5
level: strong
coverage: 0.8688
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图与图像编辑综合工作流，一站式创作新方案_2106507657149509633.json, 图片生成/文生图/Qwen Image 2.1文生图图像编辑综合工作流，效果出色多场景覆盖方案_2105734182998728706.json, 图片生成/文生图/Qwen Image2.1综合工作流｜文生图图像编辑换背景 AI小王子出品_2105552519928836097.json, 图片生成/文生图/Qwen Image2.1重磅综合工作流｜文生图与图像编辑高效创作新纪元_2106201754592436226.json, 视频生成/文生视频/AI角色姿态导演台Character Pose Director，文生视频图生视频姿势精准控制_2103202510185000962.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_177

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图与图像编辑综合工作流，一站式创作新方案_2106507657149509633.json、图片生成/文生图/Qwen Image 2.1文生图图像编辑综合工作流，效果出色多场景覆盖方案_2105734182998728706.json、图片生成/文生图/Qwen Image2.1综合工作流｜文生图图像编辑换背景 AI小王子出品_2105552519928836097.json、图片生成/文生图/Qwen Image2.1重磅综合工作流｜文生图与图像编辑高效创作新纪元_2106201754592436226.json、视频生成/文生视频/AI角色姿态导演台Character Pose Director，文生视频图生视频姿势精准控制_2103202510185000962.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
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
- `AnySwitch` —— 4/5 个有
- `Anything Everywhere` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `VAEEncode` —— 4/5 个有
- `GetImageSize` —— 1/5 个有
- `VNCCS_PoseStudio` —— 1/5 个有

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
