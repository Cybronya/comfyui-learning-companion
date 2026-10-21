---
name: text_to_image_sampler_clip_checkpoint_7
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9085
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/1928363238206128129.json, 图片生成/文生图/1931623761387433985.json, 图片生成/文生图/SDXL 双阶段高清精修工作流_2083092060114079745.json, 图片生成/文生图/Text-to-Image + LoRA_1878782083018514433.json, 图片生成/文生图/【遇见AI】基础放大方法之潜空间放大_2011365312960139265.json, 图片生成/文生图/剪影块面分割_2061724652694757378.json, 图片生成/文生图/图像细节放大_2012407929160343554.json, 图片生成/文生图/文生图基础款_1990029530519793666.json, 图片生成/文生图/质感笔触干练_2060512709078241281.json, 图片生成/文生图/赛博废土带笔触场景_2063495974462513153.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1928363238206128129.json、图片生成/文生图/1931623761387433985.json、图片生成/文生图/SDXL 双阶段高清精修工作流_2083092060114079745.json、图片生成/文生图/Text-to-Image + LoRA_1878782083018514433.json、图片生成/文生图/【遇见AI】基础放大方法之潜空间放大_2011365312960139265.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/10 个有
- `LatentUpscaleBy` —— 6/10 个有
- `LoraLoader` —— 6/10 个有
- `LatentUpscale` —— 4/10 个有
- `KSampler //Inspire` —— 3/10 个有
- `JjkText` —— 1/10 个有
- `Lora Loader` —— 1/10 个有
- `TextCombinerTwo` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | 0.35 - 1.15 | 6 | 52% |
| LoRA 文本强度 | 0.7 | 0.35 - 1 | 6 | 60% |
| 宽度 | 896 | 512 - 1568 | 10 | 66% |
| 高度 | 952 | 512 - 1280 | 10 | 67% |
| 采样步数 | 25 | 15 - 40 | 10 | 68% |
| Prompt 约束强度(CFG) | 8 | 3.5 - 8 | 10 | 79% |
| 采样算法 | dpmpp_2m | - | 10 | 40% |
| 调度器 | karras | - | 10 | 40% |
| 重绘幅度 | 0.795 | 0.35 - 1 | 10 | 66% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，观测区间 0.35 - 1.15，6 个样本
- LoRA 文本强度 中位数 0.7，观测区间 0.35 - 1，6 个样本
- 宽度 中位数 896，观测区间 512 - 1568，10 个样本
- 高度 中位数 952，观测区间 512 - 1280，10 个样本
- 采样步数 中位数 25，观测区间 15 - 40，10 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 3.5 - 8，10 个样本
- 采样算法 最常用 dpmpp_2m，10 个样本，一致性 40%
- 调度器 最常用 karras，10 个样本，一致性 40%
- 重绘幅度 中位数 0.795，观测区间 0.35 - 1，10 个样本
