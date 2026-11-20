---
name: unknown_workflow_lora_sampler_unet_17
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.8762
common_nodes: [CLIPLoader, CR Text, ConditioningZeroOut, ImageConcatMulti, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2026QwenEidtPro三图合拼新图_2008362890092351490.json, 图片生成/图生图/Qwen-Edit-2511双图编辑 + SeedVR2.5 高清修复_2004406237934612481.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三参考图生图_2004193508749705217.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三参考图生图_2004195228674387969.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2009913119514042370.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2018149631380692993.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2028029555759386626.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2043587733939036162.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2045087991701446658.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2104424521867550721.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5双图参考图生图_2049826076968407042.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5多图图生图_2008422093519589377.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5多图图生图_2016415181395468289.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5多图图生图_2042524893127909377.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5多图图生图_2044326938562535426.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5多图图生图_2062415214137659394.json, 图片生成/图生图/Qwen-Image-Edit-2511 多图参考生图_2004752360121528322.json, 图片生成/图生图/Qwen故事短剧双主体用指定背景_2018860398941839362.json, 图片生成/图生图/VR2.5三图参考图生图_2008735009888280577.json, 图片生成/图生图/ZCWH-换装测试版_2013801696685723650.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_17

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/2026QwenEidtPro三图合拼新图_2008362890092351490.json、图片生成/图生图/Qwen-Edit-2511双图编辑 + SeedVR2.5 高清修复_2004406237934612481.json、图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三参考图生图_2004193508749705217.json、图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三参考图生图_2004195228674387969.json、图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2009913119514042370.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `ImageConcatMulti`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 19/20 个有
- `FluxKontextMultiReferenceLatentMethod` —— 19/20 个有
- `ImageConcanate` —— 19/20 个有
- `LayerUtility: PurgeVRAM V2` —— 19/20 个有
- `SeedVR2LoadDiTModel` —— 19/20 个有
- `SeedVR2LoadVAEModel` —— 19/20 个有
- `SeedVR2VideoUpscaler` —— 19/20 个有
- `TextEncodeQwenImageEditPlus` —— 19/20 个有
- `Fast Groups Bypasser (rgthree)` —— 18/20 个有
- `Fast Groups Muter (rgthree)` —— 18/20 个有
- `PreviewImage` —— 17/20 个有
- `CompressImages` —— 2/20 个有
- `Anything Everywhere` —— 1/20 个有
- `FluxKontextImageScale` —— 1/20 个有
- `PrimitiveBoolean` —— 1/20 个有
- `QwenImageLatentAspectRatio` —— 1/20 个有
- `Seed` —— 1/20 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/20 个有
- `WujiCleaner` —— 1/20 个有
- `WujiUpscaler` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 2752 | 19 | 47% |
| 高度 | 1280 | 720 - 1536 | 19 | 89% |
| 采样步数 | 8 | 6 - 8 | 20 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 2752，19 个样本，取值分散，一致性仅 47%
- 高度 中位数 1280，观测区间 720 - 1536，19 个样本，取值集中（一致性 89%）
- 采样步数 中位数 8，观测区间 6 - 8，20 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
