---
name: text_to_image_sampler_clip_checkpoint_9
type: Text To Image
frequency: 8
level: moderate
coverage: 0.9455
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/SDXL 双阶段高清精修工作流_2083092060114079745.json, 图片生成/文生图/SDXL 国潮商业海报生成器_2069501911832817666.json, 图片生成/文生图/SDXL基础文生图工作流_2070416088365621250.json, 图片生成/文生图/SDXL文生图1.0工作流_2047952695373336578.json, 图片生成/文生图/SDXL文生图基础 by Mae_1965622186373468162.json, 图片生成/文生图/controlnet文生图SD_2106555235891245058.json, 图片生成/文生图/mechaNeko_style打磨_1931623761387433985.json, 图片生成/文生图/【遇见AI】基础放大方法之潜空间放大_2011365312960139265.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_9

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/SDXL 双阶段高清精修工作流_2083092060114079745.json、图片生成/文生图/SDXL 国潮商业海报生成器_2069501911832817666.json、图片生成/文生图/SDXL基础文生图工作流_2070416088365621250.json、图片生成/文生图/SDXL文生图1.0工作流_2047952695373336578.json、图片生成/文生图/SDXL文生图基础 by Mae_1965622186373468162.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/8 个有
- `LatentUpscale` —— 3/8 个有
- `EmptyImage` —— 1/8 个有
- `FaceRestoreCFWithModel` —— 1/8 个有
- `FaceRestoreModelLoader` —— 1/8 个有
- `LoraLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 884 | 512 - 1216 | 8 | 72% |
| 高度 | 1024 | 512 - 1536 | 8 | 66% |
| 采样步数 | 20 | 15 - 35 | 8 | 73% |
| Prompt 约束强度(CFG) | 6.5 | 3.5 - 8 | 8 | 74% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | karras | - | 8 | 38% |
| 重绘幅度 | 1 | 0.35 - 1 | 8 | 67% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 884，观测区间 512 - 1216，8 个样本
- 高度 中位数 1024，观测区间 512 - 1536，8 个样本
- 采样步数 中位数 20，观测区间 15 - 35，8 个样本
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 3.5 - 8，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 karras，8 个样本，一致性 38%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，8 个样本
