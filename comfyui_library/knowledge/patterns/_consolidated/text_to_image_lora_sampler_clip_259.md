---
name: text_to_image_lora_sampler_clip_259
type: Text To Image
frequency: 8
level: strong
coverage: 0.7005
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoraLoader, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列一_汇总_2020328189045772290.json, 图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列三_汇总_2020709944613408769.json, 图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列二_汇总_2020500328235409409.json, 图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列四_汇总_2020730383855259650.json, 图片生成/文生图/B妮B妳_SDXL文生图_系列二_N_S_F_W_汇总_2021460181497942018.json, 图片生成/文生图/B妮B妳_SDXL文生图_系列五_N_S_F_W_汇总_2020753702591668225.json, 图片生成/文生图/B妮B妳_SDXL文生图_系列六_N_S_F_W_汇总_2020827252291801089.json, 图片生成/文生图/Text-to-Image + LoRA_1878782083018514433.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_259

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列一_汇总_2020328189045772290.json、图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列三_汇总_2020709944613408769.json、图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列二_汇总_2020500328235409409.json、图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列四_汇总_2020730383855259650.json、图片生成/文生图/B妮B妳_SDXL文生图_系列二_N_S_F_W_汇总_2021460181497942018.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SaveImagesToZip` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `easy promptLine` —— 7/8 个有
- `PreviewBridge` —— 6/8 个有
- `PreviewImage` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1344 | 8 | 90% |
| 高度 | 1720 | 1280 - 1728 | 8 | 91% |
| 采样步数 | 25 | 20 - 25 | 8 | 93% |
| Prompt 约束强度(CFG) | 7 | 7 - 8 | 8 | 95% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | karras | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 0.6 | 0.4 - 0.6 | 8 | 88% |
| LoRA 文本强度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1344，8 个样本，取值集中（一致性 90%）
- 高度 中位数 1720，观测区间 1280 - 1728，8 个样本，取值集中（一致性 91%）
- 采样步数 中位数 25，观测区间 20 - 25，8 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 8，8 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 karras，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，观测区间 0.4 - 0.6，8 个样本，取值集中（一致性 88%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
