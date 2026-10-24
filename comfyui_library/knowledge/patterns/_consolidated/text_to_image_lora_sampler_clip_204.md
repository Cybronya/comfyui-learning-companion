---
name: text_to_image_lora_sampler_clip_204
type: Text To Image
frequency: 9
level: strong
coverage: 0.721444
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoraLoader, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列一_汇总_2020328189045772290.json, 图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列三_汇总_2020709944613408769.json, 图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列二_汇总_2020500328235409409.json, 图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列四_汇总_2020730383855259650.json, 图片生成/文生图/B妮B妳_SDXL文生图_系列二_N_S_F_W_汇总_2021460181497942018.json, 图片生成/文生图/B妮B妳_SDXL文生图_系列五_N_S_F_W_汇总_2020753702591668225.json, 图片生成/文生图/B妮B妳_SDXL文生图_系列六_N_S_F_W_汇总_2020827252291801089.json, 图片生成/文生图/Text-to-Image + LoRA_1878782083018514433.json, 图片生成/文生图/【AI小王子】20.LCM lora八步生成_2046843881974665218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_204

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列一_汇总_2020328189045772290.json、图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列三_汇总_2020709944613408769.json、图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列二_汇总_2020500328235409409.json、图片生成/文生图/B妮B妳_N_S_F_W_SDXL文生图_系列四_汇总_2020730383855259650.json、图片生成/文生图/B妮B妳_SDXL文生图_系列二_N_S_F_W_汇总_2021460181497942018.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SaveImagesToZip` —— 7/9 个有
- `PreviewAny` —— 7/9 个有
- `easy promptLine` —— 7/9 个有
- `PreviewBridge` —— 6/9 个有
- `PreviewImage` —— 3/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1344 | 9 | 91% |
| 高度 | 1720 | 1024 - 1728 | 9 | 85% |
| 采样步数 | 25 | 8 - 25 | 9 | 76% |
| Prompt 约束强度(CFG) | 7 | 1.5 - 8 | 9 | 72% |
| 采样算法 | euler | - | 9 | 67% |
| 调度器 | karras | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 0.6 | 0.4 - 1 | 9 | 76% |
| LoRA 文本强度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1344，9 个样本，取值集中（一致性 91%）
- 高度 中位数 1720，观测区间 1024 - 1728，9 个样本，取值集中（一致性 85%）
- 采样步数 中位数 25，观测区间 8 - 25，9 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 1.5 - 8，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 67%
- 调度器 最常用 karras，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，观测区间 0.4 - 1，9 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
