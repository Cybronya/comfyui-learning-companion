---
name: text_to_image_video_lora_sampler_25
type: Text To Image
frequency: 18
level: strong
coverage: 0.77
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087143209582546946.json, 视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087154037660672001.json, 视频生成/图生视频/MiniMax-H3无限视频生成工作流｜分段接力长视频创作_2097784874290733057.json, 视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json, 视频生成/图生视频/MiniMaxH3文生视频极速二采高质量图ENGENG_2087151474047537153.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2110652655700889602.json, 视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话｜加速版长视频处理工具_2107983189108154369.json, 视频生成/图生视频/Minimax H3双时钟采样参考图生视频｜4步turbo极速出片_2111270718934708225.json, 视频生成/图生视频/Minimax H3开源参考生视频创意视频 漫剧工作流，角色设计图生视频方案_2107927267103035393.json, 视频生成/图生视频/Minimax H3开源参考生视频创意视频短剧漫剧工作流，角色设计图生视频方案_2107965040040177666.json, 视频生成/图生视频/light2v8步lora正式版双时钟｜minimax图生视频工作流_2088212552772841473.json, 视频生成/图生视频/全能参考二采高清放大｜H3 4步加速Lora图生视频_2096298417860468738.json, 视频生成/图生视频/全能参考去油防MINIMAX-H3脸崩工作流ENG_2087124608590901249.json, 视频生成/图生视频/四步加速出片｜H3全能参考二采高清放大带Lora_2096538998759059458.json, 视频生成/图生视频/超级多合一官方V2｜MiniMax H3场景特效图生视频_2089454565593804802.json, 视频生成/图生视频/首尾帧生成视频｜MiniMax H3官方工作流图生视频_2090268705291849730.json, 视频生成/文生视频/4步加速二采放大｜MinimaxH3全能参考三模视频_2094739286921928705.json, 视频生成/文生视频/Fenglairh MiniMax H3 官方版｜完整工作流集合最新加速_2097556019563028482.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087143209582546946.json、视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087154037660672001.json、视频生成/图生视频/MiniMax-H3无限视频生成工作流｜分段接力长视频创作_2097784874290733057.json、视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json、视频生成/图生视频/MiniMaxH3文生视频极速二采高质量图ENGENG_2087151474047537153.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 17/18 个有
- `MiniMaxH3AVDecodeT8` —— 17/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/18 个有
- `RandomNoise` —— 17/18 个有
- `孤海注释` —— 13/18 个有
- `LoraLoaderBypassModelOnly` —— 11/18 个有
- `CR Prompt Text` —— 10/18 个有
- `LoadAudio` —— 10/18 个有
- `MiniMaxH3AudioConditioningT8` —— 10/18 个有
- `BasicScheduler` —— 8/18 个有
- `KSamplerSelect` —— 8/18 个有
- `MiniMaxH3DualClockSamplerT8` —— 8/18 个有
- `MiniMaxH3ReferenceToVideo` —— 8/18 个有
- `ModelAttentionBackend` —— 8/18 个有
- `Fast Groups Bypasser (rgthree)` —— 7/18 个有
- `GetNode` —— 7/18 个有
- `ImageResizeKJv2` —— 7/18 个有
- `PT_H3ConcatAVLatent` —— 7/18 个有
- `SetNode` —— 7/18 个有
- `VAEEncode` —— 7/18 个有
- `VHS_LoadVideo` —— 7/18 个有
- `SaveImage` —— 6/18 个有
- `PreviewImage` —— 5/18 个有
- `SolAttnMiniMax` —— 5/18 个有
- `Text` —— 5/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/18 个有
- `RunningHub Deepcleaner` —— 4/18 个有
- `PrimitiveStringMultiline` —— 3/18 个有
- `VAEEncodeAudio` —— 3/18 个有
- `MiniMaxH3ImageToVideo` —— 2/18 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/18 个有
- `FL_Audio_BPM_Analyzer` —— 1/18 个有
- `FL_Audio_Drum_Detector` —— 1/18 个有
- `HAIGC_VideoLastFrame` —— 1/18 个有
- `JWFloatToString` —— 1/18 个有
- `Label (rgthree)` —— 1/18 个有
- `LoadAudioUI` —— 1/18 个有
- `PathchSageAttentionKJ` —— 1/18 个有
- `PixaromaGroupSwitch` —— 1/18 个有
- `PreviewAny` —— 1/18 个有
- `Qwen3ASRLoader_DFT` —— 1/18 个有
- `Qwen3ASRTranscribe_DFT` —— 1/18 个有
- `RHLLMChatNode` —— 1/18 个有
- `RTXVideoSuperResolution` —— 1/18 个有
- `TextCombinerSix` —— 1/18 个有
- `TextCombinerTwo` —— 1/18 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/18 个有
- `workflow>运行采样` —— 1/18 个有

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
| Steps较低可能导致细节不足 | 19/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（19/18 个样本）：Steps较低可能导致细节不足
