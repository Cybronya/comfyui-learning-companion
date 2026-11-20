---
name: text_to_image_sampler_clip_checkpoint_10
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9917
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [平台全量/Logo Generator_1892830173983629313.json, 平台全量/XL_lorapix_4X_1818313459481116674.json, 平台全量/XL文生图LoRA古状仙侠女_1843465014333100033.json, 平台全量/cute_doll可爱娃娃手办_1778265652243521538.json, 平台全量/像素风迷你场景模型_1790240809438793730.json, 平台全量/可爱表情包_1793208638219800578.json, 平台全量/极简插画_1783768862114717697.json, 平台全量/珠宝商品图_1778262934930120705.json, 平台全量/针织娃娃_1778295132483805185.json, 平台全量/高清商品图（文生图）_1778260517660450818.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_10

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/Logo Generator_1892830173983629313.json、平台全量/XL_lorapix_4X_1818313459481116674.json、平台全量/XL文生图LoRA古状仙侠女_1843465014333100033.json、平台全量/cute_doll可爱娃娃手办_1778265652243521538.json、平台全量/像素风迷你场景模型_1790240809438793730.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 9/10 个有
- `UpscaleModelLoader` —— 9/10 个有
- `LoraLoader` —— 7/10 个有
- `VAEEncode` —— 5/10 个有
- `CLIPSetLastLayer` —— 4/10 个有
- `VAELoader` —— 3/10 个有
- `LatentUpscaleBy` —— 2/10 个有
- `DF_Text_Box` —— 1/10 个有
- `SDXLResolutionPresets` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 10 | 90% |
| Prompt 约束强度(CFG) | 8 | 3.5 - 8 | 10 | 81% |
| 采样算法 | dpmpp_2m | - | 10 | 40% |
| 调度器 | karras | - | 10 | 60% |
| 重绘幅度 | 1 | 0.28 - 1 | 10 | 64% |
| 宽度 | 768 | 512 - 1024 | 10 | 79% |
| 高度 | 1024 | 512 - 1280 | 10 | 72% |
| LoRA 模型强度 | 0.55 | 0.45 - 1 | 7 | 71% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，10 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 3.5 - 8，10 个样本，取值集中（一致性 81%）
- 采样算法 最常用 dpmpp_2m，10 个样本，一致性 40%
- 调度器 最常用 karras，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.28 - 1，10 个样本
- 宽度 中位数 768，观测区间 512 - 1024，10 个样本
- 高度 中位数 1024，观测区间 512 - 1280，10 个样本
- LoRA 模型强度 中位数 0.55，观测区间 0.45 - 1，7 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
