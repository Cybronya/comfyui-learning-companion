---
name: unknown_workflow_sampler_unet_vae_13
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.813038
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3-图生视频_2084259365334372354.json, 视频生成/图生视频/MiniMax-H3-图生视频（4步生视频超级加速）_2085221255543877633.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成_2084247428697518082.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2085948478043283457.json, 视频生成/图生视频/MiniMax-H3-首尾帧视频_2084274212876939265.json, 视频生成/图生视频/MiniMax-H3全能参考工作流_2084872705010130945.json, 视频生成/图生视频/MiniMax-H3开源版 图生视频 加速版_2084237228296986625.json, 视频生成/图生视频/MiniMax-H3开源版 图生视频 加速版_2084248036343115777.json, 视频生成/图生视频/MiniMax-H3开源版 图生视频 加速版_2093286738599960577.json, 视频生成/图生视频/MiniMax-H3开源版 声音克隆数字人+全节点注释_2084492386390077442.json, 视频生成/图生视频/MiniMax-H3开源版 多图参考生视频 短剧生成_2084629247259406338.json, 视频生成/图生视频/MiniMax-H3开源版 多图参考生视频_2084595722531459073.json, 视频生成/图生视频/MiniMax-H3开源版 数字人（视频+文案）+全节点注释_2084488671373381634.json, 视频生成/图生视频/MiniMax-H3开源版 数字人（视频+文案）+全节点注释_2093665300192514049.json, 视频生成/图生视频/MiniMax-H3数字人（图片+音频）+全节点注释_2084487098446475265.json, 视频生成/图生视频/MiniMaxH3_KeyFarmes_X2（二关键帧）视频生成工作流_2094650229818748929.json, 视频生成/图生视频/MiniMaxH3_KeyFarmes_X4（四关键帧）视频生成工作流_2094650342708436993.json, 视频生成/图生视频/Minimax H3视频模型图生视频_2084132239176192002.json, 视频生成/图生视频/Minimax-H3+图生视频-官流_2095734200711340034.json, 视频生成/图生视频/Minimax-h3 多模态全能参考_2084472101880287234.json, 视频生成/图生视频/MinimaxH3 ref2va全能多参工作流_2084512370860318722.json, 视频生成/图生视频/MinimaxH3_ref2va全能多参工作流_2116313823887060994.json, 视频生成/图生视频/VividMuse_MiniMax_H3_图生视频_2084274037685051393.json, 视频生成/图生视频/minimaxH3 ref2va多参工作流_2084130906889089025.json, 视频生成/文生视频/video_minimax_h3_r2v多参=加速_2095122591458615297.json, 视频生成/文生视频/极速版+高质开源MiniMax+H3+RE2VA开源版-多图参考生视频_2087042755322277889.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3-图生视频_2084259365334372354.json、视频生成/图生视频/MiniMax-H3-图生视频（4步生视频超级加速）_2085221255543877633.json、视频生成/图生视频/MiniMax-H3-多图参考视频生成_2084247428697518082.json、视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2085948478043283457.json、视频生成/图生视频/MiniMax-H3-首尾帧视频_2084274212876939265.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 26 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 25/26 个有
- `ResolutionSelector` —— 24/26 个有
- `MiniMaxH3ReferenceToVideo` —— 20/26 个有
- `PrimitiveStringMultiline` —— 16/26 个有
- `LoadAudio` —— 9/26 个有
- `AudioCrop` —— 7/26 个有
- `MiniMaxH3ImageToVideo` —— 7/26 个有
- `CR Text` —— 5/26 个有
- `LoraLoaderModelOnly` —— 5/26 个有
- `VHS_LoadVideo` —— 5/26 个有
- `ImageScaleToTotalPixels` —— 4/26 个有
- `ModelAttentionBackend` —— 4/26 个有
- `GetImageSize` —— 3/26 个有
- `easy cleanGpuUsed` —— 3/26 个有
- `H3SigmaRefiner` —— 2/26 个有
- `Label (rgthree)` —— 2/26 个有
- `MiniMaxH3AddGuide` —— 2/26 个有
- `EmptyMiniMaxH3LatentAV` —— 1/26 个有
- `Int` —— 1/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/26 个有
- `LoraLoaderBypassModelOnly` —— 1/26 个有
- `MiniMaxH3SigmaShift` —— 1/26 个有
- `Seed (rgthree)` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
