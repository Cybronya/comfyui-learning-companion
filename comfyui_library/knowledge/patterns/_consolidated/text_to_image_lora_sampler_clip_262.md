---
name: text_to_image_lora_sampler_clip_262
type: Text To Image
frequency: 7
level: strong
coverage: 0.955857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-图像编辑-2511-多角度-LoRA_2009558755456851970.json, 图片生成/图生图/qwen_edit_2509_nextsceneV2_1980794406355816450.json, 图片生成/图生图/qwen_image_edit_plus_2511_11_2003764361976029185.json, 图片生成/图生图/qwen_image_edit_plus_2511_1_2073946454514819073.json, 图片生成/图生图/qwen_image_edit_plus_MultipleAngles_1986272902184128514.json, 图片生成/图生图/{一图成剧}批量出分镜图 qwen_image_edit_plus2509_1978808303541194754.json, 图片生成/图生图/分镜图TEST_1980868817926668289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_262

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-图像编辑-2511-多角度-LoRA_2009558755456851970.json、图片生成/图生图/qwen_edit_2509_nextsceneV2_1980794406355816450.json、图片生成/图生图/qwen_image_edit_plus_2511_11_2003764361976029185.json、图片生成/图生图/qwen_image_edit_plus_2511_1_2073946454514819073.json、图片生成/图生图/qwen_image_edit_plus_MultipleAngles_1986272902184128514.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
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
- `easy promptLine` —— 3/7 个有
- `JjkText` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ProcessString` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1440 | 1024 - 1920 | 7 | 74% |
| 高度 | 1080 | 512 - 1920 | 7 | 59% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1440，观测区间 1024 - 1920，7 个样本
- 高度 中位数 1080，观测区间 512 - 1920，7 个样本
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
