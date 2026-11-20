---
name: text_to_image_video_lora_sampler_41
type: Text To Image
frequency: 17
level: strong
coverage: 0.898647
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3多图参考官方提示词模板｜提速40%无劣化真人短剧剧情演绎数字人_2090475334801125378.json, 数字人/数字人/动态数字人口播生成｜MiniMax H3音频驱动制作_2096471857250791426.json, 数字人/数字人/官方提示词模板提速40%｜MiniMax H3多图参考真人短剧演绎_2090193856364109826.json, 视频生成/图生视频/H3全能参考工作流，图生视频多参考视频生成方案_2108432045293793282.json, 视频生成/图生视频/H3质变音频驱动数字人｜全能参考升级版｜精准可控说话表演_2104819764299386881.json, 视频生成/图生视频/H3音频驱动数字人单人版｜口播视频高质量生成_2094900079206424577.json, 视频生成/图生视频/Minimax H3开源数字人，说话唱歌文生视频两不误_2111201846995017729.json, 视频生成/图生视频/Minimax H3开源版数字人说话唱歌 数字人口播方案_2109421181240700930.json, 视频生成/图生视频/Minimax H3开源版数字人｜说话唱歌口播一条龙免费跑_2111083053400547329.json, 视频生成/图生视频/Minimax H3开源版数字人｜说话唱歌视频都能做_2106615667175804930.json, 视频生成/图生视频/h3图生视频加速版快速出片高效生成工作流_2088357034935808002.json, 视频生成/文生视频/MiniMax H3开源版数字人说话唱歌音频驱动图生视频处理工具_2102519299419230209.json, 视频生成/文生视频/MiniMax H3开源版数字人｜音频驱动说话唱歌全能出镜_2108025468082540546.json, 视频生成/文生视频/Minimax H3开源数字人说话唱歌｜文生视频生成_2094523338252181506.json, 视频生成/文生视频/Minimax H3开源版数字人说话唱歌工作流，文生视频数字人图生视频方案_2108269811766751233.json, 视频生成/文生视频/Minimax H3开源版数字人｜说话唱歌口型同步｜文生视频图生视频都行_2102288689492746241.json, 视频生成/文生视频/MinimaxH3数字人说话唱歌开源版ENGENG_2087131139222892545.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_41

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（数字人/数字人/MiniMax H3多图参考官方提示词模板｜提速40%无劣化真人短剧剧情演绎数字人_2090475334801125378.json、数字人/数字人/动态数字人口播生成｜MiniMax H3音频驱动制作_2096471857250791426.json、数字人/数字人/官方提示词模板提速40%｜MiniMax H3多图参考真人短剧演绎_2090193856364109826.json、视频生成/图生视频/H3全能参考工作流，图生视频多参考视频生成方案_2108432045293793282.json、视频生成/图生视频/H3质变音频驱动数字人｜全能参考升级版｜精准可控说话表演_2104819764299386881.json…）

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
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `MiniMaxH3ReferenceToVideo` —— 16/17 个有
- `PathchSageAttentionKJ` —— 15/17 个有
- `AudioCrop` —— 14/17 个有
- `LoadAudio` —— 14/17 个有
- `PrimitiveStringMultiline` —— 14/17 个有
- `SoundFlow_GetLength` —— 14/17 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 14/17 个有
- `PreviewAudio` —— 13/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/17 个有
- `Int` —— 10/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/17 个有
- `SaveImage` —— 8/17 个有
- `ResolutionSelector` —— 7/17 个有
- `EasyCache` —— 3/17 个有
- `VAEDecodeAudio` —— 3/17 个有
- `FlashVSRNode` —— 2/17 个有
- `GetImageSize` —— 2/17 个有
- `LoraLoaderBypassModelOnly` —— 2/17 个有
- `ModelAttentionBackend` —— 2/17 个有
- `ResizeImageMaskNode` —— 2/17 个有
- `Sleep` —— 2/17 个有
- `Textbox` —— 2/17 个有
- `EnhancedLoadDiffusionModel` —— 1/17 个有
- `MiniMaxH3ImageToVideo` —— 1/17 个有
- `RHHiddenNodes` —— 1/17 个有
- `SolAttnPatch` —— 1/17 个有
- `Text` —— 1/17 个有

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
