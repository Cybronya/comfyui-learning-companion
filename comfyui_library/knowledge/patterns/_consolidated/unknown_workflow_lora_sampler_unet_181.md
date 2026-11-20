---
name: unknown_workflow_lora_sampler_unet_181
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.901
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图海报2_2067154054463180802.json, 图片生成/图生图/快速图生海报_2070417761507045378.json, 图片生成/文生图/qwen_image_edit_2511_2003692026312966146.json, 平台全量/Qwen 2509图像编辑可控一致性换背景电商_1978341875440607234.json, 平台全量/Qwen Edit 2511 姿势编辑_2004888107784826882.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_181

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图生图海报2_2067154054463180802.json、图片生成/图生图/快速图生海报_2070417761507045378.json、图片生成/文生图/qwen_image_edit_2511_2003692026312966146.json、平台全量/Qwen 2509图像编辑可控一致性换背景电商_1978341875440607234.json、平台全量/Qwen Edit 2511 姿势编辑_2004888107784826882.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `EmptyLatentImage` —— 3/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `GetImageSize+` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `DWPreprocessor` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768 | 512 - 768 | 3 | 82% |
| 高度 | 1024 | 768 - 1024 | 3 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 768，3 个样本，取值集中（一致性 82%）
- 高度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
