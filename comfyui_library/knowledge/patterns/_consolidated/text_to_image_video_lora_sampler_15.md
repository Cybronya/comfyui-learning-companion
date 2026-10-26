---
name: text_to_image_video_lora_sampler_15
type: Text To Image
frequency: 29
level: strong
coverage: 0.846241
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3开源版音频驱动数字人-说话唱歌对口型MV生成加速版_2087383420715487233.json, 视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV加速版_2094877180009476098.json, 视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV生成_2094880039287476225.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2086034301048680450.json, 视频生成/图生视频/Minimax H3开源版数字人｜说话唱歌口播一条龙免费跑_2111083053400547329.json, 视频生成/图生视频/Minimax H3开源版数字人｜说话唱歌视频都能做_2106615667175804930.json, 视频生成/图生视频/Minimax H3音频驱动数字人对口型人物类特效图生视频_2088195742426030081.json, 视频生成/图生视频/MinimaxH3多参音视频生成开源版（9图3视频3音频）ENGENG_2087124578177998850.json, 视频生成/图生视频/对口型音频驱动MiniMax H3数字人唱歌工作流，一张图一段音频生成视频_2106864466716614658.json, 视频生成/图生视频/数字人单人极速版｜Minimax H3角色一致图生视频_2092026882165403650.json, 视频生成/图生视频/数字人唱歌口播｜MiniMax H3图生视频一键直出_2090220837587742722.json, 视频生成/图生视频/数字人说话唱歌MV｜MiniMaxH3开源版音频驱动对口型加速生成_2090848011483172865.json, 视频生成/图生视频/海螺H3全能参考生视频加速开源版 9图3视频3音频多模态输入_2105370711207538690.json, 视频生成/图生视频/海螺H3全能参考生视频开源加速版｜9图3视频3音频全支持_2105262580620161026.json, 视频生成/图生视频/让效果图动起来_2102598028669579265.json, 视频生成/图生视频/音频驱动对口型MV｜MiniMaxH3开源数字人加速版_2095079699335700481.json, 视频生成/图生视频/音频驱动对口型｜Minimax H3数字人人物特效图生视频_2089446222766624769.json, 视频生成/图生视频/音频驱动数字人MV｜MiniMaxH3开源版 说话唱歌对口型加速生成_2105524576473141249.json, 视频生成/图生视频/音频驱动数字人对口型｜MiniMaxH3开源版说话唱歌MV生成加速_2090840855216222210.json, 视频生成/图生视频/音频驱动数字人｜MiniMaxH3说话唱歌对口型MV加速版_2090544996637302786.json, 视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085422971736383489.json, 视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085791756154654721.json, 视频生成/文生视频/MiniMax H3开源版数字人说话唱歌音频驱动图生视频处理工具_2102519299419230209.json, 视频生成/文生视频/MiniMax H3开源版数字人｜音频驱动说话唱歌全能出镜_2108025468082540546.json, 视频生成/文生视频/Minimax H3开源数字人说话唱歌｜文生视频生成_2094523338252181506.json, 视频生成/文生视频/Minimax H3开源版数字人说话唱歌工作流，文生视频数字人图生视频方案_2108269811766751233.json, 视频生成/文生视频/Minimax H3开源版数字人｜说话唱歌口型同步｜文生视频图生视频都行_2102288689492746241.json, 视频生成/文生视频/MinimaxH3数字人说话唱歌开源版ENGENG_2087131139222892545.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版｜文生视频数字人图生视频_2090448002296147970.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3开源版音频驱动数字人-说话唱歌对口型MV生成加速版_2087383420715487233.json、视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV加速版_2094877180009476098.json、视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV生成_2094880039287476225.json、视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2086034301048680450.json、视频生成/图生视频/Minimax H3开源版数字人｜说话唱歌口播一条龙免费跑_2111083053400547329.json…）

- **类型**：Text To Image
- **样本数**：29
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 29 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 28/29 个有
- `PrimitiveStringMultiline` —— 28/29 个有
- `孤海注释` —— 25/29 个有
- `AudioCrop` —— 22/29 个有
- `PreviewAudio` —— 22/29 个有
- `SoundFlow_GetLength` —— 22/29 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 22/29 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/29 个有
- `ResolutionSelector` —— 13/29 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/29 个有
- `Any To String (mtb)` —— 8/29 个有
- `GetNode` —— 8/29 个有
- `ImageResizeKJv2` —— 8/29 个有
- `Int` —— 8/29 个有
- `PreviewImage` —— 8/29 个有
- `PrimitiveInt` —— 8/29 个有
- `SetNode` —— 8/29 个有
- `PainterVRAM` —— 7/29 个有
- `VAEDecodeAudio` —— 7/29 个有
- `VHS_LoadVideo` —— 7/29 个有
- `SaveImage` —— 4/29 个有
- `AudioConcat` —— 2/29 个有
- `EmptyAudio` —— 2/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 29 | 100% |
| 高度 | 80 | 80 - 80 | 29 | 100% |
| 采样步数 | 4 | 4 - 4 | 29 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 29 | 100% |
| 采样算法 | er_sde | - | 29 | 100% |
| 调度器 | beta | - | 29 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，29 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，29 个样本，一致性 100%
- 调度器 最常用 beta，29 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 高发问题（29/29 个样本）：Steps较低可能导致细节不足
