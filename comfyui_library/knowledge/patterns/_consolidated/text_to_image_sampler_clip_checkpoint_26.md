---
name: text_to_image_sampler_clip_checkpoint_26
type: Text To Image
frequency: 3
level: moderate
coverage: 0.813
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [平台全量/Pixel Art Workflow_1864574343366787073.json, 平台全量/Workflow 18 (Silhouette- Juggernaut XI)_1867466563682271234.json, 平台全量/xl卡通风格文生图_1777968814491766785.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_26

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Pixel Art Workflow_1864574343366787073.json、平台全量/Workflow 18 (Silhouette- Juggernaut XI)_1867466563682271234.json、平台全量/xl卡通风格文生图_1777968814491766785.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 2/3 个有
- `FreeU_V2` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `VAELoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1056 | 3 | 71% |
| 高度 | 1024 | 512 - 1024 | 3 | 72% |
| 采样步数 | 30 | 20 - 37 | 3 | 76% |
| Prompt 约束强度(CFG) | 7 | 5.5 - 7 | 3 | 89% |
| 采样算法 | dpmpp_sde_gpu | - | 3 | 33% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 0.33 - 1 | 3 | 59% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1056，3 个样本
- 高度 中位数 1024，观测区间 512 - 1024，3 个样本
- 采样步数 中位数 30，观测区间 20 - 37，3 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 5.5 - 7，3 个样本，取值集中（一致性 89%）
- 采样算法 最常用 dpmpp_sde_gpu，3 个样本，一致性 33%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.33 - 1，3 个样本
