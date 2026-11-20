---
name: text_to_image_lora_sampler_clip_449
type: Text To Image
frequency: 4
level: strong
coverage: 0.9175
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptyLatentImage, FluxKontextImageScale, GetImageSize, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen_image_edit_2509动作姿势参考_1971944011525189634.json, 图片生成/图生图/qwen_image_edit_2509封面文字包装专用_1971771856065851394.json, 图片生成/图生图/qwen_image_edit_2509封面文字包装专用_1979943851597139969.json, 图片生成/图生图/qwen_image_edit_2509编辑图像对齐解决版_1970873027892256769.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_449

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen_image_edit_2509动作姿势参考_1971944011525189634.json、图片生成/图生图/qwen_image_edit_2509封面文字包装专用_1971771856065851394.json、图片生成/图生图/qwen_image_edit_2509封面文字包装专用_1979943851597139969.json、图片生成/图生图/qwen_image_edit_2509编辑图像对齐解决版_1970873027892256769.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FluxKontextImageScale`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `PreviewImage` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1920 - 1920 | 4 | 100% |
| 高度 | 1080 | 1080 - 1080 | 4 | 100% |
| 采样步数 | 20 | 8 - 20 | 4 | 69% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 1.5 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 1920 - 1920，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，观测区间 1080 - 1080，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 1.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
