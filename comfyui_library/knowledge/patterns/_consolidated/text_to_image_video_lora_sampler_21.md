---
name: text_to_image_video_lora_sampler_21
type: Text To Image
frequency: 20
level: strong
coverage: 0.88605
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3超写实数字人｜真假难分_2089545869266866177.json, 视频生成/图生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086425565711654914.json, 视频生成/图生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086449565611413505.json, 视频生成/图生视频/三图multi_ref参考生成｜minimax h3 i2v视频_2094928789578014722.json, 视频生成/图生视频/三图参考生视频｜multi_ref_minimax_h3_i2v生成_2095108277595099138.json, 视频生成/图生视频/单人音频驱动数字人（最高15秒）MiniMax-H3_2087437541388673025.json, 视频生成/图生视频/口播直出｜MinimaxH3数字人图生视频生成_2089809950645248002.json, 视频生成/图生视频/数字人生成｜minimaxh3图生视频口播直出_2089485343300083713.json, 视频生成/图生视频/海螺H3全能参考生视频加速开源版 9图3视频3音频多模态输入_2105370711207538690.json, 视频生成/图生视频/海螺H3全能参考生视频开源加速版｜9图3视频3音频全支持_2105262580620161026.json, 视频生成/图生视频/让效果图动起来_2102598028669579265.json, 视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085422971736383489.json, 视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085791756154654721.json, 视频生成/文生视频/MiniMax H3开源版数字人说话唱歌音频驱动图生视频处理工具_2102519299419230209.json, 视频生成/文生视频/MiniMax H3开源版数字人｜音频驱动说话唱歌全能出镜_2108025468082540546.json, 视频生成/文生视频/Minimax H3开源数字人说话唱歌｜文生视频生成_2094523338252181506.json, 视频生成/文生视频/Minimax H3开源版数字人说话唱歌工作流，文生视频数字人图生视频方案_2108269811766751233.json, 视频生成/文生视频/Minimax H3开源版数字人｜说话唱歌口型同步｜文生视频图生视频都行_2102288689492746241.json, 视频生成/文生视频/MinimaxH3数字人说话唱歌开源版ENGENG_2087131139222892545.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版｜文生视频数字人图生视频_2090448002296147970.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3超写实数字人｜真假难分_2089545869266866177.json、视频生成/图生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086425565711654914.json、视频生成/图生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086449565611413505.json、视频生成/图生视频/三图multi_ref参考生成｜minimax h3 i2v视频_2094928789578014722.json、视频生成/图生视频/三图参考生视频｜multi_ref_minimax_h3_i2v生成_2095108277595099138.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 19/20 个有
- `PathchSageAttentionKJ` —— 19/20 个有
- `PrimitiveFloat` —— 19/20 个有
- `PrimitiveStringMultiline` —— 19/20 个有
- `LoadAudio` —— 18/20 个有
- `孤海注释` —— 14/20 个有
- `ResolutionSelector` —— 13/20 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 12/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/20 个有
- `AudioCrop` —— 9/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/20 个有
- `PainterVRAM` —— 8/20 个有
- `SoundFlow_GetLength` —— 8/20 个有
- `VAEDecodeAudio` —— 8/20 个有
- `Int` —— 7/20 个有
- `PreviewAudio` —— 7/20 个有
- `VHS_LoadVideo` —— 6/20 个有
- `SaveAudio` —— 3/20 个有
- `SaveImage` —— 3/20 个有
- `TrimAudioDuration` —— 3/20 个有
- `YK_LoadImageFromURL` —— 2/20 个有
- `CR Prompt Text` —— 1/20 个有
- `JWIntegerToString` —— 1/20 个有
- `LayerUtility: PurgeVRAM V2` —— 1/20 个有
- `MathExpression|pysssss` —— 1/20 个有
- `SimpleMath+` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（21/20 个样本）：Steps较低可能导致细节不足
