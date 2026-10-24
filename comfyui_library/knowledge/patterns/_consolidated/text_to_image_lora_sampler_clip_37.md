---
name: text_to_image_lora_sampler_clip_37
type: Text To Image
frequency: 20
level: strong
coverage: 0.89335
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/6步加速版换头换脸 Qwen Image 2.1高效出图_2104765577515585538.json, 图片生成/图生图/BF16精度Qwen_Image_2.1图片编辑，小字不崩的图生图处理方案_2105505352971280385.json, 图片生成/图生图/Face+Swap++Qwen-Image-2.1｜模特换头换脸 图生图电商救星_2105546422262263810.json, 图片生成/图生图/Qwen Image 2.1一键图片换装图生图处理工具_2102528994515181569.json, 图片生成/图生图/Qwen Image 2.1一键图片换装图生图，人物服饰替换处理工具_2102908589479387138.json, 图片生成/图生图/Qwen Image 2.1一键图片换装｜换装类图生图专用｜服装替换细节到位_2102270303454982146.json, 图片生成/图生图/Qwen Image 2.1一键扩图图生图处理生成工具_2102516145378127874.json, 图片生成/图生图/Qwen Image 2.1一键扩图图生图工作流，图生图写实扩图处理工具_2107231075868172290.json, 图片生成/图生图/Qwen Image 2.1一键扩图实战版｜边界延展不留痕｜横竖屏随你切换_2102626840547516418.json, 图片生成/图生图/Qwen Image 2.1一键扩图｜画面秒变超宽幅｜构图不够能延展_2102603964750581761.json, 图片生成/图生图/Qwen Image 2.1一键换装图片服装替换，电商模特图生图自动完成工具_2103901904890851329.json, 图片生成/图生图/Qwen Image 2.1一键换装｜图片服装替换自动完成｜电商模特好帮手_2102224257387425794.json, 图片生成/图生图/Qwen Image 2.1人物换头图片换脸图生图处理工具_2102520964331425794.json, 图片生成/图生图/Qwen Image 2.1单图编辑产品展示图生图处理工具_2102489354336821249.json, 图片生成/图生图/Qwen Image 2.1图像编辑模式图生图处理生成工具_2102461309957791745.json, 图片生成/图生图/Qwen Image 2.1多图编辑人物面部加全身三视图角色表，图生图工具_2105781931915964417.json, 图片生成/图生图/Qwen Image 2.1换头换脸6步加速版｜图生图换脸又快又稳_2104541964841607170.json, 图片生成/图生图/Qwen image2.1单图编辑｜图片换背景轻松搞定｜模特产品展示利器_2102227263780642818.json, 图片生成/图生图/Qwen_image2.1单图编辑｜图片换背景轻松搞定｜模特产品展示利器_2104449836132159489.json, 图片生成/图生图/Qwen_image2.1多图编辑实用版｜多张图片统一处理｜其它图片处理通吃_2102321477453443073.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/6步加速版换头换脸 Qwen Image 2.1高效出图_2104765577515585538.json、图片生成/图生图/BF16精度Qwen_Image_2.1图片编辑，小字不崩的图生图处理方案_2105505352971280385.json、图片生成/图生图/Face+Swap++Qwen-Image-2.1｜模特换头换脸 图生图电商救星_2105546422262263810.json、图片生成/图生图/Qwen Image 2.1一键图片换装图生图处理工具_2102528994515181569.json、图片生成/图生图/Qwen Image 2.1一键图片换装图生图，人物服饰替换处理工具_2102908589479387138.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
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
- `QwenImage21Cache` —— 18/20 个有
- `ResolutionSelector` —— 18/20 个有
- `孤海注释` —— 17/20 个有
- `TextGenerateLTX2Prompt` —— 13/20 个有
- `BatchImagesNode` —— 12/20 个有
- `CR Prompt Text` —— 7/20 个有
- `PreviewImage` —— 5/20 个有
- `CR Text` —— 4/20 个有
- `RHLLMChatNode` —— 4/20 个有
- `EmptyImage` —— 3/20 个有
- `ResizeLongestToNode` —— 3/20 个有
- `ShowText|pysssss` —— 3/20 个有
- `ConcatTextOfUtils` —— 2/20 个有
- `LoraLoaderBypassModelOnly` —— 2/20 个有
- `QwenImage21SageAttentionT8` —— 2/20 个有
- `Note Plus (mtb)` —— 1/20 个有
- `SaveImageAdvanced` —— 1/20 个有
- `easy showAnything` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（24/20 个样本）：Steps较低可能导致细节不足
