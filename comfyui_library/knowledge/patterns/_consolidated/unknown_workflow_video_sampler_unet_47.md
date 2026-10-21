---
name: unknown_workflow_video_sampler_unet_47
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.842
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3 参考图像-视频-音频生成视频_2084427820587114497.json, 视频生成/图生视频/H3 数字人和声音克隆。_2084429432323928065.json, 视频生成/图生视频/H3音频驱动数字人单人版_2084863843855060993.json, 视频生成/图生视频/Mini max H3数字人对口型_2084517715892592641.json, 视频生成/图生视频/MiniMax_ref2v_imgvideoaudio_2092306138221072386.json, 视频生成/图生视频/MinimaxH3音频驱动数字人单人加速版_2088648115644620802.json, 视频生成/图生视频/h3-参考生成视频-加速版_2085877996057088001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_47

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/H3 参考图像-视频-音频生成视频_2084427820587114497.json、视频生成/图生视频/H3 数字人和声音克隆。_2084429432323928065.json、视频生成/图生视频/H3音频驱动数字人单人版_2084863843855060993.json、视频生成/图生视频/Mini max H3数字人对口型_2084517715892592641.json、视频生成/图生视频/MiniMax_ref2v_imgvideoaudio_2092306138221072386.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ComfyMathExpression` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `VAEDecodeAudio` —— 5/7 个有
- `AudioCrop` —— 4/7 个有
- `FlashVSRNode` —— 4/7 个有
- `LoraLoaderBypassModelOnly` —— 4/7 个有
- `PainterVRAM` —— 4/7 个有
- `SaveImage` —— 4/7 个有
- `Sleep` —— 4/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `Audio Duration (mtb)` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `SaveAudioAdvanced` —— 2/7 个有
- `SoundFlow_GetLength` —— 2/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/7 个有
- `EasyCache` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `SolAttnPatch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
