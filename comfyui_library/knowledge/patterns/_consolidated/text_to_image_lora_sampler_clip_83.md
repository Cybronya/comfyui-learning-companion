---
name: text_to_image_lora_sampler_clip_83
type: Text To Image
frequency: 14
level: strong
coverage: 0.885929
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json, 图片生成/反推提示词/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json, 图片生成/反推提示词/Qwen Image 2.1图像编辑 反推提示词图生图处理工具_2113056983065653250.json, 图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json, 图片生成/图生图/Qwen 2.1图像编辑4步加速，电商产品图生图多场景处理工作流_2103186678771970050.json, 图片生成/图生图/Qwen 2.1图像编辑4步加速｜电商产品图改图全靠它_2103067038968279041.json, 图片生成/图生图/Qwen Image 2.1 PE 图像编辑t8加速版｜图生图一键重绘提速神器_2104018991554580482.json, 图片生成/图生图/Qwen Image 2.1 PE图像编辑 加速版，角色设计图生图处理工具_2106137062041804802.json, 图片生成/图生图/Qwen Image 2.1 PE图像编辑工作流，人像写真图生图其它图片处理方案_2107212690769928193.json, 图片生成/图生图/Qwen Image 2.1 PE图像编辑高速版 指令式局部修改一键出图_2104260036716486658.json, 图片生成/图生图/Qwen Image 2.1 PE多图编辑｜最多9张图一起混合处理_2103039755335323650.json, 图片生成/图生图/Qwen Image 2.1人物换脸工作流，图生图面部替换处理工具_2106469574010036225.json, 图片生成/图生图/Qwen Image 2.1人物换脸工作流｜图生图换脸自然贴合_2103056179755835394.json, 图片生成/图生图/Qwen Image 2.1人物换脸，高保真面部替换图生图方案_2103185191014588417.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/反推提示词/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json、图片生成/反推提示词/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json、图片生成/反推提示词/Qwen Image 2.1图像编辑 反推提示词图生图处理工具_2113056983065653250.json、图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json、图片生成/图生图/Qwen 2.1图像编辑4步加速，电商产品图生图多场景处理工作流_2103186678771970050.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
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
- `LoadImage` —— 12/14 个有
- `QwenPERewriteT8` —— 12/14 个有
- `easy showAnything` —— 12/14 个有
- `CR Prompt Text` —— 11/14 个有
- `ComfySwitchNode` —— 11/14 个有
- `ResolutionSelector` —— 11/14 个有
- `easy cleanGpuUsed` —— 11/14 个有
- `QwenImage21Cache` —— 10/14 个有
- `QwenImage21BlockCacheT8` —— 5/14 个有
- `QwenImage21SageAttentionT8` —— 5/14 个有
- `QwenImage21SpectrumT8` —— 5/14 个有
- `ColorMatch` —— 3/14 个有
- `GrowMaskWithBlur` —— 3/14 个有
- `Image Comparer (rgthree)` —— 3/14 个有
- `LayerUtility: CropByMask V2` —— 3/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/14 个有
- `LayerUtility: ImageScaleRestore V2` —— 3/14 个有
- `LayerUtility: RestoreCropBox` —— 3/14 个有
- `PreviewAny` —— 2/14 个有
- `TextGenerate` —— 2/14 个有
- `CR Text` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `StringConstantMultiline` —— 1/14 个有
- `StringFunction|pysssss` —— 1/14 个有
- `StringReplace` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（16/14 个样本）：Steps较低可能导致细节不足
