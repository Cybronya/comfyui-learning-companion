---
name: text_to_image_lora_sampler_clip_73
type: Text To Image
frequency: 16
level: strong
coverage: 0.767125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-2.1五视图透明背景版｜角色多角度展示底图随意换_2103686363605454849.json, 图片生成/图生图/Qwen-2.1图片编辑利器｜局部修改元素增删图生图全能王_2103684849763700737.json, 图片生成/图生图/Qwen-Image-2.1一键扩图图生图｜写实风格扩展轻松搞定_2106928805460922369.json, 图片生成/图生图/Qwen-Image-2.1一键扩图图生图｜选区外内容智能补画｜操作零门槛_2102268788170387457.json, 图片生成/图生图/Qwen-Image-2.1一键扩图｜扩图类图生图快捷版｜其它图片处理顺带_2102277686113693698.json, 图片生成/图生图/Qwen-Image-2.1人物换头图片换脸｜换脸类图生图特效｜衔接自然不穿帮_2102290282900451330.json, 图片生成/图生图/Qwen-Image-2.1图像编辑10张参考图｜局部重绘换装 图生图全能_2104094197203685378.json, 图片生成/图生图/Qwen-Image-2.1图像编辑｜最多10张参考图图生图随心改_2106230157538324481.json, 图片生成/图生图/Qwen-Image-2.1扩图实战版｜一键延展画布不违和｜其它图片处理友好_2102283966899380226.json, 图片生成/图生图/Qwen-Image-2.1换头换脸二合一｜人物头部替换与图片换脸一步搞定_2102211983704678402.json, 图片生成/图生图/QwenImage2.1 I2I官方提示词助手｜图生图有帮手｜描述写不好也能改图_2102637170602364929.json, 图片生成/图生图/QwenImage2.1图片编辑加提示词助手｜局部重绘超顺手_2103087888484356098.json, 图片生成/图生图/QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2102838137943838722.json, 图片生成/图生图/最多10张参考图 Qwen-Image-2.1图像编辑2K输出换装局部重绘_2104274563130548225.json, 图片生成/文生图/Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json, 视频生成/图生视频/QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2105866245517168642.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Qwen-2.1五视图透明背景版｜角色多角度展示底图随意换_2103686363605454849.json、图片生成/图生图/Qwen-2.1图片编辑利器｜局部修改元素增删图生图全能王_2103684849763700737.json、图片生成/图生图/Qwen-Image-2.1一键扩图图生图｜写实风格扩展轻松搞定_2106928805460922369.json、图片生成/图生图/Qwen-Image-2.1一键扩图图生图｜选区外内容智能补画｜操作零门槛_2102268788170387457.json、图片生成/图生图/Qwen-Image-2.1一键扩图｜扩图类图生图快捷版｜其它图片处理顺带_2102277686113693698.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 15/16 个有
- `ComfySwitchNode` —— 14/16 个有
- `BatchImagesNode` —— 10/16 个有
- `TextGenerateLTX2Prompt` —— 10/16 个有
- `Fast Groups Bypasser (rgthree)` —— 8/16 个有
- `GetNode` —— 8/16 个有
- `PrimitiveStringMultiline` —— 8/16 个有
- `SetNode` —— 8/16 个有
- `ImageScaleToTotalPixels` —— 5/16 个有
- `easy showAnything` —— 5/16 个有
- `Any Switch (rgthree)` —— 4/16 个有
- `ImageBatchMulti` —— 4/16 个有
- `JsonExtractString` —— 4/16 个有
- `SaveImageAdvanced` —— 4/16 个有
- `TextConcatenator` —— 4/16 个有
- `TextGenerate` —— 4/16 个有
- `CR Prompt List` —— 1/16 个有
- `HAIGC_SaveImagesToZip` —— 1/16 个有
- `Image Comparer (rgthree)` —— 1/16 个有
- `MultiTextConcatenate` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `PrimitiveBoolean` —— 1/16 个有
- `Seed (rgthree)` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
