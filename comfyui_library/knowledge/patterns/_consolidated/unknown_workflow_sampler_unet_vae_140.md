---
name: unknown_workflow_sampler_unet_vae_140
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.878375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/制作音乐MV Minimax H3_2084282697115070466.json, 视频生成/图生视频/单人数字人 图片加音频生成视频 minimax H3_2085731885287825410.json, "视频生成/数字人/对口型,音频驱动,MiniMax H3,数字人,AI视频,唱歌_2106267271646769154.json", 视频生成/数字人/对口型MinimaxH3音频驱动数字人单人版_2085644184278622209.json, 视频生成/文生视频/DG_(音频+图片)音频驱动+单图单人+最大1280加速海螺H3(minimax H3)_2094359602430304258.json, 视频生成/文生视频/DG_h3+ref2va+最大1280无加速lora高质量_2087798268825792513.json, 视频生成/文生视频/DG_多参考图+视频参考｜minimax_h3 sage加速视频生成_2086004965662875649.json, 视频生成/文生视频/DG_音频驱动+单图单人+最大1280加速海螺H3(minimax H3)_2085981571416416257.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_140

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/制作音乐MV Minimax H3_2084282697115070466.json、视频生成/图生视频/单人数字人 图片加音频生成视频 minimax H3_2085731885287825410.json、视频生成/数字人/对口型,音频驱动,MiniMax H3,数字人,AI视频,唱歌_2106267271646769154.json、视频生成/数字人/对口型MinimaxH3音频驱动数字人单人版_2085644184278622209.json、视频生成/文生视频/DG_(音频+图片)音频驱动+单图单人+最大1280加速海螺H3(minimax H3)_2094359602430304258.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 7/8 个有
- `LoadAudio` —— 7/8 个有
- `PreviewAudio` —— 7/8 个有
- `SoundFlow_GetLength` —— 7/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 7/8 个有
- `ComfyMathExpression` —— 6/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/8 个有
- `PrimitiveFloat` —— 6/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `Getter` —— 4/8 个有
- `ImageConcatMulti` —— 4/8 个有
- `Setter` —— 4/8 个有
- `CreateVideo` —— 3/8 个有
- `SaveVideo` —— 3/8 个有
- `VHS_LoadVideo` —— 3/8 个有
- `JjkText` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `EasyCache` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `Int` —— 1/8 个有
- `MiniMaxH3AVDecodeT8` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `VAEDecodeAudio` —— 1/8 个有
- `VideoInfoLoaded` —— 1/8 个有
- `easy anythingIndexSwitch` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
