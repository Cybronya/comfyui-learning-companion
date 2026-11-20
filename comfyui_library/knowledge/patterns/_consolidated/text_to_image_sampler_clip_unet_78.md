---
name: text_to_image_sampler_clip_unet_78
type: Text To Image
frequency: 9
level: weak
coverage: 0.842778
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2_turbo 4K放大_2079597154166988801.json, 图片生成/文生图/Krea2_turbo 4K放大_2080129101544906754.json, 图片生成/文生图/Krea2_turbo_4K放大_2080939525467099137.json, 图片生成/文生图/Krea2_turbo_4K放大_2095797338735468546.json, 图片生成/文生图/Krea2_turbo_4K放大_2096154230204751874.json, 图片生成/文生图/Krea2_turbo高清放大4K｜美少女文生图画质增强_2096327079028678658.json, 图片生成/文生图/Krea2文生图极简工作流｜输入描述直接出高质量图_2107649169803534338.json, 图片生成/文生图/Krea2特定风格人像大作文生图｜固定风格批量出人像大片_2099133481472315394.json, 图片生成/文生图/▶▷Krea2文生图_2107457543818801153.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_78

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Krea2_turbo 4K放大_2079597154166988801.json、图片生成/文生图/Krea2_turbo 4K放大_2080129101544906754.json、图片生成/文生图/Krea2_turbo_4K放大_2080939525467099137.json、图片生成/文生图/Krea2_turbo_4K放大_2095797338735468546.json、图片生成/文生图/Krea2_turbo_4K放大_2096154230204751874.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 8/9 个有
- `PreviewImage` —— 7/9 个有
- `SeedVR2LoadDiTModel` —— 6/9 个有
- `SeedVR2LoadVAEModel` —— 6/9 个有
- `SeedVR2VideoUpscaler` —— 6/9 个有
- `TextConcatenate` —— 6/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `JjkText` —— 3/9 个有
- `solarL_SaveImagesToZip` —— 3/9 个有
- `孤海注释` —— 3/9 个有
- `Seed (rgthree)` —— 2/9 个有
- `easy anythingIndexSwitch` —— 2/9 个有
- `easy ifElse` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 9 | 37% |
| 高度 | 1024 | 80 - 1280 | 9 | 36% |
| 采样步数 | 8 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 9 | 24% |
| 采样算法 | euler | - | 9 | 67% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 37%
- 高度 中位数 1024，观测区间 80 - 1280，9 个样本，取值分散，一致性仅 36%
- 采样步数 中位数 8，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（12/9 个样本）：Steps较低可能导致细节不足
