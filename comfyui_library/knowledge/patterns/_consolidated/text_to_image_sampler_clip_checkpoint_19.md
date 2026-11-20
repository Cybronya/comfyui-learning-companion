---
name: text_to_image_sampler_clip_checkpoint_19
type: Text To Image
frequency: 3
level: strong
coverage: 0.784333
common_nodes: [CLIPTextEncode, CR Text Concatenate, CheckpointLoaderSimple, EmptyLatentImage, KSampler, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/007.其他-功能风格008.XL二次元文生图工作流_2035405849501372417.json, 图片生成/文生图/真人视觉文生图-LORA-XL-SZ_1982645105960067073.json, 图片生成/文生图/真实视觉文生图SDXL-LORA-sz_1982665506299756546.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/007.其他-功能风格008.XL二次元文生图工作流_2035405849501372417.json、图片生成/文生图/真人视觉文生图-LORA-XL-SZ_1982645105960067073.json、图片生成/文生图/真实视觉文生图SDXL-LORA-sz_1982665506299756546.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `WD14Tagger|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 784 | 768 - 784 | 3 | 99% |
| 高度 | 1024 | 1024 - 1280 | 3 | 89% |
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 7 | 6 - 7 | 3 | 93% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 784，观测区间 768 - 784，3 个样本，取值集中（一致性 99%）
- 高度 中位数 1024，观测区间 1024 - 1280，3 个样本，取值集中（一致性 89%）
- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 7，3 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
