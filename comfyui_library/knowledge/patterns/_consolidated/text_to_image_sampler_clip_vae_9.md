---
name: text_to_image_sampler_clip_vae_9
type: Text To Image
frequency: 10
level: weak
coverage: 0.7412
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions]
members: [图片生成/文生图/1940313410569682946.json, 图片生成/文生图/1942186080890204162.json, 图片生成/文生图/1944743997447524354.json, 图片生成/文生图/1951531387230826497.json, 图片生成/文生图/F.1 在线生图-反推_1873979338214559746.json, 图片生成/文生图/Z-image 平替Flux2 图片反推+文生图  最强真实人物细节多场景生成 Z-image_1993908699964047361.json, 图片生成/文生图/Z-imageTurbo 快速高清 4K 工作流_1995495345377443841.json, 图片生成/文生图/图片反推+Z-image最强真实人物细节多场景生成_1993853085036511234.json, 图片生成/文生图/图片反推+Z-image最强真实人物细节多场景生成_1998679334598664193.json, 图片生成/文生图/图片反推+Z-image最强真实人物细节多场景生成_2002784165995114497.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_9

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1940313410569682946.json、图片生成/文生图/1942186080890204162.json、图片生成/文生图/1944743997447524354.json、图片生成/文生图/1951531387230826497.json、图片生成/文生图/F.1 在线生图-反推_1873979338214559746.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 9/10 个有
- `ShowText|pysssss` —— 9/10 个有
- `UNETLoader` —— 9/10 个有
- `DeepTranslatorTextNode` —— 7/10 个有
- `Fast Groups Muter (rgthree)` —— 6/10 个有
- `CLIPLoader` —— 5/10 个有
- `FluxGuidance` —— 5/10 个有
- `easy saveText` —— 5/10 个有
- `AspectRatio` —— 4/10 个有
- `DualCLIPLoader` —— 4/10 个有
- `PreviewImage` —— 4/10 个有
- `easy promptList` —— 4/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `Anything Everywhere3` —— 1/10 个有
- `NunchakuFluxDiTLoader` —— 1/10 个有
- `NunchakuTextEncoderLoaderV2` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 512 - 1920 | 10 | 58% |
| 高度 | 1080 | 512 - 1920 | 10 | 69% |
| 采样步数 | 15 | 10 - 30 | 10 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 10 | 0% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1052，观测区间 512 - 1920，10 个样本
- 高度 中位数 1080，观测区间 512 - 1920，10 个样本
- 采样步数 中位数 15，观测区间 10 - 30，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，10 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: JoyCaptionBeta1、LayerUtility: LoadJoyCaptionBeta1Model、LayerUtility: JoyCaptionBeta1ExtraOptions
