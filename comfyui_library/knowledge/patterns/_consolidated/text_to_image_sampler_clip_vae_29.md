---
name: text_to_image_sampler_clip_vae_29
type: Text To Image
frequency: 5
level: strong
coverage: 0.8534
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/图文生图工作流_2109162579229757442.json, 图片生成/文生图/文生图课A1：SD1.5 入门，comfyui从入门到躺平系列教程_1979111789180915714.json, 图片生成/文生图/文生图（LORA）_1999295749642911745.json, 图片生成/文生图/文生图（LORA）_2017116078291296258.json, 图片生成/文生图/视频跟练_2106961244719767554.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_29

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/图文生图工作流_2109162579229757442.json、图片生成/文生图/文生图课A1：SD1.5 入门，comfyui从入门到躺平系列教程_1979111789180915714.json、图片生成/文生图/文生图（LORA）_1999295749642911745.json、图片生成/文生图/文生图（LORA）_2017116078291296258.json、图片生成/文生图/视频跟练_2106961244719767554.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 4/5 个有
- `LoraLoader` —— 2/5 个有
- `easy ipadapterApplyEncoder` —— 1/5 个有
- `unCLIPCheckpointLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1128 | 5 | 74% |
| 高度 | 768 | 512 - 1280 | 5 | 70% |
| 采样步数 | 28 | 24 - 30 | 5 | 91% |
| Prompt 约束强度(CFG) | 7 | 3 - 7 | 5 | 74% |
| 采样算法 | dpmpp_2m | - | 5 | 40% |
| 调度器 | karras | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1128，5 个样本
- 高度 中位数 768，观测区间 512 - 1280，5 个样本
- 采样步数 中位数 28，观测区间 24 - 30，5 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 3 - 7，5 个样本
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 40%
- 调度器 最常用 karras，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
