---
name: text_to_image_lora_sampler_clip_199
type: Text To Image
frequency: 9
level: strong
coverage: 0.879889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1替换主体工作流，图生图主体更换处理方案_2103910976172154882.json, 图片生成/图生图/Qwen2.1漫转真｜图生图漫画转写实 二次元一键变真人质感_2104112523195801601.json, 图片生成/图生图/Qwen2.1自定义修改工作流，千问驱动图生图自定义编辑工具_2103912464470597634.json, 图片生成/图生图/Qwen_Image_2.1单图编辑角色四视图工作流，角色设计图生图处理工具_2110158334325256194.json, 图片生成/图生图/Qwen_Image_2.1图生图工作流，人像写真风格化图生图处理方案_2109102844388397058.json, 图片生成/图生图/qwen2.1去除卡片 图片元素精准移除_2104692967377293313.json, 图片生成/图生图/qwen2.1去除油腻｜图生图人像修图 AI感一扫自然出片_2104109391455809538.json, 图片生成/图生图/qwen2.1替换主体工作流｜产品模特随意换场景不翻车_2103712617431912449.json, 图片生成/图生图/画面去油腻 qwen2.1图片质感清爽优化_2104333923810635777.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_199

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen2.1替换主体工作流，图生图主体更换处理方案_2103910976172154882.json、图片生成/图生图/Qwen2.1漫转真｜图生图漫画转写实 二次元一键变真人质感_2104112523195801601.json、图片生成/图生图/Qwen2.1自定义修改工作流，千问驱动图生图自定义编辑工具_2103912464470597634.json、图片生成/图生图/Qwen_Image_2.1单图编辑角色四视图工作流，角色设计图生图处理工具_2110158334325256194.json、图片生成/图生图/Qwen_Image_2.1图生图工作流，人像写真风格化图生图处理方案_2109102844388397058.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 8/9 个有
- `Anything Everywhere3` —— 7/9 个有
- `孤海注释` —— 7/9 个有
- `Text` —— 6/9 个有
- `ImageToMask` —— 5/9 个有
- `PixaromaInpaintCrop` —— 5/9 个有
- `PixaromaUncrop` —— 5/9 个有
- `ImageColorMatch+` —— 3/9 个有
- `EmptyImage` —— 2/9 个有
- `Image Remove Alpha JK` —— 2/9 个有
- `ResolutionSelector` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
