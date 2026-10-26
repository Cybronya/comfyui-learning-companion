---
name: unknown_workflow_sampler_unet_vae_13
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.803417
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3-图生视频_2084259365334372354.json, 视频生成/图生视频/MiniMax-H3-图生视频（4步生视频超级加速）_2085221255543877633.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成_2084247428697518082.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2085948478043283457.json, 视频生成/图生视频/MiniMax-H3-首尾帧视频_2084274212876939265.json, 视频生成/图生视频/MiniMax-H3全能参考工作流_2084872705010130945.json, 视频生成/图生视频/MiniMax-H3开源版 图生视频 加速版_2084237228296986625.json, 视频生成/图生视频/MiniMax-H3开源版 图生视频 加速版_2084248036343115777.json, 视频生成/图生视频/MiniMax-H3开源版 图生视频 加速版_2093286738599960577.json, 视频生成/图生视频/MiniMax-H3开源版 声音克隆数字人+全节点注释_2084492386390077442.json, 视频生成/图生视频/MiniMax-H3开源版 多图参考生视频 短剧生成_2084629247259406338.json, 视频生成/图生视频/MiniMax-H3开源版 多图参考生视频_2084595722531459073.json, 视频生成/图生视频/MiniMax-H3开源版 数字人（视频+文案）+全节点注释_2084488671373381634.json, 视频生成/图生视频/MiniMax-H3开源版 数字人（视频+文案）+全节点注释_2093665300192514049.json, 视频生成/图生视频/MiniMax-H3数字人（图片+音频）+全节点注释_2084487098446475265.json, 视频生成/图生视频/MiniMax-H3最强开源版 图片开口说话数字人 图像音频参考生视频_2084591926610849793.json, 视频生成/图生视频/MiniMax-H3最强开源版 图片开口说话数字人 图像音频参考生视频_2084625798031568897.json, 视频生成/图生视频/MiniMaxH3 图片数字人！加速版！B站艾橘溪_2084158052382625793.json, 视频生成/图生视频/MiniMaxH3视频生成工作流加速版首尾帧ENGENG_2087088340184162306.json, 视频生成/图生视频/Minimax-h3 多模态全能参考_2084472101880287234.json, 视频生成/图生视频/MinimaxH3 ref2va全能多参工作流_2084512370860318722.json, 视频生成/图生视频/The digital avatar speaks H3数字人说话_2100389571778404353.json, 视频生成/图生视频/minimax h3多图参考视频工作流（int8底模+8步提速方案）_2087813787285020674.json, 视频生成/图生视频/minimaxH3 ref2va多参工作流_2084130906889089025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3-图生视频_2084259365334372354.json、视频生成/图生视频/MiniMax-H3-图生视频（4步生视频超级加速）_2085221255543877633.json、视频生成/图生视频/MiniMax-H3-多图参考视频生成_2084247428697518082.json、视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2085948478043283457.json、视频生成/图生视频/MiniMax-H3-首尾帧视频_2084274212876939265.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 23/24 个有
- `MiniMaxH3ReferenceToVideo` —— 20/24 个有
- `PrimitiveStringMultiline` —— 13/24 个有
- `AudioCrop` —— 11/24 个有
- `LoadAudio` —— 11/24 个有
- `CR Text` —— 5/24 个有
- `MiniMaxH3ImageToVideo` —— 5/24 个有
- `AILab_QwenVL` —— 4/24 个有
- `JoinStrings` —— 4/24 个有
- `LoraLoaderModelOnly` —— 4/24 个有
- `PathchSageAttentionKJ` —— 4/24 个有
- `VHS_LoadVideo` —— 3/24 个有
- `GetImageSize` —— 2/24 个有
- `ImageScaleToTotalPixels` —— 2/24 个有
- `MiniMaxH3SigmaShift` —— 2/24 个有
- `EasyCache` —— 1/24 个有
- `EmptyMiniMaxH3LatentAV` —— 1/24 个有
- `JjkText` —— 1/24 个有
- `ResizeAndPadImage` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
