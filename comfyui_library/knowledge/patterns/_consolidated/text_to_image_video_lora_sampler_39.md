---
name: text_to_image_video_lora_sampler_39
type: Text To Image
frequency: 18
level: strong
coverage: 0.895222
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimax h3多参工作流｜多图参考图生视频生成_2094887223530450946.json, 视频生成/图生视频/minimax h3电商带货视频自动提示词模特产品展示_2088181792762318849.json, 视频生成/图生视频/全能参考加速版图生视频｜AIGC短剧视频生成工作流_2087223105965084673.json, 视频生成/图生视频/全能参考工作流｜MiniMax H3图生视频一键生成_2090270213274165249.json, 视频生成/图生视频/全能视频生成｜MiniMax H3开源图生视频直出_2089796312794488834.json, 视频生成/图生视频/加速版MiniMax H3图文一键生视频 快速出片方案_2109082909939429378.json, 视频生成/图生视频/动作镜头参考洗稿｜MiniMax-H3视频运镜生成_2093772942814572545.json, 视频生成/图生视频/去油版数字人口播唱歌MV加速开源版｜MiniMax H3角色设计人物类特效图生视频_2088339977326383106.json, 视频生成/图生视频/去油版数字人口播唱歌MV加速开源｜MiniMax H3人物类特效角色设计图生视频_2088325534035042306.json, 视频生成/图生视频/去油版数字人口播唱歌MV加速版MiniMax H3开源版图生视频_2088371949490761729.json, 视频生成/图生视频/参考生视频开源版｜Minimax-H3短剧漫剧角色表演_2094781908717756417.json, 视频生成/图生视频/双时钟采样4步无损加速｜MiniMAX-H3-T8图生视频_2096272908212588545.json, 视频生成/图生视频/唱歌MV数字人｜H3音频驱动多参视频生成对口型_2093102730167541762.json, 视频生成/图生视频/镜头动作参考洗稿｜MiniMax-H3视频运镜图生视频_2093442197000646657.json, 视频生成/图生视频/音频驱动唱歌MV｜H3数字人多参视频生成_2093260475822854145.json, 视频生成/文生视频/H3音频驱动数字人加速版参考生视频超长时长处理工具_2100639863480606722.json, 视频生成/文生视频/MiniMax H3音频驱动数字人加速版长视频直出处理工具_2101009649368653826.json, 视频生成/文生视频/MiniMax H3音频驱动数字人加速版｜参考生视频长视频直出_2100769157192183810.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_39

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/minimax h3多参工作流｜多图参考图生视频生成_2094887223530450946.json、视频生成/图生视频/minimax h3电商带货视频自动提示词模特产品展示_2088181792762318849.json、视频生成/图生视频/全能参考加速版图生视频｜AIGC短剧视频生成工作流_2087223105965084673.json、视频生成/图生视频/全能参考工作流｜MiniMax H3图生视频一键生成_2090270213274165249.json、视频生成/图生视频/全能视频生成｜MiniMax H3开源图生视频直出_2089796312794488834.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 15/18 个有
- `MiniMaxH3DualClockSamplerT8` —— 14/18 个有
- `ModelAttentionBackend` —— 12/18 个有
- `CR Prompt Text` —— 10/18 个有
- `LoadAudio` —— 10/18 个有
- `PrimitiveStringMultiline` —— 6/18 个有
- `SolAttnMiniMax` —— 6/18 个有
- `PreviewAudio` —— 5/18 个有
- `TrimAudioDuration` —— 5/18 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 4/18 个有
- `ImageResizeKJv2` —— 3/18 个有
- `SaveImage` —— 3/18 个有
- `easy int` —— 3/18 个有
- `CR Text` —— 2/18 个有
- `Fast Groups Bypasser (rgthree)` —— 2/18 个有
- `GetImageSize` —— 2/18 个有
- `ImageConcanate` —— 2/18 个有
- `MiniMaxH3BlockCacheT8` —— 2/18 个有
- `VHS_LoadVideo` —— 2/18 个有
- `ImageScaleToTotalPixels` —— 1/18 个有
- `RHHiddenNodes` —— 1/18 个有
- `RHLLMChatNode` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
