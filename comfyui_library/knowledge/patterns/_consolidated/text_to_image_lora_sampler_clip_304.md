---
name: text_to_image_lora_sampler_clip_304
type: Text To Image
frequency: 7
level: strong
coverage: 0.673571
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, HAIGC_SaveImagesToZip, KSampler, LoraLoader, PreviewAny, SaveImage, VAEDecode, easy promptLine]
problems: []
missing: []
members: [图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列一_汇总_2020328189045772290.json, 图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列三_汇总_2020709944613408769.json, 图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列二_汇总_2020500328235409409.json, 图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列四_汇总_2020730383855259650.json, 图片生成/文生图/B妮B妳_SDXL文生图_系列二_N_S_F_W_汇总_2021460181497942018.json, 图片生成/文生图/B妮B妳_SDXL文生图_系列五_N_S_F_W_汇总_2020753702591668225.json, 图片生成/文生图/B妮B妳_SDXL文生图_系列六_N_S_F_W_汇总_2020827252291801089.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_304

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列一_汇总_2020328189045772290.json、图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列三_汇总_2020709944613408769.json、图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列二_汇总_2020500328235409409.json、图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列四_汇总_2020730383855259650.json、图片生成/文生图/B妮B妳_SDXL文生图_系列二_N_S_F_W_汇总_2021460181497942018.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `HAIGC_SaveImagesToZip`
- `KSampler`
- `LoraLoader`
- `PreviewAny`
- `SaveImage`
- `VAEDecode`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `PreviewBridge` —— 6/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1344 | 7 | 90% |
| 高度 | 1720 | 1720 - 1728 | 7 | 100% |
| 采样步数 | 25 | 25 - 25 | 7 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | karras | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 0.6 | 0.6 - 0.6 | 7 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1344，7 个样本，取值集中（一致性 90%）
- 高度 中位数 1720，观测区间 1720 - 1728，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 karras，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.6，7 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
