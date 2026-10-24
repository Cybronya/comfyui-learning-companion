---
name: text_to_image_lora_sampler_clip_41
type: Text To Image
frequency: 19
level: strong
coverage: 0.882211
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json, 图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json, 图片生成/图生图/Qwen 2.1图像编辑4步加速，电商产品图生图多场景处理工作流_2103186678771970050.json, 图片生成/图生图/Qwen 2.1图像编辑4步加速｜电商产品图改图全靠它_2103067038968279041.json, 图片生成/图生图/Qwen Image 2.1 PE 图像编辑t8加速版｜图生图一键重绘提速神器_2104018991554580482.json, 图片生成/图生图/Qwen Image 2.1 PE图像编辑 加速版，角色设计图生图处理工具_2106137062041804802.json, 图片生成/图生图/Qwen Image 2.1 PE图像编辑工作流，人像写真图生图其它图片处理方案_2107212690769928193.json, 图片生成/图生图/Qwen Image 2.1 PE图像编辑高速版 指令式局部修改一键出图_2104260036716486658.json, 图片生成/图生图/Qwen Image 2.1 PE多图编辑｜最多9张图一起混合处理_2103039755335323650.json, 图片生成/图生图/Qwen Image 2.1人物换脸工作流，图生图面部替换处理工具_2106469574010036225.json, 图片生成/图生图/Qwen Image 2.1人物换脸工作流｜图生图换脸自然贴合_2103056179755835394.json, 图片生成/图生图/Qwen Image 2.1人物换脸，高保真面部替换图生图方案_2103185191014588417.json, 图片生成/图生图/Qwen Image 2.1整张图像编辑加速工作流，图生图处理方案_2106468101410869249.json, 图片生成/图生图/Qwen2.1图像编辑PE增强版，已清理think的图生图处理工作流_2103888095346257922.json, 图片生成/图生图/qwen2.1图像编辑 局部修改指令式操作_2104648645625860097.json, 图片生成/图生图/qwen2.1移除rgba背景｜图生图透明通道处理利器_2104569513869135873.json, 图片生成/图生图/qwen2.1移除rgba通道 透明背景图处理_2104688268930535425.json, 图片生成/文生图/Qwen Image 2.1 ControlNet工作流，精准控制改图文生图图生图方案_2106521489427222529.json, 图片生成/文生图/qwen_image_21_controlnet可控生成｜文生图图生图精准控制_2106248623163011074.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/反推提示词/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json、图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json、图片生成/图生图/Qwen 2.1图像编辑4步加速，电商产品图生图多场景处理工作流_2103186678771970050.json、图片生成/图生图/Qwen 2.1图像编辑4步加速｜电商产品图改图全靠它_2103067038968279041.json、图片生成/图生图/Qwen Image 2.1 PE 图像编辑t8加速版｜图生图一键重绘提速神器_2104018991554580482.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 19 个 workflow 都包含：
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
- `ComfySwitchNode` —— 18/19 个有
- `LoadImage` —— 17/19 个有
- `ResolutionSelector` —— 16/19 个有
- `QwenImage21Cache` —— 15/19 个有
- `easy showAnything` —— 13/19 个有
- `CR Prompt Text` —— 12/19 个有
- `QwenPERewriteT8` —— 12/19 个有
- `easy cleanGpuUsed` —— 12/19 个有
- `Image Comparer (rgthree)` —— 9/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/19 个有
- `PreviewAny` —— 7/19 个有
- `StringConstantMultiline` —— 7/19 个有
- `StringFunction|pysssss` —— 7/19 个有
- `StringReplace` —— 7/19 个有
- `TextGenerate` —— 7/19 个有
- `BatchImagesNode` —— 6/19 个有
- `QwenImage21BlockCacheT8` —— 6/19 个有
- `QwenImage21SageAttentionT8` —— 6/19 个有
- `QwenImage21SpectrumT8` —— 6/19 个有
- `easy seed` —— 6/19 个有
- `FluxKontextImageScale` —— 5/19 个有
- `ColorMatch` —— 3/19 个有
- `GrowMaskWithBlur` —— 3/19 个有
- `LayerUtility: CropByMask V2` —— 3/19 个有
- `LayerUtility: ImageScaleRestore V2` —— 3/19 个有
- `LayerUtility: RestoreCropBox` —— 3/19 个有
- `AIO_Preprocessor` —— 2/19 个有
- `ModelPatchLoader` —— 2/19 个有
- `PreviewImage` —— 2/19 个有
- `ZImageFunControlnet` —— 2/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（22/19 个样本）：Steps较低可能导致细节不足
