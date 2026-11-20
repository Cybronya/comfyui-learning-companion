---
name: text_to_image_lora_sampler_clip_127
type: Text To Image
frequency: 12
level: strong
coverage: 0.885583
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1图像编辑接超分放大工作流，图生图高清修复方案_2103976463702781954.json, 图片生成/图生图/Qwen Image 2.1图像编辑模式图生图处理生成工具_2102461309957791745.json, 图片生成/图生图/Qwen Image 2.1图片换头换脸，一键面部替换的图生图处理工具_2102824071833673730.json, 图片生成/图生图/Qwen Image 2.1图片换头换脸｜人像替换自然贴合｜光影肤色都照顾到_2102597696380030977.json, 图片生成/图生图/Qwen Image 2.1多图编辑 多张输入精准改图_2105377023228203010.json, 图片生成/图生图/Qwen Image 2.1多图编辑Multi Image Editing工作流，角色设计图生图_2106164834009174018.json, 图片生成/图生图/Qwen Image 2.1多图编辑人物面部加全身三视图角色表，图生图工具_2105781931915964417.json, 图片生成/图生图/Qwen Image 2.1多图编辑图片编辑全节点注释处理工具_2102541742317850626.json, 图片生成/图生图/Qwen Image 2.1多图编辑｜多张参考图合并编辑出图_2108046219019898882.json, 图片生成/图生图/Qwen Image 2.1多图编辑｜多张素材融合处理一步到位_2107681855259627522.json, 图片生成/图生图/Qwen Image 2.1整张图像编辑加速工作流，图生图处理方案_2106468101410869249.json, 图片生成/图生图/Qwen-Image 2.1多图编辑T8加速版｜批量改图效率翻倍_2113515421499478017.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_127

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图像编辑接超分放大工作流，图生图高清修复方案_2103976463702781954.json、图片生成/图生图/Qwen Image 2.1图像编辑模式图生图处理生成工具_2102461309957791745.json、图片生成/图生图/Qwen Image 2.1图片换头换脸，一键面部替换的图生图处理工具_2102824071833673730.json、图片生成/图生图/Qwen Image 2.1图片换头换脸｜人像替换自然贴合｜光影肤色都照顾到_2102597696380030977.json、图片生成/图生图/Qwen Image 2.1多图编辑 多张输入精准改图_2105377023228203010.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextGenerateLTX2Prompt` —— 9/12 个有
- `BatchImagesNode` —— 8/12 个有
- `CR Prompt Text` —— 3/12 个有
- `CR Text` —— 3/12 个有
- `QwenImage21BlockCacheT8` —— 3/12 个有
- `QwenImage21SageAttentionT8` —— 3/12 个有
- `QwenImage21SpectrumT8` —— 3/12 个有
- `easy showAnything` —— 3/12 个有
- `QwenPERewriteT8` —— 2/12 个有
- `easy cleanGpuUsed` —— 2/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `CFGGuider` —— 1/12 个有
- `CM_IntToFloat` —— 1/12 个有
- `ImageScaleToTotalPixels` —— 1/12 个有
- `KSamplerSelect` —— 1/12 个有
- `ManualSigmas` —— 1/12 个有
- `Note Plus (mtb)` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `RandomNoise` —— 1/12 个有
- `SamplerCustomAdvanced` —— 1/12 个有
- `easy imageConcat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
