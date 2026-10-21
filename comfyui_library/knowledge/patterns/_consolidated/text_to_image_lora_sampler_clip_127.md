---
name: text_to_image_lora_sampler_clip_127
type: Text To Image
frequency: 9
level: strong
coverage: 0.858667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, GetImageSize, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/单图生成视频｜MiniMax H3 FL2VA开源版工作流_2093251838228393985.json, 视频生成/图生视频/单图生成视频｜MiniMax H3 FL2VA开源版工作流_2094055607228780545.json, 视频生成/图生视频/单图生成视频｜MiniMax H3 FL2VA开源版直出_2093852526583050241.json, 视频生成/图生视频/去高动态噪点加速版｜Minimax H3图生视频首尾帧高清出片_2088736756886757378.json, 视频生成/图生视频/图生视频加速版｜MiniMax H3人物场景特效生成_2093842351939743746.json, 视频生成/图生视频/图生视频轻松上手｜MiniMax H3 基础款快速出片_2096251513273405442.json, 视频生成/图生视频/官流直出美少女视频｜Minimax-H3 图生视频原汁原味_2096269567709499393.json, 视频生成/图生视频/桌面女友互动形象生成，图生图转图生视频方案_2111234634200735745.json, 视频生成/图生视频/桌面女友图生视频｜暖心陪伴向AI视频一键生成_2111272944059117569.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_127

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/单图生成视频｜MiniMax H3 FL2VA开源版工作流_2093251838228393985.json、视频生成/图生视频/单图生成视频｜MiniMax H3 FL2VA开源版工作流_2094055607228780545.json、视频生成/图生视频/单图生成视频｜MiniMax H3 FL2VA开源版直出_2093852526583050241.json、视频生成/图生视频/去高动态噪点加速版｜Minimax H3图生视频首尾帧高清出片_2088736756886757378.json、视频生成/图生视频/图生视频加速版｜MiniMax H3人物场景特效生成_2093842351939743746.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `GetImageSize`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 6/9 个有
- `ImageScale` —— 6/9 个有
- `PrimitiveBoolean` —— 6/9 个有
- `PrimitiveInt` —— 6/9 个有
- `ResolutionSelector` —— 5/9 个有
- `ImageScaleToTotalPixels` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `ImageCompositeMasked` —— 2/9 个有
- `ImageScaleBy` —— 2/9 个有
- `Int` —— 2/9 个有
- `ManualSigmas` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `QwenImage21Cache` —— 2/9 个有
- `SamplerCustom` —— 2/9 个有
- `SaveImage` —— 2/9 个有
- `TextEncodeQwenImage21` —— 2/9 个有
- `ExtendIntermediateSigmas` —— 1/9 个有
- `H3SigmaRefiner` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LayerUtility: TextBox` —— 1/9 个有
- `MiniMaxH3SigmaShift` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `ResizeImageMaskNode` —— 1/9 个有
- `Wan_Organic_Skin` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
