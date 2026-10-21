---
name: text_to_image_sampler_clip_vae_19
type: Text To Image
frequency: 3
level: moderate
coverage: 0.770667
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/test1_2081667502253371394.json, 图片生成/文生图/vibex-simple-txt2img-workflow_2101489827303743489.json, 图片生成/文生图/【尺素】RED-Z-IMAGE-AIO文生图_2074013706979209217.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/test1_2081667502253371394.json、图片生成/文生图/vibex-simple-txt2img-workflow_2101489827303743489.json、图片生成/文生图/【尺素】RED-Z-IMAGE-AIO文生图_2074013706979209217.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/3 个有
- `CheckpointLoader` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1000 | 3 | 74% |
| 高度 | 1280 | 512 - 1904 | 3 | 54% |
| 采样步数 | 20 | 10 - 20 | 3 | 72% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 3 | 42% |
| 采样算法 | dpmpp_sde | - | 3 | 33% |
| 调度器 | karras | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1000，3 个样本
- 高度 中位数 1280，观测区间 512 - 1904，3 个样本
- 采样步数 中位数 20，观测区间 10 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，3 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 33%
- 调度器 最常用 karras，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
