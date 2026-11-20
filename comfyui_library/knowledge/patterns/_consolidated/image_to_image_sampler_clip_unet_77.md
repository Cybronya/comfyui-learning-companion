---
name: image_to_image_sampler_clip_unet_77
type: Image To Image
frequency: 6
level: weak
coverage: 0.950667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/cos后期美颜-klein_2028764345802428418.json, 图片生成/图生图/krea2-i2i_2070052084354994178.json, 图片生成/图生图/krea2-线条_2079130154605043714.json, 图片生成/图生图/krea2一键无脑图生图反推工作流_2089918500935651330.json, 图片生成/图生图/krea2图生图反推工作流_2092086082128138241.json, 图片生成/文生图/一键生成橙光易次元文游立绘Krea2_2099360460041707522.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/cos后期美颜-klein_2028764345802428418.json、图片生成/图生图/krea2-i2i_2070052084354994178.json、图片生成/图生图/krea2-线条_2079130154605043714.json、图片生成/图生图/krea2一键无脑图生图反推工作流_2089918500935651330.json、图片生成/图生图/krea2图生图反推工作流_2092086082128138241.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `AILab_QwenVL` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `KSamplerAdvanced` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `SeedVR2LoadDiTModel` —— 1/6 个有
- `SeedVR2LoadVAEModel` —— 1/6 个有
- `SeedVR2VideoUpscaler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 9 | 6 | 0% |
| 采样算法 | euler | - | 6 | 33% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 0.6 | 0.4 - 0.99 | 5 | 70% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 9，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 33%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 0.6，观测区间 0.4 - 0.99，5 个样本
- 高发问题（9/6 个样本）：Steps较低可能导致细节不足
