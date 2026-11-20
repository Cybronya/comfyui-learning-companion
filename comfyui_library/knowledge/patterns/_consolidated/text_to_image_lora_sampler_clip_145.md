---
name: text_to_image_lora_sampler_clip_145
type: Text To Image
frequency: 11
level: strong
coverage: 0.906909
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097150470786736129.json, 图片生成/反推提示词/Krea 2 Turbo高美学文生图｜提示词反推风格生成_2097094295093334018.json, 图片生成/反推提示词/Qwenimage2.1便捷多功能 文生图多图编辑处理工具_2113374691258888193.json, 图片生成/图生图/10图Qwen Image 2.1多图编辑工作流，图生图多图编辑处理工具_2108330608001896449.json, 图片生成/图生图/QWEN2.1图像编辑工作流｜图片精修局部修改全能处理｜图生图必备_2102213493909966850.json, 图片生成/图生图/QWen2.1图像编辑利器｜图生图轻松改图修图一键搞定_2106200271583014914.json, 图片生成/图生图/QWen2.1官方图像编辑工作流，简洁高效的图生图处理方案_2102808314856955905.json, 图片生成/图生图/QWen2.1官方图像编辑工作流，简洁高效的图生图处理方案_2106915667613143041.json, 图片生成/图生图/Qwen Image 2.1 IN 极速版全能编辑，2K超清透明通道十图极限融合_2103213714240528385.json, 图片生成/图生图/Qwen_Image_2.1去除AI感工作流，写实风格人像图生图自然质感提升_2105864806925430785.json, 图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098928781699407874.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_145

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/反推提示词/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097150470786736129.json、图片生成/反推提示词/Krea 2 Turbo高美学文生图｜提示词反推风格生成_2097094295093334018.json、图片生成/反推提示词/Qwenimage2.1便捷多功能 文生图多图编辑处理工具_2113374691258888193.json、图片生成/图生图/10图Qwen Image 2.1多图编辑工作流，图生图多图编辑处理工具_2108330608001896449.json、图片生成/图生图/QWEN2.1图像编辑工作流｜图片精修局部修改全能处理｜图生图必备_2102213493909966850.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 9/11 个有
- `LoadImage` —— 7/11 个有
- `TextEncodeQwenImage21` —— 7/11 个有
- `QwenImage21Cache` —— 6/11 个有
- `ResolutionSelector` —— 6/11 个有
- `ComfySwitchNode` —— 5/11 个有
- `CR Text` —— 4/11 个有
- `EmptyImage` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `PrimitiveBoolean` —— 4/11 个有
- `ModelSamplingAuraFlow` —— 3/11 个有
- `PathchSageAttentionKJ` —— 3/11 个有
- `easy loraStack` —— 3/11 个有
- `easy loraStackApply` —— 3/11 个有
- `ImageCompositeMasked` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `ImageStitch` —— 1/11 个有
- `LiaoQwenImage21Studio` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（14/11 个样本）：Steps较低可能导致细节不足
