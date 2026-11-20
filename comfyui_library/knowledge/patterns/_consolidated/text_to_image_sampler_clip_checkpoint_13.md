---
name: text_to_image_sampler_clip_checkpoint_13
type: Text To Image
frequency: 7
level: moderate
coverage: 0.928571
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/反推提示词/【茗翠Ai】提示词反推+自动负面提示词_1955507310078693378.json, 图片生成/文生图/Anima最新动漫文生图模型_2018993897048903682.json, 图片生成/文生图/【茗翠Ai】comfyui工作流入门到精通1_1953425536221675521.json, 图片生成/文生图/【茗翠Ai】comfyui工作流入门到精通2_1954083787858690050.json, 图片生成/文生图/文生图（LORA）_1999295749642911745.json, 图片生成/文生图/文生图（LORA）_2017116078291296258.json, 平台全量/电商主图使用_2052623591581200385.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_13

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/【茗翠Ai】提示词反推+自动负面提示词_1955507310078693378.json、图片生成/文生图/Anima最新动漫文生图模型_2018993897048903682.json、图片生成/文生图/【茗翠Ai】comfyui工作流入门到精通1_1953425536221675521.json、图片生成/文生图/【茗翠Ai】comfyui工作流入门到精通2_1954083787858690050.json、图片生成/文生图/文生图（LORA）_1999295749642911745.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/7 个有
- `Label (rgthree)` —— 3/7 个有
- `LoraLoader` —— 3/7 个有
- `WD14Tagger|pysssss` —— 3/7 个有
- `AutoNegativePrompt` —— 1/7 个有
- `DF_String_Concatenate` —— 1/7 个有
- `VAELoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1920 | 7 | 54% |
| 高度 | 768 | 512 - 1536 | 7 | 67% |
| 采样步数 | 30 | 20 - 40 | 7 | 78% |
| Prompt 约束强度(CFG) | 7 | 4.5 - 8 | 7 | 84% |
| 采样算法 | dpmpp_2m | - | 7 | 57% |
| 调度器 | karras | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | 0.5 - 1 | 3 | 72% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1920，7 个样本
- 高度 中位数 768，观测区间 512 - 1536，7 个样本
- 采样步数 中位数 30，观测区间 20 - 40，7 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 4.5 - 8，7 个样本，取值集中（一致性 84%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 57%
- 调度器 最常用 karras，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.5 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
