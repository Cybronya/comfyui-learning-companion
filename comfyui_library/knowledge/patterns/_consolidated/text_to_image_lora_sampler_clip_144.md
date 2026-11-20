---
name: text_to_image_lora_sampler_clip_144
type: Text To Image
frequency: 11
level: strong
coverage: 0.881818
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json, 图片生成/图生图/Qwen Image 2.1单图编辑角色四视图工作流，角色设计图生图处理工具_2106859828982407170.json, 图片生成/图生图/Qwen Image 2.1参考图融合编辑ref2i，多图参考身份保持图生图方案_2103215198285946882.json, 图片生成/图生图/Qwen Image 2.1图像编辑修复版，角色一致性图生图抠图多场景工具_2103593422190899202.json, 图片生成/图生图/Qwen Image 2.1多图编辑｜多参考图融合修改｜批量改图效率翻倍_2104764482592534530.json, 图片生成/图生图/Qwen2.1图像编辑PE增强版，已清理think的图生图处理工作流_2103888095346257922.json, 图片生成/图生图/qwen2.1图像编辑 局部修改指令式操作_2104648645625860097.json, 图片生成/图生图/qwen2.1移除rgba背景｜图生图透明通道处理利器_2104569513869135873.json, 图片生成/图生图/qwen2.1移除rgba通道 透明背景图处理_2104688268930535425.json, 图片生成/文生图/Qwen Image 2.1 ControlNet工作流，精准控制改图文生图图生图方案_2106521489427222529.json, 图片生成/文生图/qwen_image_21_controlnet可控生成｜文生图图生图精准控制_2106248623163011074.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_144

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json、图片生成/图生图/Qwen Image 2.1单图编辑角色四视图工作流，角色设计图生图处理工具_2106859828982407170.json、图片生成/图生图/Qwen Image 2.1参考图融合编辑ref2i，多图参考身份保持图生图方案_2103215198285946882.json、图片生成/图生图/Qwen Image 2.1图像编辑修复版，角色一致性图生图抠图多场景工具_2103593422190899202.json、图片生成/图生图/Qwen Image 2.1多图编辑｜多参考图融合修改｜批量改图效率翻倍_2104764482592534530.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

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
- `LoadImage` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `TextGenerate` —— 9/11 个有
- `BatchImagesNode` —— 8/11 个有
- `PreviewAny` —— 7/11 个有
- `QwenImage21Cache` —— 7/11 个有
- `StringConstantMultiline` —— 7/11 个有
- `StringFunction|pysssss` —— 7/11 个有
- `StringReplace` —— 7/11 个有
- `ComfySwitchNode` —— 6/11 个有
- `Image Comparer (rgthree)` —— 6/11 个有
- `easy seed` —— 6/11 个有
- `FluxKontextImageScale` —— 5/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/11 个有
- `AIO_Preprocessor` —— 2/11 个有
- `Anything Everywhere3` —— 2/11 个有
- `CR Prompt Text` —— 2/11 个有
- `ModelPatchLoader` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `ZImageFunControlnet` —— 2/11 个有
- `CR Text Concatenate` —— 1/11 个有
- `Seed (rgthree)` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有
- `TextConcatenator` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
