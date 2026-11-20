---
name: text_to_image_lora_sampler_clip_72
type: Text To Image
frequency: 16
level: strong
coverage: 0.870062
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1图片编辑神器｜配饰配件随心换_2103041179548995585.json, 图片生成/图生图/Qwen Image 2.1图片编辑配件可用，帽子等配饰换装图生图工具_2103195052028813313.json, 图片生成/图生图/Qwen Image 2.1图片编辑，简洁实用的图生图处理工作流_2103255755200749569.json, 图片生成/图生图/Qwen Image 2.1图生图处理生成工具_2102468898800095234.json, 图片生成/图生图/Qwen Image 2.1图生图工作流图片编辑，商品替换换装多场景工具_2103607408328273922.json, 图片生成/图生图/Qwen Image 2.1图生图工作流图片编辑，商品替换换装多场景工具_2103971820344004609.json, 图片生成/图生图/Qwen Image 2.1图生图提示词增强处理生成工具_2102560585291493377.json, 图片生成/图生图/Qwen Image 2.1多图编辑工作流，图生图高质量图像处理方案_2107899694994247682.json, 图片生成/图生图/Qwen Image 2.1多图编辑工作流，多图融合局部修改精准控制高效出图_2114433401469095937.json, 图片生成/图生图/Qwen Image 2.1多图编辑工作流，多张参考图同时编辑的图生图方案_2103201028756824065.json, 图片生成/图生图/Qwen Image 2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2102833574943744001.json, 图片生成/图生图/Qwen Image 2.1多图编辑工作流｜角色一致性轻松保｜批量改图不跑脸_2102623788155363330.json, 图片生成/图生图/Qwen Image 2.1多图编辑提示词增强in 版图生图处理工具_2102480198032781314.json, 图片生成/图生图/qwen image 2.1编辑工作流｜文生图图生图双支持｜日常改图必备款_2102232264989036546.json, 视频生成/图生视频/Qwen_Image_2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2106172420255207425.json, 视频生成/图生视频/qwen_image_2.1编辑工作流｜文生图图生图双支持｜日常改图必备款_2102310384794427394.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图片编辑神器｜配饰配件随心换_2103041179548995585.json、图片生成/图生图/Qwen Image 2.1图片编辑配件可用，帽子等配饰换装图生图工具_2103195052028813313.json、图片生成/图生图/Qwen Image 2.1图片编辑，简洁实用的图生图处理工作流_2103255755200749569.json、图片生成/图生图/Qwen Image 2.1图生图处理生成工具_2102468898800095234.json、图片生成/图生图/Qwen Image 2.1图生图工作流图片编辑，商品替换换装多场景工具_2103607408328273922.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
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
- `ComfySwitchNode` —— 15/16 个有
- `ResolutionSelector` —— 15/16 个有
- `孤海注释` —— 14/16 个有
- `QwenImage21Cache` —— 13/16 个有
- `BatchImagesNode` —— 11/16 个有
- `TextGenerateLTX2Prompt` —— 11/16 个有
- `PrimitiveStringMultiline` —— 10/16 个有
- `easy showAnything` —— 9/16 个有
- `Fast Groups Bypasser (rgthree)` —— 5/16 个有
- `PrimitiveBoolean` —— 5/16 个有
- `Fast Groups Muter (rgthree)` —— 3/16 个有
- `Image Comparer (rgthree)` —— 3/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/16 个有
- `PreviewImage` —— 3/16 个有
- `SaveImageAdvanced` —— 3/16 个有
- `EmptyImage` —— 2/16 个有
- `ImageMergeNode` —— 2/16 个有
- `QwenImage21PromptEnhancerT8` —— 2/16 个有
- `ImageConcatMulti` —— 1/16 个有
- `ImpactConditionalBranch` —— 1/16 个有
- `Int` —— 1/16 个有
- `Text Multiline` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（18/16 个样本）：Steps较低可能导致细节不足
