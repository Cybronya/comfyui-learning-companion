---
name: text_to_image_video_lora_sampler_43
type: Text To Image
frequency: 15
level: strong
coverage: 0.883333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086449565611413505.json, 视频生成/图生视频/数字人单人极速版｜Minimax H3角色一致图生视频_2092026882165403650.json, 视频生成/图生视频/数字人唱歌口播｜MiniMax H3图生视频一键直出_2090220837587742722.json, 视频生成/图生视频/数字人生成｜minimaxh3图生视频口播直出_2089485343300083713.json, 视频生成/图生视频/让效果图动起来_2102598028669579265.json, 视频生成/图生视频/超级加速多图参考生视频｜Minimax_h3角色一致性角色表演工作流_2087208437443809281.json, 视频生成/图生视频/音频驱动对口型｜Minimax H3数字人人物特效图生视频_2089446222766624769.json, 视频生成/文生视频/3视频)3音频全能参考(9图H3加速优化版MiniMax_2086537090464047105.json, 视频生成/文生视频/MiniMax H3开源版数字人说话唱歌音频驱动图生视频处理工具_2102519299419230209.json, 视频生成/文生视频/MiniMax H3开源版数字人｜音频驱动说话唱歌全能出镜_2108025468082540546.json, 视频生成/文生视频/Minimax H3开源数字人说话唱歌｜文生视频生成_2094523338252181506.json, 视频生成/文生视频/Minimax H3开源版数字人说话唱歌工作流，文生视频数字人图生视频方案_2108269811766751233.json, 视频生成/文生视频/Minimax H3开源版数字人｜说话唱歌口型同步｜文生视频图生视频都行_2102288689492746241.json, 视频生成/文生视频/MinimaxH3数字人说话唱歌开源版ENGENG_2087131139222892545.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版｜文生视频数字人图生视频_2090448002296147970.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086449565611413505.json、视频生成/图生视频/数字人单人极速版｜Minimax H3角色一致图生视频_2092026882165403650.json、视频生成/图生视频/数字人唱歌口播｜MiniMax H3图生视频一键直出_2090220837587742722.json、视频生成/图生视频/数字人生成｜minimaxh3图生视频口播直出_2089485343300083713.json、视频生成/图生视频/让效果图动起来_2102598028669579265.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 15 个 workflow 都包含：
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
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 14/15 个有
- `PrimitiveFloat` —— 14/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/15 个有
- `孤海注释` —— 13/15 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 12/15 个有
- `AudioCrop` —— 11/15 个有
- `PathchSageAttentionKJ` —— 11/15 个有
- `PreviewAudio` —— 10/15 个有
- `SoundFlow_GetLength` —— 10/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/15 个有
- `ResolutionSelector` —— 8/15 个有
- `Int` —— 7/15 个有
- `VAEDecodeAudio` —— 3/15 个有
- `PainterVRAM` —— 2/15 个有
- `SaveImage` —— 2/15 个有
- `VHS_LoadVideo` —— 2/15 个有
- `AudioConcat` —— 1/15 个有
- `EmptyAudio` —— 1/15 个有
- `Fast Groups Muter (rgthree)` —— 1/15 个有
- `JWIntegerToString` —— 1/15 个有
- `LoadVideo` —— 1/15 个有
- `RTXVideoSuperResolution` —— 1/15 个有
- `SaveAudio` —— 1/15 个有
- `SimpleMath+` —— 1/15 个有
- `TrimAudioDuration` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
