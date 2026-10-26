---
name: text_to_image_lora_sampler_clip_151
type: Text To Image
frequency: 11
level: strong
coverage: 0.889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1精准扩图｜按25%或300像素延展画布，一键扩展16_9_2104507613303107585.json, 图片生成/图生图/Qwen Image 2.1角色四视图及三视图生成，图生图角色设计方案_2103618237505294338.json, 图片生成/图生图/Qwen Image 2.1透明图层抠图｜主体分离PNG直出_2103035249222574081.json, 图片生成/图生图/Qwen image 2.1二合一工作流｜万物移除与局部重绘，擦除修复全能_2104547539398778881.json, 图片生成/图生图/Qwen image2.1替换工作流_2109602458845667330.json, 图片生成/图生图/Qwen image2.1最佳换头换脸 人物面部精准替换_2104627780217561090.json, 图片生成/图生图/Qwen-image2.1万物移除工作流｜图生图一键抹除多余物体无痕迹_2104023831454244865.json, 图片生成/图生图/Qwen-image2.1扩图工作流｜图生图智能扩展画幅 边缘补全自然_2104027097525211138.json, 图片生成/图生图/万物移除加局部重绘二合一 Qwen image 2.1图像编辑工作流_2104778416783446018.json, 图片生成/图生图/画面向外扩展补全 Qwen image2.1智能扩图工作流_2104303227163467778.json, 图片生成/图生图/画面杂物一键清除 Qwen image2.1万物移除图生图编辑_2104261593684074497.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_151

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1精准扩图｜按25%或300像素延展画布，一键扩展16_9_2104507613303107585.json、图片生成/图生图/Qwen Image 2.1角色四视图及三视图生成，图生图角色设计方案_2103618237505294338.json、图片生成/图生图/Qwen Image 2.1透明图层抠图｜主体分离PNG直出_2103035249222574081.json、图片生成/图生图/Qwen image 2.1二合一工作流｜万物移除与局部重绘，擦除修复全能_2104547539398778881.json、图片生成/图生图/Qwen image2.1替换工作流_2109602458845667330.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/11 个有
- `CR Prompt Text` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/11 个有
- `DrawMaskOnImage` —— 7/11 个有
- `Int` —— 4/11 个有
- `Mask Fill Holes` —— 4/11 个有
- `ImpactSwitch` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `ImagePadForOutpaint` —— 2/11 个有
- `YYZZipImageSave` —— 1/11 个有
- `easy imageSizeByLongerSide` —— 1/11 个有
- `easy int` —— 1/11 个有
- `孤海外补画板按方向` —— 1/11 个有

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
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
