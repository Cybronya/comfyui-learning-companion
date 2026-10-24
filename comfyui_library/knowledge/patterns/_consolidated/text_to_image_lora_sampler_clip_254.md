---
name: text_to_image_lora_sampler_clip_254
type: Text To Image
frequency: 7
level: moderate
coverage: 0.928143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed_Edit图像编辑与扩图重绘_2026977014363721729.json, 图片生成/图生图/fireRed_edit_workflow_2025984865023299586.json, 图片生成/图生图/fireRed_edit_workflow_2029377409757224961.json, 图片生成/图生图/qwen_image_edit_2509动作姿势参考_1971944011525189634.json, 图片生成/图生图/qwen_image_edit_2509封面文字包装专用_1971771856065851394.json, 图片生成/图生图/qwen_image_edit_2509封面文字包装专用_1979943851597139969.json, 图片生成/图生图/qwen_image_edit_2509编辑图像对齐解决版_1970873027892256769.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_254

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FireRed_Edit图像编辑与扩图重绘_2026977014363721729.json、图片生成/图生图/fireRed_edit_workflow_2025984865023299586.json、图片生成/图生图/fireRed_edit_workflow_2029377409757224961.json、图片生成/图生图/qwen_image_edit_2509动作姿势参考_1971944011525189634.json、图片生成/图生图/qwen_image_edit_2509封面文字包装专用_1971771856065851394.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/7 个有
- `FluxKontextImageScale` —— 4/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `PreviewImage` —— 2/7 个有
- `RH_LLMAPI_NODE` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `DrawMaskOnImage` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `ImagePadForOutpaint` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 7 | 55% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 1.5 | 7 | 81% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1920 | 720 - 1920 | 7 | 58% |
| 高度 | 1080 | 1080 - 1280 | 7 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 1.5，7 个样本，取值集中（一致性 81%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 720 - 1920，7 个样本
- 高度 中位数 1080，观测区间 1080 - 1280，7 个样本，取值集中（一致性 92%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
