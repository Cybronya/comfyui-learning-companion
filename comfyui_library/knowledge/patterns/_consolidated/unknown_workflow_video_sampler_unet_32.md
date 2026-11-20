---
name: unknown_workflow_video_sampler_unet_32
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.82375
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, PreviewAudio, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/图像原声驱动数字人_OmniRef八步加速_2119383916514725890.json, 平台全量/图像原声驱动数字人_OmniRef八步加速_2119604596661383169.json, 平台全量/图像原声驱动数字人_Pika六步极速_2119388267597619201.json, 数字人/数字人/MinimaxH3-数字人MV制作_2085594233104322561.json, 数字人/数字人/minimax H3 数字人(音频驱动)_2092695013871407105.json, 数字人/数字人/minimax H3图片+音频驱动数字人加速版_2085532607906934785.json, 数字人/数字人/方格智联-MINI-H3数字人_2086681804894986242.json, 视频生成/图生视频/CG迷-MiniMax H3_MV音乐对口型_2085601628832493570.json, 视频生成/图生视频/MiniMax H3音乐MV自动4参图提示词_2085602209005391874.json, 视频生成/图生视频/MiniMax H3音乐MV自动优化提示词_2084709296801148930.json, 视频生成/图生视频/MiniMax H3音乐MV自动优化提示词加速版_2085381440862248961.json, 视频生成/图生视频/MiniMax H3音乐MV自动优化提示词加速版_2085381668067692545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_32

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/图像原声驱动数字人_OmniRef八步加速_2119383916514725890.json、平台全量/图像原声驱动数字人_OmniRef八步加速_2119604596661383169.json、平台全量/图像原声驱动数字人_Pika六步极速_2119388267597619201.json、数字人/数字人/MinimaxH3-数字人MV制作_2085594233104322561.json、数字人/数字人/minimax H3 数字人(音频驱动)_2092695013871407105.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `PreviewAudio`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 11/12 个有
- `PrimitiveStringMultiline` —— 11/12 个有
- `MiniMaxH3ReferenceToVideo` —— 9/12 个有
- `TrimAudioDuration` —— 9/12 个有
- `PrimitiveFloat` —— 8/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `SoundFlow_GetLength` —— 7/12 个有
- `MelBandRoFormerModelLoader` —— 5/12 个有
- `MelBandRoFormerSampler` —— 5/12 个有
- `PathchSageAttentionKJ` —— 5/12 个有
- `VAEDecodeAudio` —— 5/12 个有
- `MemoryCleaner` —— 4/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/12 个有
- `MiniMaxH3SigmaShift` —— 4/12 个有
- `ModelAttentionBackend` —— 4/12 个有
- `RHHiddenNodes` —— 4/12 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/12 个有
- `图像缩放V2_孤海` —— 4/12 个有
- `孤海注释` —— 4/12 个有
- `AudioCrop` —— 3/12 个有
- `BlockSparseAttention` —— 3/12 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/12 个有
- `FlashVSRNode` —— 3/12 个有
- `GIMMVFI_interpolate` —— 3/12 个有
- `MiniMaxH3AudioConditioningT8` —— 3/12 个有
- `SDVN Fast Groups Bypasser` —— 3/12 个有
- `EasyCache` —— 2/12 个有
- `ManualSigmas` —— 1/12 个有
- `MiniMaxH3HybridCompatibilityAuditT8Advanced` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `SmartImageConcat` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
