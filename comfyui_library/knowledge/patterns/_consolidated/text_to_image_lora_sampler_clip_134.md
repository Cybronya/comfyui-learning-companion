---
name: text_to_image_lora_sampler_clip_134
type: Text To Image
frequency: 12
level: strong
coverage: 0.95525
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen_edit-剧本场景制作-lora素材制作_1979342758429233153.json, 图片生成/图生图/qwen_edit-剧本场景制作-lora素材制作_2059284183662546945.json, 图片生成/图生图/qwen_edit_2511_最强全角度切换_2010524177542946818.json, 图片生成/图生图/qwen_edit_2511_最强生图修图拼图_2004371887692152833.json, 图片生成/图生图/qwen_image_edit_plus_multiangle_2009465484042833922.json, 图片生成/图生图/qwen_image_edit_plus_nextscene_1977038049123147778.json, 图片生成/图生图/qwen_image_edit_plus_unblur_2010375997945815041.json, 图片生成/图生图/qwen_image_edit_plus_upscale4k_1977064282565300225.json, 图片生成/图生图/qwen_image_edit_plus_use_name_1977395256004091906.json, 图片生成/图生图/图像不同角度  切换角度_2011081053884125185.json, 图片生成/图生图/图像角度控制器-qwen_image_edit_2511_2009827945770127361.json, 图片生成/图生图/测试_1988591335890403329.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_134

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/qwen_edit-剧本场景制作-lora素材制作_1979342758429233153.json、图片生成/图生图/qwen_edit-剧本场景制作-lora素材制作_2059284183662546945.json、图片生成/图生图/qwen_edit_2511_最强全角度切换_2010524177542946818.json、图片生成/图生图/qwen_edit_2511_最强生图修图拼图_2004371887692152833.json、图片生成/图生图/qwen_image_edit_plus_multiangle_2009465484042833922.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/12 个有
- `CR Prompt List` —— 3/12 个有
- `DeepTranslatorTextNode` —— 3/12 个有
- `Get Image Size` —— 3/12 个有
- `Text Multiline` —— 3/12 个有
- `QwenMultiangleCameraNode` —— 2/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `ImageResize+` —— 1/12 个有
- `easy imageSize` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1920 | 768 - 1920 | 12 | 74% |
| 高度 | 1080 | 720 - 1080 | 12 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 768 - 1920，12 个样本
- 高度 中位数 1080，观测区间 720 - 1080，12 个样本，取值集中（一致性 83%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
