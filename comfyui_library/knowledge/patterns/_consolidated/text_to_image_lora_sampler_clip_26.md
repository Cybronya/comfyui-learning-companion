---
name: text_to_image_lora_sampler_clip_26
type: Text To Image
frequency: 23
level: strong
coverage: 0.898435
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/v2.0多参双采样图影音｜minimax h3电影感大片生成_2094317653564420098.json, 视频生成/图生视频/一键换脸生成新人物｜MiniMax H3角色替换图生视频 视频生视频_2090814396544151553.json, 视频生成/图生视频/加速版图生视频｜H3高质量快速生成工作流_2095093795384811522.json, 视频生成/图生视频/加速版图生视频｜h3图片转视频工作流_2088324394362957826.json, 视频生成/图生视频/去除ai感全能参考｜minimax h3转场运镜图生视频_2093435277451812865.json, 视频生成/图生视频/去除ai感转场运镜｜minimax h3全能参考图生视频_2093764750915231745.json, 视频生成/图生视频/图像+视频+音频参考｜H3生成视频多模态工作流_2094735141095694338.json, 视频生成/图生视频/多参双采样图影音电影感大片 minimax h3 v2.0视频制作_2094183296849768450.json, 视频生成/图生视频/极致电影质感｜Minimax-H3转场运镜图生视频_2093229463424299009.json, 视频生成/图生视频/海螺H3全能参考生视频加速开源版 9图3视频3音频多模态输入_2105370711207538690.json, 视频生成/图生视频/海螺H3全能参考生视频开源加速版｜9图3视频3音频全支持_2105262580620161026.json, 视频生成/图生视频/电影级视频多参版v1.0｜minimax H3制作工作流_2093475759825440770.json, 视频生成/图生视频/电影质感极致呈现｜Minimax-H3运镜转场图生视频_2093071322497769473.json, 视频生成/图生视频/让效果图动起来_2102598028669579265.json, 视频生成/文生视频/8步加速电影质感 Minimax H3 文生视频LoRA强化出片_2094165667820957697.json, 视频生成/文生视频/9图3视频3音频全能多参音视频生成开源加速版｜海螺H3文生图生视频工作流_2088148034331963394.json, 视频生成/文生视频/H3真实电影质感全能参考 文生视频图生视频_2100309862587654145.json, 视频生成/文生视频/H3真实电影质感正式版 全能参考Latent放大_2099956140791656450.json, 视频生成/文生视频/MiniMax H3真实电影质感｜高质量视频生成_2095284422009507842.json, 视频生成/文生视频/MiniMax H3远景模糊人脸修复视频生成处理工具_2101368651281682433.json, 视频生成/文生视频/真实电影质感｜MiniMax H3文生图生视频生成_2094051162357063682.json, 视频生成/文生视频/真实电影质感｜MiniMax H3文生图生视频直出_2093845276451753986.json, 视频生成/文生视频/远景模糊人脸修复利器｜MiniMax_H3视频增强_2101179629947146242.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/v2.0多参双采样图影音｜minimax h3电影感大片生成_2094317653564420098.json、视频生成/图生视频/一键换脸生成新人物｜MiniMax H3角色替换图生视频 视频生视频_2090814396544151553.json、视频生成/图生视频/加速版图生视频｜H3高质量快速生成工作流_2095093795384811522.json、视频生成/图生视频/加速版图生视频｜h3图片转视频工作流_2088324394362957826.json、视频生成/图生视频/去除ai感全能参考｜minimax h3转场运镜图生视频_2093435277451812865.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 23 个 workflow 都包含：
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
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 22/23 个有
- `VAEDecodeAudio` —— 22/23 个有
- `孤海注释` —— 22/23 个有
- `LoadAudio` —— 21/23 个有
- `MiniMaxH3ReferenceToVideo` —— 21/23 个有
- `PathchSageAttentionKJ` —— 21/23 个有
- `VHS_LoadVideo` —— 21/23 个有
- `CreateVideo` —— 15/23 个有
- `MiniMaxH3BlockCacheT8` —— 15/23 个有
- `SaveVideo` —— 15/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/23 个有
- `easy anythingIndexSwitch` —— 14/23 个有
- `MiniMaxH3ImageToVideo` —— 11/23 个有
- `Fast Groups Bypasser (rgthree)` —— 10/23 个有
- `H3SigmaRefiner` —— 9/23 个有
- `easy showAnything` —— 9/23 个有
- `SaveImage` —— 8/23 个有
- `VHS_VideoCombine` —— 8/23 个有
- `DisableNoise` —— 7/23 个有
- `SplitSigmas` —— 7/23 个有
- `LoraLoaderBypassModelOnly` —— 6/23 个有
- `FlashVSRNode` —— 4/23 个有
- `H3LatentUpscaleByJingchen573` —— 4/23 个有
- `LTXVConcatAVLatent` —— 4/23 个有
- `LTXVSeparateAVLatent` —— 4/23 个有
- `MinimaxH3LatentUpscaler3D` —— 4/23 个有
- `PainterVRAM` —— 4/23 个有
- `Sleep` —— 4/23 个有
- `easy cleanGpuUsed` —— 4/23 个有
- `EasyCache` —— 2/23 个有
- `H3FaceStitch` —— 2/23 个有
- `H3FaceTrackCrop` —— 2/23 个有
- `H3InjectVideoLatent` —— 2/23 个有
- `H3PerFrameDenoise` —— 2/23 个有
- `MiniMaxH3NativeAudioLock` —— 2/23 个有
- `MuyeTextEditOutput` —— 2/23 个有
- `ShowText|pysssss` —— 2/23 个有
- `SolAttnPatch` —— 2/23 个有
- `Any Switch (rgthree)` —— 1/23 个有
- `Int` —— 1/23 个有
- `Text` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（23/23 个样本）：Steps较低可能导致细节不足
