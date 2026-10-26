---
name: text_to_image_lora_sampler_clip_150
type: Text To Image
frequency: 11
level: strong
coverage: 0.871091
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1图像编辑修复版，角色一致性图生图抠图多场景工具_2103593422190899202.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102548100928856066.json, 图片生成/图生图/Qwen Image 2.1图像编辑基础版｜改字改色改细节｜日常修图够用了_2102634269028999170.json, 图片生成/图生图/Qwen Image 2.1图像编辑工作流，图生图图像处理方案_2107519626568622081.json, 图片生成/图生图/Qwen Image 2.1图像编辑流｜局部重绘换装一键搞定_2108041550201708545.json, 图片生成/图生图/Qwen Image 2.1图生图工作流图片编辑，商品替换换装多场景工具_2103607408328273922.json, 图片生成/图生图/Qwen Image 2.1图生图工作流图片编辑，商品替换换装多场景工具_2103971820344004609.json, 图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102105087035400194.json, 图片生成/图生图/Qwen image 2.1图片编辑｜图生图改图如此简单 指哪改哪_2105534138802593793.json, 图片生成/文生图/QWen2.1文生图工作流｜千问模型文字生图轻松创作_2106996835603800065.json, 图片生成/文生图/Qwen 2.1文生图工作流，高质量文本到图像生成方案_2107183009446326274.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_150

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图像编辑修复版，角色一致性图生图抠图多场景工具_2103593422190899202.json、图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102548100928856066.json、图片生成/图生图/Qwen Image 2.1图像编辑基础版｜改字改色改细节｜日常修图够用了_2102634269028999170.json、图片生成/图生图/Qwen Image 2.1图像编辑工作流，图生图图像处理方案_2107519626568622081.json、图片生成/图生图/Qwen Image 2.1图像编辑流｜局部重绘换装一键搞定_2108041550201708545.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 10/11 个有
- `QwenImage21Cache` —— 10/11 个有
- `LoadImage` —— 9/11 个有
- `ResolutionSelector` —— 8/11 个有
- `PrimitiveStringMultiline` —— 6/11 个有
- `SaveImageAdvanced` —— 6/11 个有
- `TextGenerate` —— 5/11 个有
- `PreviewAny` —— 4/11 个有
- `BatchImagesNode` —— 3/11 个有
- `CR Prompt Text` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `ImageCompare` —— 2/11 个有
- `PrimitiveBoolean` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `CM_FloatToInt` —— 1/11 个有
- `QwenPERewriteT8` —— 1/11 个有
- `Text` —— 1/11 个有
- `TextConcatenator` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

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
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
