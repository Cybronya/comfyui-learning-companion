---
name: text_to_image_lora_sampler_clip_106
type: Text To Image
frequency: 13
level: strong
coverage: 0.902692
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1指定抠图模式图生图处理生成工具_2102459788658569217.json, 图片生成/图生图/Qwen Image 2.1换头换脸6步加速版｜图生图换脸又快又稳_2104541964841607170.json, 图片生成/图生图/Qwen Image 2.1文生图图生图处理生成工作流_2102091301226369025.json, 图片生成/图生图/Qwen Image 2.1文生图图生图处理生成工作流_2102101983669866498.json, 图片生成/图生图/Qwen Image 2.1精准抠图工作流指哪扣哪交互式图生图体验，图生图抠图工具_2107258835344904194.json, 图片生成/图生图/Qwen Image 2.1精准抠图工作流，指哪扣哪的交互式图生图体验_2102816199997480961.json, 图片生成/图生图/Qwen Image 2.1自动抠图透明背景，图生图一键去底处理工具_2103602803808759810.json, 图片生成/图生图/Qwen_Image_2.1图像编辑工作流，简洁实用的图生图处理方案_2106169452948709378.json, 图片生成/图生图/Qwen_Image_2.1精准抠图工作流，指哪扣哪的交互式图生图体验_2106553795676303362.json, 图片生成/图生图/Qwen_image2.1多图编辑实用版｜多张图片统一处理｜其它图片处理通吃_2102321477453443073.json, 图片生成/图生图/Qwen一键出人物三视图｜角色一致性拉满的图生图神器_2111264557317574658.json, 图片生成/文生图/Qwen-Image-2.1-Turbo汉服美学写真｜一键国风服装展示文生图_2111051887217827841.json, 数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2105115732848766978.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_106

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1指定抠图模式图生图处理生成工具_2102459788658569217.json、图片生成/图生图/Qwen Image 2.1换头换脸6步加速版｜图生图换脸又快又稳_2104541964841607170.json、图片生成/图生图/Qwen Image 2.1文生图图生图处理生成工作流_2102091301226369025.json、图片生成/图生图/Qwen Image 2.1文生图图生图处理生成工作流_2102101983669866498.json、图片生成/图生图/Qwen Image 2.1精准抠图工作流指哪扣哪交互式图生图体验，图生图抠图工具_2107258835344904194.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 12/13 个有
- `LoadImage` —— 12/13 个有
- `QwenImage21Cache` —— 11/13 个有
- `CR Text` —— 9/13 个有
- `孤海注释` —— 9/13 个有
- `PreviewImage` —— 6/13 个有
- `ResolutionSelector` —— 6/13 个有
- `EmptyImage` —— 5/13 个有
- `CR Prompt Text` —— 4/13 个有
- `Color Grading JK` —— 1/13 个有
- `ConcatTextOfUtils` —— 1/13 个有
- `LoraLoaderBypassModelOnly` —— 1/13 个有
- `MultiTextConcatenate` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `QwenImage21SageAttentionT8` —— 1/13 个有
- `RHLLMChatNode` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（16/13 个样本）：Steps较低可能导致细节不足
