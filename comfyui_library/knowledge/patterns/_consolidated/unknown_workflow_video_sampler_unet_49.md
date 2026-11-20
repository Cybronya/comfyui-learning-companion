---
name: unknown_workflow_video_sampler_unet_49
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.830333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/CG迷-MiniMax H3_MV音乐对口型_2085601628832493570.json, 视频生成/图生视频/H3 参考图像-视频-音频生成视频_2084427820587114497.json, 视频生成/图生视频/H3 数字人和声音克隆。_2084429432323928065.json, 视频生成/图生视频/H3音频驱动数字人单人版_2084863843855060993.json, 视频生成/图生视频/Mini max H3数字人对口型_2084517715892592641.json, 视频生成/图生视频/h3-参考生成视频-加速版_2085877996057088001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_49

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/CG迷-MiniMax H3_MV音乐对口型_2085601628832493570.json、视频生成/图生视频/H3 参考图像-视频-音频生成视频_2084427820587114497.json、视频生成/图生视频/H3 数字人和声音克隆。_2084429432323928065.json、视频生成/图生视频/H3音频驱动数字人单人版_2084863843855060993.json、视频生成/图生视频/Mini max H3数字人对口型_2084517715892592641.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `VAEDecodeAudio` —— 5/6 个有
- `FlashVSRNode` —— 4/6 个有
- `LoraLoaderBypassModelOnly` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `Sleep` —— 4/6 个有
- `AudioCrop` —— 3/6 个有
- `PainterVRAM` —— 3/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `Audio Duration (mtb)` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `SaveAudioAdvanced` —— 2/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/6 个有
- `EasyCache` —— 1/6 个有
- `MelBandRoFormerModelLoader` —— 1/6 个有
- `MelBandRoFormerSampler` —— 1/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/6 个有
- `SolAttnPatch` —— 1/6 个有
- `SoundFlow_GetLength` —— 1/6 个有
- `TrimAudioDuration` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
