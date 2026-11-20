---
name: text_to_image_lora_sampler_clip_556
type: Text To Image
frequency: 3
level: strong
coverage: 0.851333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Seedance2.0Mini文生视频，文字转视频高效直出_2111880856880111618.json, 图片生成/文生图/Z Image文生图标准版工作流，高质量文本到图像生成方案_2105786409570361346.json, 图片生成/文生图/Z-Image Turbo九宫格文生图｜手动提示词基础版｜动漫角色设计一次出九张_2104798488964984833.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_556

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Seedance2.0Mini文生视频，文字转视频高效直出_2111880856880111618.json、图片生成/文生图/Z Image文生图标准版工作流，高质量文本到图像生成方案_2105786409570361346.json、图片生成/文生图/Z-Image Turbo九宫格文生图｜手动提示词基础版｜动漫角色设计一次出九张_2104798488964984833.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageGridComposite3x3` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `RH_RhartVideoSparkvideo20MiniTextToVideo` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（12/3 个样本）：Steps较低可能导致细节不足
