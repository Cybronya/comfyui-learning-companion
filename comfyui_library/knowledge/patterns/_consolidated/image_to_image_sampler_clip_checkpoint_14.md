---
name: image_to_image_sampler_clip_checkpoint_14
type: Image To Image
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/SDXL ControlNet开启5.0_2095761958334197762.json, 图片生成/图生图/SDXL4.0_2095753350984851457.json, 平台全量/真人漫改（插画风格）_1932358846465867777.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SDXL ControlNet开启5.0_2095761958334197762.json、图片生成/图生图/SDXL4.0_2095753350984851457.json、平台全量/真人漫改（插画风格）_1932358846465867777.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetApplySD3` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 采样步数 | 18 | 18 - 25 | 3 | 84% |
| Prompt 约束强度(CFG) | 7 | 3 - 7 | 3 | 67% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 0.2 | 0.2 - 0.6 | 3 | 43% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 18，观测区间 18 - 25，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 3 - 7，3 个样本
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 0.6，3 个样本，取值分散，一致性仅 43%
