---
name: text_to_image_lora_sampler_clip_19
type: Text To Image
frequency: 25
level: strong
coverage: 0.88636
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1图像编辑修复版，角色一致性图生图抠图多场景工具_2103593422190899202.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102548100928856066.json, 图片生成/图生图/Qwen Image 2.1图像编辑基础版｜改字改色改细节｜日常修图够用了_2102634269028999170.json, 图片生成/图生图/Qwen Image 2.1图像编辑工作流，图生图图像处理方案_2107519626568622081.json, 图片生成/图生图/Qwen Image 2.1图像编辑流｜局部重绘换装一键搞定_2108041550201708545.json, 图片生成/图生图/Qwen Image 2.1图生图工作流图片编辑，商品替换换装多场景工具_2103607408328273922.json, 图片生成/图生图/Qwen Image 2.1图生图工作流图片编辑，商品替换换装多场景工具_2103971820344004609.json, 图片生成/图生图/Qwen Image 2.1多参考图生图｜标准版稳定出图首选_2105137018840899585.json, 图片生成/图生图/Qwen Image 2.1多图编辑 多张输入精准改图_2105377023228203010.json, 图片生成/图生图/Qwen Image 2.1多图编辑Multi Image Editing工作流，角色设计图生图_2106164834009174018.json, 图片生成/图生图/Qwen Image 2.1多图编辑工作流，图生图高质量图像处理方案_2107899694994247682.json, 图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换_2105790956023926785.json, 图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换工具_2105730994383974402.json, 图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换工具_2106109794053607425.json, 图片生成/图生图/Qwen Image 2.1电商换装神器｜模特服装自动替换一键完成_2103671470185603074.json, 图片生成/图生图/Qwen-Image-2.1一键扩图图生图｜写实风格扩展轻松搞定_2106928805460922369.json, 图片生成/图生图/Qwen-Image-2.1一键扩图图生图｜选区外内容智能补画｜操作零门槛_2102268788170387457.json, 图片生成/图生图/Qwen-Image-2.1一键扩图｜扩图类图生图快捷版｜其它图片处理顺带_2102277686113693698.json, 图片生成/图生图/Qwen-Image-2.1人物换头图片换脸｜换脸类图生图特效｜衔接自然不穿帮_2102290282900451330.json, 图片生成/图生图/Qwen-Image-2.1扩图实战版｜一键延展画布不违和｜其它图片处理友好_2102283966899380226.json, 图片生成/图生图/Qwen-Image-2.1换头换脸二合一｜人物头部替换与图片换脸一步搞定_2102211983704678402.json, 图片生成/图生图/qwen image 2.1编辑工作流｜文生图图生图双支持｜日常改图必备款_2102232264989036546.json, 图片生成/图生图/千问Qwen Image 2.1多图编辑｜一次处理多张素材图_2103029100855255041.json, 图片生成/文生图/Qwen Image 2.1图像编辑工作流，图生图处理高质量方案_2105774125573828610.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2107518180074807297.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图像编辑修复版，角色一致性图生图抠图多场景工具_2103593422190899202.json、图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102548100928856066.json、图片生成/图生图/Qwen Image 2.1图像编辑基础版｜改字改色改细节｜日常修图够用了_2102634269028999170.json、图片生成/图生图/Qwen Image 2.1图像编辑工作流，图生图图像处理方案_2107519626568622081.json、图片生成/图生图/Qwen Image 2.1图像编辑流｜局部重绘换装一键搞定_2108041550201708545.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 25 个 workflow 都包含：
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
- `ComfySwitchNode` —— 24/25 个有
- `LoadImage` —— 24/25 个有
- `QwenImage21Cache` —— 24/25 个有
- `ResolutionSelector` —— 22/25 个有
- `BatchImagesNode` —— 19/25 个有
- `TextGenerateLTX2Prompt` —— 16/25 个有
- `PrimitiveStringMultiline` —— 7/25 个有
- `SaveImageAdvanced` —— 6/25 个有
- `TextGenerate` —— 4/25 个有
- `PreviewAny` —— 3/25 个有
- `Fast Groups Bypasser (rgthree)` —— 2/25 个有
- `ImageCompare` —— 2/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/25 个有
- `easy imageConcat` —— 2/25 个有
- `CM_FloatToInt` —— 1/25 个有
- `CR Prompt Text` —— 1/25 个有
- `Text` —— 1/25 个有
- `TextConcatenator` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高发问题（28/25 个样本）：Steps较低可能导致细节不足
