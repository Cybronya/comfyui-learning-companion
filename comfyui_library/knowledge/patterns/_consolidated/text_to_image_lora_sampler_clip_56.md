---
name: text_to_image_lora_sampler_clip_56
type: Text To Image
frequency: 17
level: strong
coverage: 0.884529
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1一键融图｜透视光影让产品自然融入背景_2111096424543903746.json, 图片生成/图生图/Qwen Image 2.1一键透视光影融图产品完美融入背景 产品图融合方案_2109742070738014209.json, 图片生成/图生图/Qwen Image 2.1一键透视光影融图产品完美融入背景 产品图融合方案_2109776737675595778.json, 图片生成/图生图/Qwen Image 2.1人物姿势图转白模工作流，人物角色图生图处理工具_2108305851978182657.json, 图片生成/图生图/Qwen Image 2.1人物姿势图转白模｜角色动作参考一键转换_2108021000834215937.json, 图片生成/图生图/Qwen Image 2.1人物转白模工作流，图生图人物白模处理工具_2108284091366989826.json, 图片生成/图生图/Qwen Image 2.1动作迁移2工作流，图生图动作迁移处理工具_2107952880333443074.json, 图片生成/图生图/Qwen Image 2.1动漫转真人工作流，图生图动漫风格转换处理工具_2108307387378659329.json, 图片生成/图生图/Qwen Image 2.1动漫转真人｜二次元角色写实化一秒落地_2108031740731289601.json, 图片生成/图生图/Qwen Image 2.1单图编辑4步加速版，高效图生图处理工具_2103183698848993281.json, 图片生成/图生图/Qwen Image 2.1单图编辑｜4步加速版出图快人一步_2103053267889639426.json, 图片生成/图生图/Qwen Image 2.1参考图融合编辑ref2i，多图参考身份保持图生图方案_2103215198285946882.json, 图片生成/图生图/Qwen Image 2.1图片编辑神器｜配饰配件随心换_2103041179548995585.json, 图片生成/图生图/Qwen Image 2.1图片编辑配件可用，帽子等配饰换装图生图工具_2103195052028813313.json, 图片生成/图生图/Qwen Image 2.1图生图处理生成工具_2102468898800095234.json, 图片生成/图生图/Qwen Image 2.1超细节多图像编辑，最多十一张参考图局部重绘风格化_2102875534593183745.json, 图片生成/图生图/Qwen_Image_2.1超细节多图像编辑，最多十一张参考图局部重绘风格化_2105123251163848705.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1一键融图｜透视光影让产品自然融入背景_2111096424543903746.json、图片生成/图生图/Qwen Image 2.1一键透视光影融图产品完美融入背景 产品图融合方案_2109742070738014209.json、图片生成/图生图/Qwen Image 2.1一键透视光影融图产品完美融入背景 产品图融合方案_2109776737675595778.json、图片生成/图生图/Qwen Image 2.1人物姿势图转白模工作流，人物角色图生图处理工具_2108305851978182657.json、图片生成/图生图/Qwen Image 2.1人物姿势图转白模｜角色动作参考一键转换_2108021000834215937.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
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
- `孤海注释` —— 16/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/17 个有
- `Image Comparer (rgthree)` —— 10/17 个有
- `PreviewImage` —— 7/17 个有
- `ImpactInt` —— 5/17 个有
- `ResolutionSelector` —— 5/17 个有
- `easy seed` —— 5/17 个有
- `QwenImage21Cache` —— 4/17 个有
- `ComfySwitchNode` —— 3/17 个有
- `KSampler (Efficient)` —— 3/17 个有
- `Text Multiline` —— 3/17 个有
- `EmptyImage` —— 2/17 个有
- `INTConstant` —— 2/17 个有
- `QwenImage21PromptEnhancerT8` —— 2/17 个有
- `easy showAnything` —— 2/17 个有
- `Int` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（19/17 个样本）：Steps较低可能导致细节不足
