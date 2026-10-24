---
name: text_to_image_sampler_clip_checkpoint_17
type: Text To Image
frequency: 4
level: strong
coverage: 0.81325
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/007.其他-功能风格008.XL二次元文生图工作流_2035405849501372417.json, 图片生成/文生图/Anima最新动漫文生图模型_2018993897048903682.json, 图片生成/文生图/真人视觉文生图-LORA-XL-SZ_1982645105960067073.json, 图片生成/文生图/真实视觉文生图SDXL-LORA-sz_1982665506299756546.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/007.其他-功能风格008.XL二次元文生图工作流_2035405849501372417.json、图片生成/文生图/Anima最新动漫文生图模型_2018993897048903682.json、图片生成/文生图/真人视觉文生图-LORA-XL-SZ_1982645105960067073.json、图片生成/文生图/真实视觉文生图SDXL-LORA-sz_1982665506299756546.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `JjkText` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `WD14Tagger|pysssss` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 784 | 768 - 1024 | 4 | 87% |
| 高度 | 1152 | 1024 - 1536 | 4 | 83% |
| 采样步数 | 27.5 | 25 - 40 | 4 | 80% |
| Prompt 约束强度(CFG) | 6.5 | 4.5 - 7 | 4 | 83% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 784，观测区间 768 - 1024，4 个样本，取值集中（一致性 87%）
- 高度 中位数 1152，观测区间 1024 - 1536，4 个样本，取值集中（一致性 83%）
- 采样步数 中位数 27.5，观测区间 25 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 4.5 - 7，4 个样本，取值集中（一致性 83%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
