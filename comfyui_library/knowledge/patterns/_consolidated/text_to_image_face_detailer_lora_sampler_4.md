---
name: text_to_image_face_detailer_lora_sampler_4
type: Text To Image
frequency: 3
level: strong
coverage: 0.899333
common_nodes: [CLIPTextEncode, CR Text, CheckpointLoaderSimple, EmptyLatentImage, FaceDetailer, Joy_caption_two_advanced, Joy_caption_two_load, Joy_extra_options, KSampler, LoadImage, LoraLoader, RH_Translator, SAMLoader, SaveImage, ShowText|pysssss, Text Concatenate, UltralyticsDetectorProvider, VAEDecode, easy positive]
problems: []
missing: []
members: [图片生成/图生图/动漫角色生成_2080880897351573505.json, 图片生成/图生图/动漫角色生成_2080882019592134657.json, 图片生成/文生图/QIANSUI+动漫游戏角色生成+反推提示词_1984641878358376449.json]
source: knowledge_consolidation
---

# text_to_image_face_detailer_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/动漫角色生成_2080880897351573505.json、图片生成/图生图/动漫角色生成_2080882019592134657.json、图片生成/文生图/QIANSUI+动漫游戏角色生成+反推提示词_1984641878358376449.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FaceDetailer`
- `Joy_caption_two_advanced`
- `Joy_caption_two_load`
- `Joy_extra_options`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `RH_Translator`
- `SAMLoader`
- `SaveImage`
- `ShowText|pysssss`
- `Text Concatenate`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1920 | 1536 - 1920 | 3 | 90% |
| LoRA 模型强度 | 0.5 | 0.2 - 0.5 | 3 | 65% |
| LoRA 文本强度 | 1 | 0.7 - 1 | 3 | 84% |
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 8 | 3 | 94% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1536 - 1920，3 个样本，取值集中（一致性 90%）
- LoRA 模型强度 中位数 0.5，观测区间 0.2 - 0.5，3 个样本
- LoRA 文本强度 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）
- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 8，3 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
