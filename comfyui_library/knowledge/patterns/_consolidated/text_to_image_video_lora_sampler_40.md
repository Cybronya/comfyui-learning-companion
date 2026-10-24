---
name: text_to_image_video_lora_sampler_40
type: Text To Image
frequency: 16
level: strong
coverage: 0.893563
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086449565611413505.json, 视频生成/图生视频/数字人单人极速版｜Minimax H3角色一致图生视频_2092026882165403650.json, 视频生成/图生视频/数字人唱歌口播｜MiniMax H3图生视频一键直出_2090220837587742722.json, 视频生成/图生视频/数字人生成｜minimaxh3图生视频口播直出_2089485343300083713.json, 视频生成/图生视频/文戏向多图参考生视频｜MINIMAX-H3剧情图生视频_2093803832823336961.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3剧情向图生视频_2093777220228702209.json, 视频生成/图生视频/文戏多图参考｜MINIMAX-H3图生视频生成_2094025328523042818.json, 视频生成/文生视频/MiniMax H3开源版数字人｜音频驱动说话唱歌全能出镜_2108025468082540546.json, 视频生成/文生视频/Minimax H3开源数字人说话唱歌｜文生视频生成_2094523338252181506.json, 视频生成/文生视频/Minimax H3开源版数字人｜说话唱歌口型同步｜文生视频图生视频都行_2102288689492746241.json, 视频生成/文生视频/MinimaxH3数字人说话唱歌开源版ENGENG_2087131139222892545.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版｜文生视频数字人图生视频_2090448002296147970.json, 视频生成/文生视频/fengjing风景文生视频｜自然场景动态画面生成_2105256241860792321.json, 视频生成/文生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086255484864131074.json, 视频生成/文生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086540912632623105.json, 视频生成/文生视频/h3开源版H3数字人单人版运镜MiniMax图生视频口播数字人参考音频_2086497674601263105.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086449565611413505.json、视频生成/图生视频/数字人单人极速版｜Minimax H3角色一致图生视频_2092026882165403650.json、视频生成/图生视频/数字人唱歌口播｜MiniMax H3图生视频一键直出_2090220837587742722.json、视频生成/图生视频/数字人生成｜minimaxh3图生视频口播直出_2089485343300083713.json、视频生成/图生视频/文戏向多图参考生视频｜MINIMAX-H3剧情图生视频_2093803832823336961.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
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
- `LoadImage` —— 15/16 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 13/16 个有
- `孤海注释` —— 13/16 个有
- `AudioCrop` —— 12/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/16 个有
- `PrimitiveFloat` —— 12/16 个有
- `Int` —— 9/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/16 个有
- `PathchSageAttentionKJ` —— 8/16 个有
- `SoundFlow_GetLength` —— 8/16 个有
- `PreviewAudio` —— 7/16 个有
- `ResolutionSelector` —— 7/16 个有
- `JWIntegerToString` —— 4/16 个有
- `SimpleMath+` —— 4/16 个有
- `ExtendIntermediateSigmas` —— 3/16 个有
- `H3SigmaRefiner` —— 3/16 个有
- `INTConstant` —— 3/16 个有
- `LoraLoaderBypassModelOnly` —— 3/16 个有
- `VAEDecodeAudio` —— 3/16 个有
- `MiniMaxH3BlockCacheT8` —— 1/16 个有
- `PrimitiveString` —— 1/16 个有
- `SaveAudio` —— 1/16 个有
- `Text` —— 1/16 个有
- `TrimAudioDuration` —— 1/16 个有
- `ZML_MergeText` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（17/16 个样本）：Steps较低可能导致细节不足
