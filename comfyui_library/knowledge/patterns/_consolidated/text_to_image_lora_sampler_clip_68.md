---
name: text_to_image_lora_sampler_clip_68
type: Text To Image
frequency: 17
level: strong
coverage: 0.901882
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3开源版图片编辑｜多图合成换背景创意生图_2097158027400007682.json, 图片生成/图生图/MiniMax H3开源版图片编辑｜多图编辑换背景创意生图人物特效_2089713767801245698.json, 图片生成/图生图/MiniMax_H3开源版图片编辑｜多图编辑换背景创意生图_2097098299735101441.json, 图片生成/图生图/krea2自用图生图｜图像编辑一键生成直出_2092320745304182786.json, 图片生成/图生图/图片视频图片编辑｜MiniMax_H3图生图换背景_2092940233808637954.json, 图片生成/图生图/自用图生图工具｜krea2低幅度重绘一键出图_2092549239720210433.json, 图片生成/文生图/2K加速版文生图｜MiniMaxH3开源美少女写实出图_2089063557869694977.json, 视频生成/文生视频/5秒1080p仅8分钟｜MiniMax-H3图生视频全节点注释版_2093768843360563202.json, 视频生成/文生视频/5秒1080p只要8分钟｜MiniMax-H3图生视频全节点注释_2094005447392063489.json, 视频生成/文生视频/5秒1080p文生视频8分钟出片 MiniMax-H3 全节点注释_2094187651468455937.json, 视频生成/文生视频/8步加速文生视频｜minimax_h3文字生成视频工作流_2088367583484538882.json, 视频生成/文生视频/8步加速电影质感 Minimax H3 文生视频LoRA强化出片_2094165667820957697.json, 视频生成/文生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100678580580732929.json, 视频生成/文生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086197329035616258.json, 视频生成/文生视频/H3真实电影质感全能参考 文生视频图生视频_2100309862587654145.json, 视频生成/文生视频/真实电影质感｜MiniMax H3文生图生视频生成_2094051162357063682.json, 视频生成/文生视频/真实电影质感｜MiniMax H3文生图生视频直出_2093845276451753986.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/MiniMax H3开源版图片编辑｜多图合成换背景创意生图_2097158027400007682.json、图片生成/图生图/MiniMax H3开源版图片编辑｜多图编辑换背景创意生图人物特效_2089713767801245698.json、图片生成/图生图/MiniMax_H3开源版图片编辑｜多图编辑换背景创意生图_2097098299735101441.json、图片生成/图生图/krea2自用图生图｜图像编辑一键生成直出_2092320745304182786.json、图片生成/图生图/图片视频图片编辑｜MiniMax_H3图生图换背景_2092940233808637954.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 16/17 个有
- `LoadImage` —— 15/17 个有
- `ResolutionSelector` —— 15/17 个有
- `PathchSageAttentionKJ` —— 14/17 个有
- `ComfyMathExpression` —— 10/17 个有
- `CreateVideo` —— 10/17 个有
- `MiniMaxH3ReferenceToVideo` —— 10/17 个有
- `SaveVideo` —— 10/17 个有
- `VAEDecodeAudio` —— 10/17 个有
- `EasyCache` —— 9/17 个有
- `SaveImage` —— 9/17 个有
- `MiniMaxH3ImageToVideo` —— 7/17 个有
- `PrimitiveFloat` —— 7/17 个有
- `PrimitiveStringMultiline` —— 7/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/17 个有
- `ImageFromBatch` —— 5/17 个有
- `LoadAudio` —— 5/17 个有
- `VHS_LoadVideo` —— 5/17 个有
- `Int` —— 4/17 个有
- `LayerUtility: ImageReel` —— 4/17 个有
- `LayerUtility: ImageReelComposit` —— 4/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/17 个有
- `MiniMaxH3BlockCacheT8` —— 4/17 个有
- `easy anythingIndexSwitch` —— 4/17 个有
- `CR Text` —— 3/17 个有
- `DisableNoise` —— 3/17 个有
- `H3SigmaRefiner` —— 3/17 个有
- `SplitSigmas` —— 3/17 个有
- `Fast Groups Bypasser (rgthree)` —— 2/17 个有
- `ImageScaleToTotalPixels` —— 2/17 个有
- `VAEEncode` —— 2/17 个有
- `easy showAnything` —— 2/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
