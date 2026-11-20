---
name: text_to_image_sampler_clip_unet_72
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9215
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001.Z-image生图巅峰009.Z-回车批量文生图+flux-vae_2033738805638860802.json, 图片生成/文生图/1.阿清的z-image工作流_2037804089450438658.json, 图片生成/文生图/33号特工：Z-image小钢炮，文生图+本地解码+彩图_2046531810259116033.json, 图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图002.Z-image批量文生图.json_2021966315602317313.json, 图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069624809176256513.json, 图片生成/文生图/LH-DMT版本-2.生图片类-029.Z-image智能改词文生图-NF_2016493278639693826.json, 图片生成/文生图/Zimage-turbo保暖内衣_2051484069925531650.json, 图片生成/文生图/krea2+z_image+boogu模型测试对比_2069616764018843650.json, 图片生成/文生图/zimage+krea2+boogu三模型对比_2069599329727373314.json, 平台全量/Gemma4+Zimage-turbo反推文生图_2095912752433946625.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/001.Z-image生图巅峰009.Z-回车批量文生图+flux-vae_2033738805638860802.json、图片生成/文生图/1.阿清的z-image工作流_2037804089450438658.json、图片生成/文生图/33号特工：Z-image小钢炮，文生图+本地解码+彩图_2046531810259116033.json、图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图002.Z-image批量文生图.json_2021966315602317313.json、图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069624809176256513.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 9/10 个有
- `String Literal` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `CR Prompt List` —— 8/10 个有
- `CR Text` —— 5/10 个有
- `Dapao_LlamaCaption` —— 5/10 个有
- `Dapao_LlamaCaptionOptions` —— 5/10 个有
- `LoadImage` —— 5/10 个有
- `RegexReplace` —— 5/10 个有
- `easy cleanGpuUsed` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `LayerUtility: ImageReel` —— 2/10 个有
- `LayerUtility: ImageReelComposit` —— 2/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `ExecutionBlocker` —— 1/10 个有
- `ProcessString` —— 1/10 个有
- `TT_img_enc_v2` —— 1/10 个有
- `easy promptList` —— 1/10 个有
- `llama_cpp_instruct_adv` —— 1/10 个有
- `llama_cpp_model_loader` —— 1/10 个有
- `llama_cpp_parameters` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1280 | 10 | 78% |
| 高度 | 1280 | 720 - 1280 | 10 | 86% |
| 采样步数 | 9 | 4 - 20 | 10 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 10 | 97% |
| 采样算法 | res_2s | - | 10 | 40% |
| 调度器 | bong_tangent | - | 10 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1280，10 个样本
- 高度 中位数 1280，观测区间 720 - 1280，10 个样本，取值集中（一致性 86%）
- 采样步数 中位数 9，观测区间 4 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，10 个样本，取值集中（一致性 97%）
- 采样算法 最常用 res_2s，10 个样本，一致性 40%
- 调度器 最常用 bong_tangent，10 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
